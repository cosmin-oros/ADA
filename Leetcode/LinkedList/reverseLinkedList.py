# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # recursive way
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead


def printList(head):
    while head:
        print(head.val)
        head = head.next


sol = Solution()
# 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# reverse the linked list
reversed_head = sol.reverseList(head)

current_node = reversed_head
printList(current_node)
