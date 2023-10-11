# move this to a separete file at some point
def login_required(route):
    def decorated_route(*args, **kwargs):
        if 'logged_in' in session:
            return route(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return decorated_route