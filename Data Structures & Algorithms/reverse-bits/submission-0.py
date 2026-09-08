class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary_list = [int(bit) for bit in f"{n:032b}"]
        i,j=0,31
        res=[0]*32
        for b in binary_list:
            res[i]=binary_list[j]
            i=i+1
            j=j-1
            number = int("".join(map(str, res)), 2)
        return number
        