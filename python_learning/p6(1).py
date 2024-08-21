#Program to check if the alphabet is uppercase

alpha = input('Enter the input Alphabet: ')
if len(alpha) > 1:
  print('Enter only one character'
  )
elif alpha.isupper():
  print("Alphabet is in uppercase.")