# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None



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


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# l1 = [2, 4, 3] & l2 = [5, 6, 4]
class Solution(object):
    def addTwoNumbers(self, ll1, ll2):

        carry = 0
        out = ListNode(0)
        last = out

        while ll1 or ll2 or carry:
            val1 = ll1.val if ll1 else 0
            val2 = ll2.val if ll2 else 0
            carry, r = divmod(val1+val2+carry, 10)
            #print(divmod(val1+val2+carry,10))

            last.next = ListNode(r)
            last = last.next

            ll1 = ll1.next if ll1 else None
            ll2 = ll2.next if ll2 else None
            print(last.val)
        return last.next

solve = Solution()
finalsolve = solve.addTwoNumbers(l1, l2)