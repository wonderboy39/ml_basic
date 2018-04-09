#-*- coding:utf8 -*-

l_sequence = range(1,21)
l_square = []
for number in l_sequence:
    l_square.append(number*number)

print l_square

l_square = [number*number for number in l_sequence]
print l_square


even_square = [n*n for n in range(1,21) if n%2 == 0]
print even_square


# gugudan 1단 ~ 3단
gugu_1_4 = []
for i in range(1,5):
    for step in range(1,10):
        gugu_1_4.append(i*step)

print gugu_1_4

gugu_1_4_test = [number*step for number in range(1,5) for step in range(1,10)]
print gugu_1_4_test


print ""
print "====================================="
matrix = [
    [1, 2, 3, 4,  5,  6,  7,  8,  9],
    [2, 4, 6, 8,  10, 12, 14, 16, 18],
    [3, 6, 9, 12, 15, 18, 21, 24, 27],
    [4, 8, 12,16, 20, 24, 28, 32, 36]
]

l_matrix = [row for row in matrix]
print l_matrix

print ""
print "============================="
print "==== 2차원 배열을 1차원 배열로 ===="
listed_matrix = [data for each_row in matrix for data in each_row]
print listed_matrix

matrix = [
    [1, 2, 3, 4,  5,  6,  7,  8,  9],
    [2, 4, 6, 8,  10, 12, 14, 16, 18],
    [3, 6, 9, 12, 15, 18, 21, 24, 27],
    [4, 8, 12,16, 20, 24, 28, 32, 36]
]


print ""
print "=== 전치행렬 예제 =================================="
matrix = [
    [1, 2, 3, 4,  5,  6,  7,  8,  9],
    [2, 4, 6, 8,  10, 12, 14, 16, 18],
    [3, 6, 9, 12, 15, 18, 21, 24, 27],
    [4, 8, 12,16, 20, 24, 28, 32, 36]
]

transpose = []

# [0,0],[1,0],[2,0],[3,0]
# [0,1],[1,1],[2,1],[3,1]
# ...
# [0,8],[1,8],[2,8],[3,8]

for i in range(0,9):
    l_temp = []
    for j in range(0,4):
        l_temp.append(matrix[j][i])
    transpose.append(l_temp)

print transpose

## or
transpose = []
for i in range(0,9):
    l_temp = []
    for row in matrix:
        l_temp.append(row[i])
    transpose.append(l_temp)

print "==========="
print transpose

