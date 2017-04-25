from datetime import datetime, timezone
from dateutil import parser

def calculate_age(date):
    now = datetime.now(timezone.utc)
    age = now - date
    return age.days

def calculate_age_from_iso(iso):
    date = parser.parse(iso)
    return calculate_age(date)

def format_message(issue, text):
    issue_author_login = issue.data['user']['login']
    return text.format(login=issue_author_login)
