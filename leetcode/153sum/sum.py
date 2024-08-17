# two pointers
# time O(n^2)
# space O(1)
def threeSum(nums):

    nums.sort()
    sol = []

    for a in range(0, len(nums) - 2):

      if nums[a] > 0:
        return sol  

      b = a + 1  
      c = len(nums) - 1 

      while b < c:
        if (nums[a] + nums[b] + nums[c]) == 0 and [nums[a], nums[b], nums[c]] not in sol:
          sol.append((nums[a], nums[b], nums[c]))
        
        if nums[a] + nums[b] + nums[c] > 0: 
          c -= 1
        else:
          b += 1

    return list(set(sol))


# assuming we dont need indexes provided but just values
# time O(n^2)
# space O(3n)
def threeSum_sets(data):

    if len(data) < 3:
        return []

    if len(data) == 3:
        if data[0] + data[1] + data[2] == 0:
            return [(data[0], data[1], data[2])]
        else:
            return []

    res = set()

    # O(n): divide the numbers to negative, positive and zeros
    n, p, z = [], [], []
    for num in data:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    # O(n) sets here will make lookup to be O(1)
    N, P = set(n), set(p)

    # O(n)
    if z:
        for num in P:
            if -num in N:
                res.add((-num, 0, num))

    # if we have three zeros then this is valid solution too
    if len(z) >= 3:
        res.add((0,0,0))

    # O(n^2)
    for  i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -(n[i]+n[j])
            if target in P:
                # sorted here + set will ensure no duplicates
                res.add(tuple(sorted((n[i], n[j], target))))
    
    # O(n^2)
    for  i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -(n[i]+n[j])
            if target in N:
                # sorted here + set will ensure no duplicates
                res.add(tuple(sorted((n[i], n[j], target))))

    return list(res)
