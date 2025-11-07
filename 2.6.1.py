
def build_matrix(rows, cols):
    x = [0]
    for i in range(cols - 1):
        x.append(0)

    y = [x]
    for j in range(rows - 1):
        y.append(x.copy()) 

    return y
def position_to_letter(rows, cols):

    letter_matrix = build_matrix(rows, cols)
    position = 1
    
    for i in range(rows):
        for j in range(cols):
            letter_matrix[i][j] = chr(position+96)
            position+=1

    return letter_matrix


rows, cols = 4, 4
matrix = build_matrix(rows, cols)
letter_matrix = position_to_letter(rows, cols)
for i in range(rows):
    print(letter_matrix[i])

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"Input value for {letter_matrix[i][j]}: "))

for i in range(rows):
    print(matrix[i])
