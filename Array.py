# Array operations
# 1)Traversal
# 1.1)Linear Seqential Traversal
# arr = [34,24,46,67,48,38]
# print("Linear (Sequential) Traversal:", end="")
# print("\nElements of array are:",end="")
# print(arr)

# 1.2)Reverse Traversal

arr = [40,50,60,70,80,90]
print("Reverse Array Traversal:",end="")
print("\nElements of array are:",end="")
for idx in range(len(arr) - 1, -1, -1):  
    print(arr[idx], end=" ")  
print(arr)


#Insertion In Arry

arr = [30,29,48,38,50]
ele = 14
print("Before insertion,thr array is")
for j in range(len(arr)):
    print(arr[j], end=" ")  

arr.insert(0,ele)
print("After insertion,the array is")
for j in range(len(arr)):
    print(arr[j], end=" ")

#Insertion of element at aspecific index


arr = [30,29,48,38,50]
ele = 14
print("Before insertion,thr array is")
for j in range(len(arr)):
    print(arr[j], end=" ")  

arr.insert(3,ele)





print("After insertion,the array is")
for j in range(len(arr)):
    print(arr[j], end=" ")
    


 