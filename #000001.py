# Enter an integer n. Calculate the product of even numbers from 1 to n and print to the screen. 


n = int(input().strip())
if n >= 2:
    temp = 1
    for i in range(2,n+1,2):
        res = temp*i
        temp = res
    print(res)
else:
    print('error')
