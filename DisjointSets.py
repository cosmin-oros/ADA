class DisjointSetForest:
    def __init__(self, size):
        # initialize the parent and rank arrays for the forest
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        # find the root of the set that x belongs to, with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # merge the sets that x and y belong to, with union by rank
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            # if x and y are already in the same set, do nothing
            return
        if self.rank[x_root] < self.rank[y_root]:
            # if the rank of x's root is smaller, merge x's set into y's set
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            # if the rank of y's root is smaller, merge y's set into x's set
            self.parent[y_root] = x_root
        else:
            # if the ranks are equal, merge y's set into x's set and increase x's rank
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def count_groups(n, pairs):
    # create a DisjointSetForest of size n
    dsf = DisjointSetForest(n)

    # merge the sets for each pair of direct friendships
    for a, b in pairs:
        dsf.union(a, b)

    # create a set of the root elements of all the sets in the forest
    # which represents the distinct groups of friends
    groups = set()
    for i in range(n):
        groups.add(dsf.find(i))
        
    # return the number of distinct groups
    return len(groups)


if __name__ == "__main__":
    with open("g_undir_disconn_unweigh_10_9.txt", "r") as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        pairs = []
        for i in range(m):
            a, b = map(int, f.readline().strip().split())
            pairs.append((a, b))
    print(count_groups(n, pairs))
