def scrambled_keyword_detection(s,p):
    a=len(p)
    b=len(s)
    lst=[]
    for i in range(0,b-a+1):
        if sorted(s[i:i+a])==sorted(p):
            lst.append(i)
    return lst

s='cbaebabacd'
p='abc'
print(scrambled_keyword_detection(s,p))









