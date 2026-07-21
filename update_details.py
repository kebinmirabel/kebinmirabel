from datetime import date
from calendar import monthrange

birth = date(2003, 8, 4)   # bday :D

today = date.today()

years = today.year - birth.year
months = today.month - birth.month
days = today.day - birth.day

if days < 0:
    months -= 1
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month != 1 else today.year - 1
    days += monthrange(prev_year, prev_month)[1]

if months < 0:
    years -= 1
    months += 12

uptime = (
    f"{years} years, {months} months, {days} days "
    "and a partridge in a pear tree."
)

with open("README.md", encoding="utf8") as f:
    readme = f.read()

import re

readme = re.sub(
    r"<!--UPTIME-->.*",
    f"<!--UPTIME-->{uptime}",
    readme,
)

with open("README.md", "w", encoding="utf8") as f:
    f.write(readme)