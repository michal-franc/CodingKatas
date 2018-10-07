import unittest

# Keep next free index in separate array, check this arraay where to put new item on push
# Initialize array with a default size and double the size if we reach out of bound
# This solution is simple but creates a lot of unused space when only one stack increases
# [1, None, None, 2, None, None, 3, None, None, 4]
#
# It is not space efficcient but time efficient as apart from growing and resizing
# all pop, push operations will be O(1) only when we hit the imit there is some
# Amortization as we need to spend more time growing the array

# [stack1 stack2 stack3 .. stack3 stack1 ..]
class ThreeStacksNotMemOptimized(object):
    def __init__(self):
        default_size = 10
        self.index = [0, 0, 0]
        self.arr = [None] * default_size

    def __get_index(self, number):
        local_number = number - 1
        return (self.index[local_number] * 3) + local_number

    def __double_size(self):
        new_length = len(self.arr)
        self.arr = self.arr + ([None] * new_length)

    def push(self, number, item):
        index = self.__get_index(number)

        if index >= len(self.arr):
            self.__double_size()

        self.arr[self.__get_index(number)] = item
        self.index[number - 1] += 1

    def pop(self, number):
        self.index[number - 1] -= 1

        if self.index[number - 1] < 0:
            self.index[number - 1] = 0

        item = self.arr[self.__get_index(number)]
        self.arr[self.__get_index(number)] = None
        return item

#
# More efficient solution maintains start and capacity of each stack and position them in the array
# whenever you reach the end you shift the array and insert new empty space
# [stack1...stack1 stack2...stack2 stack3...stack3]
# [stack1...........stack1 stack2...stack2 stack3...stack3]
# each part can grow independently
#

class StackInfo(object):
    def __init__(self, start, initial_size):
        self.start = start
        self.capacity = initial_size
        self.index = 0

    def should_grow(self):
        return self.index >= self.capacity

    def grow_double(self):
        self.capacity = self.capacity * 2

    def get_next_index(self):
        return self.start + self.index

    def inc_index(self):
        self.index += 1

    def dec_index(self):
        self.index -= 1

        if self.index <= 0:
            self.index = 0

class MultiStack(object):
    def __init__(self, number_of_stacks):
        default_size = 10
        self.number_of_stacks = number_of_stacks
        self.arr = [None] * (self.number_of_stacks * default_size)
        self.info = []

        for i in range(number_of_stacks):
            initial_start = (i * default_size)
            self.info.append(StackInfo(initial_start, default_size))

    def __grow_and_shift(self, n_stack):
        grow_stack = self.info[n_stack]

        # growing first stack
        if n_stack == 0:
            new_arr = self.arr[:grow_stack.capacity] + ([None] * grow_stack.capacity) + self.arr[grow_stack.capacity:]

            self.arr = new_arr

            # shift start positions of other stacks
            for i in self.info[1:]:
                i.start += grow_stack.capacity

        # growing last stack
        elif n_stack == len(self.info) - 1:
            self.arr = self.arr + ([None] * grow_stack.capacity)
        # growing middle stack
        else:
            end_of_current_stack = grow_stack.start + grow_stack.capacity
            new_arr = self.arr[:end_of_current_stack] + ([None] * grow_stack.capacity) + self.arr[end_of_current_stack:]

            # shift start positions of other stacks
            for i in self.info[n_stack + 1:]:
                i.start += grow_stack.capacity

            self.arr = new_arr

        grow_stack.grow_double()

    def push(self, n_stack, new_item):
        stack_info = self.info[n_stack]
        if stack_info.should_grow():
            self.__grow_and_shift(n_stack)

        index = stack_info.get_next_index()
        self.arr[index] = new_item
        stack_info.inc_index()


    def pop(self, n_stack):
        stack_info = self.info[n_stack]
        stack_info.dec_index()
        index = stack_info.get_next_index()
        item = self.arr[index]
        self.arr[index] = None
        return item

class FuncTest(unittest.TestCase):

    def test_three_stack_grow_middle(self):
        sut = MultiStack(3)

        for i in range(4):
            sut.push(2, i)

        for i in range(20):
            sut.push(1, 200 + i)

        for i in range(30):
            sut.push(0, i)

    def test_two_stack_grow_1st(self):
        sut = MultiStack(2)

        for i in range(10):
            sut.push(1, 100 + i)

        for i in range(40):
            sut.push(0, i)

        for i in range(10):
            sut.push(1, 100 + i)

    def test_two_stack_grow_2nd(self):
        sut = MultiStack(2)

        for i in range(12):
            sut.push(1, 10 + i)

        for i in range(11, -1, -1):
            self.assertEqual(sut.pop(1), 10 + i)

        for i in range(22):
            sut.push(1, 10 + i)


    def test_two_stack(self):
        sut = MultiStack(2)
        sut.push(0, 10)
        sut.push(0, 20)
        sut.push(0, 30)
        sut.push(1, 11)
        sut.push(1, 21)
        sut.push(1, 31)

        self.assertEqual(sut.pop(0), 30)
        self.assertEqual(sut.pop(0), 20)
        self.assertEqual(sut.pop(0), 10)
        self.assertEqual(sut.pop(0), None)
        self.assertEqual(sut.pop(1), 31)
        self.assertEqual(sut.pop(1), 21)
        self.assertEqual(sut.pop(1), 11)
        self.assertEqual(sut.pop(1), None)

    def test_one_stack_grow(self):
        sut = MultiStack(1)
        sut.push(0, 1)
        sut.push(0, 2)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)
        sut.push(0, 3)

        self.assertEqual(sut.pop(0), 3)
        self.assertEqual(sut.pop(0), 3)
        self.assertEqual(sut.pop(0), 3)

    def test_one_stack(self):
        sut = MultiStack(1)
        sut.push(0, 1)
        sut.push(0, 2)
        sut.push(0, 3)

        self.assertEqual(sut.pop(0), 3)
        self.assertEqual(sut.pop(0), 2)
        self.assertEqual(sut.pop(0), 1)
        self.assertEqual(sut.pop(0), None)
