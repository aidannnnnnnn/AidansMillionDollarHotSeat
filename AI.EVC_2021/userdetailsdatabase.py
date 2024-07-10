# import the date time module
import datetime                     

# Creates an object constructor for the Data Base
class DataBase: 

    def __init__(self, filename): 
        self.filename = filename  
        self.users = None         
        self.file = None          
        self.load()               

    # a function that loads the user details from the text file.
    def load(self):                                                     
        # open the users file, for reading purposes
        self.file = open(self.filename, "r")                            
        # create an empty dictionary for the users
        self.users = {}                                                 

        # for each line in the file
        for line in self.file:                                          
            # split the email, password, name and date created by a ";"
            email, password, name, created = line.strip().split(";")    
            # match each user email with the password, name of user and the date created.
            self.users[email] = (password, name, created)               

        # close the file
        self.file.close()                                               

    # this function demonstrates what happens if the user wants to "get" their email
    def get_user(self, email):                                          
        # if the email exists in the user dictionary
        if email in self.users:                                         
            # return the users email
            return self.users[email]                                    
        else:
            # else return that the user does not exist
            return -1                                                   

    # This function declares what happens if the user chooses to create a new account
    def add_user(self, email, password, name):                                                  
        # if the email is not in the user list...
        if email.strip() not in self.users:                                                     
            # add the new user with stripped values and current date/time for account creation
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())   
            # calls the self.save function
            self.save()                                                                         
            # Return 1: The email was created
            return 1                                                                            
        else:
            # If the email is in the user dictionary, print that it already exists
            print("Email exists already")           
            # return -1 to show the occurrence was False
            return -1                               

    # this function shows what happens when the user validates their email and password (i.e. the app confirms if their details are legitimate)
    def validate(self, email, password):                
        # if the user email is not a false occurrence (i.e. it exists)
        if self.get_user(email) != -1:                  
            # Return the password to the email that the user has entered
            return self.users[email][0] == password     
        else:
            # If the user email is a false occurrence, return False to represent this
            return False                                

    # This function defines what happens once the user creates their account and submits it
    def save(self):                                         
        # Open the user database to write to is
        with open(self.filename, "w") as fileToOpen:        
            # For the user in the user dictionary
            for user in self.users:                         
                # Write the user's details to the file, splitting each aspect with a ";", and adding a newline at the end
                fileToOpen.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")    

    # method can be called on the class itself
    @staticmethod
    def get_date():                                         
        # return the time of the login
        return str(datetime.datetime.now()).split(" ")[0]   