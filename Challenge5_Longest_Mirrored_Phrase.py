def longest_palindromic_substring(s):
    if not s:
        return ""
    n=len(s)
    max_start,max_end=0,0
    def expand(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    for center in range(n):
        start1,end1=expand(center,center)
        start2,end2=expand(center,center+1)
        if end1-start1>max_end-max_start:
            max_start,max_end=start1,end1
        if end2-start2>max_end-max_start:
            max_start,max_end=start2,end2
    return s[max_start:max_end+1]
input_string=input("Enter the string: ").strip()
print("Longest palindromic substring:", longest_palindromic_substring(input_string))
