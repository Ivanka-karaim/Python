import argparse
parser = argparse.ArgumentParser()
parser.add_argument("op1", help="one operand", type=int)
parser.add_argument("op", help="operator", type=str, choices=['+', '-', '*', '/'])
parser.add_argument("op2", help="two operand", type=int)
args = parser.parse_args()
if args.op == '+':
        print(args.op1 + args.op2)
elif args.op == '-':
        print(args.op1 - args.op2)
elif args.op == '*':
        print(args.op1 * args.op2)
elif args.op == '/':
        print(args.op1 / args.op2)