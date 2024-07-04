import random
import string


v1=list(string.ascii_lowercase)
v2=list(string.ascii_uppercase)
v3=list(string.digits)
v4=list(string.punctuation)
random.shuffle(v1)
random.shuffle(v2)
random.shuffle(v3)
random.shuffle(v4)
number_of_character=int(input("give the length of password:"))
part1=round(number_of_character*(30/100))
part2=round(number_of_character*(50/100))


password=""

for i in range(part1):
    password=password+v1[i]
    password=password+v2[i]
for i in range(part2):
    password=password+v3[i]
    password=password+v4[i]
    
    
print(f"your password is {password}")
    
    






