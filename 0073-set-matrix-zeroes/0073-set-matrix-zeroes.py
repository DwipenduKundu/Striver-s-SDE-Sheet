class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        column=len(matrix[0])
        dic={}
        for i_row in range(row):
            for j_col in range(column):
                if matrix[i_row][j_col]==0:
                    if i_row not in dic:
                        dic[i_row]=[]
                    dic[i_row].append(j_col)
        for key in dic:
            for i_row in range(row):
                for j_col in range(column):
                    if i_row==key :
                        matrix[i_row][j_col]=0
            for i in dic[key]:
                for i_row in range(row):
                    for j_col in range(column):
                        if j_col==i:
                            matrix[i_row][j_col]=0

        return matrix