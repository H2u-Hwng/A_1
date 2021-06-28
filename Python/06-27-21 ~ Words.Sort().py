# Write a program that accepts as input a string of words separated by spaces, remove duplicates, sorts them alphabetically, and then prints them.
# The input is: hello world and practice makes perfect and hello world again
# The output is: again and hello makes perfect practice world


s = []
[s.append(x) for x in input().strip().split() if x not in s]
s.sort()
print(' '.join(s))
