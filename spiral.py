def create_spiral_matrix(n):
    # Matritsani nol bilan to'ldirish
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Yo'nalishlar: o'ng, past, chap, yuqoriga
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    current_dir = 0  # Dastlab o'ngga harakatlanadi
    
    row, col = 0, 0  # Boshlang'ich nuqta
    for num in range(1, n*n + 1):
        matrix[row][col] = num
        # Keyingi qadamni hisoblash
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        # Agar keyingi qadam matritsa chegarasidan chiqsa yoki joy band bo'lsa, yo'nalishni o'zgartirish
        if (next_row < 0 or next_row >= n or
            next_col < 0 or next_col >= n or
            matrix[next_row][next_col] != 0):
            current_dir = (current_dir + 1) % 4  # Yo'nalishni o'zgartirish
            next_row = row + directions[current_dir][0]
            next_col = col + directions[current_dir][1]
        
        row, col = next_row, next_col
    
    return matrix

def print_matrix(matrix):
    n = len(matrix)
    # Matritsani chiroyli formatda chiqarish
    for row in matrix:
        print(' '.join(f"{num:2d}" for num in row))

# 7x7 matritsa yaratish
n = 7
spiral_matrix = create_spiral_matrix(n)

# Matritsani chop etish
print_matrix(spiral_matrix)
