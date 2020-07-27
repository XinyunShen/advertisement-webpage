"""
Nearal event view.

URLs include:
/
"""
import hashlib
import flask
import nearal


@nearal.app.route('/event/', methods=['GET', 'POST'])
def event():
    event = {'name': 'User Research and Testing Conference',
            'img_url': 'event.png',
            'start_time': 'Jun.15, Monday, 2:00pm',
            'end_time': 'Jun.16, Tuesday, 5:00pm',
            'location': 'Sunnyvale, CA'}
    phone = 'ios'
    context = {
        'event': event,
        'phone': phone
    }
    return flask.render_template("event.html", **context)
