#STRINGMIX FUNCTION

import random 
sample_string = "This string will get shuffled"
print(sample_string)

#Shuffled String
shuffled_string = ''.join(random.sample(sample_string, len(sample_string)))
print(shuffled_string)
