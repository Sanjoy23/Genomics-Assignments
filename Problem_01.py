import numpy as np

v = 'TACGGGTAT'
w = 'GGACGTACG'


length_of_v = len(v)
length_of_w = len(w)

#Create Matrices
#matrix = [[0 for i in range(length_of_v+1)] for j in range(length_of_w+1)]
direction = [[0 for i in range(length_of_v+1)] for j in range(length_of_w+1)]
matrix = np.zeros((len(v)+1,len(w)+1))

match = 5
mismatch = -5
indel = -5

# Initialisation
for i in range(length_of_v+1):
    matrix[0][i] = i* indel
    matrix [i][0] = i* indel

#Matrix Filling
for i in range(1,length_of_w+1):
    for j in range(1,length_of_v+1):

        if (w[i-1] == v[j-1]):
            #print(i,j)
            diagonal_value = matrix[i-1][j-1] + match
            upper_value = matrix[i-1][j] + indel
            left_value = matrix[i][j-1] + indel
            maxx = max(diagonal_value, upper_value, left_value)
            if(maxx == diagonal_value):
                direction[i][j] = 'd'
            if(maxx == upper_value):
                direction[i][j] = 'u'
            if(maxx ==left_value):
                direction[i][j] = 'l'
            matrix[i][j] = max(diagonal_value,upper_value,left_value)
            #print(diagonal_value,upper_value,left_value)
        elif (w[i-1] != v[j-1]):
            diagonal_value = matrix[i - 1][j - 1] + mismatch
            upper_value = matrix[i - 1][j] + indel
            left_value = matrix[i][j - 1] + indel
            maxx = max(diagonal_value, upper_value, left_value)
            if (maxx == diagonal_value):
                direction[i][j] = 'd'
            if (maxx == upper_value):
                direction[i][j] = 'u'
            if (maxx == left_value):
                direction[i][j] = 'l'
            matrix[i][j] = max(diagonal_value, upper_value, left_value)
            #print(i,j,diagonal_value, upper_value, left_value)

#printing Matrix
print ("           T     A     C     G     G     G     T     A     T")
row_labels = [' ','G','G','A','C','G','T','A','C','G']

for row_label, row in zip(row_labels, matrix):
    print ('%s [%s]' % (row_label, ' '.join('%05s' % i for i in row)))

#for i in range(length_of_w+1):
 #   print(matrix[i])


#traceback
seq1 = ''
seq2 = ''

i= 9
j=9
while(i>0 and j>0):
    if(direction[i][j] == 'd'):
        seq1 = v[j-1]+seq1
        seq2 = w[i-1] + seq2
        i = i-1
        j = j-1
    elif(direction[i][j] == 'u'):
        seq1 = '-'+seq1
        seq2 = w[i-1] + seq2
        i = i-1
    else:
        seq2 = '-' + seq2
        seq1 = v[j - 1] + seq1
        j = j - 1

#printing final alignment and final score,
total_match = 0
total_mismatch = 0
for i in range(11):
    if(seq2[i] == seq1[i]):
        total_match = total_match + 1
    else:
        total_mismatch = total_mismatch + 1
#print(total_match)
#print(total_mismatch)

print(v + ', after alignment: '+seq1)
print(w + ', after alignment: '+seq2)

score = mismatch*total_mismatch + match*total_match

print('Final Score: ' + str(score))


