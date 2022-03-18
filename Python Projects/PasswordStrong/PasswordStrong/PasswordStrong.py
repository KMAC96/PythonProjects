import random
import array
 
# maximum length of password
Maximum_Length = 8
 
# declare arrays of the character that we need in password
# Represented as chars to enable easy string concatenation
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

Lowercase_Characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
 
Uppercase_Characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
 
Special_Characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
 
# combines all the character arrays above to form one array
Combination_List = Numbers + Lowercase_Characters + Uppercase_Characters + Special_Characters
 
# randomly select at least one character from each character set above
rand_numbers = random.choice(Numbers)
rand_upper = random.choice(Uppercase_Characters)
rand_lower = random.choice(Lowercase_Characters)
rand_symbol = random.choice(Special_Characters)
 
# combine the character randomly selected above
# 8 Character password
strong_password = rand_numbers + rand_upper + rand_lower + rand_symbol
 
 

for x in range (Maximum_Length - 4):
    strong_password = strong_password + random.choice(Combination_List)
 
    # convert password into array
    strongpassword_list = array.array('u', strong_password)
    random.shuffle(strongpassword_list)
 
#Form the password
password = ""
for x in strongpassword_list:
        password = password + x
         
# print out password
print(password)
