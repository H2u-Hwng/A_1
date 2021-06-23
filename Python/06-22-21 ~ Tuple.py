# Write a program that accepts a comma-separated string of numbers that produces a list and a tuple containing all the numbers.
# For example: The input is: 34,67,55,33,12,98 then the output is: 
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


lst = input().strip().split(',')
res = tuple(lst)
print(lst, res, sep='\n')
