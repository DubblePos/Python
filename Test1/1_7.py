"""
날짜 : 2021/08/12
이름 : 박승필
내용 : 파이썬 기본 입출력
"""

n1 = 1
n2 = 2

print(n1, end=',')
print(n2, end=',')

for i in range(1, 10):
    n3 = n1 + n2
    print(n3, end=',')

    n1 = n2
    n2 = n3