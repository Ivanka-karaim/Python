class Node:
    """
    A class BINARY TREE
    Attributes
    _________
    code: int
        product code
    price: float, int
        product price
    left: Node
        left subtree
    right: Node
        right subtree
    Methods
    _______
    insert(code, price):
        adds new nodes to the tree
    return_price(code):
        returns the price of one product by code
    """
    def __init__(self, code, price):
        """
        Sets all the necessary attributes for the Binary tree
        :param code: int
            product code
        :param price: float, int
            product price
        """
        if not isinstance(code, int) or not isinstance(price, (float, int)):
            raise TypeError("Wrong type of code or price")
        if code <= 0:
            raise ValueError("Wrong value of code(code>0)")
        if price <= 0:
            raise ValueError("Wrong value of price(price>0)")
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        """
        Adds new nodes to the tree
        :param code: int
            new product code
        :param price: float, int
            new product price
        :return: None
        """

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
        """
        Returns the price of one product by code
        :param code:int
            the product code you want to find
        :return: price: float, int
              the price of one product by code
        """
        if code < self.code:
            if self.left is None:
                return None
            else:
                return self.left.return_price(code)
        elif code > self.code:
            if self.right is None:
                return None
            else:
                return self.right.return_price(code)
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
    if number <= 0:
        raise ValueError
    x = root.return_price(code_product)
    if x:
        print(x*number)
    else:
        print("Error, " + str(code_product) + " not found:(")
except ValueError:
    print("Incorrectly entered data...")
    exit(1)
