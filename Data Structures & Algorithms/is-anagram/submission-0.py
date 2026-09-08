class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_a={}
        dict_b={}
        dict_a={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,
                'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,
                's':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
        }
        dict_b={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,
                'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,
                's':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
        }
        for ch in s:
            dict_a[ch]+=1
        for ch in t:
            dict_b[ch]+=1
        if(dict_a==dict_b):
            return True
        else:
            return False
