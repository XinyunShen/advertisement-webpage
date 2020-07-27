"""
Nearal work view.

URLs include:
/
"""
import flask
import nearal


@nearal.app.route('/work/', methods=['GET', 'POST'])
def work():
    work = {'company': 'Walmart Inc.',
            'img_url': 'temp.png',
            'position': 'Accountant',
            'location': 'Mountain View, CA'}
    phone = 'ios'
    context = {
        'work': work,
        'phone': phone
    }
    return flask.render_template("work.html", **context)
