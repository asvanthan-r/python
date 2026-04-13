class Notification:
    def __init__(self, msg:str):
        self.msg = msg
    def sendMessage(self, rec, msg):
        print(f"Message{self.msg} to {rec}")

class EmailNotification(Notification):
    def __init__(self,msg, emailid):
        super().__init__(msg)
        self.emailid =emailid
    def sendMessage(self, message, emailid):
        print(f"Message{self.msg} in email {self.emailid}")

class SMSNotification(Notification):
    def __init__(self, msg, phoneno):
        super().__init__(msg)
        self.phoneno =phoneno
    def sendMessage(self, msg, phoneno):
        print(f"Message{msg} in phoneno {self.phoneno}")

class PushNotification(Notification):
    def __init__(self, rec, devid):
        super().__init__(rec)
        self.devid =devid
    def sendMessage(self, message, phoneno):
        print(f"Message{message} to {self.rec} in devid {self.devid}")

sendemail = EmailNotification("Alice","jasjahs@jkkj")
sendemail.sendMessage("Hello!", "example@jjj")