# a=["ap","dh","dhar"]
# b=["ple","as","vin"]
# c=""
# for i in range (len(a)):

#     c+=a[i]+b[i]
#     c+=" "
# print(c) 

# a=["ap","dh","dhar"]
# b=["ple","as","vin"]
# c=[]

# for i in range (len(a)):
     
#     c+=a[i]+b[i]
#     c="".join(c)+" "
# print(c)    

a="programming"
b="gram"
res=""
for i in range(len(a)):
    if a[i:i+len(b)]==b:
        res+=a[:i]+a[i+len(b):]
        break
print(res)