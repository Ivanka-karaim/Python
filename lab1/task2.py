import argparse
import operator
vocabulary1 = {"add", "sub", "mul", "div", "pow", "mod"}
vocabulary2 = {"abs", "neg", "pos"}
vocabulary = {"add", "sub", "mul", "div", "pow", "mod", "abs", "neg", "pos"}
parser = argparse.ArgumentParser()
parser.add_argument("operation", help="operator", type=str, choices=vocabulary)
parser.add_argument("operands", nargs="*")
args = parser.parse_args()
if args.operation in vocabulary1:
    if len(args.operands) == 2:
        print(eval("operator."+args.operation)(int(args.operands[0]), int(args.operands[1])))
    else:
        print("Wrong number of operands")
if args.operation in vocabulary2:
    if len(args.operands) == 1:
        print(eval("operator."+args.operation)(int(args.operands[0])))
    else:
        print("Wrong number of operands")
