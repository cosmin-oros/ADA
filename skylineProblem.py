def merge(left, right):
    # Merge two skylines into one.
    i, j = 0, 0
    left_h, right_h = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x, left_h = left[i]
            i += 1
        else:
            x, right_h = right[j]
            j += 1
        h = max(left_h, right_h)
        if not result or h != result[-1][1]:
            result.append((x, h))
    result += left[i:] + right[j:]
    return result


def skyline(buildings):
    # Divide and conquer approach to the skyline problem.
    n = len(buildings)
    if n == 0:
        return []
    if n == 1:
        left, right, height = buildings[0]
        return [(left, height), (right, 0)]
    mid = n // 2
    left = skyline(buildings[:mid])
    right = skyline(buildings[mid:])
    return merge(left, right)


buildings = [(2, 9, 10), (3, 6, 15), (5, 12, 12), (13, 16, 10), (15, 17, 5)]
result = skyline(buildings)
print(result)
