class Bank:
    def getinterest(self):
        return 5.0
    
class SBI(Bank):
    def getinterest(self):
        return 6.0
    
class HDFC(Bank):
    def getinterest(self):
        return 7.0

bank1 = SBI()
bank2 = HDFC()

print(f"ROI: {bank1.getinterest()}")

print(f"ROI: {bank2.getinterest()}")