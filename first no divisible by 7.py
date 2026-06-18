#first no divisble by 7
for i in range(1,100):
    if i%7==0:
        print(i)
        break
#skip even no
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

#sum of nat no
i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
print("sum=",sum)
#sn=n(n+1)/2 