number = int(input("Enter the number "))
temp = number
rev = 0
while number > 0:
    pal = number%10
    rev = rev*10+pal
    number=number//10
if temp == rev:
    print('Is palindrome')
else:
    print("Not Palindrome")

    