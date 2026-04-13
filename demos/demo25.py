def calculate_discount(ordertotal, customer_type):
    if customer_type == "VIP":
        return ordertotal * 0.15
    elif customer_type == "Emp":
        return ordertotal*0.10
    elif customer_type == "Reg":
        return ordertotal*0.05
    else:
        return 0
    
####O-OCP
from abc import ABC, abstractmethod

class Discountploicy(ABC):
    @abstractmethod
    def discount(self, total):
        pass
class VipCustomer(Discountploicy):
    def discount(self, total):
        return total * 0.15

class EmpCustomer(Discountploicy):
    def discount(self, total):
        return total * 0.10

class RegCustomer(Discountploicy):
    def discount(self, total):
        return total * 0.05
    
def final_total(total, policy:Discountploicy) ->float:
    return total-policy.discount(total)

print(final_total(100, RegCustomer()))