# Find all numbers that are divisible by 7 but not multiples of 5, within the range 2000 and 3200 (including 2000 and 3200).
# The resulting numbers will be printed as a string on one line, separated by commas.


res = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        res.append(i)
print(*res, sep=',')
