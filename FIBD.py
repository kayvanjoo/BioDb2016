
# coding: utf-8

# In[ ]:

n,m = 93,16
arr = [0 for i in range(m-1)]
arr.append(1)
for gen in range(n-1):
    newR = sum([arr[i] for i in range(m-1)])
    for i in range(m-1):
        arr[i] = arr[i+1]        
    arr[m-1] = newR
print (sum(arr))

