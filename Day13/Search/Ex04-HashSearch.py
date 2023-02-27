'''
Ex04-HashSearch

해시 검색(Hash Search)
    해시 테이블(Hash Table)을 이용하여 데이터를 검색하는 방법.
    해시 테이블은 key : Value 구성된 데이터를 저장하는 자료구조
    키를 이용 값을 빠르게 검색할 수 있다.
'''

class HashTable:
    def __init__(self,size):
        self.size = size

        # 빈 리스트를 size 개 만큼 생성하여 2차원 리스트 초기화
        self.hash_table = [[] for _ in range(self.size)]