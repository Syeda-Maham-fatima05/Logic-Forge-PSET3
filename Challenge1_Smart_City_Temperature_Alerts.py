def smart_city_alerts(N,K,temps,queries):
    next_hot=[0]*N
    stack=[]
    for i in range(N-1,-1,-1):
        while stack and temps[stack[-1]]<temps[i]+K:
            stack.pop()
        next_hot[i]=stack[-1]+1 if stack else 0
        stack.append(i)
    next_cold=[0]*N
    stack=[]
    for i in range(N-1,-1,-1):
        while stack and temps[stack[-1]]>temps[i]-K:
            stack.pop()
        next_cold[i]=stack[-1]+1 if stack else 0
        stack.append(i)
    alert=[0]*N
    for i in range(N):
        if next_hot[i] and next_cold[i]:
            alert[i]=min(next_hot[i]-1,next_cold[i]-1)
        elif next_hot[i]:
            alert[i]=next_hot[i]-1
        elif next_cold[i]:
            alert[i]=next_cold[i]-1
    pref=[0]*N
    pref[0]=1 if alert[0]!=0 else 0
    for i in range(1, N):
        pref[i]=pref[i-1]+(1 if alert[i]!=0 else 0)
    results=[]
    for q in queries:
        parts=q.split()
        if parts[0]=="NEXT":
            x=int(parts[1])
            results.append(str(alert[x]) if alert[x]!=0 else "No Alert")
        elif parts[0]=="COUNT":
            L, R=int(parts[1]),int(parts[2])
            count=pref[R]-(pref[L-1] if L> 0 else 0)
            results.append(str(count))
    return results
N,K,Q=8,3,2
temps=[73,74,75,71,69,72,76,73]
queries=["NEXT 3","COUNT 0 7"]
output=smart_city_alerts(N,K,temps,queries)
for line in output:
    print(line)



