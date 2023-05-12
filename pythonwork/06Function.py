#함수 function
def print_max(a,b):
    if a>b:
        print(a,'가 더큼 얘보다->',b)
    elif a==b:
        print(a,'<=둘이 같음=>',b)
    else:
        print(b,'가 더크다 얘보다->',a)

print_max(7,2)

def mul(a,b=1):
    c=a*b
    return(c)
print(mul(3,7))
print(mul(2))
print()
#전역 및 지역변수
x=100
def func(x):
    print(x)
    x=2
    print(x)
func(x)

def func2():
    global x
    print(x)
    x=2
    print(x)
func2()

def f(i,lst):
    i+=1
    lst.append(0)
k=100
m=[1,2,3]
f(k,m)
print(k,m)

def reprint(a,b,c):
    print(a+2,b*2,c/2)
reprint(6,4,16)
reprint(c=16, a=6, b=4)

#가변길이파라미터
def sum(*numbers):
    tot = 0
    for num in numbers:
        tot += num
    return tot

print(sum(1,2,3,4,5,6,7,8,9,10))

def sum2(*numbers):
    count=0
    tot=0
    for num in numbers:
        count+=1
        tot+=num
    return count,tot

count,sum=sum2(1,3,4,5,6,7,45,3)
print(count,sum)