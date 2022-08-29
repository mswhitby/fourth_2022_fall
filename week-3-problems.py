# Adding Numbers
def adding(number1, number2):
  return number1 + number2
  
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
answer = adding(number1, number2)
print(answer)

# List of Multiples
def list_of_multiples(num, length):
  multiple_list = []
  for value in range(1, length+1):
    multiple = num * value
    multiple_list.append(multiple)
    # print(f"{num} * {value} = {multiple}")
    
  return multiple_list
    
num = int(input("Enter a number: "))
length = int(input("Enter another number: "))
ans = my_function(num, length)
print(ans)
