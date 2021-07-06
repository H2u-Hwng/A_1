# Write a program that accepts a sentence as input, counts the number of letters and digits in that sentence. 
# Input: hello world! 123
# Output:
# Number of letters: 10
# Number of digits: 3


s = input().strip()
c = {'LETTERS':0,'DIGITS':0}
for e in s:
    if e.isalpha():
        c['LETTERS'] += 1
    elif e.isdigit():
        c['DIGITS']  += 1

print('number of letters:',c['LETTERS'])
print('number of digits:' ,c['DIGITS'])
