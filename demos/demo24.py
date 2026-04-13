
path = ""
class InvoiceService:
    def __init__(self, invoice):
        self.invoice = invoice
    def calculate_total(self):
        total = sum(item['price'] *item['quantity'] for
        item in self.invoice['items'])
        return total
    def save_to_file(self):
        with open(path, 'w', encoding = "utf-8") as f:
            f.write(str(self.invoice))
    def email_customer(self):
        print(f"Email sent to customer with{self.invoice}")

########################S in Solid
class InvoiceCalculator:
    def __init__(self, invoice):
        self.invoice =invoice
    def calculate_total(self):
        total = sum(item['price'] *item['quantity'] for
        item in self.invoice['items'])
        return total
class InvoivePresistance:
    def __init__(self, invoice):
        self.invoice =invoice
    def save_to_file(self):
        with open(path, 'w', encoding = "utf-8") as f:
            f.write(str(self.invoice))