import time
import matplotlib.pyplot as plt

def lcs(X, Y, m, n):#return the length of the longest common subsequence
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1)
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


def lcs_word(s1, s2):#return the longest common subsequence
    # rows -> s1 , cols -> s2
    rows = len(s1) + 1
    cols = len(s2) + 1

    # row0 and col0 will be 0 as they will signify null strings
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):

            # if the chars match, go for left-top diagonal value + 1
            if s1[i - 1] == s2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            # otherwise get max of top or left
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

    # length of longest common sub-sequence
    # return dp_array[rows-1][cols-1]

    # store the common sequence (will be stored in reverse)
    sub_sequence = []

    i = rows - 1
    j = cols - 1

    # find the lcs
    while i > 0 and j > 0:
        # if top is not equal, that means present char was used
        if dp_array[i][j] != dp_array[i - 1][j]:
            sub_sequence.append(s1[i - 1])
            i -= 1
            j -= 1
        # not used
        else:
            i -= 1

    # return length of lcs, list of char containing the lcs elements
    return sub_sequence[::-1]#dp_array[rows - 1][cols - 1]

#x = int(input("Please enter number of sequences: "))
#arr = []
#for i in range(x):
#    word = input("Please enter the words")
#    arr.append(word)

#arr = ["ABCDEFG", "ABCDEF", "ABCDE", "ABCD"]
#arr = ["AGGT12", "12TXAYB", "A2XBA"]
"""
i = 0
if len(arr) % 2 == 0:
    while i < len(arr):
        if i + 1 < len(arr) - 1 or len(arr) % 2 == 0:
            if i + 1 < len(arr):
                m = len(arr[i])
                n = len(arr[i + 1])
                k = lcs_word(arr[i], arr[i + 1])  # arr[i] =
                a = ""
                for z in range(len(k)):
                    a = a + k[z]
                arr[i] = a
                k = arr.pop(i + 1)
                i += 1
            else:
                break
        else:
            arr[i] = arr[i + 1]
            k = arr.pop(i + 1)
            i = 0
else:
    while i < len(arr):
        if i + 1 < len(arr) - 1 or len(arr) % 2 == 0:
            if i + 1 < len(arr):
                m = len(arr[i])
                n = len(arr[i + 1])
                k = lcs_word(arr[i], arr[i + 1])  # arr[i] =
                a = ""
                for z in range(len(k)):
                    a = a + k[z]
                arr[i] = a
                # k = arr.pop(i + 1)
                i += 1
            else:
                break
        else:
            arr[i] = arr[i + 1]
            k = arr.pop(i + 1)
            i = 0
    k = arr.pop(1)
print("Length of LCS:", len(arr[0]))
"""
arr = []
def multiple_sequence_LCS(arr):
    i = 0
    if len(arr) % 2 == 0:
        while i < len(arr):
            if i + 1 < len(arr) - 1 or len(arr) % 2 == 0:
                if i + 1 < len(arr):
                    m = len(arr[i])
                    n = len(arr[i + 1])
                    k = lcs_word(arr[i], arr[i + 1])  # arr[i] =
                    a = ""
                    for z in range(len(k)):
                        a = a + k[z]
                    arr[i] = a
                    k = arr.pop(i + 1)
                    i += 1
                else:
                    break
            else:
                arr[i] = arr[i + 1]
                k = arr.pop(i + 1)
                i = 0
    else:
        while i < len(arr):
            if i + 1 < len(arr) - 1 or len(arr) % 2 == 0:
                if i + 1 < len(arr):
                    m = len(arr[i])
                    n = len(arr[i + 1])
                    k = lcs_word(arr[i], arr[i + 1])  # arr[i] =
                    a = ""
                    for z in range(len(k)):
                        a = a + k[z]
                    arr[i] = a
                    # k = arr.pop(i + 1)
                    i += 1
                else:
                    break
            else:
                arr[i] = arr[i + 1]
                k = arr.pop(i + 1)
                i = 0
        k = arr.pop(1)
    return arr[0]

#for i in range(len(arr)):
#    print(arr[i])

matrix = [["ABC", "ABCD", "ABCDE"], ["ABC", "ABCD", "ABCDE", "ABCDEF"], ["ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG"], ["ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG", "ABCDEFGH"]]
hold = []
matrix_size = []
results = []
for i in range(len(matrix)):
    total = 0
    matrix_size.append(len(matrix[i]))
    for k in range(50):
        matrix = [["ABC", "ABCD", "ABCDE"], ["ABC", "ABCD", "ABCDE", "ABCDEF"],
                  ["ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG"],
                  ["ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG", "ABCDEFGH"]]
        start = time.time()
        result = multiple_sequence_LCS(matrix[i])
        end = time.time()
        total += (end - start)
    results.append(total / 50)

plt.plot(matrix_size, results, linewidth=2.0)
plt.xlabel('Input size')
plt.ylabel('Running time (s)')
plt.show()