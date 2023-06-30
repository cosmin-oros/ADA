# Design a time-based key-value data structure that can store multiple values for the same key at different time
# stamps and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure. void set(String key, String value, int timestamp) Stores
# the key key with the value value at the given time timestamp. String get(String key, int timestamp) Returns a value
# such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values,
# it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap(object):

    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, []) # [] default return

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # the first value is the value and the second is the timestamp in the list/ pair
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


timeMap = TimeMap()

timeMap.set("key1", "value1", 100)
timeMap.set("key1", "value2", 200)
timeMap.set("key1", "value3", 300)

timeMap.set("key2", "valueA", 150)
timeMap.set("key2", "valueB", 250)
timeMap.set("key2", "valueC", 350)

print(timeMap.get("key1", 150))  # Output: "value1"
print(timeMap.get("key1", 250))  # Output: "value2"
print(timeMap.get("key1", 400))  # Output: "value3"

print(timeMap.get("key2", 200))  # Output: "" (no values at or before 200)
print(timeMap.get("key2", 300))  # Output: "valueB"
print(timeMap.get("key2", 400))  # Output: "valueC"