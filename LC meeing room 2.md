## pre for quora oa

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required. 

For example, 

Given [[0, 30],[5, 10],[15, 20]], 
return 2. 

basic idea is scanning line 

```

def minMeetingRoom(intervals):
    mark = []
    for intv in intervals:
        mark.append((intv[0],True))
        mark.append((intv[1],False))
    print(mark)
    mark = sorted(mark, key = lambda v: v[0])
    print(mark)
    cnt = 0
    res = 0
    for i in mark:
        if i[1]:
            cnt += 1
        else:
            cnt -= 1
        res = max(cnt,res)
    print(res)
    return res
```
