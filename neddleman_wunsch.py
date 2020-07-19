'''
Needleman Wunsch algorithm implemention
Global alignment of string a to b
'''
def neddle(str1, str2, score):
    m, n = len(str1), len(str2)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1): dp[i][0] = i * score["gap"]
    for j in range(1, n + 1): dp[0][j] = j * score["gap"]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:
                s = score["match"]
            else:
                s = score["mismatch"]

            dp[i][j] = max(
                dp[i-1][j] + score["gap"], 
                dp[i][j-1] + score["gap"],
                dp[i - 1][j - 1] + s
            )

    print(dp)
    return dp[m][n]


if __name__ == "__main__":
    score = {"gap": -2, "mismatch": -1, "match": 2}
    str2 = "ccg"
    str1 = "cgg"
    ans = neddle(str1, str2, score)
    print("Best global alignment score =", ans)