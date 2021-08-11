"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 교재 p65 - while 반복문 예
"""
# (1) 카운터와 누적변수
cnt = tot = 0 # 변수 초기화
while cnt <5 : # True : loop 수행
    cnt += 1 # 카운터 변수(cnt = cnt + 1)
    tot += cnt # 누적변수 : tot = tot + cnt
    print(cnt, tot)

# [실습] 1~100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = [] # 빈 list

while cnt < 100 : # 100회 반복
    cnt += 1 # 카운터
    if cnt % 3 == 0:
        tot += cnt # 누적변수
        dataset.append(cnt) # cnt 쿠가
print('1~100 사이 3의 배수 합 = %d' % tot)
print('dataset = ', dataset)