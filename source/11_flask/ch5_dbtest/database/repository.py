import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', '210.121.189.12:1521/xe')
def get_emp_list():
    cursor = conn.cursor()
    sql = "SELECT * FROM EMP"
    cursor.execute(sql)
    emps = cursor.fetchall()
    cursor.description
    keys = [desc[0] for desc in cursor.description]
    emp_list = [dict(zip(keys, emp)) for emp in emps]
    return emp_list

def get_emp(empno):
    cursor = conn.cursor()
    sql = "SELECT * FROM EMP WHERE EMPNO = :empno"
    cursor.execute(sql, {'empno': empno}) # 딕셔너리 리스트
    emp = cursor.fetchone()
    keys = [desc[0].lower() for desc in cursor.description]
    emp = dict(zip(keys, emp))
    return emp

if __name__ == '__main__':
    emp_list = get_emp_list()
    print(emp_list)
    emp = get_emp(7902)
    print(emp)