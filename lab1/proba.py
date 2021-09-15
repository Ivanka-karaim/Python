import argparse
import ast
import


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("function", help="Python function to run.")
    parser.add_argument("args", nargs='*')
    opt = parser.parse_args()

    func = getattr(np, opt.function)
    args = [ast.literal_eval(arg) for arg in opt.args]

    # run the function and pass in the args, print the output to stdout
    print(func(*args))


if __name__ == "__main__":
    main()