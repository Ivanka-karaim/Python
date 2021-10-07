class Node:
    """"A class BINARY TREE"""
    def __init__(self, code, price):
        if code <= 0:
            raise ValueError("Wrong value of code(code>0)")
        if price <= 0:
            raise ValueError("Wrong value of price(price>0)")
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        """"A function that adds elements to a binary tree"""
        if self.code:
            if code == self.code:
                raise ValueError("Such a code already exists")
            if code < self.code:
                if self.left is None:
                    self.left = Node(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = Node(code, price)
                else:
                    self.right.insert(code, price)
        else:
            self.code = code

    def return_price(self, code):
        """"A function that returns the price by code """
        if code < self.code:

            if self.left is None:
                return str(code)+" Not Found"
            else:
                return self.left.returnprice(code)
        elif code > self.code:
            if self.right is None:
                return str(code)+" Not Found"
            else:
                return self.right.returnprice(code)
        else:
            return self.price


root = Node(1, 200)
root.insert(2, 300)
root.insert(3, 400)
root.insert(4, 500)
try:
    data = str(input('Enter data in the format: product code, number of products ')).split(',', 2)
    code_product = int(data[0])
    number = int(data[1])
    x = root.return_price(code_product)
    if type(x) == int:
        print(x*number)
    else:
        print(x)
except ValueError:
    print("Incorrectly entered data...")
    exit(1)
