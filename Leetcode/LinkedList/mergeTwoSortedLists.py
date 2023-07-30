# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
#
# Return the head of the merged linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list2 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
sol = Solution()
result = sol.mergeTwoLists(list1, list2)

while result:
    print(result.val, end=" -> ")
    result = result.next