#연산자
#산술연산자
num1=10
num2=7

print('더하기',num1+num2)
print('빼기',num1-num2)
print('곱하기',num1*num2)
print('나누기',num1/num2)
print('나눠서나머지',num1%num2)
print('나눠서몫',num1//num2)
print('제곱',num1**num2)

#관계 연산자 , 논리 연산자
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)
print(num1>=5 and num2<=1)
print(num1>=5 or num2<=1)
print(not(num1>=50))

#대입 연산자
i = 10
print(i)
i = i +1
print(i)
i += 1
print(i)
i *= 2
print(i)

i=j=100
print(i,j)
i,j=99,88
j,i=i,j
print(i,j)

lst=[1,2,3,4,5]
i,*j=lst
print(i,j)
*i,j=lst
print(i,j)
i,*j,k=lst
print(i,j,k)