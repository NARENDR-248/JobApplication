# str="nani"
# s=""
# for i in str:
#     s+=i
# length=0
# for j in s:
#     length+=1
# mid=length//2
# if length%2==0:
#     print(s[mid-1]+s[mid])
# else:
#     print(s[mid])




# input :75547
# output:first+last=reaming



n=7547
tem=n
end=tem%10
rev=0
while tem>0:
    d=tem%10
    rev=rev*10+d
    tem=tem//10
firt=rev%10
sum=0
tem2=n
while tem2>0:
    d=tem2%10
    sum+=d
    tem2=tem2//10
remaing=sum-(end+firt)
if remaing==end+firt:
    print(True)
else:
    print(False)