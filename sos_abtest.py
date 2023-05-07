from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS # flask- React 같이 다른 서버 사용 시 response에 header 지원
from sos_view import sos
from sos_control.user_mngmt import User
import os

# https만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' 

app = Flask(__name__, static_url_path='/static') #html에서 가져올 file은 전부 static 폴더에서
CORS(app) 
app.secret_key = 'lsh_server3' # 일단 고정 값 사용

app.register_blueprint(sos.sos_abtest, url_prefix='/sos')
login_manager = LoginManager() # 로그인 관리 객체 생성
login_manager.init_app(app) # app(플라스크 객체) 등록
login_manager.session_protection = 'strong' # session 더욱 복잡하게

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) #mysql에서 해당 id 가져와 객체로 return

@login_manager.unauthorized_handler # 로그인된 사용자가 로그인 필수인 api 사용시 호출 
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == '__main__': # 이 코드가 main일 경우 실행
    app.run(host='0.0.0.0', port='8080', debug=True)
