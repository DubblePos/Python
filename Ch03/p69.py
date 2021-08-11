"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 교재 p69 - break, continue 예
"""
i =0
while i < 10 :
    i += 1 # 카운터
    if i == 3:
        continue #다음 문장 skip
    if i == 6 : # 탈출조건
        break # exit
    print(i, end='')