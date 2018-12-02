# in terminal
# $env:FLASK_APP = ".py"
# flask run

from flask import Flask, render_template, request

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"

d = {
    'Shoulder-Taps':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/06_shoulder_taps.png',
    'Bird-Dog':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/08_bird_dog.png',
    'Elbow-Knee':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/12_elbow_to_knee.png',
    'Hip-Openers':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/15_hip_openers.png',
    'Fast-Mountain-Climbers':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/17_fast_mountain_climbers.png',
    'Side-Plank-Rotation':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/18_side_plank_with_rotation.png',
    'Scissors':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/22_scissors.png',
    'High-Knees':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/24_high_knees.png',
    'Cross-Overs':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/25_cross_overs.png',
    'Dead-Bug':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/26_dead_bug.png',
    'Side-Plank':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/28_side_plank.png',
    'Cross-Body-Mountain-Climbers':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/30_cross_body_mountain_climbers.png',
    'Side-Plank-Extension':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/36_side_plank_with_extension.png'
}

@app.route('/<action>')
def home(action):
    return render_template('home.html', action=d[action])

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
