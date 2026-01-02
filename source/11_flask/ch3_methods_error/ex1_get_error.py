# 가상환경 생성 방법1 : python -m venv .venv
# 가상환경 생성 방법2 : ctrl+shift+p => select interpreter => 가상환경만들기 => .venv로 가상환경만들기 => 인터프리터 경로 입력 => 찾기(python.exe)
# 가상환경 생성방법2를 사용하면 pip 업그레이드와 가상환경 들어가기까지 포함
# pip install pydantic
# pip install flask
# pip freeze > requirements.txt

from flask import Flask
from flask import render_template
from flask import request # get/post방식으로 파라미터 데이터 받기
from flask import abort # 강제 예외발생
from models import Member
from filters import mask_password

app = Flask(__name__)
# 필터링 추가(str->str문자갯수만큼 *로 전환)
app.template_filter("mask_pw")(mask_password)

@app.route('/user/<name>') # /user/hong (동적라우팅 : update, delete할때)
def viewFunction_handlerFunction(name):
    return f"<h1>{name}님 환영합니다</h1>"

@app.route('/user') # /user?name=hong (정적라우팅 : read/create 할 때)
def get_user():
    name = request.args.get('name') # get 방식 파라미터 값 받기
    if name:
        return f"<h1>전달받은 이름 {name}님 반갑습니다 </h1>"
    else:
        abort(404)

# 예외 페이지 처리
@app.errorhandler(404)
def errorHandler(error):
    return render_template("error_page.html")

@app.route('/')
def index():
    return render_template('1_onlyget/index.html')

@app.route('/join_form')
def join_form():
    return render_template('1_onlyget/join.html')

@app.route('/join')
def join():
    name = request.args.get('name')
    id = request.args.get('id')
    pw = request.args.get('pw')
    addr = request.args.get('addr')
    
    try:
        member = Member(name=name, id=id, pw=pw, addr=addr)
    except:
        return render_template('error_page.html', msg='유효하지 않은 값을 입력'), 500
    return render_template('1_onlyget/result.html', member=member)

if __name__=='__main__':
    app.run(debug=True, port=80)