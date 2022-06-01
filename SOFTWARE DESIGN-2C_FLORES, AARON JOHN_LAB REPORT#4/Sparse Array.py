class SparseArray(object):

        def __init__(self,items=0):

            self.L = [0]*items

        def __setitem__(self, j, e):

            self.L[j] = e

        def __getitem__(self, j):

            return self.L[j]

        def __str__(self):

            return str(self.L)

sa=SparseArray(5)

sa[0]=(13,"elmao")

sa[1]=(22,"lmao")

sa[2]=(1,"limao")

sa[3]=(7,"noni")

sa[4]=(10,"kure")

print("Sparse Array Content: \n",sa)
