# https://www.hackerrank.com/challenges/crossword-puzzle/problem

def can_place(crossword, word, direction, i, j):
    if direction == 'H':
        for e in range(i, len(crossword)):
            if crossword[e][j] != '+':
                if len(word) > 0:
                    word[1:]
                else:
                    return False
            else:
                if len(word) > 0:
                    return False
        return True
    elif direction == 'V':
        for e in range(j, len(crossword[i])):
            if crossword[i][e] != '+':
                if len(word) > 0:
                    word[1:]
                else:
                    return False
            else:
                if len(word) > 0:
                    return False
        return True


def crosswordPuzzle(crossword, words, i):
    if i == len(words) - 1:
        print(crossword)
        return

    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            c = crossword[i][j]
            if crossword[i][j] in ('-', words[i][0]):
                if can_place(crossword, words[i], 'H', i, j):
                    b
                    crosswordPuzzle(crossword, words, i + 1)
                    crossword[i][j] = c
                if can_place(crossword, words[i], 'V', i, j):
                    crossword[i][j] = words[i][0]
                    crosswordPuzzle(crossword, words, i + 1)
                    crossword[i][j] = c


crosswordPuzzle(
    ['+-++++++++', '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++',
     '++------++', '+++++-++++',
     '+++++-++++'],
    ['LONDON', 'DELHI', 'ICELAND', 'ANKARA'], 0);
