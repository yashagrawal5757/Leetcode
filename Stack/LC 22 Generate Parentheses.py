class Solution:
    def rec(self,n,open,close,output, string):
        if open == 0 and close == 0:
            output.append(string)
            return 
        if open>0:
            self.rec(n,open-1,close, output,string + "(")  #pass open-1, string + "(" dynamically in funcn call. do not update inplace
        if close>open: 
            #we cant use close>0 because for say (), it will allow 
            self.rec(n,open,close-1, output,string + ")")
        
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        open,close = n,n
        string = ""
        self.rec(n, open, close, output, string)
        return output

        