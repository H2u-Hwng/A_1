# A website requires users to enter a username and password to register. Write a program to check the validity of the password entered by the user.
# Password check criteria include:
# 1. At least 1 letter is in [a-z]
# 2. At least 1 number is in [0-9]
# 3. At least 1 character in [A-Z]
# 4. At least 1 character inside [$#@]
# 5. Minimum password length: 6
# 6. Maximum password length: 12
# Input: ABd1234@1,a F1#,2w3E*,2We3345
# Output: ABd1234@1


import re
result = []
values = [x for x in input().strip().split(',')]
for e in values:
    if not len(e) in range(6,13):
        continue
    elif not re.search('[a-z]',e):
        continue
    elif not re.search('[0-9]',e):
        continue
    elif not re.search('[A-Z]',e):
        continue
    elif not re.search('[$#@]',e):
        continue
    else:
        pass
    result.append(e)
print(','.join(result)
