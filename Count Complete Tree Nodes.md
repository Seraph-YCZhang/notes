Given a complete binary tree, count the number of nodes.

```
     1
  2    3
4  5  6  
```
so if we have a complete binary tree, like this  
Though the value not like this in the problem, we can see them as no.
According to the defination of complete binary tree, there will only be not fully filled in the last layer.  
if left height equals right height, it is a full binary tree, its total nodes is 2 ** d - 1
# Assuming the tree has 'd' depth, there will be 2 ** (d - 1) - 1 nodes in layers but the last one.  
Next step, try to find what node in last layer is the last one.  Like 6 , so we have totally six nodes.  
And we can use binary search to find it. We know that we at least has 2 ** (d - 1) nodes which is 4 in this situtaion. 
And max is 7. In this way, the range is [4, 7].

code is like this
```
class Solution:
  def countNodes(self, root):
    if not root:
        return 0
    def findLeftHeight(node):
    
    def findRightHeight(node):
    
    def has(p, node):
       # some explaination
       # if we want to find 5,
       # from 5 back to root, the path  is 5 -> 2 -> 1
       # if finding 4, it is 4 -> 2 -> 1
       # so if next is double go left , if double plus one, go right
       # we try go from 1 -> target, if find return True, if None, which means it path or tree ends before target, we return False
       k = p
       path = []
       while k > 0:
        path.append(k)
        k // = 2
       for i in range(len(path) - 1, -1, -1):
        if node == None: 
          return False
        if path[i] == p:
          return True
        if path[i-1] == path[i] * 2:
           node = node.left
        else:
            node = node.right
            
    left_height = findLeftHeight(root)
    right_height = findRightHeight(root)
    if left_height == right_height:
      return pow(2,left_height) - 1
    # do binary search
    left = pow(2, right_height) 
    right = pow(2, left_height) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if has(mid, root):
        left = mid + 1
      else:
        right = mid - 1
     # [4,5,6,None] => [6,None] => mid = 6 , left = 6 + 1 => return left - 1
     return left - 1
     
```

we also have a recursive way to solve this.

```
def countNodes(self, root):
  l,r = findLeft(root), findRight(root)
  if l == r:
    return pow(2,l) - 1
  else:
    return self.countNodes(root.left) + self.countNodes(root.right) + 1
```
