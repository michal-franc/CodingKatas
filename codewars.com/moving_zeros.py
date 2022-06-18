from simple_unittest  import test

def moving_zeros(a):

    # loop thropugh list with O(n)
    # if zero found increase counter of zeros

    zeros_count = 0;
    for i in range(len(a)):
        if a[i] == 0:
            zeros_count += 1;
        else:
            a[i-zeros_count] = a[i];

            # if we are on first index and there is no zero we should zero it as there will be no shift yet
            # we can zero in this value as its preseverd after shift and will be overwritter later
            if zeros_count != 0:
                a[i] = 0;

    return a

test('[0]', moving_zeros([0]), [0]);
test('[0, 1]', moving_zeros([0, 1]), [1, 0]);
test('[0, 1, 2, 3, 3, 4, 5, 6]', moving_zeros([0, 1, 2, 3, 3, 4, 5, 6]), [1, 2, 3, 3, 4, 5, 6, 0]);
test('', moving_zeros( [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), 
                       [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);

    
