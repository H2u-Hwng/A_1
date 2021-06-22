# Write a program to create a dictionary containing (i, i * i) from 1 to n (including 1 and n).
# Example: Suppose n is 8 then the result will be: {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64}.


n = int(input().strip())

d = dict()
for i in range(1,n+1):
    d[i] = i*i

print(d)
