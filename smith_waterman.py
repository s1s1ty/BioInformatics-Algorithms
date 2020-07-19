'''
Smith waterman algorithm for local allignment
overall global score will be >= 0
'''


def smith_waterman(seq1, seq2, score):
    '''Calculated score matrix for given sequence and scoring schema. 
    '''
    row, col = len(seq1), len(seq1)
    max_score = 0
    matrix = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            similarity = score["match"] if str1[i - 1] == str2[j - 1] else score["mismatch"]

            score_matrix = max(
                0,
                matrix[i - 1][j] + score["gap"],
                matrix[i][j - 1] + score["gap"],
                matrix[i - 1][j - 1] + similarity
            )
            matrix[i][j] = score_matrix
            max_score = max(score_matrix, max_score)
    
    return matrix, max_score

def print_matrix(martix):
    '''Print calculated scoring matrix.
    '''
    print("Smith Waterman matrix :")
    for r in matrix:
        print(r, sep=", ")

def main():
    score = {"gap": -2, "mismatch": -1, "match": 2}
    str2 = "ccg"
    str1 = "cgg"
    matrix, max_score = smith_waterman(str1, str2, score)
    print_matrix(matrix)
    print("Local alignment score =", max_score)


if __name__ == "__main__":
    main()



