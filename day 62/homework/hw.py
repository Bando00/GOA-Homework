def greet(name):
    return f"Hello, {name} how are you doing today?"


def litres(time):
    return int(time * 0.5)


def solution(s):
    result = ""
    for c in s:
        if c.isupper():
            result += " " + c
        else:
            result += c
    return result