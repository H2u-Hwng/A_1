# Write a program that can calculate the factorial of a given number. 


n = int(input().strip())
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
print(fact(n))
