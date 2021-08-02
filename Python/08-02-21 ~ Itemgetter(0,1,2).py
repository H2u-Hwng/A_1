# Write a tuple that sorts the program (name, age, score) in ascending order, name is string, age and height are numbers.
# Sort by name then sort by age, then sort by score. Priority is name > age > points.
# Input:
# Tom, 19, 80
# John, 20, 90
# Jony, 17, 91
# Jony, 17, 93
# Json, 21, 85
# Output: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21 ','85'), ('Tom','19','80')]


from operator import itemgetter
result = []
while True:
    s = input().strip()
    if not s:
        break
    result.append(tuple(s.split(',')))
print(sorted(result, key=itemgetter(0,1,2)))
