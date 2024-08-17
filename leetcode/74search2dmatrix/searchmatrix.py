# this is like binary search but the array is split into multiple dimensions

# 1 - merge array to single array and transform the problem to binary searchMatrix
# - this will take O(n) and we will lose the value of binary search
# - in this scenario it would be just better to `scan` the whole array in one pass as it would also take O(n)

# 2 - log n*m
# - just use simple binary search and hide the 2d matrix complexity behind simple translation layer
def searchMatrix(matrix, target):
    lenX = len(matrix)
    lenY = len(matrix[0])
    
    left = 0
    right = (lenX * lenY) - 1
    while left <= right:
        pivot = (left+right)//2
        
        translationX = pivot // lenY
        translationY = pivot % lenY

        num = matrix[translationX][translationY]

        if ( num == target):
            return True

        if (num < target):
            left = pivot + 1
        else:
            right = pivot - 1

    return False
