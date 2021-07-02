# Write a program to find all the numbers in the range 1000 and 3000 (including both)
# Conditions: all the digits in the number are even. 
# Prints the found numbers as comma-separated strings, on one line.


lst = []
for x in range(1000,3001,2):
    y = str(x)
    if int(y[0])%2==0 and int(y[1])%2==0 and int(y[2])%2==0 and int(y[3])%2==0:
        lst.append(y)
print(','.join(lst))
