class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def rec(candidates, target, subset,index, output):
            if target == 0: 
                output.append(subset[:])
                return output
            if target<0:
                return
            if index == len(candidates):
                return 

            subset.append(candidates[index])
            rec(candidates, target - candidates[index],subset,index, output )
            subset.pop()
            rec(candidates, target, subset, index+1, output)

        rec(candidates, target, [], 0,output)
        return output
        