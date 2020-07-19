'''
Edit distance:
Minimum number of edit(insertion , deletion, substitution)
to covert one string to another one.
'''

def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1): dp[i][0] = i
    for j in range(1, n + 1): dp[0][j] = j

    score = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] != str2[j - 1]:
                score = 1
            else:
                score = 0

            dp[i][j] = min(
                dp[i-1][j] + 1, 
                dp[i][j-1] + 1,
                dp[i - 1][j - 1] + score 
            )

    return dp[m][n]


if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    ans = edit_distance(str1, str2)
    print("Minimum number of edit =", ans)