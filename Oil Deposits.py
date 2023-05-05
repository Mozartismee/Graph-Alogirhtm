"""
function dfs(matrix, i, j, visited)
    if i < 0 or i >= matrix.rows or j < 0 or j >= matrix.columns then
        return // 当前位置超出了矩阵边界，返回
    end if

    if matrix[i][j] == '*' or visited[i][j] then
        return // 当前位置是空格或已访问，返回
    end if

    visited[i][j] = true // 将当前位置标记为已访问

    for dx, dy in {-1, 0, 1} x {-1, 0, 1} do
        if dx == 0 and dy == 0 then
            continue // 当前位置，跳过
        end if

        dfs(matrix, i+dx, j+dy, visited) // 递归访问当前位置的上下左右相邻位置
    end for
end function

"""
def dfs(matrix, i, j , visited):
    # Boundary check
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    
    # Check if current position is * or visited
    if matrix[i][j] == '*' or visited[i][j]
        return
    
    # Mark current position as visited
    visited[i][j] == True

    # Recursively visit the adjacent positions
    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        dfs(matrix, i+dx, j+dy, visited)






# Main function

def countOilDeposits(matrix):
    rows = len(matrix)
    column = len(matrix[0])
    visited = [[False for i in range(column)] for j in range(rows)]

    count = 0
    maxCount = 0

    for i in range(rows):
        for j in (column):
            if matrix[i][j] == '@' and not visited[i][j]:
                dfs(matrix, i, j, visited)
                maxCount = max(maxCount, count)
    
    return maxCount

                

    


"""
function countOilDeposits(matrix)
    rows = matrix.rows
    columns = matrix.columns
    visited = create a new boolean array with size rows x columns, initialized to false

    maxCount = 0 // 最大联通数，用于记录油井数量

    for i = 0 to rows-1 do
        for j = 0 to columns-1 do
            if matrix[i][j] == '@' and not visited[i][j] then
                count = dfs(matrix, i, j, visited) // 从当前未访问的油井位置开始遍历，并得到油井的大小
                maxCount = max(maxCount, count) // 更新最大联通数
            end if
        end for
    end for

    return maxCount // 返回最大联通数
end function
"""

