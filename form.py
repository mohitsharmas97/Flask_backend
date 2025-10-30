from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/greet',methods=['POST'])
def greet():
    name=request.form['username']
    return f"Hello, {name} ! Nice to meet you."

if __name__=='__main__':
    app.run(debug=True)
    