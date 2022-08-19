# 1. Must not contain any letters
# 2. Must contain at least 3 astertics
# 3. Must not be longer than 8 characters

def user_password():
  password = input(
    """
    1. Must not contain any letters
    2. Must contain at least 3 astertics
    3. Must not be longer than 8 characters
    
    
    """
    
    "Please create a password that meets the conditions above: "
  )
  
  return password

def check_letters(password):
  no_letter = True
  for char in password:
    
    if char.isalpha():
      print("Your password must not contain letters")
      no_letter = False
      break
     
  return no_letter
  
def check_astertics(password):  
  passed_astertic = False
  if password.count('*') >= 3:
    passed_astertic = True
  
  if not passed_astertic:
    print("Your password must contain three astertics")

  return passed_astertic  

def check_length(password):
  less_than_8 = True 
  if len(password) > 8:
    less_than_8 = False 
    print("Your password must not be longer than 8 characters")
    
  return less_than_8  
  
def check_all_rules(rule1,rule2,rule3):
  if rule1 and rule2 and rule3:
    print("Your password was correct")
    return True
# if passed_1 and passed_2 and passed_3: 
#   print("This passwork meets our conditions")

passed_all_rules = False
while not passed_all_rules:
  password = user_password()
  rule_1 = check_letters(password)
  rule_2 = check_astertics(password)
  rule_3 = check_length(password)
  passed_all_rules = check_all_rules(rule_1,rule_2,rule_3)
  