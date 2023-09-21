from winotify import Notification, audio # Importing winotify for notifications
import pickle # Importing pickle to saves events in files
import datetime # Importing datetime to deal with dates
import requests # Importing requests to extract info from the web
import sys # Importin sys to stop program execution

class EventManagement: # Class EventManagement deals with everything related to the events
    events = [] # List were are events are saved
       
    @classmethod
    def addEvent(cls, date, name): # Classmethod addEvent adds a dictionary to the events list
        newEvent = {'date': date, 'name': name} # The event must contain a date and a name
        cls.events.append(newEvent) # Event is added to the list
                  
    @classmethod
    def arrangeEvents(cls): # Classmethod arrangeEvents orders the event list by date
        cls.events = sorted(cls.events, key=lambda d: d['date']) # Sorting events by date
        
    @classmethod
    def saveEvents(cls): # Classmethod saveEvents stores the events in a pickle file
        print()
        print("Saving events...") # Print message
        with open('pickle.pk', 'wb') as fi: # Open pickle file
            pickle.dump(cls.events, fi) # The event list is saved on the pickle file
            fi.close() # Close pickle file
        print("Done") # Print message
        print()

    @classmethod
    def loadEvents(cls): # Classmethod loadEvents retrives all events from the pickle file
        print()
        print("Loading saved events...") # Print message
        with open('pickle.pk', 'rb') as fi: # Open pickle file
            cls.events = pickle.load(fi) # Saves in event list events from the pickle file
            fi.close() # Close pickle file
        print("Done") # Print message
        print()
    
    @classmethod
    def clearEvents(cls): # Classmethod clearEvents deletes all events
        print()
        print("Clearing all events") # Print message
        empty_list = [] # Create empty list
        with open('pickle.pk', 'wb') as fi: # Open pickle file
            pickle.dump(empty_list, fi) # Insert empty list inside pickle file
            fi.close() # Close pickle file
        cls.events = empty_list # and event list is equaled to empty list
        print("Done") # Print message
        print()
            
    @classmethod
    def deletePastEvents(cls): # Cassmethod deletePastEvents detletes events that have already past
        for x in cls.events: # For every event on the list
            if x['date'] < datetime.date.today(): # If the date of the event is less than todays date
                cls.events.remove(x) # The event will be deleted
   
class Notification1: # Class Notification1 deals with notifying the user
    @staticmethod
    def notify(): # Staticmethod notifies when an event is today
        today = datetime.datetime.now() # Save today's date
        for x in EventManagement.events: # For every event on the list
            if x['date'] == today: # If the events date equals today's date:
                name = str(x['name']) # A notification is send
                toast = Notification(app_id="Reminder", title=name, msg= "This event happens Today!",
                                     duration="short") 
                toast.set_audio(audio.Reminder, loop=False)
                toast.show() # Showing the notification
                
                        
class WeatherForecasting: # Class WeatherForecasting deals with the weather forecasting
    @staticmethod   
    def displayWeather(city): # Staticmethod displayWeather displays the weather forecast
        print() # Display the message
        print('Displaying Weater report for: ' + city)
        url = 'https://wttr.in/{}'.format(city) # fetch the weather details
        res = requests.get(url)
        print(res.text) # display the result
        
class Validations: # Class Validations validates user input
    @staticmethod        
    def validateYear(): # Staticmethod validateYear verifies the inputted year
        currentYear=datetime.datetime.now().year # Saving current year in a variable
        year=0
        while(year < currentYear): # while the inputted year is in the past
            year = input("In what year will the event be?") # Asks user for year
            try: # Try to use inputted year in a datetime object
                year=int(year)
                y=datetime.date(year, 1, 1) # Generic date used to check if year is valid
                if(year<currentYear): # Checks if the valid year is not in the past
                    print() # Display message for invalid, returns to start of while loop
                    print("Invalid: The event cannot be in the past.\nPlease try again:")
            except: # If not valid, set to zero to keep iterating inside while loop
                year=0
                print() # Display message for invalid, returns to start of while loop
                print("Invalid input for year.\nPlease try again")
        return year
    
    @staticmethod
    def validateMonth(year): # Staticmethod validateMonth verifies the inputted month
        currentYear=datetime.datetime.now().year # Saving current year in a variable
        currentMonth=datetime.datetime.now().month # Saving current month in a variable
        valid=False
        while(valid == False): # While invalid ask user for month
            month = input("In what month will the event happen?\nPlease write in number form:")
            if(year == currentYear): # if the year of the event is same as current year
                try: # Try to use inputted month in a datetime object
                    month = int(month)
                    m=datetime.date(1, month, 1)
                    if(month < currentMonth): # Check month is not in the past
                        print() # Display message for invalid, returns to start of while loop
                        print("Invalid: The event cannot be in the past.\nPlease try again:")
                    else:
                        valid = True # If not, then the date is valid, while loop can end
                except:
                    print() # Display message for invalid, returns to start of while loop
                    print("Invalid input for month.\nPlease try again")
            else: # If the year is not the same as current year then:
                try: # Try to use inputted month in a datetime object
                    month = int(month)
                    m=datetime.date(1, month, 1)
                    valid=True # If no errors then the date is valid, while loop can end
                except:
                    print() # Display message for invalid, returns to start of while loop
                    print("Invalid input for month.\nPlease try again")
        return month
    
    def validateDay(month, year): # Staticmethod validateDay verifies the inputted day
        currentYear=datetime.datetime.now().year # Saving current year in a variable
        currentMonth=datetime.datetime.now().month # Saving current month in a variable
        currentDay=datetime.datetime.now().day # Saving current day in a variable
        valid=False
        while(valid==False): # While invalid ask user for day
            day = input("What day of the month will the event happen in?\nPlease write in number form:")
            # if the year and the month of the event are same as the current
            if((year == currentYear) and (month==currentMonth)):
                try: # Try to use inputted month in a datetime object
                    day = int(day)
                    d=datetime.date(1, 1, day)
                    if(day < currentDay): # Check day is not in the past
                        print() # Display message for invalid, returns to start of while loop
                        print("Invalid: The event cannot be in the past.\nPlease try again:")
                    else:
                        valid = True # If not, then the date is valid, while loop can end
                except:
                    print() # Display message for invalid, returns to start of while loop
                    print("Invalid input for day.\nPlease try again")
            else: # If the year and month is not the same as current year then:
                try: # Try to use inputted month in a datetime object
                    day = int(day)
                    d=datetime.date(1, 1, day)
                    valid=True # If no errors then the date is valid, while loop can end
                except:
                    print() # Display message for invalid, returns to start of while loop
                    print("Invalid input for day.\nPlease try again")
        return day
    

class Main(EventManagement, WeatherForecasting): #Class Main has two methods
    def options(self):
        print() # Display program options to user
        print("Would you like to perform any of the following actions?:")
        print("Add an event ----------- Press 1")
        print("See upcoming events ---- Press 2")
        print("Clear all events ------- Press 3")
        print("Check the weather ------ Press 4")
        print("Exit ------------------- Press 5")
        opt = input() # Takes an input from the user
        print()
        return opt # Returns the option chosen by the user
    
    def actions(self): # Class actions takes decisions depending on user input
        option=0 # This ensures the while loop will run atleast once
        while(option != '5'): # While the input is not 5, because 5 is to exit the program
            option = self.options() # Options is equal to the method options
            if option == '1': # If user option is #1 then:
                # Asks user for the name of event
                name = input("What would you like the name of the new event to be?")
                year = Validations.validateYear() # Calls year validation
                month = Validations.validateMonth(year) # Calls month validation
                day = Validations.validateDay(month, year) # Calls day validation
                # After year, month and day has been verified, they are inserted into date object
                date = datetime.date(year, month, day)
                super().addEvent(date, name) # calling add-event method 
                super().arrangeEvents() # Sorting all events by date
            
            elif(option == '2'): # If user option is #2 then:
                print("Your upcoming events are:") # Print message
                for x in super().events: # For every event in event list
                # Print a formatted message of the date and name of each event
                    print(x['name']," --> " , str(x['date'])) 
                if super().events == []: # If the list is empty, print following message:
                    print("There are no saved events.") # Print message
                    print()
            
            elif(option == '3'): # If user option is #3 then:
                super().clearEvents() # Call clearEvents method to delete all events
            
            elif(option == '4'): # If user option is #4 then:
                # Asks for the name of the city you would like the weather forecast from
                city = input("From what city would you like a weather forecast?:")
                super().displayWeather(city) # Calls displayWeather method to display weather
            
            elif(option == '5'): # If user option is #5 then:
                super().saveEvents() # Call saveEvents method to save all events before exiting
                Notification1.notify() # Run notification method in case an event is today
                print("Goodbye!") # Goodbye message
                sys.exit() # Exits program
            
            else: # If not one of the previous options, input must be invalid
                print("Invalid input, try again:") # Print message
                self.actions() # Calls method again
                                        


print("Welcome!") # Welcome message

# Object for Main class
m = Main()
# Object for EventMangement
EM = EventManagement()

try:
    # Load events from previous executions of the program if any
    EM.loadEvents()
    # Delete events that already happend
    EM.deletePastEvents()
except: # If there is no existing pickle file
    with open('pickle.pk', 'wb') as fi: # Creating pickle file for the first time
        fi.close()
    
# Call notification method in case an event is today
Notification1.notify()

# Message to tell how many events are currently saved
print("You currently have", len(EM.events), "saved event(s).")

# Call Main method actions, to ask user what they want to do
m.actions()
