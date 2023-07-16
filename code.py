def enter():
    while True:
        print(50*'-')
        input('please enter number of rows and columns') # prompts user to enter number of rows and columns
        while True:
            try:
                r1,c1=map(int,input('please number of row and col for first matrix ').split()) # prompts user to enter dimensions of first matrix
                r2,c2=map(int,input('please number of row and col for second matrix ').split()) # prompts user to enter dimensions of second matrix
                break
            except ValueError:
                print('please enter data in wright way') # handles ValueError if user inputs incorrect format

        if c1==r2:
            return [r1,r2,c1,c2] # returns a list containing the dimensions of the matrices if they can be multiplied
        else:
            print('sorry you can\'t multiply two matrices') # prints error message if matrices cannot be multiplied


def matrix(li):
    m1=[]
    m2=[]
    for i in range(li[0]):
        row=[]
        for j in range(li[1]):
            row.append(int(input(f'enter [{i}][{j}] for first matrix'))) # prompts user to enter values for first matrix
        m1.append(row)
    print(50*'-')
    for i in range(li[2]):
        row=[]
        for j in range(li[3]):
            row.append(int(input(f'enter [{i}][{j}] for second matrix'))) # prompts user to enter values for second matrix
        m2.append(row)
    return m1,m2


def mult(m1,m2,li):
    out=[]
    for i in range(li[0]):
        row=[]
        for j in range(li[3]):
            row.append(sum([x * y for x, y in zip(m1[i], [row[j] for row in m2])])) # performs matrix multiplication
        out.append(row)
    return out


li=enter()
m1,m2=matrix(li)
out=mult(m1,m2,li)

print('the answer is')
for i in range(li[0]):
    for j in range(li[3]):
        print(out[i][j],end='      ') # prints the resulting matrix
    print()