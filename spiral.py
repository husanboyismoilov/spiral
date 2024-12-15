def create_spiral_matrix(n, start=1, end=None, reverse=False):
    if end is None:
        end = n * n + start
    # Matritsani nol bilan to'ldirish
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Yo'nalishlar: o'ng, past, chap, yuqoriga
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    current_dir = 0  # Dastlab o'ngga harakatlanadi
    
    row, col = 0, 0  # Boshlang'ich nuqta
    if reverse:
        step = -1
        current_num = end - 1
    else:
        step = 1
        current_num = start

    for _ in range(n * n):
        matrix[row][col] = current_num
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
        current_num += step

    return matrix

def print_side_by_side(matrix1, matrix2):
    n = len(matrix1)
    for i in range(n):
        # Formatlash: har bir son uchun 2 raqamli joy ajratish
        row1 = ' '.join(f"{num:2d}" for num in matrix1[i])
        row2 = ' '.join(f"{num:2d}" for num in matrix2[i])
        print(f"{row1}    {row2}")  # Oraliq uchun 4 bo'sh joy

def main():
    n = 7  # Matritsa o'lchami
    # Birinchi matritsa: 1 dan 49 gacha spiral
    spiral_matrix1 = create_spiral_matrix(n, start=1, end=50, reverse=False)
    # Ikkinchi matritsa: 49 dan 1 gacha spiral
    spiral_matrix2 = create_spiral_matrix(n, start=1, end=50, reverse=True)
    
    print("Birinchi Matritsa (1 dan 49 gacha):\tIkkinchi Matritsa (49 dan 1 gacha):")
    print_side_by_side(spiral_matrix1, spiral_matrix2)

if name == "main":
    main()
