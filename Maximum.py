# Question: Find the maximum number in a list of numbers.

list_num = [10,50,20,3,8]

max_num = list_num[0]

for num in list_num:
    if num > max_num:
        max_num = num

print("Maximum Number: ", max_num)