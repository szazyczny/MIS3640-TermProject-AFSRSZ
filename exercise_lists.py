# Creating lists of exercises and muscle group categories

import random

# Abs = [
#     'Bodyweight Shoulder Taps',
#     'Bodyweight Bird Dog',
#     'Bodyweight Elbow to Knee',
#     'Bodyweight Hip Openers',
#     'Bodyweight Fast Mountain Climbers',
#     'Bodyweight Side Plank with Rotation',
#     'Bodyweight Scissors',
#     'Bodyweight High Knees',
#     'Bodyweight Cross Overs',
#     'Bodyweight Dead Bug',
#     'Bodyweight Side Plank',
#     'Bodyweight Cross Body Mountain Climbers',
#     'Bodyweight Side Plank with Extension'
# ]

# Arms = [
#     'Bodyweight Dirty Dogs',
#     'Bodyweight Dive Bomber Push Ups',
#     'Bodyweight Plank to Push Up',
#     'Bodyweight Breakdancer Push Ups'
# ]

# Back = [
#     'Bodyweight Back Extensions',
#     'Bodyweight Single Leg Up and Down Dogs',
#     'Bodyweight Cross Body Extension'
# ]

# Chest = [
#     'Bodyweight Push Ups',
#     'Bodyweight T Push Ups',
#     'Bodyweight Mountain Climber Push Ups'
# ]

# Legs = [
#     'Bodyweight Y Squats',
#     'Bodyweight Single Leg Deadlift',
#     'Bodyweight Bridge',
#     'Bodyweight Forward Lunge',
#     'Bodyweight Lateral Squat',
#     'Bodyweight Static Lunge',
#     'Bodyweight Yoga Squat',
#     'Bodyweight Single Leg Deadlift with Overhead Reach',
#     'Bodyweight Burpees',
#     'Bodyweight Jump Squats',
#     'Bodyweight Reverse Lunge and Hop',
#     'Bodyweight Jumping Lunges',
#     'Bodyweight Single Leg Burpee'
# ]


Abs = [
    'Shoulder-Taps',
    'Bird-Dog',
    'Elbow-Knee',
    'Hip-Openers',
    'Fast-Mountain-Climbers',
    'Side-Plank-Rotation',
    'Scissors',
    'High-Knees',
    'Cross-Overs',
    'Dead-Bug',
    'Side-Plank',
    'Cross-Body-Mountain-Climbers',
    'Side-Plank-Extension'
]

Arms = [
    'Dirty-Dogs',
    'Dive-Bomber-Push-Ups',
    'Plank-Push-Up',
    'Breakdancer-Push-Ups'
]

Back = [
    'Back-Extensions',
    'Single-Leg-Up-Down-Dogs',
    'Cross-Body-Extension'
]

Chest = [
    'Push-Ups',
    'T-Push-Ups',
    'Mountain-Climber-Push-Ups'
]

Legs = [
    'Y-Squats',
    'Single-Leg-Deadlift',
    'Bridge',
    'Forward-Lunge',
    'Lateral-Squat',
    'Static-Lunge',
    'Yoga-Squat',
    'Single-Leg-Deadlift-Overhead-Reach',
    'Burpees',
    'Jump-Squats',
    'Reverse-Lunge-Hop',
    'Jumping-Lunges',
    'Single-Leg-Burpee'
]


UpperBody = Arms + Back + Chest

CoreBody = Abs

LowerBody = Legs

FullBody = UpperBody + CoreBody + LowerBody


import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Next!\n\n')


def demo(muscle, duration):
    counter = 0
    if duration == 'ten':
        while counter < 10:
            print(random.choice(muscle))
            counter += 1
            countdown(2)
        else:
            print('YAY, U NOT FAT!')
    elif duration == 'twenty':
        while counter < 20:
            print(random.choice(muscle))
            counter += 1
            countdown(2)
        else:
            print('YAY, U NOT FAT!')
    else:
        while counter < 30:
            print(random.choice(muscle))
            counter += 1
            countdown(2)
        else:
            print('YAY, U NOT FAT!')



def main():
    demo(FullBody, 's')

#     muscle = input('Select Muscle Group: ')
#     duration = input('Select your duration: ')

#     demo(muscle, duration)
#     # print(Abs)
#     # print(Arms)
#     # print(Back)
#     # print(Chest)
#     # print(Legs)

#     # print(CoreBody)
#     # print(UpperBody)
#     # print(LowerBody)
#     # print(FullBody)

#     # print(Duration)

    
    

if __name__ == '__main__':
    main()