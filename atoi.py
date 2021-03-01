class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)<=1:
            if len(s)==0:
                return 0
            else:
                if s.isdigit():
                    return int(s)
                else:
                    return 0
        neg = False
        dec = False
        if s[0:2] == "+-" or s[0:2] == "-+":
            return 0
        if s[0] == '-':
            neg = True
            s = s[1:]
        if s[0] == '+':
            s=s[1:]
        if s[0].isdigit()==False:
            return 0
        while s[0]=="0":
            s = s[1:]
            if len(s) ==0:
                return 0
            
            
        index =0
        if s[0].isdigit()==False:
            return 0
        middleofdigit = False
        if int(s.isdigit()) == False:
            for i in s:
                if i.isdigit()==False:
                    middleofdigit=True
                    index = s.index(i)
                    if i == ".":
                        dec = True
                        middleofdigit = False
                        continue
                    s = s[0:s.index(i)] + s[s.index(i)+1:]
                else:
                    if middleofdigit:
                        s = s[0:index]
                        break
                        
                        
                        
                        
        if dec:
            r = int(float(s))
        else:
            r = int(s)
        max =2**31 -1
        min= -2**31
        if neg:
            r*=-1
        if r > max:
            r = max
        if r < min:
            r = min
        
        return r
