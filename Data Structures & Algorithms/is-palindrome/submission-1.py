class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while(left<right):
            print("s[left] = " , s[left], "s[right] = ", s[right])
            if(not s[left].isalnum()):
                print("incemented left")
                left+=1
                continue
            if(not s[right].isalnum()):
                print("decremented right")
                right-=1
                continue
            if(s[left].lower()==s[right].lower()):
                print("Equal: s[left] = " , s[left], "s[right] = ", s[right])
                left+=1
                right-=1
                continue
            if(s[left].lower()!=s[right].lower()):
                print("not equal: s[left] = " , s[left], "s[right] = ", s[right])
                return False
        return True
            