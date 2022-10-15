from typing import Tuple
#  handles input for initial type validation
def validate_input_type(question) -> int:
  try: 
    return int(input(f"{question}: "))
  except Exception as err:
    print("Error: ", err, "\nValue must be an integer")
    return -1
  
# handles input for non-negative integer check
def validate_input_range(value: int) -> bool:
  if not value > 0:
    print("Error: value must be positive")
    return False
  return True
  
# validates user input for an iteration
def is_invalid_input(suggested_val) -> Tuple[int, bool]:
    return not validate_input_range(suggested_val)

# handler for input loop
def handle_input(question: str) -> int:
  is_invalid = True
  while is_invalid:
    suggested_val = validate_input_type(question)
    is_invalid = is_invalid_input(suggested_val)
  return suggested_val