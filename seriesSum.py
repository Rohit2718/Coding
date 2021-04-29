limit = int(input('Enter the limit '))
sum = 0
fact = 1
for i in range(1,limit+1):
    fact =fact*i
    sum =sum+(i/fact)
print('The sum of the series is ',sum)


    