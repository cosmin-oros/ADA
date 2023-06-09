def lps(s):
    n = len(s)

    # a[i] is going to store length
    # of longest palindromic subsequence
    # of substring s[0..i]
    a = [0] * n

    # Pick starting point
    for i in range(n - 1, -1, -1):

        back_up = 0

        # Pick ending points and see if s[i]
        # increases length of longest common
        # subsequence ending with s[j].
        for j in range(i, n):

            # similar to 2D array L[i][j] == 1
            # i.e., handling substrings of length
            # one.
            if j == i:
                a[j] = 1

                # Similar to 2D array L[i][j] = L[i+1][j-1]+2
            # i.e., handling case when corner characters
            # are same.
            elif s[i] == s[j]:
                temp = a[j]
                a[j] = back_up + 2
                back_up = temp

            # similar to 2D array L[i][j] = max(L[i][j-1],
            # a[i+1][j])
            else:
                back_up = a[j]
                a[j] = max(a[j - 1], a[j])

    return a[n - 1]


string = "character"
print(lps(string))
