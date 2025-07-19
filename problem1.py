# num =5
# sum=0
# for i in range(num+1):
#     sum+=i
# print(sum)

# num=5
# sum=0
# while num>0:
#     sum+=num
#     num-=1

# print(sum)


# factorial numbers

# n=5
# fact=1
# while n>1:
#     fact*=n
#     n-=1
# print(fact)

# n =5
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     n-=1
# print(fact)


#  sum of n to m numbers
# ===========================

# n=3
# m=6
# sum=0
# for i in range(n,m+1):
#     sum+=i
# print(sum)


# num=6
# for i in range(1,num+1):
#     if num%i==0:
#         print(i)

# str="nani"
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)


# str="nani"
# strlenth=len(str)
# rev=""
# while strlenth>0:
#     rev +=str[strlenth-1]
#     strlenth -=1
# print(rev)



# num=123
# rev=""
# for i in  str(num):
#     rev=i+rev
# print(rev)

# num=123
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)



# num =112
# sum=0
# for i in str(num):
#     sum +=int(i)
# print(sum)

# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(sum)


num=153
sum=0
while num>0:
    digit=num%10
    sum +=digit**3
    num=num//10
if num==sum:
    print("amstrong")
else:
    print("this not")

  