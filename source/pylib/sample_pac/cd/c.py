# python sample_pac.cd.c.py 할시
import sys
sys.path.append(r'C:\ai\source\pylib')
from sample_pac.ab import a

# python -m sample_pac.cd.c 할시
#from ..ab import a

def nice():
    print("sample_pac/cd 패키지 안의 c 모듈 안의 nice 함수")
    a.hello()


if __name__ == '__main__':
    nice()