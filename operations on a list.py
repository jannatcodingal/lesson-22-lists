L=[4,6,8,3,9,5]
print("original list: ",L)
count=0
for i in L:
    count += 1
avg=count/len(L)
print("sum",count)
print("average",avg)
L.sort()
print("the smallest element is: ",L[0])
print("the largest element is: "[-1])