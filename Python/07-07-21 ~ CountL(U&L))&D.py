# Write a program that accepts a sentence as input, counts the number of letters (if input is letter, count the number of upper case and lower case) and digits in that sentence. 
# Input: Hello World! 123
# Output:
# Number of letters: 10
# Number of upper case: 2
# Number of lower case: 8
# Number of digits: 3


s = input().strip()
c = {'LETTERS':0,'UPPER CASE':0,'LOWER CASE':0,'DIGITS':0}
for e in s:
    if e.isalpha():
        c['LETTERS'] += 1
        if e.isupper():
            c['UPPER CASE'] += 1
        else:
            c['LOWER CASE'] += 1
    elif e.isdigit():
        c['DIGITS']  += 1
    else:
        pass

print('number of letters:',c['LETTERS'])
print('number of upper case:',c['UPPER CASE'])
print('number of lower case:' ,c['LOWER CASE'])
print('number of digits:' ,c['DIGITS'])
