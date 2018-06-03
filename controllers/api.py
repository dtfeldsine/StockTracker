# Here go your api methods.

@auth.requires_login()
def get_stocks():
    user_email = request.vars.user_email