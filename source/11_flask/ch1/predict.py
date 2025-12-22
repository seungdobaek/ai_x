# 가상환경 만들기 : python -m venv 가상환경이름 : 가상환경이름을 가진 가상확경 생성
# 가상환경 들어가기 : 가상환경이름\Scripts\activate
# python -m pip install --upgrade pip
# pip install statsmodels joblib
# pip install xlwings
# pip install flask

# pip freeze > requirements.txt     # 내가 다운받은 패키지를 requirements.txt에 저장
# pip install -r requirements.txt   # requirements.txt 안에 패키지를 버전을 동일하게 설치

import joblib
loaded_model = joblib.load('model/apt.joblib')


def predict_apt_price(year, square, floor):
    input_data = [[int(year), int(square), int(floor), 1]]
    result = round(loaded_model.predict(input_data)[0]*10000)
    return format(result, ',') + '원입니다'

if __name__=="__main__":
    year = input('건축년도?')
    square = input('몇 제곱미터?')
    floor = input('몇층?')
    print('예측한 금액은 ', predict_apt_price(year, square, floor))