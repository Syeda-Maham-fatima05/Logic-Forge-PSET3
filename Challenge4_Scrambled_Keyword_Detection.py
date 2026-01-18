def scrambled_keyword_detection(s,p):
    if len(p)>len(s):
        return []
    res=[]
    p_count={}
    for ch in p:
        p_count[ch]=p_count.get(ch,0)+1
    window_count={}
    left=0
    for right in range(len(s)):
        window_count[s[right]]=window_count.get(s[right],0)+1
        if right-left+1>len(p):
            window_count[s[left]]-=1
            if window_count[s[left]]==0:
                del window_count[s[left]]
            left+=1
        if window_count==p_count:
            res.append(left)
    return res
s="cbaebabacd"
p="abc"
print(scrambled_keyword_detection(s, p))








