class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        target=0
        for i in range(0,len(prices)):
            print("i= ",i)
            buy=prices[i]
            print("buy= ",buy)
            for  j in range(i+1,len(prices)):
                print("j= ",j)
                if(prices[j]>buy):
                    print("price is greater than buy= ",prices[j])
                    if(target<prices[j]-buy):
                        target=prices[j]-buy
                        print("target",target)
        return target
        


            
        