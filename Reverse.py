# Question: Reverse a given string. 

user_input = input("Enter any word: ")

reversed_string = ""

for i in range(len(user_input) - 1, -1, -1):
    reversed_string += user_input[i]

print("Reversed string:", reversed_string)
