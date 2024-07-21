from simple_unittest import test

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return ''.join(['%s->' % self.val, str(self.next)])
        else:
            return '%s' % self.val
def is_even(number):
    return number % 2 == 0

def swap(pair_first, pair_second):

    # this is to cover 1 element 'linked list'
    if pair_second is None:
        return pair_first

    # this is node returned from next pair
    next_pair_first = None

    # we check if another pair is possible
    if pair_second.next and pair_second.next.next:
        next_pair_first = swap(pair_second.next, pair_second.next.next)
    # if its not possible then we check if the last element is 'odd' -> doesnt have pair
    elif pair_second.next:
        # this is the next pair element
        next_pair_first = pair_second.next

    # we swap pairs
    pair_second.next = pair_first
    pair_first.next = next_pair_first

    # this is new entry point to this pair
    return pair_second

head_node = ListNode(1)
head_node.next = ListNode(2)
head_node.next.next = ListNode(3)
head_node.next.next.next = ListNode(4)
head_node.next.next.next.next = ListNode(5)

print head_node

new_head = swap(head_node, head_node.next)

print new_head
