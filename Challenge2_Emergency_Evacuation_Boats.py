def count_boats(w, p, lim):
    n=len(w)
    used=[0] * n
    boat=0
    for i in range(n):
        if used[i]==1:
            continue
        used[i]=1
        paired=0
        for j in range(i+1,n):
            if used[j]==0:
                if w[i]+w[j]<=lim and not (p[i]==1 and p[j]==1):
                    used[j]=1
                    paired=1
                    break
        boat+=1
    return boat
def left_people(w,p,lim,B):
    n=len(w)
    used=[0] * n
    boat=0
    for i in range(n):
        if boat==B:
            break
        if used[i]==1:
            continue
        used[i]=1
        paired=0
        for j in range(i+1,n):
            if used[j]==0:
                if w[i]+w[j]<=lim and not (p[i]==1 and p[j]==1):
                    used[j]=1
                    paired=1
                    break
        boat+=1
    left=0
    for x in used:
        if x==0:
            left+=1
    return left


n, q, limit=map(int, input().split())
weight=list(map(int, input().split()))
priority=list(map(int, input().split()))
min_boat=count_boats(weight, priority, limit)
print("Minimum boats =",min_boat)
for _ in range(q):
    query=input().split()
    if query[0] == "CANPAIR":
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
