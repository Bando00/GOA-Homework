def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"






def number_to_string(num):
    return str(num)






def solution(string):
    return string[::-1]



def make_negative(number):
    return -abs(number)




def opposite(number):
    return -number






def bool_to_word(boolean):
    return "Yes" if boolean else "No"






def positive_sum(arr):
    return sum(num for num in arr if num > 0)







def remove_char(s):
    return s[1:-1]



def repeat_str(repeat, string):
    return string * repeat



def square_sum(numbers):
    return sum(x ** 2 for x in numbers)



def summation(num):
    return num * (num + 1) / 2



def greet():
    return "hello world!"



def count_sheeps(sheep):
    return sheep.count(True)





