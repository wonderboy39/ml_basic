#-*- coding:utf-8 -*-

matrix = [
    [1, 2, 3, 4,  5,  6,  7,  8,  9],
    [2, 4, 6, 8,  10, 12, 14, 16, 18],
    [3, 6, 9, 12, 15, 18, 21, 24, 27],
    [4, 8, 12,16, 20, 24, 28, 32, 36]
]

# [0,0],[1,0],[2,0],[3,0]
# [0,1],[1,1],[2,1],[3,1]
# ...
# [0,8],[1,8],[2,8],[3,8]

print "이를 나열해보면 아래와 같다."
transpose = [sublist[0] for sublist in matrix]
print transpose
transpose = [sublist[1] for sublist in matrix]
print transpose
transpose = [sublist[2] for sublist in matrix]
print transpose
transpose = [sublist[3] for sublist in matrix]
print transpose
transpose = [sublist[4] for sublist in matrix]
print transpose
print " ..... "
transpose = [sublist[8] for sublist in matrix]
print transpose

## ...
## ...
## ... 위의 과정을 계속 반복하면 되는데...
## ...
## ...
## 결과값은 리스트들을 담는 또 하나의 큰 리스트가 되어야 하므로 컴프리헨션이
## 두개가 되어야 한다는 것을 파악할 수 있어야 한다.
transpose = []
temp = []

transpose = [ [ each_item for each_item in sublist][0]
             for sublist in matrix]
print ""
print "========================="
print "정직하게 나열해가며 풀다보니..."
print transpose
print ""

# 위의 0이 들어갈 변수값을 변화시켜야 한다는 점에 착안해서 풀어보면...
# 0열에 대해 0행, 1행, 2행, 3행 의 값을 얻어오고
# 1열에 대해 0행, 1행, 2행, 3행 의 값을 얻오오고..

transpose = []
transpose = [[sublist[i] for sublist in matrix] for i in range(0,9)]
print "========================="
print "아래는 컴프리헨션을 표현해본 결과"
print transpose
