# Import Kivy modules for UI development
from kivy.app import App                                    
from kivy.lang import Builder                               
from kivy.uix.screenmanager import ScreenManager, Screen    
from kivy.properties import ObjectProperty                  
from kivy.uix.popup import Popup                            
from kivy.uix.label import Label                            

# Import database module for user details storage
from userdetailsdatabase import DataBase                    

# Import subprocess module for calling external Python scripts
from subprocess import call                                 

# Define a class for the Create Account window
class CreateAccountWindow(Screen):  
    username = ObjectProperty(None) 
    email = ObjectProperty(None)    
    password = ObjectProperty(None) 

    # Define the submit method for account creation
    def submit(self):               
        # Check if the form inputs are valid, calling invalidForm() if not valid
        if self.username.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:  

            # check if the user's email already exists
            if UserDetails.get_user(self.email.text) != -1:
                # check if password is entered or not - this will impact on the error message printed
                if self.password.text == "":
                    invalidForm()    
                else:
                    alreadyExists()
            elif self.password.text != "":                                                                 
                UserDetails.add_user(self.email.text, self.password.text, self.username.text)       

                self.reset()                                                                        

                ScreenManagers.current = "login"                                                    
            else:
                invalidForm()                                                                       
        else:
            invalidForm()                                                                           

    # Define the login method for navigating to the login screen
    def login(self):                        
        self.reset()               
        # refers to the current Kivy screen in my.kv         
        ScreenManagers.current = "login"    

    # Define the reset method for clearing form inputs
    def reset(self):             
        self.email.text = ""     
        self.password.text = ""  
        self.username.text = ""  

# Define a class for the Login window
class LoginWindow(Screen):           
    email = ObjectProperty(None)     
    password = ObjectProperty(None)  

    # Define the login button method
    def loginBtn(self):                                                 
        if UserDetails.validate(self.email.text, self.password.text):   
            MainWindow.current = self.email.text                        
            self.reset()                                                
            ScreenManagers.current = "main"                             
        else:
            invalidLogin()                                              

    # Define the create account button method
    def createBtn(self):                            
        self.reset()                     
        # refers to the current Kivy screen in my.kv                    
        ScreenManagers.current = "create"           

    # Define the reset method for clearing form inputs
    def reset(self):                                
        self.email.text = ""                        
        self.password.text = ""                     

# Define a class for the Main window
class MainWindow(Screen):
    accountname = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    # Define the Game button method
    def GameButton(self):                       
        ScreenManagers.current = "IntroGame"    

    # Define the logout method
    def logOut(self):                           
        ScreenManagers.current = "login"        

# Define a class for the Game window
class GameWindow(Screen):                       
    pass                                        

# Define a class for the Intro Game window
class IntroGameWindow(Screen):                  
    pass                                        

# Define a class for the Instructions window
class InstructionsWindow(Screen):               
    # Define the GameRun method for starting the game
    def GameRun(self):                          
        call(["python", "game.py"])             

# Define a class for managing screens
class WindowManager(ScreenManager):             
    pass                                        

# Define the invalid login popup
def invalidLogin():   
    pop = Popup(title='Invalid Login', 
    content=Label(text='Invalid username or password.',
                    size_hint=(None, None), size=(480, 480), 
                    text_size=(480, None), 
                    halign='center', valign='middle'), 
    size_hint=(None, None), size=(500, 500))
    pop.open()                                                                                                             

# Define the invalid form popup
def invalidForm():      
    # also wrap the text so it doesn't go over the margin
    pop = Popup(title='Invalid Form',
    content=Label(text='Please fill in all inputs with valid information.',
                    size_hint=(None, None), size=(480, 480), 
                    text_size=(480, None), 
                    halign='center', valign='middle'), 
    size_hint=(None, None), size=(500, 500))
    pop.open()    

# let user know the email already exists
def alreadyExists():
    pop = Popup(title='Existing account',
    content=Label(text='The email you entered already exists! Please try again',
                    size_hint=(None, None), size=(480, 480), 
                    text_size=(480, None), 
                    halign='center', valign='middle'), 
    size_hint=(None, None), size=(500, 500))
    pop.open()                                                                    

# Load the Kivy language file that defines our screen conditions
kv = Builder.load_file("my.kv")             

# Initialize the screen manager
ScreenManagers = WindowManager()            
UserDetails = DataBase("users.txt")         

# Define the list of screens
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),               
           MainWindow(name="main"),                                                     
           GameWindow(name="game"), IntroGameWindow(name="IntroGame"),                  
           InstructionsWindow(name="instructions")]      

# Add screens to the screen manager
for screen in screens:                  
    ScreenManagers.add_widget(screen)   

# Set the initial screen
ScreenManagers.current = "login"        

# Define the main application class
class MyMainApp(App):                   
    def build(self):                    
        return ScreenManagers           

# Run the application if this is the main module
if __name__ == "__main__": 
    MyMainApp().run()      