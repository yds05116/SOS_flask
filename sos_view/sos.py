from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from sos_control.user_mngmt import User
from sos_control.session_mngmt import sosSession
import datetime

sos_abtest = Blueprint('sos', __name__) # Blueprint


@sos_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('sos.test_sos'))
    else:
        # print('set_email', request.headers)
        # content type 이 application/json 인 경우
        # print('set_email', request.get_json())
        # print('set_email', request.form['user_email'])
        # print('set_email', request.form['blog_id'])
        user = User.create(request.form['user_email'], request.form['sos_id'])
        # https://docs.python.org/3/library/datetime.html#timedelta-objects
        login_user(user, remember=True, duration=datetime.timedelta(days=365))

        return redirect(url_for('sos.sos_fullstack1'))

    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)


@sos_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('sos.sos_fullstack1'))


@sos_abtest.route('/sos_fullstack1')
def sos_fullstack1():
    if current_user.is_authenticated:
        webpage_name = sosSession.get_sos_page(current_user.sos_id)
        sosSession.save_session_info(
            session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = sosSession.get_sos_page()
        sosSession.save_session_info(
            session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)