print ('Input your number:')
x = input()
x = str(x)
def findMax (a):
    if (a[0] != '9'):
        max = a[0]
        for j in a:
            if j == max:
                a = a.replace(j, '9')
        return (a)

    else:
        for i in range(len(a)):
            if (a[i] == '9'):
                pass
            elif (a[i] == '0'):
                max = a[i]
                for j in a:
                    if j == max:
                        a = a.replace(j, '9')
                return (a)
            elif (a[i] != '8'):
                max = a[i]
                for j in a:
                    if j == max:
                        a = a.replace(j, '8')
                return (a)


def findMin (b):
    if (b[0] != '1'):
        min = b[0]
        for j in b:
            if j == min:
                b = b.replace(j, '1')
        return (b)
    else:
        for i in range(len(b)):
            if (b[i] == '1' or b[i] == '0'):

                #print(i)
                pass
            elif (b[i] != '0'):
                min = b[i]
                for j in b:
                    if j == min:
                        b = b.replace(j, '0')
                #print(b)
                return (b)
        return(b)
print('FinalMax =',findMax(x))
print('FinalMin =',findMin(x))
result=int(findMax(x))-int(findMin(x))

print('Differance Value =',(result))
