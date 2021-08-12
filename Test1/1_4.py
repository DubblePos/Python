"""
날짜 : 2021/08/12
이름 : 박승필
내용 : 파이썬 기본 입출력
"""

for i in range(1, 7):
    for j in range(1, 7):

        tot = i +j

        if tot == 6 :
            print('첫번째 주사위 : %d, 두번째 주사위 : %d' %(i, j))