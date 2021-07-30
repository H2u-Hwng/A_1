# Write a list to filter odd numbers from a list entered by the user.
# Input: 1,2,3,4,5,6,7,8,9 --> Output: 1,3,5,7,9


values = input()
n = [x for x in values.split(',') if int(x)%2!=0]
print(','.join(n))
