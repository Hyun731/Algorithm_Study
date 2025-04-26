class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
    def scala_mul(self,scalar, matrix):
        result = [[scalar * val for val in row] for row in self.matrix]
        return Matrix(result)
    def transfose(self,matrix):
        transposed = list(map(list,zip(*matrix.matrix)))
        return Matrix(transposed)
    def determinant(self,matrix):
        if matrix.rows == 1:
            return matrix.matrix[0][0]
        elif matrix.rows == 2:
            return matrix.matrix[0][0] * matrix.matrix[1][1]
        else:
            temp = 0
            for j in range(matrix.cols):
                temp += (-1)**(j) * matrix.matrix[0][j]* self.determinant(self.cofactor((matrix,0,j)))
            return temp
                
    def cofactor(self,matrix,x,y):
        new_matrix = []
        for i in range(matrix.rows):
            temp =[]
            if i == x: continue
            for j in range(matrix.cols):
                if j == y: continue
                temp.append(matrix[i][j])
            new_matrix.append(temp)
        return Matrix(new_matrix)
    
    def adjoint(self,matrix):
        new_matrix = []
        for i in range(matrix.rows):
            temp = []
            for j in range(matrix.cols):
                temp.append((-1)**(i+j)*self.determinant(self.cofactor(matrix.matrix,i,j)))
            new_matrix.append(temp)
        return self.transfose(Matrix(new_matrix))
    def __pow__(self,n):
        if n == -1:
            self.scala_mul(1/self.determinant(self),self.adjoint(self))