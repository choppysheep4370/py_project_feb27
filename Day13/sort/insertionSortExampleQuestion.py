'''
아래의 리스트를 삽입 정렬을 사용하여 오름차순으로 정렬해보세요.

[5, 2, 4, 6, 1, 3]
예를 들어, 정렬된 리스트는 아래와 같이 나와야 합니다.


[1, 2, 3, 4, 5, 6]
이 문제는 삽입 정렬 알고리즘을 이해하고, Python으로 구현하는 것을 연습할 수 있는 좋은 예제입니다.
삽입 정렬은 간단하면서도 효율적인 정렬 알고리즘 중 하나이며, 알고리즘을 이해하면 구현이 쉽습니다.
'''

def insertion_Sort(arr):
    n = len(arr)
    for i in range(arr):
        key = arr[i]


