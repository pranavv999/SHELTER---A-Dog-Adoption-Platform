from flask import render_template
from shelter import app, db


@app.errorhandler(404)
def not_found_error(error):
    header = 'Content Not Found'
    message = 'Content may be deleted or try entering proper url'
    return render_template('errors.html', header=header, message=message), 404


@app.errorhandler(403)
def forbidden_error(error):
    header = '''Access Denied'''
    message = 'You do not have permission\
 to view the requested file or resource'
    return render_template('errors.html', header=header, message=message), 403


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    header = 'An unexpected error has occurred'
    message = 'The administrator has been notified.\
Sorry for the inconvenience!'
    return render_template('errors.html', header=header, message=message), 500
