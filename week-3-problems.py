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


# FuzzBuzz - Saw
num = int(input("Enter a number: "))
length = int(input("Enter another number: "))
ans = my_function(num, length)
print(ans)


def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
    
  elif num % 3 == 0:
    print("fizz")
    
  elif num % 5 == 0:
    print("buzz")
    
  
    
num = int(input())
ans = fizz_buzz(num)
