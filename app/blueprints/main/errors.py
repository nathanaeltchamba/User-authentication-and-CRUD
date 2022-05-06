from flask import current_app as app

@app.errorhandler(404)
def not_found_error(error):
    return 'That resource cannot be found on our server'

def internal_error(error):
    return 'There is an error with the server. Contact the system administrator'