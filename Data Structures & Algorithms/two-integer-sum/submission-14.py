class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        seen={}
        for index,num in enumerate(nums):
            complement=target-num
            if(complement in seen):
                
                return [seen[complement],index]
            
            seen[num]=index
        
        return []

        '''
        i,j=0,0
        for i in range (0,len(nums)):
            for j in range (i,len(nums)):
                if(i!=j):
                    if(nums[i]+nums[j]==target):
                        print(i,j)
                        result.append(i)
                        result.append(j)
                        return result
                    
                
                j+=1
            i+=1
        '''


        