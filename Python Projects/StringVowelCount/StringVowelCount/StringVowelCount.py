#COUNT THE VOWELS WITHIN THE STRING
string = "Guess how many vowels and not consonants are in this sentence"
count = 0
vowels = ['a', 'e', 'i', 'o', 'u' 'A' 'E' 'I' 'O' 'U']

for alphabet in string:
  if alphabet in vowels:
     count += 1

print(count)
