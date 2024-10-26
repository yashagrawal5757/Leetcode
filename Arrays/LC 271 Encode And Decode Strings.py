class Solution:

    def encode(self, strs: List[str]) -> str:
        #Basically encode the string. Keep len(string)# as delimiter
        enc_str = ""
        for string in strs:
            enc_str = enc_str + str(len(string)) + "#"  + string
        return enc_str



    def decode(self, s: str) -> List[str]:
        #
        i = 0
        #Loop
        answer = []
        #Till i is inside length of string
        while(i<len(s)):
            #You want to find out length part (can be >9)
            j = i
            while(s[j]!='#'):
                j+= 1
            #Extract length part
            length = int(s[i:j])
            #from next char to j+1+length
            answer.append(s[j+1:j+1+length])
            #update i
            i = j+1+length
        return answer
            
