N,Q,K=map(int, input().split())
follow=[set() for _ in range(N + 1)]
all_messages=[]
time=0
msg_id=0
for _ in range(Q):
    op=input().split()
    if op[0]=='S':
        u=int(op[1])
        v=int(op[2])
        follow[u].add(v)
    elif op[0]=='U':
        u=int(op[1])
        v=int(op[2])
        if v in follow[u]:
            follow[u].remove(v)
    elif op[0]=='B':
        u=int(op[1])
        m=int(op[2])
        time+=1
        msg_id+=1
        critical=(m%3==0)
        all_messages.append([time, msg_id, u, critical])
    elif op[0]=='F':
        u=int(op[1])
        feed=[]
        for msg in all_messages:
            sender=msg[2]
            if sender==u or sender in follow[u]:
                feed.append(msg)
        if len(feed)==0:
            print("EMPTY")
            continue
        feed.sort(key=lambda x: (-x[0], -x[3]))
        count=0
        for msg in feed:
            print(msg[1], end=" ")
            count+=1
            if count==10:
                break
        print()
