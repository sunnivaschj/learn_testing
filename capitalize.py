# Gjør den første bokstaven om til stor bokstav
def capitalize_case(x):
  if not isinstance(x, str):
    raise TypeError('Please provide a string argument')
  return x.capitalize()

