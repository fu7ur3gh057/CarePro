import re


def remove_brackets(text: str) -> str:
    pattern = r"\(.*?\)"
    result_string = re.sub(pattern, "", text)
    return result_string.strip()


def get_str_or_empty(text: str | None) -> str:
    if text:
        return text
    else:
        return ""
