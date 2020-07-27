"""
Nearal user view.

URLs include:
/
"""
import hashlib
import flask
import nearal


@nearal.app.route('/user/', methods=['GET', 'POST'])
def user():
    user = {'username': 'Luke Samuel',
            'img_url': 'temp.png',
            'position': 'Legal Advisor',
            'company': 'DLA Piper USA'}
    phone = 'ios'
    context = {
        'user': user,
        'phone': phone
    }
    return flask.render_template("user.html", **context)
