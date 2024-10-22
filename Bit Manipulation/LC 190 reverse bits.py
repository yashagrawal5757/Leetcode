class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        binary = self.int_binary(n)
        appended_str = (32-len(binary))*'0'+binary

        sum = 0
        for i in range(0,len(appended_str)):
            sum =sum + (int(appended_str[i])* (2**i))
        return sum
        '''
        #using inbuilt methods
        binary = bin(n)[2:]
        appended_str = (32-len(binary))*'0'+binary
        rev = appended_str[::-1]
        return int(rev,2)


    def int_binary(self,n):
        if n==0:
            return ""
        return self.int_binary(n//2) + str(n%2)

    
        