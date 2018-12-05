# in powershell terminal
# $env:FLASK_APP = "flasktest.py"
# flask run

from flask import Flask, render_template, request

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = "Some secret string here"

d = {
    # Abs
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
    'Side-Plank-Extension':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/36_side_plank_with_extension.png',
    # Arms
    'Dirty-Dogs':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/33_dirty_dogs.png',
    'Dive-Bomber-Push-Ups':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/35_dive_bomber_push_ups.png',
    'Plank-Push-Up':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/38_plank_to_push_up.png',
    'Breakdancer-Push-Ups': 'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/43_breakdancer_push_ups.png',
    # Back
    'Back-Extensions' : 'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/09_back_extensions.png',
    'Single-Leg-Up-Down-Dogs': 'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/39_single_leg_up_and_down_dogs.png',
    'Cross-Body-Extension': 'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/47_cross_body_extension.png',
    # Chest
    'Push-Ups':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/19_push_ups.png',
    'T-Push-Ups': 'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/41_t_push_ups.png',
    'Mountain-Climber-Push-Ups':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/51_mountain_climber_push_ups.png',
    # Legs
    'Y-Squats':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/03_y_squats.png',
    'Single-Leg-Deadlift': 'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/02_single_leg_deadlift.png',
    'Bridge':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/01_bridge.png',
    'Forward-Lunge':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/04_forward_lunge.png',
    'Lateral-Squat':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/05_lateral_swing.png',
    'Static-Lunge':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/07_static_lunge.png',
    'Yoga-Squat':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/10_yoga_squat.png',
    'Single-Leg-Deadlift-Overhead-Reach':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/31_single_leg_deadlift_with_overhead_reach.png',
    'Burpees':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/34_burpees.png',
    'Jump-Squats':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/37_jump_squats.png',
    'Reverse-Lunge-Hop':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/44_reverse_lunge_and_hop.png',
    'Jumping-Lunges':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/48_jumping_lunges.png',
    'Single-Leg-Burpee':'https://kettlebellsworkouts.com/wp-content/uploads/2018/06/50_single_leg_burpee.png'
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<action>')
def actionapp(action):
    return render_template('home.html', action=d[action])

# if __name__ == '__main__':
#     app.run()
