#1) Write a program that calculates and prints the sum of numbers from 1 to 10 using a for loop.

sum = 0
for i in range(1, 11):
    sum += i
print("1 დან 10 ის ჩათვლით რიცხვების ჯამი არის: ", sum)



#2)Print the squares of numbers from 1 to 15.
for i in range(1, 15):
    print(i*i)



#3)Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop.
sum = 0
for i in range(1,6):
    print(i*i)
    sum+=i


#4)Print numbers divisible by both 3 and 5 from 1 to 100 inclusive.

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)


#5)Write a program that prints numbers from 10 to 1 in reverse order using a for loop.
for num in range(10, 0, -1):
    print(num)

