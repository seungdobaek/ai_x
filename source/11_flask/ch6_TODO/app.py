from flask import Flask, request, render_template, url_for, redirect, abort, session
from database.repository import get_todos, get_next_id, get_todo, create_todo, update_todo, delete_todo
from models import Todo

app = Flask(__name__)
app.secret_key = 'abc123!' # 세션을 사용할 경우 필수
# app.config['SECRET_KEY'] = 'abc123!' # 위와 동일

@app.route('/')
def index():
    "로그인 성공 로직(세션에 로그인 정보) 저장 후 /todos로 이동 "
    session['user_id'] = 'hong'
    session['user_name'] = '홍길동'
    # return redirect("/todos") # /todos 요청경로로 이동
    return redirect(url_for("todos")) # todos 함수로 이동

@app.route('/logout')
def logout():
    "로그아웃 성공 로직(세션에 로그인 정보 삭제) 후 /toods로 이동"
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for("todos")) # todos 함수로 이동

@app.route('/todos')
def todos():
    "tood 목록 보여주기"
    order = request.args.get('order', 'asc') # GET 방식 요청
    todos = get_todos(order)
    next_id = get_next_id()
    return render_template('todo/todos.html', todos=todos, next_id=next_id)

@app.route('/create', methods=['POST'])
def create():
    "todo 생성"
    # todo = Todo(content=request.form['content'])
    todo = Todo(**request.form.to_dict())
    create_todo(todo)
    return redirect(url_for('todos', order='desc'))

@app.route('/todos/<int:id>')
def todo(id):
    "todo 상세 보여주기"
    todo = get_todo(id)
    if todo:
        return render_template('todo/todo.html', todo=todo)
    return abort(404, description=f"{id}번은 논재하지 않는 할일입니다")

@app.errorhandler(404)
def not_found(error):
    return render_template('page_not_found.html', error=error), 404

@app.route('/update/<int:id>')
def update_page(id):
    "todo 수정 페이지"
    todo = get_todo(id)
    if todo:
        return render_template('todo/update.html', todo=todo)
    return abort(404, description=f"{id}번은 논재하지 않는 할일입니다")

@app.route('/update/<int:id>/<string:content>/<string:is_done>', methods=['PUT'])
def update(id, content, is_done):
    "todo 수정"
    todo = Todo(id=id, content=content, is_done=is_done)
    return update_todo(todo)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    "todo 삭제"
    return delete_todo(id)