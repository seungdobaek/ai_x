import customer as c

def main():
    global customer_list
    customer_list = c.load_customers()
    while True:
        print("1:입력 ","2:전체출력 ","3:삭제 ","4:이름찾기 ","5:내보내기 (CSV)", "9:종료", sep=' | ', end='')
        fn = int(input('메뉴선택: '))
        if fn == 1:
            customer = c.fn1_insert_customer_info()
            customer_list.append(customer)
        elif fn == 2:
            c.fn2_print_customers(customer_list)
        elif fn == 3:
            c.fn3_delete_customer(customer_list)
        elif fn == 4:
            c.fn4_search_customer(customer_list)
        elif fn == 5:
            c.fn5_save_customer_csv(customer_list)
        elif fn == 9:
            c.fn9_save_customer_txt(customer_list)
            break
if __name__ == '__main__':
    main()
    