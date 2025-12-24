# PowerShell 관리자 모드 Get-ExecutionPolicy를 쳐보면 Restricted로 되어있음 이를 RemoteSigned로 변경해야함
# Set-ExecutionPolicy RemoteSigned을 쳐서 RemoteSigned으로 변경 가능
# app.py 생성 후 ctrl+j 터미널 창을 열기
# 가상환경 만들기 : python -m venv .venv
# pip 업그레이드 : python -m pip install --upgrade pip
# pip install flask

# pip freeze > requirements.txt
# pip install -r requirements.txt
from flask import Flask
app = Flask(__name__) # 웹서버 객체 (앱 인스턴스 생성)
@app.route('/') # 데코레이터를 통해 가능한 url 등록
def main_handler():
    return "<h1>Hello, World</h1>"

@app.route('/apt')
def apt_handler():
    return "<h1>예상 금액은 1,000원입니다</h1>"
    # return {
    #     'price':'1,000',
    #     'unit':'won'
    # }

# app.py에서 실행 : flask run --port=80 --debug
# app.py가 아닌 파일 플라ㅡ크 실행 : python ex1_app.py
if __name__=="__main__":
    app.run(port=80, debug=True) # 소스 수정시 서버 자동 재시작, port=80번