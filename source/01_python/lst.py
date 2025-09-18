def safe_index(lst, item):
    '''
    첫번째 매개변수 lst에서 item 요소가 있는 index를 반환.
    item 요소가 없으면 -1을 반환
    lst: 요소를 찾고 싶은 리스트
    item: 찾고 싶은 값
    '''
    if item in lst:
        return(lst.index(item))
    return -1