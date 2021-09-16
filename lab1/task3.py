Sign = {'+', '-'}
Number = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


def check(index):
    if (
        (expression[index] not in Number and expression[index] not in Sign) or
        (expression[index-1] not in Number and expression[index] == '0' and expression[index] in Number) or
        (expression[index] in Sign and expression[index+1] in Sign)
    ):
        return False, None
    if index == len(expression)-2:
        if expression[index+1] not in Number and expression[index+1] not in Sign:
            return False, None
        else:
            return True, eval(expression)
    return check(index+1)


expression = str(input("Enter expression: "))
if (expression == "") or (expression[0] not in Number and expression[0] != '-') or (expression[len(expression) - 1] not in Number):
    print((False, None))
    exit(1)
print(check(1))
