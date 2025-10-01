import re
import csv
class Customer:
    '''
    고객을 나타내는 객체, 6가지의 정보를 저장한다
    name : 고객의 성함
    phone : 고객의 휴대번호
    email : 고객의 이메일
    age : 고객의 나이
    grade : 고객의 등급
    etc : 고객의 기타사항
    age와 grade는 정수로 저장되고 나머지는 문자열로 저장된다
    '''
    def __init__(self, name, phone, email, age, grade, etc=''):
        '''
        고객 객체를 초기화한다. 6가지 정보를 넣어야한다
        name : 고객의 성함
        phone : 고객의 휴대번호
        email : 고객의 이메일
        age : 고객의 나이
        grade : 고객의 등급
        etc : 고객의 기타사항(default=''(빈 string))
        '''
        self.name = name
        self.phone = phone
        self.email = email
        self.age = int(age)
        self.grade = int(grade)
        self.etc = etc
        
    def as_dic(self):
        '고객 정보를 딕셔너리로 변환하여 return'
        return self.__dict__
    def to_txt_style(self):
        '고객 정보를 "이름, 휴대번호, 이메일, 나이, 등급, 기타사항" 순의 텍스트 변환하여 return'
        return '{}, {}, {}, {}, {}, {}'.format(self.name, self.phone, self.email, self.age, self.grade, self.etc)
    def __str__(self):
        return ('{:>5} {:>4} {:14} {:25} {:3} {}'.format('*'*self.grade, self.name, self.phone, self.email, self.age, self.etc))


def to_customer(row):
    '''
    txt 파일의 내용 한줄(row)를 Customer 객체로 변환
    row : (이름, 휴대번호, 이메일, 나이, 등급, 기타사항) 순의 튜플데이터
        나이와 등급은 int로 나머지는 string으로 받는다
    '''
    return Customer(*row)

def load_customers():
    '''
    data/ch09_customers.txt 파일의 고객 내용을 불러온다
    '''
    customer_list = []
    try:
        with open('data/ch09_customers.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                customer = to_customer(tuple(line.strip().split(', ')))
                customer_list.append(customer)
    except FileNotFoundError:
        with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
            pass
    except Exception as e:
        #다른 오류
        print(e)
    return customer_list

def fn1_insert_customer_info():
    '새로운 고객을 추가합니다'
    while True:
        name = input('이름 : ').strip()
        if re.search(r'[가-힣]{2,}', name):
            break
        print('이름의 형식이 아닙니다. 다시 입력해주세요')
        
    while True:
        phone = input('전화번호(-를 꼭 사용해서 적어주세요) : ').strip()
        if re.search(r'\d{2,3}\-\d{3,4}\-\d{4}', phone):
            break
        print('전화번호의 형식이 아닙니다. 다시 입력해주세요')
        
    while True:
        email = input('이메일 : ').strip()
        if re.search(r'\w+@\w+(\.\w+){1,2}', email):
            break
        print('이메일의 형식이 아닙니다. 다시 입력해주세요')
        
    while True:
        age = input('나이 : ').strip()
        if age.isdigit():
            break
        print('나이가 숫자가 아닙니다. 다시 입력해주세요')
    
    while True:
        grade = input('고객등급(1~5) : ').strip()
        if grade.isdigit() and 1 <= int(grade) <= 5:
            break;
        print('고객등급이 숫자가 아니거나 범위를 벗어났습니다. 다시 입력해주세요')
    
    etc = input('기타 정보 : ').strip()
    
    return Customer(name, phone, email, age, grade, etc)

def fn2_print_customers(customer_list):
    '고객 리스트'
    print('='*70)
    print('{:^60}'.format('고객정보'))
    print('-'*70)
    print('GRADE 이름   전화             메일                     나이 기타')
    print('='*70)
    for customer in customer_list:
        print(customer)
    print('='*70)

def fn3_delete_customer(customer_list):
    name = input('삭제할 고객 이름 : ').strip()
    idx_list = []
    for idx, customer in enumerate(customer_list):
        if customer.name == name:
            idx_list.append(idx)
    
    if len(idx_list) >= 2:
        fn2_print_customers([customer_list[idx] for idx in idx_list])
        print('{}님이 2명 이상입니다'.format(name))
        email = input('삭제할 {}님의 이메일 : '.format(name)).strip()
        del_index = -1
        for idx in idx_list:
            if customer_list[idx].email == email:
                del_index = idx_list[idx]
                break
        if del_index==-1:
            print('{}을 가진 {}님이 없습니다. 초기화면으로 돌아갑니다'.format(email, name))
            return
    elif len(idx_list) == 1:
        del_index = idx_list[0]
    else:
        print('{}님이 없습니다. 초기화면으로 돌아갑니다'.format(name))
        return
    
    fn2_print_customers([customer_list[del_index]])
    while True:
        check = input('정말 {}님을 삭제하시겠습니까?(Y/N) : '.format(name)).strip().upper()
        if check == 'Y':
            del customer_list[del_index]
            print('{}님을 삭제하였습니다. 초기화면으로 돌아갑니다'.format(name))
            return
        elif check == 'N':
            print('{}님을 삭제하지 않고 초기화면으로 돌아갑니다'.format(name))
            return
        else:
            print('Y 또는 N으로 답변해주세요')
            
def fn4_search_customer(customer_list):
    list_=[]
    name = input('찾으실 고객 이름 : ').strip()
    for customer in customer_list:
        if customer.name == name:
            list_.append(customer)

    if len(list_) >= 2:
        fn2_print_customers(list_)
        print('{}님으로 검색된 고객이 2명 이상입니다'.format(name))
        email = input('찾으실 {}님의 이메일 : '.format(name)).strip()
        for customer in list_:
            if customer.email == email:
                list_ = [customer]
                break
        if len(list_) != 1:
            print('{} 이메일의 {}님을 찾을 수 없습니다. 초기화면으로 돌아갑니다'.format(email, name))
            return
    elif not list_:
        print('{}님을 찾을 수 없습니다. 초기화면으로 돌아갑니다'.format(name))
        return
    
    print('찾으신 고객의 정보를 출력합니다')
    fn2_print_customers(list_)
    
def fn5_save_customer_csv(customer_list):
    with open('data/ch09_customers.csv', 'w', encoding='utf-8', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'age', 'grade', 'etc'])
        dict_writer.writeheader()
        dict_writer.writerows([customer.as_dic() for customer in customer_list])
        
def fn9_save_customer_txt(customer_list):
    with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
        f.writelines([customer.to_txt_style()+'\n' for customer in customer_list])