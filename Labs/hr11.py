def isPalindrome(s):
    
    s1=s.lower()
    n=len(s1)
    s2=s1[::-1]
    
    if s1==s2:
        return 1
    else:
        return 0

s=input()
print(isPalindrome(s))
