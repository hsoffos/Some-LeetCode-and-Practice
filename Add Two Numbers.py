# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Input: l1 = [2,4,3], l2 = [5,6,4]
if __name__ == '__main__':
    # empty list plus nodes
    l1 = ListNode(2)
    l1second = ListNode(4)
    l1third = ListNode(3)
    l2 = ListNode(5)
    l2second = ListNode(6)
    l2third = ListNode(4)

    # link it all together
    l1.next = l1second
    l1second.next = l1third
    l2.next = l2second
    l2second.next = l2third

    while l1 or l2:
        val1 = l1.val
        val2 = l2.val
        print(val1, val2)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None


