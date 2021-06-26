# Write a program that accepts a string of words entered by the user, separated by commas, and prints the words in alphabetical order, separated by commas.
# Input is: without,hello,bag,world, the output will be: bag,hello,without,world.


items = [i for i in input().split(',')]
items.sort()
print(','.join(items))
