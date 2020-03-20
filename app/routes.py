from app import app


@app.route('/')
@app.route('/index')
def index():
    return "<h1>I have a strong system!</h1>"
