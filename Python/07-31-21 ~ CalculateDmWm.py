# Write a program that calculates the actual amount of a bank account based on the transaction log entered from the console.
# D: Deposit, W: Withdrawal.
# Input:
# D 300
# D 300
# W 200
# D 100
# Output: 500


result = 0
while True:
    values = input().strip().split()
    if not values:
        break
    elif values[0] == 'D':
        result += int(values[1])
    elif values[0] == 'W':
        result -= int(values[1])
print(result)
