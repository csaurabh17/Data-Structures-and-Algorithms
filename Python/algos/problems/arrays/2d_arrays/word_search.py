# https://leetcode.com/problems/word-search/

def word_search(matrix, i, j, direction, word, target_word):
    if i >= len(matrix) or j >= len(matrix[i]):
        return False
    if word + matrix[i][j] not in target_word:
        return False
    if word + matrix[i][j] == target_word:
        return True

    letter = matrix[i][j]
    matrix[i][j] = "-1"
    # go right
    return word_search(matrix, i + 1, j, 'r', word + letter, target_word) \
           or word_search(matrix, i, j + 1, 'd', word + letter, target_word) \
           or word_search(matrix, i - 1, j, 'd', word + letter, target_word) \
           or word_search(matrix, i, j - 1, 'd', word + letter, target_word)

    matrix[i][j] = letter
    return False


print(word_search([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 0, 0, '', '', "ABCCEDX"))
