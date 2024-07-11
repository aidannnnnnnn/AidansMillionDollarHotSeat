# Aidan's Million Dollar Hot Seat

Hello, and welcome to what essentially was my major project work in 2021 (I have recently modified it since). Here, I have made my own version of the Million Dollar Hot Seat Game, at the time, using my skills in Python (mainly relating to database management, and new skills in Python app development using Kivy and Tkinter), as this is aa language that I am extremely keen on maximising my knowledge and learning from. 

This was a challenging project, as I was balancing some new libraries and skills for the first time (Tkinter and Kivy), which when I was doing this in 2021, took me a while to learn. 

# The files in this repository
- **data.json -** This file stores both the question and answer base for our question list
- **game.py -** This file focuses more on the navigation process and setup of the GUI that we have within the game itself - positioning and setting titles, buttons, the game board, checking and responding with the correct answers based on the progress of the game, and so on
- **main.py -** This file concerns building the main kivy framework for the app - navigating between login and signup screens and its appropriate commands based on the situation (login, wrong password etc.), up until the user chooses to begin playing the game. 
- **my.kv -** This concerns the positioning, layout and setup of our kivy screens (the screens used to set up and login to the game)
- **runapp.py -** A one line executable that runs the game/app (through main.py, as runapp.py calls main.py)
- **userdetailsdatabase.py -** This focuses on our database management for users - checking logins against the database, adding new users, and so on
- **users.txt -** A text file storing the names, emails, passwords and date of signup for each user

This project was made in Python 3.9, and run using Visual Studio Code. For the below setup and execution of the programs to work, please ensure you have a minimum Python version of Python 3.9. installed, and are in the AI.EVC_2021 folder:

`cd AI.EVC_2021`

# Installing required libraries
For the code to work, you will need to install a set of libraries in your terminal, such as Kivy. Most of the libraries I have used are in the Python standard library , hence the list of required libraries is limited. All the required libraries are listed in requirements.txt, hence you can quickly install them by running:

`pip install -r requirements.txt`

# Running the program
To make the program running as seamless as possible, please ensure that you are in the AI.EVC_2021 folder. Once you are there, you can run the following command, which will load the game:

`python3 runapp.py`

## Beginning the game
Upon running the above, you will get to a page asking for login details. You can either create an account (by pressing the "Don't have an Account? Create One" button) or login to our test account. The details for the test account are as follows (included as this does not risk data):

`Username: test@test.test`
`Password: test`

Once you have entered your details to login, you can press the "Game" button, then the "Play game" button. This will take you to the Instructions page for the game, listing the rules for playing this game. Once you are ready to play, you can press the "Press this button to Play" game, which takes you to begin playing the game. 

At any time before beginning the game, you are able to navigate to the previous screen by pressing the "Back" or "Return to Previous Page" button. 

## Playing the Game
Upon entering the game, you will be prompted to enter your name. Once done, the game centre will display the amount of money the question is worth, and a money board on the right of the page, showing the steps you need to take to win the maximum prize for the game. 

You will be asked up to 24 questions related to entertainment purposes. For each question you get correct, you are given an option to leave with the "money" that you were playing for. If you choose not to leave, the game continues until you get a question wrong/complete all 24 questions. 

If you get a question wrong, choose to leave with a certain amount of "money", or complete the game, the game will let you know of this, and return you to the instructions page. 

At any time, you are able to quit the game, which returns you to the instructions page for the game. 

# Disclaimer
Please note that the answers to the questions were correct as of July 2021 - I will look to update this to new questions or use a question API to have a wider question bank. 

# Contact me: 
If you have any questions or comments, please feel free to contact me by the following:

- [LinkedIn](www.linkedin.com/in/aidan-robinson-102439264)