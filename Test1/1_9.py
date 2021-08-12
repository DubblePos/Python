"""
날짜 : 2021/08/12
이름 : 박승필
내용 : 파이썬 기본 입출력
"""

dataset = [3, 5, 1, 2, 4]
size = len(dataset)

for i in range(size - 1):

    for j in range(i+1, size):

        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print('%d Round : %s' % (i, dataset))

print('Result : ', dataset)