from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import TableStyle, SimpleDocTemplate, Spacer, Paragraph, Table
import os
from django.conf import settings
from apps.results.models import Result, Answer

from reportlab.pdfbase import pdfmetrics

from utils.text_util import get_str_or_empty


class PDFGenerator:
    def __init__(self, result: Result):
        self._result = result
        pdfmetrics.registerFont(TTFont("FreeSans", "fonts/FreeSans.ttf"))
        # Create a style for the text
        self._styles = getSampleStyleSheet()
        self._style = self._styles["Normal"]
        self._style.fontName = "FreeSans"
        # Add style to the table
        self._table_style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )

    def _mkdir(self):
        # Define the folder name you want to create
        folder_name = "docs/"
        # Create the folder path using BASE_DIR
        folder_path = os.path.join(settings.BASE_DIR, folder_name)
        # Check if the directory already exists
        if not os.path.exists(folder_path):
            # If it doesn't exist, create it
            os.makedirs(folder_path)

    def _empty_if_none(self, comment: str | None) -> str:
        if comment is None:
            return ""
        return comment

    def _add_paragraph(self, elements: list, text_dict: list) -> list:
        # Add the text lines to the document
        for line in text_dict:
            elements.append(Paragraph(line, self._style))
            elements.append(Spacer(1, 12))  # Add space between lines
        return elements

    def _is_file_already_exists(self, filename) -> bool:
        file_path = os.path.join(
            "docs", filename
        )  # Specify the relative path to your file
        if os.path.isfile(file_path):
            return True
        else:
            return False

    def _get_table_content_data(self, answers: list[Answer]) -> list:
        result_data = []
        for answer in answers:
            check_list = answer.check_list.all()
            comment = ""
            if check_list and len(check_list) != 0:
                comment = check_list.first().comment
            answer_data = [
                f"{answer.question.numeration}",
                f"{answer.average_score}",
                f"{comment}",
            ]
            result_data.append(answer_data)
        return result_data

    def generate(self) -> str:
        filename = f"{self._result.student.tg_id}_{self._result.exam.pk_id}.pdf"
        file_path = f"docs/{filename}"
        if self._is_file_already_exists(filename=filename):
            return file_path
        answers = self._result.answers.all().order_by("question__numeration")
        final_score = sum(answer.average_score for answer in answers)
        # Create a PDF document
        document = SimpleDocTemplate(file_path, pagesize=letter)
        # Create a list to store document elements
        elements = []
        endtime = self._result.end_time.strftime("%m/%d/%Y")
        title_text = [
            f"Дата сдачи: {endtime}",  # TODO Add to Test_bot end time
            f"Предмет: {self._result.exam.subject.title}",
            f"Класс: {self._result.exam.subject.grade.number}",
            f"Фамилия Имя: {self._result.student.name}",
        ]
        self._add_paragraph(elements, text_dict=title_text)
        table_data = [["№", "Балл", "Комментарий эксперта"]]
        table_content_data = self._get_table_content_data(answers=list(answers))
        combined_data = table_data + table_content_data
        table = Table(combined_data)
        # Set the font for all cells in the table
        for i in range(len(combined_data)):
            for j in range(len(combined_data[i])):
                self._table_style.add("FONTNAME", (j, i), (j, i), "FreeSans")
        table.setStyle(self._table_style)
        # Add the table to the document elements
        elements.append(table)
        # Add Footer
        footer_text = ["Первичный балл:", f"{final_score}"]
        self._add_paragraph(elements, text_dict=footer_text)
        # Build the PDF document
        document.build(elements)
        return file_path
