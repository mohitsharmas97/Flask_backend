# from flask import Flask

# app=Flask(__name__)

# @app.route('/')
# def home():
#     return "lets run basic syntax of flask"

# if __name__=='__main__':
    
    
#     app.run(debug=True)


from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my flask app"

@app.route('/about')
def about():
    return "this is the about page"

@app.route('/contact')
def contact():
    return "Contact us at mksharmah675@gmail.com"

if __name__=='__main__':
    app.run(debug=True)

