#Program to Print Math table of a number

print('Code for Math table of a number.')
num = int(input('Enter a number: '))
for i in range(1,11):
  print(f'{num} x {i:2d} = {num * i}')