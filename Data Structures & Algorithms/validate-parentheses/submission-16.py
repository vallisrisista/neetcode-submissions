class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        for i in s:

            if(i=='(' or i=='{' or i == '['):
                print("i=",i)
                stack.append(i)
                print("in if, stack=", stack)
            elif(i==')' or i=='}' or i == ']'):
                if not stack:
                    return False
                top=stack[-1]
                if((i==')' and top=='(') or (i=='}' and top=='{') or (i==']' and top=='[')):
                    print("in else, popping=", stack[-1])
                    stack.pop()
                else:
                    return False
        if not stack:
            return True

        else:
            return False
        
           
        
    



        '''
        left=0
        right=len(s)-1
        while(left<right):
            if((s[left]=='(' and s[right]==')') or ((s[left]=='[' and s[right]==']')) or (s[left]=='{' and s[right]=='}')):
                left+=1
                right-=1
            else:
                return False
        return True
        '''
        