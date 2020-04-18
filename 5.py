import random
def createMatrix(n):
    # j = columns
    # i = rows
    random_matrix = [[random.randint(1,99) for j in range(n)] for i in range(n)]
    for i in range(n):
        print(random_matrix[i])

    # sum of diagonal
    total = 0
    for x in range(n):
        total += random_matrix[x][x]
    maximum = n-1
    for x in range(n):
        total += random_matrix[maximum][x]
        maximum -= 1
    print("Total: ",total)
createMatrix(3)

# source
# -https://stackoverflow.com/questions/28711163/create-matrix-of-random-integers-in-python-with-a-desired-step-size
# -https://docs.python.org/3/library/random.html
# -https://stackoverflow.com/questions/11559062/concatenating-string-and-integer-in-python
# -https://stackoverflow.com/questions/36575328/python-get-value-from-row-and-column-from-a-matrix
