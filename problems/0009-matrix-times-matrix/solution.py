def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
            if (len(b) != len(a[0])):
                return -1

            new_mat = [[] for _ in range(len(a))]
            
            for v in range(len(b[0])):  
                for i in range(len(a)):
                    t = 0
                    for j in range(len(a[0])):
                        t += a[i][j]*b[j][v]
                    new_mat[i].append(t)
            return new_mat  
    
	