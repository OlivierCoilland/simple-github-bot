from datetime import datetime, timezone
from dateutil import parser

def age(date):
    now = datetime.now(timezone.utc)
    age = now - date
    return age.days

def age_from_iso(iso):
    date = parser.parse(iso)
    return age(date)
