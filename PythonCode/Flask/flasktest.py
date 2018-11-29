# in terminal
# $env:FLASK_APP = ".py"
# flask run

from flask import Flask, render_template, request

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"


@app.route('/')
def home():
    return render_template('home.html')

# POST user request sent to backend 
# @app.route('/workout/', methods=['GET', 'POST'])
# def calculate():
#     if request.method == 'POST':
#         a = float(request.form['a'])
#         b = float(request.form['b'])
#         c = float(request.form['c'])
#         root_1, root_2 = quadratic(a, b, c)

#         if root_1:
#             return render_template('calculator_result.html', a=a, b=b, c=c,
#                                    root_1=root_1, root_2=root_2)
#         else:
#             return render_template('calculator_form.html', error=True)
#     return render_template('calculator_form.html', error=None)


# if __name__ == '__main__':
#     app.run()
