#기본자료형
#   리터럴 상수, 리스트(list), 튜플(tuple), 딕션너리(dictionary),집합(set)

var1 = "Hello python"
print(var1)
print(type(var1))

var1 = 100
print(var1)
print(type(var1))

var1=123.23
print(var1)
print(type(var1))

var1=True
print(var1)
print(type(var1))

#자료형 변환(casting)
a=10.5
b=20.14
sum=int(a+b)
print('합계:',sum)

print(int(True),int(False))
strs='2'
print(int(strs)*4)
print(int(strs)**3)

#문자열
#   따옴표 (',')(",")(''' .... ''')
oneLine = 'abcdefghijklmnopqrstuvwxyz'
print(oneLine)
oneLine = "abcdefghijklmnopqrstuvwxyz"
print(oneLine)
multiLine = ''' abcd
efghijkl
mnopqrstu
vwxyz'''
print(multiLine)
multiLine="abcde\nfghijklmn\nopqrs\ntuvwxyz"
print(multiLine)

input = "영일이삼사오육칠팔구십일이삼사오육칠"
print(input[7:14])
print(input[-1])
print('python'+"application")
print('python'+str(3.0))
print('python'+repr(3.0))
