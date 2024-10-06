import numpy as np
import random


nums = list(range(1, 26))

nums1 = nums.copy()
nums2 = nums.copy()

random.shuffle(nums1)
random.shuffle(nums2)

mat1 = np.array(nums1).reshape(5,5)
mat2 = np.array(nums2).reshape(5,5)


i=0

while i < len(nums):
    mynum = int(input("Enter your Numbe  :  "))
    index1 = np.where(mat1 == mynum)
    index2 = np.where(mat2 == mynum)

    mat1[index1] = 0
    mat2[index2] = 0

    # print(mat,'\n\n')
    print(mat1,'\n\n')
    print(mat2)
    print('\n\n\n')


    col_zero_1 = sum(mat1)
    row_zero_1 = sum(np.transpose(mat1))

    col_zero_2 = sum(mat2)
    row_zero_2 = sum(np.transpose(mat2))

    col_index_zero_1 = np.where(col_zero_1 == 0)
    row_index_zero_1 = np.where(row_zero_1 == 0)

    col_index_zero_2 = np.where(col_zero_2 == 0)
    row_index_zero_2 = np.where(row_zero_2 == 0)

    totalzero_1 = len(col_index_zero_1[0]) + len(row_index_zero_1[0])
    totalzero_2 = len(col_index_zero_2[0]) + len(row_index_zero_2[0])

    print('***********************************************')
    print(f'Player 1 cross {totalzero_1} lines.')
    print('\n\n')
    print(f'Player 2 cross {totalzero_2} lines.')
    print('***********************************************')
    print('\n\n\n')

    if totalzero_1 == 5:
        print('Player 1 win')
        break
    elif totalzero_2 == 5:
        print('Player 2 win')
        break
    else:
        i += 1