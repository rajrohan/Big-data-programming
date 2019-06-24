import numpy as np

# exercise 1
# Replace item that staify a condition with another value in numpy array

array1 = np.array([1,2,3,4,5,6,7,8,9])
print('\nExercise 1')
print(np.where(array1%2==1,-1,array1))

# exercise 2
# Reshape array

array2 = np.arange(10).reshape((2,5))
print('\nExercise 2')
print (array2)

# exercise 3
# Generate custom sequence

array3 = np.array([1,2,3])
print('\nExercise 3')
print (np.hstack((np.repeat(array3,3),np.tile(array3,3))))

# exercise 4
# Common item between array

array41 = np.array([1,2,3,2,3,4,3,3,4,5,6])
array42 = np.array([7,2,10,2,7,4,9,4,9,8,3])
print('\nExercise 4')
print(np.intersect1d(array41,array42))

# exercise 5
# Position where items are equal

array51 = np.array([1,2,3,2,3,4,3,3,4,5,6])
array52 = np.array([7,2,10,2,7,4,9,4,9,8,3])
print('\nExercise 5')
print(np.where(np.equal(array51,array52)))

# exercise 6
# random float between 5 and 10

array6 = np.random.uniform(5,10,size=15)
print('\nExercise 6')
print (array6.reshape((3,5)))

# exercise 7
# limit printed item to 6

print('\nExercise 7')
array7 = np.arange(15)
np.set_printoptions(threshold=6)
print(array7)

# exercise 8
# print array by suppressing scientific notation

np.random.seed(100)
array8 = np.random.random([3,3])/ 1e3
np.set_printoptions(precision=6, suppress= True)
print('\nExercise 8')
print(array8)

# exercise 9
# swap 2 columns in a 2d array

array9 = np.arange(9).reshape(3,3)
print('\nExercise 9')
print(array9)
array9[:,[0, 1]] = array9[:,[1, 0]]
print('After swapping columns')
print(array9)

# exercise 10
# swap 2 rows in a 2d array

array10 = np.arange(9).reshape(3,3)
print('\nExercise 9')
print(array10)
array9[[0, 1],:] = array9[[1, 0],:]
print('After swapping rows')
print(array10)
