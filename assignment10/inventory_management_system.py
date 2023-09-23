class InventoryManagementSystem:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.stock = []
        self.invoices = []
        self.customers = []

    def addCustomer(self, name, balance):
        customer = Customer(name, balance)
        self.customers.append(customer)

    def addItem(self, name, price):
        item = Item(name, price)
        self.stock.append(item)

    def addInvoice(self, customer_id, items):
        invoice = Invoice(customer_id, items)
        self.changeBalance(customer_id, invoice.total_price)
        self.invoices.append(invoice)

    def getPayment(self, customer_id, amount):
        self.changeBalance(customer_id, amount*-1)

    def getItem(self, id):
        for item in self.stock:
            if (item.id == id):
                return item
        print("Invalid Id")

    def getCustomer(self, id):
        for customer in self.customers:
            if (customer.id == id):
                return customer
        print("Invalid Id")

    def getInvoice(self, id):
        for invoice in self.invoices:
            if (invoice.id == id):
                return invoice
        print("Invalid Id")

    def puchaseItem(self, id, qty):
        for i in range(len(self.stock)):
            if (self.stock[i].id == id):
                self.stock[i].qty += qty
                return
        print("Invalid Id")

    def changeBalance(self, customer_id, amount):
        for customer in self.customers:
            if (customer.id == customer_id):
                customer.balance += amount
                return
        print("Invalid Id")

    



class Invoice:
    count = 0
    def __init__(self, customer_id, items):
        Invoice.count += 1
        self.id = Invoice.count
        self.customer_id = customer_id
        self.items = items
        self.total_price = self.calculatePrice(items)

    def calculatePrice(self, items):
        total_price = 0
        for item in items:
            amount = item.price * item.qty
            total_price += amount
        return total_price
    
    def __str__(self):
        string = f"Invoice:\nId:{self.id}\nCustomer Id:{self.customer_id}\nTotal Price:{self.total_price}\nItems:"
        for item in self.items:
            string += item.__str__()
        return string


    

class Item:
    count = 0
    def __init__(self, name, price):
        Item.count += 1
        self.id = Item.count
        self.name = name
        self.price = price
        self.qty = 0

    def __str__(self):
        return f"Item(id={self.id}, name={self.name}, price={self.price}, qty={self.qty})"

class Customer:
    count = 0
    def __init__(self, name, balance):
        Customer.count += 1
        self.id = Customer.count
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Customer(id={self.id}, name={self.name}, balance={self.balance})"