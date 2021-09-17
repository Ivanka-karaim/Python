import argparse
parser = argparse.ArgumentParser()
parser.add_argument("op1", help="one operand", type=int)
parser.add_argument("op", help="operator", type=str, choices=['+', '-', '*', '/'])
parser.add_argument("op2", help="two operand", type=int)
args = parser.parse_args()
c = str(args.op1) + args.op + str(args.op2)
try:
    print(eval(c))
except ZeroDivisionError:
    print("Error, division by zero")