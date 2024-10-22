class Solution:
    def hammingWeight(self, n: int) -> int:
        #O(n) solution
        '''
        binary = self.dec2bin(n)
        answer = 0
        for i in binary:
            if i == '1':
                answer += 1
        return answer
        '''
        #O(no of ones) solution
        answer = 0
        while(n>0):
            n = n & (n-1)
            answer += 1
        return answer
        #TC = O(no of ones)
        #SC = O(1)
        
    def dec2bin(self, no):
        if no == 0:
            return ""
        return self.dec2bin(no//2) + str(no%2)
        
        #TC = O(n)
        #SC = O(logn) - recursion stack can have logn calls