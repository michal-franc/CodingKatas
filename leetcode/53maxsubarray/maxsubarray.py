def maxSubArray(arr):
    # nums = [-2,1,-3,4,-1,2,1,-5,4]

    # observation 1:
    # if we move left to right - and we see negative value 
    # then its not a big deal if preeceding sum is highe
    # then we can take this value with no problem

    # 1. take whole array as 3+1>-2, -2 is not significant enough
    # 3, 1, -2, 4    
    # 2. ignore -2 and preeceding numbers it would have negative impact on sum
    # 1, -2, 4     

    # observation 2:
    # minus number can be a only take into account if number before or after compensate it

    highestSum = current = arr[0]

    for x in arr[1:]:
        current = max(x, current + x)
        highestSum = max(current, highestSum)


    return highestSum
