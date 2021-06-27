# Write a program that accepts strings as input lines, converts these lines to uppercase letters, and prints them to the screen. 
# Assuming the input is:
# Hello world
# Practice makes perfect
# Then the output will be:
# HELLO WORLD
# PRACTICE MAKES PERFECT


lines = []
while True:
   s = input()
   if s:
      lines.append(s.upper())
   else:
      break;
    
for sentence in lines:
    print(sentence)
