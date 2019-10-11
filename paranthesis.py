class check():
    def validate(self,para):
        d={'(':')','[':']','{':'}'}
        s=[]
        for i in para:
            if i in d:
                s.append(i)
            elif(len(s)==0 or d[s.pop()]!=i):
                return False
        return len(s)==0
strng=input()
print(check().validate(strng))
    

        
