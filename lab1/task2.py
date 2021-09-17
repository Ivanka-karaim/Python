import argparse
import operator
vocabulary1 = {"add", "sub", "mul", "truediv", "pow", "mod"}
vocabulary2 = {"abs", "neg", "pos"}
vocabulary = {"add", "sub", "mul", "truediv", "pow", "mod", "abs", "neg", "pos"}
parser = argparse.ArgumentParser()
parser.add_argument("operation", help="operator", type=str)
parser.add_argument("operands", nargs="*")
args = parser.parse_args()
try:
    if args.operation in vocabulary1:
        result = eval("operator." + args.operation)(int(args.operands[0]), int(args.operands[1]))
        print(result)
    else:
        result = eval("operator." + args.operation)(int(args.operands[0]))
        print(result)
except IndexError:
    print("Error with number of values!")
except:
    print("Error! Incorrect function!")
