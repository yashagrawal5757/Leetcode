class StockSpanner:

    def __init__(self):
        self.stack = []  #store (c,value)

        self.c = 0  #index for current element
        
        #self.nums = []  #for two stack approach

    def next(self, price: int) -> int:
        self.c += 1 #increase index
        while(self.stack and self.stack[-1][1]<= price):  
            self.stack.pop()
        if len(self.stack) == 0:
            answer = self.c - 0  #if all elements deleted from cth index or when first element inserteed
            self.stack.append((self.c,price))
            return answer
        else:
            answer = self.c - self.stack[-1][0]
            self.stack.append((self.c,price))
            return answer

        # Two stack approach
        '''
        self.nums.append(price)
        #since our logic contains i, we find i -> last index of current list
        i = len(self.nums) -1 
        


        while(len(self.stack)!=1 and price >= self.nums[self.stack[-1]]):
            self.stack.pop()
        result = i - self.stack[-1]
        self.stack.append(i)

        return result
        '''
            


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)