from collections import deque
def add_subscription(subs,user,target):
    subs[user].add(target)
def remove_subscription(subs,user,target):
    subs[user].discard(target)
def broadcast_message(msgs,user,value,time,msg_id,limit):
    critical=(value%3==0)
    msgs[user].append((time,msg_id,critical))
    if len(msgs[user])>limit:
        msgs[user].popleft()
def get_feed(user,subs,msgs):
    feed=[]
    for followed in subs[user]:
        feed.extend(msgs[followed])
    return feed
def print_feed(feed):
    if not feed:
        print("EMPTY")
        return
    feed.sort(key=lambda x:(-x[0],-x[2]))
    ans=[]
    for i in range(min(10,len(feed))):
        ans.append(str(feed[i][1]))
    print(" ".join(ans))

units,operations,max_msgs=map(int, input().split())
follow_list=[set() for _ in range(units+1)]
user_msgs=[deque() for _ in range(units+1)]
time_counter=0
msg_counter=0
for _ in range(operations):
    cmd=input().split()
    if cmd[0]=='S':
        u=int(cmd[1])
        v=int(cmd[2])
        add_subscription(follow_list,u,v)
    elif cmd[0]=='U':
        u=int(cmd[1])
        v=int(cmd[2])
        remove_subscription(follow_list,u,v)
    elif cmd[0]=='B':
        u=int(cmd[1])
        m=int(cmd[2])
        time_counter+=1
        msg_counter+=1
        broadcast_message(user_msgs,u,m,time_counter,msg_counter,max_msgs)
    elif cmd[0]=='F':
        u=int(cmd[1])
        feed_data=get_feed(u,follow_list,user_msgs)
        print_feed(feed_data)
