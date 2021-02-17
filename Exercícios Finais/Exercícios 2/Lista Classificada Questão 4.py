
A = [3,2,4,5,6,3,2,2,4,5,1]

b = []

def Class(A):

    b = []

    while len(A) > 0:

        indmin = 0
        for j in range(1, len(A)):
            if A[indmin] > A[j]: indmin = j

        b.append(A[indmin])
        del A[indmin]

    return b

print (Class(A))








