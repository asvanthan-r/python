print("Hello world")
import keyword

print(keyword.kwlist)

def result(a):
    return a-10
class Score:
    a = 10
    b = result(a)

print(Score.a)
print(Score.b)

number = [1,2,3,4,5]
for number in number:
    if(number == 5):
        pass
    if(number == 2):
        continue
    print(number* number)

OFFSET  = 8

def iterate(i):
    while i>0:
        print(OFFSET+i)
        i=i-1
iterate(9)

print("""
Hello
multi
line

literal
""")

s1 = "Hello"
s2 = "World"

print(s1+" "+s2)
print((s1+"\n") * 4)

num = [1,2,2]
num2 = {1,2,2,2}
num3 = (1,2,3,3)
dict_num = {'one':'1', 'two': '2'}
print(num, num2, num3, dict_num)
print(dict_num.keys)

print("is 2 in dict_num", 2 in dict_num)

var1 = 9
var2 = float(var1)
print(var1,var2, type(var1), type(var2))