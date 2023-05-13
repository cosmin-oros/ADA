def cut_rod(prices, n):
    # initialize list to store maximum profit for each length of rod
    max_profit = [0] * (n + 1)

    # initialize list to store cuts made for each length of rod
    cuts = [0] * (n + 1)

    # iterate over all possible lengths of rod and calculate maximum profit
    for i in range(1, n + 1):
        for j in range(i):
            # calculate maximum profit by cutting the rod at different positions
            if prices[j] + max_profit[i - j - 1] > max_profit[i]:
                max_profit[i] = prices[j] + max_profit[i - j - 1]
                cuts[i] = j + 1

    # generate the sequence of cuts made
    cut_seq = []
    while n > 0:
        cut_seq.append(cuts[n])
        n -= cuts[n]

    # return maximum profit and sequence of cuts
    return max_profit[-1], cut_seq


prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 4
max_profit, cut_seq = cut_rod(prices, n)
print("Maximum profit:", max_profit)
print("Sequence of cuts:", cut_seq)

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 5
max_profit, cut_seq = cut_rod(prices, n)
print("Maximum profit:", max_profit)
print("Sequence of cuts:", cut_seq)

prices = [5, 7, 2, 1, 1, 2, 2, 2, 2, 2]
n = 5
max_profit, cut_seq = cut_rod(prices, n)
print("Maximum profit:", max_profit)
print("Sequence of cuts:", cut_seq)
