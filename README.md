# MIS3640-TermProject-AFSRSZ
MIS3640 Term Project

Website: https://sites.google.com/babson.edu/dorm-room-fitness-mis3640

The Project:
The main idea for our project is an application or website to help college students work out in limited space (like dorm room) and with limited time. The idea for this program is to simulate a magic 8 ball). A magic 8 ball displays a random answer from a predetermined pool of options. This is what we want to do but instead of generating random answers to questions, our program will generate random sets of exercises. Our minimum viable product (MVP) is a program that will generate a random yet predetermined set of exercises for a full body workout. With the MVP the user can prompt the program to display a set of exercises that the user will perform. Our stretch goal would be to have a program that even though it will generate random exercise sets, it stays within the parameters set by the user regarding the type of workout they want to perform. For example, the user can choose to do a workout that exercises only legs and core and they could choose to do a short or long workout, and the program will generate random sets of exercises that still meet these requirements.

Timerapp.py:
Index function: Generates a URL that connects the python code to a web app to display the results
Timer function: Takes a time (num) and an action (if no action, default action is Shoulder-Taps). Pulls the image of the action by getting the value of the actio (key) which is the link for the image. Returns The index function to display the action, timer and image.
Minutes function: Generates a URL for timer. It calculates the minutes in the time inputed for timer by multiplying the seconds by 60.
Hours function: Generates a URL for timer. It calculates the hours in the time inputted for timer by multiplying the seconds by 3600.
Page_not_found function: Displays an error flash message if page is not found.
Demo function: Takes the muscle group and picks a randome excercise from the muscle group list. Generates a URL to connect the results of the Timer function in the web application.

Developed UI using index.html under the template folder as well as style.css and timer.js under the static folder.
The display includes a title heading, the timer (button), exercise image, and current action name.
The application will select a random exercise to display for 60 seconds. When time's up the user can click "Time's Up" for another random exercise to be generated. The user has the ability to complete as many exercises as desired.
