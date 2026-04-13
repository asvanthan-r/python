from abc import ABC, abstractmethod

class PaymentProcess(ABC):
    @abstractmethod
    def authorise(self, amount:float) ->bool:
        pass
    @abstractmethod
    def capture(self, amount:float) -> bool:
        pass
    
    def process(self, amount:float) -> None:
        if(self.authorise(amount)):
            self.capture(amount)
            print("Payment Processed", amount)
        else:
            print("Authorisaton failed")
class Strip(PaymentProcess):
    def authorise(self, amount:float) ->bool:
        print("Authorised")
        return True
    def capture(self, amount:float) -> bool:
        print("Captured amount")
        return True

class Gpay(PaymentProcess):
    def authorise(self, amount:float) ->bool:
        print("Authorised")
        return True
    def capture(self, amount:float) -> bool:
        print("Captured amount")
        return True

def checkout(amount:float, processor: PaymentProcess) ->None:
    processor.process(amount)

upi = Gpay()
card = Strip()

checkout(100, upi)
checkout(5502.2, card)