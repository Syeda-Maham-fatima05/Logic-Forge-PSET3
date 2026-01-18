def count_boats(w,p,lim):
    arr=[]
    for i in range(len(w)):
        arr.append([w[i],p[i]])
    arr.sort()
    i=0
    j=len(arr)-1
    boat=0
    while i<=j:
        if i<j:
            if arr[i][0]+arr[j][0]<=lim and not (arr[i][1]==1 and arr[j][1]==1):
                i+=1
                j-=1
            else:
                j-=1
        else:
            j-=1
        boat+=1
    return boat
def left_people(w,p,lim,B):
    arr=[]
    for i in range(len(w)):
        arr.append([w[i],p[i]])
    arr.sort()
    n=len(arr)
    used=[0]*n
    boat=0
    taken=0
    for i in range(n):
        if boat==B:
            break
        if used[i]==1:
            continue
        for j in range(i+1,n):
            if used[j]==0:
                if arr[i][0]+arr[j][0]<=lim and not (arr[i][1]==1 and arr[j][1]==1):
                    used[j]=1
                    taken+=2
                    break
        else:
            taken+=1
        used[i]=1
        boat+=1
    return len(w)-taken


n,q,limit=map(int, input().split())
weight=list(map(int, input().split()))
priority=list(map(int, input().split()))
min_boat = count_boats(weight, priority, limit)
print("Minimum boats =",min_boat)
for _ in range(q):
    query=input().split()
    if query[0]=="CANPAIR":
        x=int(query[1])
        y=int(query[2])
        if weight[x]+weight[y]<=limit and not (priority[x]==1 and priority[y]==1):
            print("Yes")
        else:
            print("No")
    else:
        B=int(query[1])
        if B>=min_boat:
            print(0)
        else:
            print(left_people(weight,priority,limit,B))
