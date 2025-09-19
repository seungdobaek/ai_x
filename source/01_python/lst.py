def safe_index(lst, item, start=0):
    '''
    첫번째 매개변수 lst[start:]에서 item 요소가 있는 index를 반환.
    item 요소가 없으면 -1을 반환
    lst: 요소를 찾고 싶은 iterable(리스트, 튜플)
    item: 찾고 싶은 값
    start: 서치를 시작할 index(기본값: 0)
    '''
    return lst.index(item,start) if (item in lst[start:]) else -1