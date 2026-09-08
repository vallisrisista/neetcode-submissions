class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        
        for i in range(0,n+1):
            print("checking of i=",i)
            count=0
            while(i):
                print("i value in while", i)
                i=i&(i-1)
                print("i after &:", i)
                count+=1
                print("count =", count)
            res.append(count)
            
                
                
            
        return res
        
        