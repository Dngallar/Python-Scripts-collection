#NO ESTA COMPLETA

class Matrix:

    def __init__(self, nr, nc):
        self.NRows = nr
        self.NCols = nc
        self.data = [ [0]*self.NCols for r in range(self.NRows) ]
        
    def max(self, m2):
        h1 = self.NRows
        c1 = self.NCols
        h2 = m2.NRows
        c2 = m2.NCols
    
        if h1 <= h2:
            h_new = h1
        else:
            h_new = h2
        if c1 <= c2:
            c_new = c1
        else:
            c_new = c2
            
        m_max = Matrix(h_new,c_new)
        
        for i in range(h_new):
            for j in range(c_new):
                if self.data[i][j] > m2.data[i][j]:
                    m_max.data[i][j] = self.data[i][j]
                else:
                    m_max.data[i][j] = m2.data[i][j]
    
        return m_max

        
    