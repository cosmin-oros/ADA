# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to
# see the 10 most recent tweets in the user's news feed.
#
# Implement the Twitter class:
#
# Twitter() Initializes your twitter object. void postTweet(int userId, int tweetId) Composes a new tweet with ID
# tweetId by the user userId. Each call to this function will be made with a unique tweetId. List<Integer>
# getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed
# must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to
# least recent. void follow(int followerId, int followeeId) The user with ID followerId started following the user
# with ID followeeId. void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing
# the user with ID followeeId.
import heapq
from collections import defaultdict


class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow(1, 2)
obj.postTweet(2, 6)
param_3 = obj.getNewsFeed(1)
print(param_3)
obj.unfollow(1, 2)
param_4 = obj.getNewsFeed(1)
print(param_4)