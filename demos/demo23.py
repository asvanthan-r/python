try: 
    num = int(input("enter a num"))
    print(num/10)
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("Enter a int/float")
else:
    print("done")
finally:
    print("opertion done")