#1) Write a program that calculates and prints the sum of numbers from 1 to 10 using a for loop
#1) დაწერეთ პროგრამა რომელიც გამოითვლის და დაპრინტავს 1 იდან 10 მდე რიცხვების ჯამს 
sum = 0
for i in range(1, 11):
    sum += i
print("1 დან 10 ის ჩათვლით რიცხვების ჯამი არის: ", sum)


#2) Print the squares of numbers from 1 to 15.
#2) დაპრინტე რიცხვების კვადრატები 1-დან 15-მდე.

for i in range(1, 15):
    print(i*i)


#3) Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop.
#3) დაწერე პროგრამა რომელიც გამოითვლის და დაპრინტავს რიცხვების კვადრატების ჯამს 1 იდან 5 მდე for loop ების გამოყენებით

sum = 0
for i in range(1,6):
    print(i*i)
    sum+=i
