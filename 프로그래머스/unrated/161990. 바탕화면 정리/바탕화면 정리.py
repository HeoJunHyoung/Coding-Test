def solution(wallpaper):
    answer = []
    min_x = min_y = float('inf')
    max_x = max_y = 0
    for row in range(0,len(wallpaper)):
        for col in range(0,len(wallpaper[row])):
            # print(wallpaper[i][j], end='')
            if wallpaper[row][col] == '#':
                if min_x > row:
                    min_x = min(min_x, row)
                if min_y > col:
                    min_y = min(min_y, col)
                if max_x < row:
                    max_x = max(max_x, row)
                if max_y < col:
                    max_y = max(max_y, col)

    answer = [min_x, min_y, max_x+1, max_y+1]
    return answer