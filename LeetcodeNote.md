# Statistic
    Total 8 Easy 8 Medium 0 Hard 0
    
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
version 2
```python
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
```

## Unique Email Addresses
version 1 76ms
```python
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        act_emails = set({})
        for str in emails:
            pos = str.index('@')
            # print(pos)
            str_l = str[0: pos]
            str_r = str[pos+1:]
            pos_ = str_l.index('+')
            str_l = str_l[0:pos_]
            str_l = str_l.replace('.', '')
            act_emails.add(str_l+'@'+str_r)
        return len(act_emails)
```
## To Lower Case
version 1 48ms
```python
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()
```
method 2
```
using ord() to get ASC II number of the character 
then plus 32 to each for getting the lower case
chr() asc II => character
```

##  N-Repeated Element in Size 2N Array
version 1 112ms
```python
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        half = 0.5 * length
        list_ = [0]*(max(A)+1)
        for _ in A:
            # print(_)
            list_[_] += 1
        return list_.index(half)
```
version 2 84ms
```python 
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return int((sum(A)-sum(set(A)))/(len(A)/2-1))
```
Offical solution 1 84ms:

collections.counter:A counter is a container that 

stores elements as dictionary keys, and their counts are stored as dictionary values.
```python
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
```
## Sort Array By Parity
```python
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        List = []
        for num in A:
            if num%2 == 0:
                List.append(num)
        for num in A:
            if num%2 != 0:
                List.append(num)
        return List
```
## flipping-an-imag
method 1 80ms
```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for line in A:
            line.reverse()
            # print(line)
            for num in range(0,len(line)):
                line[num] = line[num] ^ 1
        return A
```
method 2 72ms
```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 - num for num in line[::-1]]for line in A]

```
