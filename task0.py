import re
from datetime import datetime
def transform_logs(input_text: str) -> str:
    input_text = re.sub(
        r'\b[\w.-]+@[\w.-]+\.\w+\b',
        '[HIDDEN]',
        input_text
    )
    def convert_datetime(match):
        dt = datetime.strptime(match.group(), "%d/%m/%Y %H:%M")
        if 11 <= dt.day <= 13:
            suffix = "th"
        elif dt.day % 10 == 1:
            suffix = "st"
        elif dt.day % 10 == 2:
            suffix = "nd"
        elif dt.day % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"
        time = dt.strftime("%I:%M %p").lstrip("0")
        return f"{dt.day}{suffix} {dt.strftime('%B %Y')}, {time}"
    input_text = re.sub(
        r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}',
        convert_datetime,
        input_text
    )
    input_text = re.sub(
        r'\bERROR\b',
        '⚠️ ERROR',
        input_text
    )
    input_text = re.sub(r'[ \t]+', ' ', input_text)
    return input_text
log = "User john@mail.com logged in at 23/08/2025 14:05. ERROR: session timeout."
print(transform_logs(log))