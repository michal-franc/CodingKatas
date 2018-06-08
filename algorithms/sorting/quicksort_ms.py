def swap(items, a, b):
    items[a], items[b] = items[b], items[a]

def swap_g(items, a, b):
    if items[a] > items[b]:
        swap(items, a, b)

def pivot_rec(items, lo, hi):
    mid = lo + (hi - lo) / 2

    //main job of this algorithm is to find two partitions that have itesm greates or smaller that pivot as this ones will be used later with insertion sort
    // making sure that out of this 3 values we take the middle and moving the values in places, beacse we still have to do check
    // so we have a free check
    // this also makes sure that lo and hi and mid are in correct partitions
    swap_g(items, lo, mid)
    swap_g(items, lo, hi)
    swap_g(items, mid, hi)

    pivot = items[mid]

    // We preserve the pivot number for future as we dont want it to be checked 
    swap(items, mid, hi - 1)

    left = lo
    right = hi - 1

    // we go from left and right shuffling items to different partitons
    while left < right:
        while left < (hi - 1):
            left += 1
            if items[left] >= pivot:
                break

        while right > lo:
            right -= 1
            if items[right] < pivot:
                break

        if left >= right:
            break

        swap(items, left, right)

    // we bring back pivot to its original place assuming that item on the left is greater or equal to pivot
    swap(items, left, hi - 1)
    return left

def intro_sort(items, lo, hi):

    while hi > lo:

        part_size = hi - lo + 1

        if part_size == 1:
            return
        if part_size == 2:
            swap_g(items, lo, hi)
            return
        if part_size == 3:
            swap_g(items, lo, hi-1)
            swap_g(items, lo, hi)
            swap_g(items, hi-1, hi)
            return


        // this is were split happens initialy we go through whole array
        // we generate the pivot number and shuffle items to be in two partitions with pivot in the middle
        // then we go to one of the 'partitions'
        // the other partiton will be checked by the next 'while' iterations
        p = pivot_rec(items, lo, hi)
        intro_sort(items, p + 1, hi)
        hi = p - 1


items = [9,8,7,6,5,4,3,2,1,0]
intro_sort(items, 0, 9)
