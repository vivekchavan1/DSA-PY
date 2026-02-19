# Array operations
# 1)Traversal
# 1.1)Linear Seqential Traversal
# arr = [34,24,46,67,48,38]
# print("Linear (Sequential) Traversal:", end="")
# print("\nElements of array are:",end="")
# print(arr)

# 1.2)Reverse Traversal

# arr = [40,50,60,70,80,90]
# print("Reverse Array Traversal:",end="")
# print("\nElements of array are:",end="")
# for idx in range(len(arr) - 1, -1, -1):  
#     print(arr[idx], end=" ")  
# print(arr)


#2)Insertion In Arry

# arr = [30,29,48,38,50]
# ele = 14
# print("Before insertion,thr array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")  

# arr.insert(0,ele)
# print("After insertion,the array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")

#Insertion of element at a specific index

# arr = [30,29,48,38,50]
# ele = 14
# print("Before insertion,thr array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")  

# arr.insert(3,ele)

# print("After insertion,the array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")


#Insertion at the End:

# arr = [30,29,48,38,50]
# ele = 14
# print("Before insertion,the array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")  

# arr.append(ele)

# print("After insertion,the array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")

#3)Deleting of an array

# arr = [50,20,15,35,27,14]
# print("Before Deleting,the array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")

# del arr[0]
# del arr[3]

# print("After deleting the array is")
# for j in range(len(arr)):
#     print(arr[j], end=" ")

# sorting elements in array

my_array = [23,65,24,16,38]
# my_array.sort()
my_array.sort(reverse=True)
print(my_array)

 