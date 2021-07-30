# Write a program-calculated value of a + aa + aaa + aaaa


a = input().strip()
s1 = int('%s'%a)
s2 = int('%s%s'%(a,a))
s3 = int('%s%s%s'%(a,a,a))
s4 = int('%s%s%s%s'%(a,a,a,a))
print(s1+s2+s3+s4)
