#제어문
#조건문

# score=input()
# if int(score)>85 : print('우수')
# elif int(score)<84 and int(score)>70 : print('보통')
# else : print('부족')


# score = int(input()) 
# if score > 85 : print('우수')
# elif score <= 85 and score >= 70 : print('보통')
# else : print('부족')

# score = int(input('점수입력:'))
# grade = ''
# if score<=100 and score>=85: grade = '우수'
# elif score>=70 : grade = '보통'
# else : grade = '부족'
# print('님점수 : %d / 등급 : %s'%(score,grade))
      
num=7
result=0
if(num>6):
    result=num*2
else:
    result=num+2
print(result)

print(num*7 if num>6 else num+2)
#반복문
# while문
cnt=tot=0
datalst=[]
while cnt<5:
    cnt+=1
    tot+=cnt
    datalst.append(cnt)
    print(cnt,tot)
print(datalst)

a=b=0
ww=[]
while a<=100:
    a+=1
    if a%4==0 : 
        b+=a 
        ww.append(a)
print('4의배수의 합 :',b)
print(ww)

i=0
while i<10:
    i+=1
    if i==3:
        continue
    if i==6:
        break
    print(i,end=' ')
print()
#for문
string='가느다란물방울'
print(len(string))
for s in string:
    print(s)
    
lst = [1,2,3,4,5,6,7]
for e in lst:
    print(e)
    
print(range(10))
for e in range(10):
    print(e)
    
lst = ['A','B','C']
if 'B' in lst:
    print("Ok")
else : 
    print("no")