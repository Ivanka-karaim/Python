import argparse
res = {"add": '+', "sub": '-', "mul": '*', "div": '/', "pow": '**', "mod": '%'}
parser = argparse.ArgumentParser()
parser.add_argument("op", help="operator", type=str, choices=res)
parser.add_argument("op1", help="one operand", type=int)
parser.add_argument("op2", help="two operand", type=int)
args = parser.parse_args()
c = str(args.op1) + res[args.op] + str(args.op2)
print(eval(c))