import os
import numpy as np
import time

def print_line(li,width,separator):
    print(separator,end='')
    for el in li:
        for_print=str(el)
        left=' '*((width-len(for_print))//2)
        right=left if (width-len(for_print))%2==0 else left+' '
        print(left+for_print+right,end=separator)

def pretty_grid(grid,width,totals=False):
    n,m=grid.shape
    print('┌',end='')
    print(*['─'*width]*m,sep='┬',end='┐\n')
    for index,r in enumerate(grid):
        print_line(r.astype(int),width,'│')
        if index!=n-1: 
            print('\n├',end='')
            print(*['─'*width]*m,sep='┼',end='┤\n')
        else:
            print('\n└',end='')
            print(*['─'*width]*m,sep='┴',end='┘\n')
    if totals:
        print('Sums:')
        print_line(grid.sum(1).astype(int),width,'╎')
        print(' Rows')
        print_line(grid.sum(0).astype(int),width,'╎')
        print(' Columns')
        print('╎',int(grid.trace()), ' Main diagonal\n'+'╎',int(np.flip(grid,1).trace()),' Other diagonal')

n=int(input('Enter an odd number for size of grid: '))
exit('An even number will not work') if n%2==0 else None
magic_num=int(n*(n**2+1)/2)
number_chosen=int(input('Choose a number divisible by '+str(n)+' and greater than or equal to '+str(magic_num)+': '))
extra=(number_chosen-magic_num)/n
exit('Not divisible by '+str(n)) if n!=int(n) else None
width=len(str(number_chosen))+2

grid=np.zeros((n,n))
col,row = n//2,0

for i in range(1,n**2+1):
    os.system('cls' if os.name == 'nt' else 'clear') 
    pretty_grid(grid,width)
    grid[row][col]=i+extra
    time.sleep(.1)
    if i%n==0:
        row=(row+1)%n
    else:
        row=(row-1)%n
        col=(col+1)%n

os.system('cls' if os.name == 'nt' else 'clear') 
pretty_grid(grid,width,True)
