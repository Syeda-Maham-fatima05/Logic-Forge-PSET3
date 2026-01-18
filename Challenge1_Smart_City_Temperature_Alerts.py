def temp_next(array,temp,next):
    threshold=array[1]
    target=temp[next]
    for i in range(next+1,len(temp)):
        if temp[i]>=target+threshold:
            return i
        elif temp[i]<=target-threshold:
            return i

def temp_count(array,temp,L,R):
    count=0
    K=array[1]
    for i in range(L,R+1):
        current=temp[i]
        found=False
        for j in range(i+1,len(temp)):
            if temp[j]>=current+K or temp[j]<=current-K:
                found=True
                break
        if found:
            count+=1
    return count

array=list(map(int,input().split()))
temp=list(map(int,input().split()))
for i in range(array[2]):
    query=input().split()
    if query[0]=="NEXT":
        x=int(query[1])
        print(temp_next(array,temp,x))
    elif query[0]=="COUNT":
        y=int(query[1])
        z=int(query[2])
        print(temp_count(array,temp,y,z))



