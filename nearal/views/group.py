"""
Nearal event view.

URLs include:
/
"""
import flask
import nearal


@nearal.app.route('/group/', methods=['GET', 'POST'])
def group():
    group = {'groupname': 'UX Group',
            'img_url': 'group.png',
            'size': 200,
            'description': 'The group is designed to offer its memeber a platform to ask questions, opinions, share their current struggles, and offer others...'}
    phone = 'ios'
    context = {
        'group': group,
        'phone': phone
    }
    return flask.render_template("group.html", **context)
