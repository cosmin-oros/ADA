class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        # slow pointer and faster pointer, s moves one node at a time and fast two at a time
        s, f = head, head

        # if s and f meet each other again it means that it's a cycle
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


sol = Solution()

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(sol.hasCycle(node1))