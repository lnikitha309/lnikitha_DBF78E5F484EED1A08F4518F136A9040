def fact(n):
  if n == 0:
    return 1
  elif num<0:
    print("Factorial does not exists for negative numbers.")
  else:
    return n * fact(n - 1)
num = int(input("Enter the number:"))
result = fact(num)
print(f"The factorial of {num} is {result}")