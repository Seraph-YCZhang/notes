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

## Hamming Distance
version 1
```python
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_ = bin(x).replace('0b','')
        y_ = bin(y).replace('0b','')
        len_x = len(x_)
        len_y = len(y_)
        if len_x!=len_y:
            if len_x>len_y:
                y_ = y_.zfill(len_x)
                length = len_x
            else:
                x_ = x_.zfill(len_y)
                length = len_y
        else:
            length = len_x
        count = 0
        for i in range(length):
            if x_[i]!=y_[i]:
                count += 1
        return count
 ```

        
