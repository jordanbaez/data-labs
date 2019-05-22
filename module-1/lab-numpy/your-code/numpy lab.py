#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))
aa = np.random.random(size=(2,3,5))
aaa = np.random.randint(9,size=(2,3,5))

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.full(
    shape=(5,2,3),
    fill_value=1,
    dtype=np.int)



#6. Print b.
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?

 (np.size(a) , np.size(b))
#(np.shape(a), np.shape(b))



#8. Are you able to add a and b? Why or why not?

#operands could not be broadcast together with shapes (2,3,5) (5,2,3) 




#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b)
c = b.reshape(2,3,5)


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a+c

#it now works because each element from 1 array finds its matching element

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#[[[0.52138121 0.89056813 0.53781786 0.06658865 0.17785386]
 # [0.4560318  0.55503824 0.43715311 0.10856834 0.30254399]
  #[0.87117383 0.73879383 0.50515597 0.97264769 0.08432312]]

# [[0.62571355 0.95074893 0.06456693 0.59439601 0.95757875]
 # [0.38692392 0.57299996 0.83257093 0.39235379 0.8902883 ]
  #[0.25617972 0.12368459 0.10724054 0.87160214 0.95164398]]]

#array([[[1.52138121, 1.89056813, 1.53781786, 1.06658865, 1.17785386],
 #       [1.4560318 , 1.55503824, 1.43715311, 1.10856834, 1.30254399],
  #      [1.87117383, 1.73879383, 1.50515597, 1.97264769, 1.08432312]],
#
 #      [[1.62571355, 1.95074893, 1.06456693, 1.59439601, 1.95757875],
  #      [1.38692392, 1.57299996, 1.83257093, 1.39235379, 1.8902883 ],
   #     [1.25617972, 1.12368459, 1.10724054, 1.87160214, 1.95164398]]])

#each element in a got 1 added to itsel


#12. Multiply a and c. Assign the result to e.

e = a*c
print(e)

#13. Does e equal to a? Why or why not?

#[[[0.52138121 0.89056813 0.53781786 0.06658865 0.17785386]
 # [0.4560318  0.55503824 0.43715311 0.10856834 0.30254399]
  #[0.87117383 0.73879383 0.50515597 0.97264769 0.08432312]]

# [[0.62571355 0.95074893 0.06456693 0.59439601 0.95757875]
 # [0.38692392 0.57299996 0.83257093 0.39235379 0.8902883 ]
  #[0.25617972 0.12368459 0.10724054 0.87160214 0.95164398]]]

#e=a because a*c = a*1


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


d_Max = np.amax(d)
print(d_Max)

d_Min = np.amin(d)
print(d_Min)

d_Mean = np.mean(d)
print(d_Mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2,3,5])
print(f)


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for i in range(2):
  for j in range(3):
    for k in range(5):
      if (d_Mean >(d[i][j][k]) > d_Min): 
        f[i][j][k]=25
      elif (d_Max > (d[i][j][k]) > d_Mean): 
        f[i][j][k]=75
      elif (d[i][j][k]) == d_Mean:
        f[i][j][k]= 50
      elif (d[i][j][k]) == d_Min:
        f[i][j][k]= 0
      else:
        f[i][j][k]= 100
   
       
print(f)


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print (d) 
print (' ')
print (f)

#YAAAAAAAAAAS

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

f=np.empty([2,3,5],str)

for i in range(2):
  for j in range(3):
    for k in range(5):
      if (d_Mean >(d[i][j][k]) > d_Min): 
        f[i][j][k]='B'
      elif (d_Max > (d[i][j][k]) > d_Mean): 
        f[i][j][k]='D'
      elif (d[i][j][k]) == d_Mean:
        f[i][j][k]= 'C'
      elif (d[i][j][k]) == d_Min:
        f[i][j][k]= 'A'
      else:
        f[i][j][k]= 'E'
   
      
print(f)