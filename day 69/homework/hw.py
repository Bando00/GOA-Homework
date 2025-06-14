def calculator(txt):
    left, op, right = txt.split()
    a = len(left)
    b = len(right)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '//':
        result = a // b

    return '.' * result



def html_end_tag_by_start_tag(start_tag):
    tag_name = start_tag[1:].split()[0].rstrip('>')
    return f"</{tag_name}>"
