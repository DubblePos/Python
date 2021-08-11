"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 교재 p62 - 중첩 조건문 예
"""
score = int(input('점수 입력 : '))
grade = '' # 등급

if score >= 85 and score <=100 :
    grade = '우수'
elif score >=70:
    grade = '보통'
else :
    grade = '저조'
print('당신의 점수는 %d이고, 등급은 %s' %(score, grade))