def longest_palindromic_substring_simple(s):
    if not s:
        return ""
    n=len(s)
    max_start,max_end=0,0
    def is_palindrome(substring):
        return substring==substring[::-1]
    for start in range(n):
        for end in range(start, n):
            current_substring = s[start:end + 1]
            if is_palindrome(current_substring):
                if end-start>max_end-max_start:
                    max_start,max_end=start, end
    return s[max_start:max_end+1]
input_string=input("Enter the string: ").strip()
print("Longest palindromic substring:", longest_palindromic_substring_simple(input_string))
