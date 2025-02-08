# Question: Count the number of vowels (a, e, i, o, u) in a given string.

user_input = input("Say Something: ")

counter=0

for char in user_input:  
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        counter += 1
    
print("Number of Vowels: ",counter)
    