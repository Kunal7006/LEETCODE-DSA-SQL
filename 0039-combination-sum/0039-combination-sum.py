class Solution:
    def solve(self,idx,target,candidates,ans,ds):
        if idx == len(candidates):
            if target ==0:
                ans.append(ds.copy())
            return
        
        if candidates[idx]<=target:
            ds.append(candidates[idx])
            self.solve(idx,target-candidates[idx],candidates,ans,ds)
            ds.pop()
        
        self.solve(idx+1,target,candidates,ans,ds)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans =[]
        ds =[]
        self.solve(0,target,candidates,ans,ds)
        return ans