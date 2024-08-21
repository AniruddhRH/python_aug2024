#Program to check if the alphabet is Vowel or Consonant

print('Code check if the Alphabet is a Vowel or a Consonant.')
Vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
alpha = input('Enter an Alphabet: ')
if alpha in Vowels:
  print(f'{alpha} is a Vowel.')
elif alpha.isalpha():
  print(f'{alpha} is a Consonant.')
else:
  print('Invalid input.')