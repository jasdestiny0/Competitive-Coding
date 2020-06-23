from fractions import Fraction as f

def solution(mat):
    answer = transform(mat)
    if answer[1] == len(mat):
        return [1, 1]
    X,Y= divXY(*answer)
    i = invOfMat(X)
    answer = multiplyMatrices(i, Y)
    firstR = answer[0]
    list1 = 1
    for xValue in firstR:
        list1 = lcm(list1, xValue.denominator)
    answer = list(map(lambda a: long(a.numerator*list1/a.denominator), firstR))
    answer.append(list1)
    return answer

def onlyVal(number):
    if number<0:
        return -1*number
    return number 

def reduce(a, b):
    h = hcf(a, b)
    return f(long(a/h), long(b/h))

def lcm(a, b):
    return long(a*b/hcf(a,b))

def hcf(a, b):
    def hcf1(a, b):
        if b==0:
            return a
        return hcf1(b, a%b)
    return hcf1(onlyVal(a), onlyVal(b))

def transform(arr):
    listOfSums = list(map(sum, arr))
    booleanIndices = list(map(lambda x: x == 0, listOfSums))
    indices = set([i for i, x in enumerate(booleanIndices) if x])
    currentMatrix = []
    for i in range(len(arr)):
        currentMatrix.append(list(map(lambda x: f(0, 1) if(listOfSums[i] == 0) else reduce(x, listOfSums[i]), arr[i])))
    replaceMatrix = []
    replaceZeros = []
    for i in range(len(currentMatrix)):
        if i not in indices:
            replaceMatrix.append(currentMatrix[i])
        else:
            replaceZeros.append(currentMatrix[i])
    replaceMatrix.extend(replaceZeros)
    t = []
    for i in range(len(replaceMatrix)):
        t.append([])
        copyMatrix = []
        for j in range(len(replaceMatrix)):
            if j not in indices:
                t[i].append(replaceMatrix[i][j])
            else:
                copyMatrix.append(replaceMatrix[i][j])
        t[i].extend(copyMatrix)
    return [t, len(replaceZeros)]

def retMatrix(mat):
    cmat = []
    for i in range(len(mat)):
        cmat.append([])
        for j in range(len(mat[i])):
            cmat[i].append(f(mat[i][j].numerator, mat[i][j].denominator))
    return cmat

def GE(m, list1):
    mat = retMatrix(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('No solution')
        mat[i], mat[index] = mat[index], mat[j]
        list1[i], list1[index] = list1[index], list1[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            list1[j] += ratio * list1[i]
    answer = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) -1 -i
        end = len(mat) - 1
        while end > index:
            list1[index] -= mat[index][end] * answer[end]
            end -= 1
        answer[index] = list1[index]/mat[index][index]
    return answer

def invOfMat(mat):
    t = transpose(mat)
    inverseOfMatrix = []
    for i in range(len(t)):
        list1 = [f(int(i==j), 1) for j in range(len(mat))]
        inverseOfMatrix.append(GE(t, list1))
    return inverseOfMatrix

def multiplyMatrices(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        answer.append([])
        for y in range(len(arr2[0])):
            answer[x].append(f(0, 1))
            for z in range(len(arr1[0])):
                answer[x][y] += arr1[x][z] * arr2[z][y]
    return answer

def divXY(arr, lengthR):
    lengthX = len(arr) - lengthR
    X = []
    Y = []
    for i in range(lengthX):
        X.append([int(i==j)-arr[i][j] for j in range(lengthX)])
        Y.append(arr[i][lengthX:])
    return [X, Y]

def transpose(arr):
    t = []
    for a in range(len(arr)):
        for b in range(len(arr)):
            if a == 0:
                t.append([])
            t[b].append(arr[a][b])
    return t

