class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ""
        for char in s:
            '''
            if char.isalnum():
                s_new = s_new + char
            '''
            #If alnum not allowed, check ascii
            if ord(char) in range(48,58) or ord(char) in range(65,91) or ord(char) in range(97,123):
                s_new = s_new + char
                            #digits                 #uppercase                          #lower case
        #two pointer technique
        i, j = 0,len(s_new)-1
        while(i<j):
            if s_new[i] == s_new[j]:
                i+= 1
                j-= 1
            else:
                return False
        return True
            
        