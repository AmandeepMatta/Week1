vowels = ['a','e','i','o','u']

user_input = input("Say Something: ")

counter=0

for char in user_input.lower():
    print(char)
    if char in vowels:    
        counter+=1
    
print("Number of Vowels: ",counter)
    