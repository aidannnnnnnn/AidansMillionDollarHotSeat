#  import necessary libraries
from tkinter import *                   
import time                             
from tkinter import messagebox as mb    
from tkinter import simpledialog        
import json                             
import webbrowser                       
import random                           

# Creates an object constructor for the game
class Quiz: 
    def __init__(self): 
        #  sets the maximum amount of Questions a user can be Asked
        self.DataSize = 24                       
        #  this variable randomizes a number between 0 and 24, where that number is the Question that will be Asked                   
        self.QuestionNumber = random.randint(0, self.DataSize) 

        #  a List that stores each Asked Question
        self.AskedList = []                                         
        self.AskedList.append(self.QuestionNumber)                  
        print(self.AskedList)

        #  calls and initialises the Display Title function
        self.Display_Title()                        

        # calls and initialises the Display Question function            
        self.Display_Question()       

        # this variable holds an integer with the default value 0 (i.e. the user has not selected an answer yet)            
        self.Opt_Selected = IntVar()                            

        # declare the user's options to be shown in the format of radio buttons    
        self.Opts = self.Radio_Buttons()             

        # calls and initialises the Display Option function               
        self.Display_Options()         

        # calls and initialises the Buttons function                             
        self.Buttons()                                  

        # sets the amount of questions the user has answered correct as 0            
        self.Correct = 0                  

        # Sets the Active Question's worth at $1                          
        self.Counter = 1                                            

        # sets a popup that asks the user for their name
        self.Answer = simpledialog.askstring("Name", "What is your first name?", parent=gui)        

        # while the input is an empty string or the user presses the "cancel Button"                
        while self.Answer is None or self.Answer == "":                                                             
            mb.showinfo("Error", "You must have a name")                    
            # keeps asking user to input a name until it satisfies commands of while loop (not an empty string)                                        
            self.Answer = simpledialog.askstring("Name", "What is your first name?", parent=gui)                    

        # a label that prints a welcome message to the user, placing it at the necessary position
        WelcomeLabel = Label(gui, text="Welcome {}!".format(self.Answer), bg="green", fg="white", font=("ariel", 30, "bold"))   
        WelcomeLabel.place(x=60, y=60)                                                                              
        
        # popup message to show how much the Question is worth
        mb.showinfo("Count", "You are currently playing for ${}".format(self.Counter))                              

        self.MoneyAtStake()                                                                                         
        self.MoneyBoard()                                                                                           

    def Display_Result(self):
        # Declare an alert that tells the user how much money they have won. The format is int(round(self.Counter/2)) as the counter multiplies by 2 before this command is executed.
        FinalInitialStatement = "Congratulations! You have Answered every Question and have won the game!\n You have won ${}".format(int(round(self.Counter))) 
        mb.showinfo("Result", f"{FinalInitialStatement}")   
        mb.showinfo("Message", "Thanks for playing!")      
        # destroys the GUI
        gui.destroy()                                       

    # This function defines what will happen if the user chooses to quit the app (Choose the quit button)
    def QuitApp(self): 
        QuitMessage = mb.askquestion("Exit the Application", 'Are you sure?', icon='warning')         
        if QuitMessage == 'yes':                                                                     
            gui.destroy()                                                                             
        else:
            mb.showinfo("Return", "You will return to the current screen")                            

    # This function checks if the user has answered the question correctly
    def CheckAnswer(self, QuestionNumber): 
        # If the option that the user selects is correct...
        if self.Opt_Selected.get() == Answer[self.QuestionNumber]:      
            mb.showinfo("Result", "You were Correct!!")                 
            return True                                                 
        else:
            # Declares the position of the correct answer for the respective question.
            Correct_Answer = Answer[self.QuestionNumber]   
            # Declares the correct choice as the position of the correct answer within the question's options                                         
            Correct_choice = Options[self.QuestionNumber][Correct_Answer -1]  
            # A popup to inform the user of the correct answer.                      
            mb.showinfo("Result", "Sorry, the Correct Answer was {}.".format(Correct_choice))       
            mb.showinfo("Alert", "You have incorrectly Answered this Question.\n You have lost. ") 
            mb.showinfo("Return", "Returning to the home screen. ")         
            # Destroys/Ends the GUI                        
            gui.destroy()                                                                           

    # Declares what happens if the user presses the next button after a correct answer
    def NextButton(self): 
        if self.CheckAnswer(self.QuestionNumber):     
            # When a correct answer is received, if the amount of questions correct (+1) = the amount of questions asked                                                                  
            if (self.Correct+1) == self.DataSize:                                                                       
                self.Display_Result()                                                                                   
                gui.destroy() 

            # Offer the users to walk away from the game, winning the amount at stake                                                                                          
            continuation = mb.askquestion("Result", "Would you like to walk away with ${}?".format(self.Counter))       
            # Multiply the winnings by 2
            self.Counter *= 2                                                                                          

            # If the user chooses yes....
            # Declare an alert that tells the user how much money they have won. The format is int(round(self.Counter/2)) as the counter multiplies by 2 before this command is executed.
            if continuation == 'yes':                                                                                   
                WinningAlert = "Congratulations, you have won ${}".format(int(round(self.Counter/2)))                   
                mb.showinfo("Result", f"{WinningAlert}")                                                                
                mb.showinfo("Action", "You will now be returned to the Home Screen")                                    
                gui.destroy()                                                                                           
            else:
                # Display a pop-up that informs the user that they are moving to the next question
                mb.showinfo("Continue", "Moving on to the Next Question")   
                # suspends the code execution for 2 seconds to lengthen the flow of the game                                            
                time.sleep(2)                                                                                           
                mb.showinfo("Continue", "You are now playing for ${}".format(self.Counter))                             

        # Increment the correct questions by 1
        self.Correct += 1          
        # Randomize another question from the json file.                                                                                     
        self.QuestionNumber = random.randint(0, self.DataSize)                                                          
        print(self.QuestionNumber)

        # if the randomised question number is not in the already asked list
        if self.QuestionNumber not in self.AskedList:      
            # add the question number to the list                                                             
            self.AskedList.append(self.QuestionNumber)                                                                  
            # print(self.AskedList)
        else:
            # randomize another question from the json file
            self.QuestionNumber = random.randint(0, self.DataSize)                                                      
            if self.QuestionNumber not in self.AskedList:       
                # add to list                                
                self.AskedList.append(self.QuestionNumber)                                                             
                # print(self.AskedList)
            else:
                self.QuestionNumber = random.randint(0, self.DataSize)                                                  
                if self.QuestionNumber not in self.AskedList:                                                           
                    self.AskedList.append(self.QuestionNumber)                                                         
                    # print(self.AskedList)
                else:
                    self.QuestionNumber = random.randint(0,self.DataSize)                                               
                    if self.QuestionNumber not in self.AskedList:                                                       
                        self.AskedList.append(self.QuestionNumber)                                                     
                        # print(self.AskedList)
                    else:
                        self.QuestionNumber = random.randint(0,self.DataSize)                                           
                        if self.QuestionNumber not in self.AskedList:                                                   
                            self.AskedList.append(self.QuestionNumber)                                                 
                            # print(self.AskedList)

        # If the user has answered the same amount of questions as the Data size (24)
        if (self.Correct) == self.DataSize:           
            # Execute the Display_result function (ie tell them theyve won)                                                                  
            self.Display_Result()                                                                                       
        else:
            self.Display_Question()                                                                                    
            self.Display_Options()                                                                                      
            self.MoneyAtStake()                                                                                        
            self.MoneyBoard()                                                                                        

    # places buttons on screen - content and position
    def Buttons(self):
        NextButton = Button(gui, text="Next", command=self.NextButton, width=10, bg="green", fg="green", font=("ariel", 16, "bold"))     
        NextButton.place(x=350, y=450) 

        Quit_Button = Button(gui, text="Quit", command=self.QuitApp, width=5, bg="green", fg="green", font=("ariel", 16, " bold"))  
        Quit_Button.place(x=700, y=90) 

    # This function defines the displaying of each question.
    def Display_Options(self):               
        # Set the question value as 0               
        QuestionValue = 0                                   
        self.Opt_Selected.set(0)
        # For each option in the options for each question
        for Option in Options[self.QuestionNumber]:         
            # Set each individual text option as a possible option
            self.Opts[QuestionValue]['text'] = Option       
            # Add 1 to the question value.
            QuestionValue += 1                         

    # This function defines the question that is displayed on the screen
    def Display_Question(self): 
        QuestionNumber = Label(gui, text=Question[self.QuestionNumber], width=120, bg="green", font=('ariel', 16, 'bold'), anchor='w') 
        QuestionNumber.place(x=70, y=225)   

    # This function defines the title of the GUI
    def Display_Title(self): 
        Title = Label(gui, text="AI.EVC (Answers are correct as of December 2021)", width=50, bg="green", fg="white", font=("ariel", 20, "bold"))     
        Title.place(x=0, y=2)                                                                              

    # This function prints and positions the 4 options for each question that the user can choose from
    def Radio_Buttons(self): 
        # Creates an empty list that stores each question option.
        QuestionList = []                               
        Y_Position = 275                   

        # While the length of the QuestionList is less than 4 (for 4 options)            
        while len(QuestionList) < 4:                    
            Radio_Button = Radiobutton(gui, text=" ", variable=self.Opt_Selected, bg="green", value=len(QuestionList) + 1, font=("ariel", 14)) 
            QuestionList.append(Radio_Button)      
            # place the button at a certain position on the GUI screen     
            Radio_Button.place(x=100, y=Y_Position)     
            # Add 40 to the Y_Position, so the next button can be stored directly below the previous button
            Y_Position += 40                            
        return QuestionList                             

    # This function defines the Money at Stake for each question - defines and postiions label.
    def MoneyAtStake(self): 
        MoneyBand = Label(gui, text="Amount of money at stake: \n ${}".format(self.Counter), width=50, bg="green", fg="white", font=("ariel", 20, "bold")) 
        MoneyBand.place(x=90, y=140) 

    # a function that prints out the board showing all the money options at stake
    def MoneyBoard(self): 
        BoardCount = 0                  
        BoardLabel = Label(gui, text="Money Board: ", width = 40, bg="green", fg="white", font=("ariel", 20, "bold")) 
        BoardLabel.place(x=860, y=10)   

        # An empty list that stores all of the labels below
        BoardList = []                  
        # This refers to the maximum amount of money that can be won, from answering all 24 questions correctly.
        MaxMoney = 8388608              
        # This is the position on the y axis for the money labels below
        Y_Position = 50    
        # This refers to the maximum amount of questions that can be asked during the game (24). Remember, python counts 0 as the first character, therefore this variable is set as 23)             
        Total_Boards = 23               

        # loops through the position on the board
        while BoardCount < 24:
            AmountButton = Label(gui, text="${}".format(int(round(MaxMoney))), width=20, bg="red", fg="white", font=("ariel", 20, "bold")) 
            # Adds the above button to the boardlist.
            BoardList.append(AmountButton)              
            # places the button on the GUI
            AmountButton.place(x=1000, y=Y_Position)    
            # adds 30 to the Y_Position variable, so the next label can be placed under the previous label
            Y_Position += 30        
            # Divides the MaxMoney variable by 2 (as the money labels from top to bottom go from the highest value to the lowest value i.e. $8388608 to $1)                    
            MaxMoney /= 2                   
            # Add 1 to the BoardCount: go to the next variable            
            BoardCount += 1                             

        # If the length of the boardlist is grater than 0... (this is for when the game is active)
        if len(BoardList) > 0:                          
            BoardList[len(BoardList)-1] = Label(gui, text="${}".format(self.Counter), width=20, bg="green", fg="white", font=("ariel", 20, "bold")) 
            # Multiply 30 by the correct question + 1., to move the y variable up by Counter
            Counter = 30*(self.Correct+1)                                       
            # Place the highlighted board on the position, reducing the y variable up by counter.
            BoardList[len(BoardList)-1].place(x=1000, y=Y_Position-Counter)     
            # Reduce the total boards by 1 (i.e. move on the board above)
            Total_Boards -= 1            

        return BoardList

# Initialises the GUI as a Tkinter Window
gui = Tk()                          
# sets the size of the GUI window   
gui.geometry("1500x1000")               
# sets the title of the GUI (shown at the top of the window)
gui.title("AI.EVC Quiz")      

# Set the background color to 'grey'
gui.configure(bg='grey')

# opens and loads question data from json file
with open('data.json') as f:            
    Data = json.load(f)                

# sets the Question as parts of the json file that are under the 'Question' variable
Question = (Data['question'])      
 # sets the Options as parts of the json file that are under the 'Options' variable     
Options = (Data['options'])            
# sets the Answer as parts of the json file that are under the 'Answer' variable
Answer = (Data['answer'])               

# calls the Quiz class so it can be executed
quiz = Quiz()                           

# a command that tells python to run the Tkinter event loop
# this listens for events, such as processes or button clicks and blocks any code that comes after it from running until the window it is called on is closed.
gui.mainloop()                          