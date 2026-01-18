def detection(array):
    size=len(array)
    max_frq=size/2
    freq={}
    for x in array:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    max_value=max(freq.values())
    max_key=max(freq,key=freq.get)
    if max_value==max_frq:
        return max_key

size=6
array1=[2,1,2,5,3,2]
print("Size:",size)
print("Array:",array1)
print("Identifier",detection(array1))
print()
array2=[2,1,2,5,3,2]
print("Array:",array2)
print("Repeated Identifier",detection(array2))

