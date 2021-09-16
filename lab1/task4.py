import argparse

parser = argparse.ArgumentParser()
parser.add_argument("capacity", help="Capacity bag", type=int)
parser.add_argument("bars", nargs="*")
args = parser.parse_args()
Bars = [int(item) for item in args.bars]

length = len(Bars)
Matrix = [[0 for j in range(args.capacity + 1)] for i in range(length + 1)]
for i in range(length + 1):
    for j in range(args.capacity + 1):
        if i == 0 or j == 0:
            Matrix[i][j] = 0
        elif Bars[i - 1] <= j:
            Matrix[i][j] = max(Bars[i - 1] + Matrix[i - 1][j - Bars[i - 1]], Matrix[i - 1][j])
        else:
            Matrix[i][j] = Matrix[i - 1][j]
print("Max: ", Matrix[len(Bars)][args.capacity])
