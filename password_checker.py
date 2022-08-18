# password = input()
password = "8935*602*46=06*!!"

for char in password:
  passed_1 = False
  if char.isalpha():
    print("Your password must not contain letters")
    break
  passed_1 = True
  
passed_2 = False
if password.count('*') == 3:
  passed_2 = True

if not passed_2:
  print("Your password must contain three astertics")
  

passed_3 = True 
if len(password) > 8:
  passed_3 = False 
  print("Your password must not be longer than 8 characters")
  
  
if passed_1 and passed_2 and passed_3: 
  print("This passwork meets our conditions")
  