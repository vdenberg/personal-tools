def am_or_pm():
  h = datetime.now().hour
  return "AM" if h <= 12 else "PM"

def yes_or_no(string):
  return input(string).lower().strip()[:1] == 'y'
