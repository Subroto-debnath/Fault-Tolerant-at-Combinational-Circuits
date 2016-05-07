from solvers import KMapSolver4
all_vars = 'A, B, C, D'
KMapSolver = KMapSolver4
my_data=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
lst=raw_input("F(W,X,Y,Z)=").split(",")
for i in range(len(lst)):
    if lst[i]=='0':
        my_data[0][0]=1
    elif lst[i]=='1':
        my_data[0][1]=1
    elif lst[i]=='3':
        my_data[0][2]=1
    elif lst[i]=='2':
        my_data[0][3]=1
    elif lst[i]=='4':
        my_data[1][0]=1
    elif lst[i]=='5':
        my_data[1][1]=1
    elif lst[i]=='7':
        my_data[1][2]=1
    elif lst[i]=='6':
        my_data[1][3]=1
    elif lst[i]=='12':
        my_data[2][0]=1
    elif lst[i]=='13':
        my_data[2][1]=1
    elif lst[i]=='15':
        my_data[2][2]=1
    elif lst[i]=='14':
        my_data[2][3]=1
    elif lst[i]=='8':
        my_data[3][0]=1
    elif lst[i]=='9':
        my_data[3][1]=1
    elif lst[i]=='11':
        my_data[3][2]=1
    elif lst[i]=='10':
        my_data[3][3]=1

lst=raw_input("Don't care F'(W,X,Y,Z)=").split(",")
for i in range(len(lst)):
    if lst[i]=='0':
        my_data[0][0]=2
    elif lst[i]=='1':
        my_data[0][1]=2
    elif lst[i]=='3':
        my_data[0][2]=2
    elif lst[i]=='2':
        my_data[0][3]=2
    elif lst[i]=='4':
        my_data[1][0]=2
    elif lst[i]=='5':
        my_data[1][1]=2
    elif lst[i]=='7':
        my_data[1][2]=2
    elif lst[i]=='6':
        my_data[1][3]=2
    elif lst[i]=='12':
        my_data[2][0]=2
    elif lst[i]=='13':
        my_data[2][1]=2
    elif lst[i]=='15':
        my_data[2][2]=2
    elif lst[i]=='14':
        my_data[2][3]=2
    elif lst[i]=='8':
        my_data[3][0]=2
    elif lst[i]=='9':
        my_data[3][1]=2
    elif lst[i]=='11':
        my_data[3][2]=2
    elif lst[i]=='10':
        my_data[3][3]=2
       
print my_data
k = KMapSolver(my_data)
k.solve()
