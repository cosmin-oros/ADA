# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size
# groupSize, and consists of groupSize consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
# return true if she can rearrange the cards, or false otherwise.
import heapq


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            # minimum value
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
sol = Solution()
print(sol.isNStraightHand(hand, groupSize))
