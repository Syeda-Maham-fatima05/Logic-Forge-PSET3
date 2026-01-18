def detection(array):
    for i in range(len(array)-1):
        if array[i]==array[i+1]:
            return array[i]
    return array[0]
# array=list(map(int, input("Enter the identifiers: ").split()))
# print("Repeated Identifier:",detection(array))
size=6
array1=[2,1,2,5,3,2]
print("Size:",size)
print("Array:",array1)
print("Repeated Identifier",detection(array1))
print()
array2=[2,1,2,5,3,2]
print("Array:",array2)
print("Repeated Identifier",detection(array2))