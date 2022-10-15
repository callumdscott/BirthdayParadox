from random import choice

MONTHS = {'Jan': 31, 'Feb': 28 , 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30,
          'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
YEAR_RANGE = 4


#  sets the day range for february for leap year status
def is_leap_year() -> None:
  if choice(range(YEAR_RANGE)) == 0:
    MONTHS["Feb"] = 29
  else:
    MONTHS["Feb"] = 28

# generates a birthday instance
def generate_birthday() -> str:
  is_leap_year()
  month = choice(list(MONTHS.keys()))
  day = choice(range(1, MONTHS[month] + 1))
  return str(day) + " " + month
  
#  generates the list of birthdays
def generate_birthdays(current_capacity):
  birthdays = []
  for i in range(current_capacity):
    birthdays.append(generate_birthday())
  return birthdays

# returns True if there is a birthday match
def check_for_birthday_match(birthdays) -> bool:
  unique_birthday = set(birthdays)
  return len(unique_birthday) != len(birthdays)

#  runs an instance of the birthday paradox
def birthday_paradox_instance(people):
  birthdays = generate_birthdays(people)
  return check_for_birthday_match(birthdays)