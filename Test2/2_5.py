"""
날짜 : 2021/08/13
이름 : 박승필
내용 : 파이썬 기본 입출력
"""

class King:

    def __init__(self, name = '태조', year=1392):
        self.name = name
        self.year = year

    def show(self):
        print('----------------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':

    king1 = King()
    king2 = King('태종', 1392)
    king3 = King('세종대왕', 1418)

    king1.show()
    king2.show()
    king3.show()