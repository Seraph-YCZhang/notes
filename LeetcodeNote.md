## Two Sum
```python
def twoSum(self, nums, target):
    length = len(nums)
    for i in range(length-1):
        for j in range(i+1,length):
            if nums[i]+nums[j]==target:
                    return i,j
                    break
```
 ## Jewels and stones
 ```python
 class Solution_1:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for str_1 in J:
            if str_1 in S:
                for str_2 in S:
                    if str_2 == str_1:
                        num += 1
        return num
```
				

        
