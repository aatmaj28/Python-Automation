import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio
from asyncio import sleep
import pyautogui
import wolframalpha
from selenium import webdriver

#https://www.geeksforgeeks.org/voice-assistant-using-python/(Good source for adding more functionality)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



def search_web(input):

	driver = webdriver.Firefox()
	driver.implicitly_wait(1)
	driver.maximize_window()

	if 'youtube' in input.lower():

		speak("Opening in youtube")
		indx = input.lower().split().index('youtube')
		query = input.split()[indx + 1:]
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
		return

	elif 'wikipedia' in input.lower():

		speak("Opening Wikipedia")
		indx = input.lower().split().index('wikipedia')
		query = input.split()[indx + 1:]
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		else:

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

		return

def open_application(input):

	if "chrome" in input:
		speak("Google Chrome")
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
		return

	elif "firefox" in input or "mozilla" in input:
		speak("Opening Mozilla Firefox")
		os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
		return

	elif "word" in input:
		speak("Opening Microsoft Word")
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
		return

	elif "excel" in input:
		speak("Opening Microsoft Excel")
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
		return

	else:

		speak("Application not available")
		return
   

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/")   


        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the day' in query: 
            day = datetime.datetime.today().weekday() + 1
     
            Day_dict = {1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}
     
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("The day is " + day_of_the_week)


        elif 'open code' in query:
            codePath = "C:\\Users\\Aatmaj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to blank' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "blankyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Aatmaj bhai. I am not able to send this email")  

        elif 'quit' in query or 'bye' in query:
            speak("Quitting Sir. Thanks for your time..!!")
            print("Quitting Sir. Thanks for your time..!!")
            exit()
 
        elif 'text on whatsapp' in query:
            print(pyautogui.position())
            sleep(2)
            pyautogui.moveTo(3600,1604,1)   
            pyautogui.click()
            pyautogui.moveTo(3590,518,1)   
            pyautogui.click()
            pyautogui.write("What")
            pyautogui.moveTo(3563,752,1)
            pyautogui.click()
            pyautogui.moveTo(215,169,1)
            pyautogui.click()
            pyautogui.write("aatmaj jio")
            pyautogui.moveTo(272,380,1)
            pyautogui.click()
            pyautogui.moveTo(989,968,1)
            pyautogui.click()
            pyautogui.write("hello")
            pyautogui.moveTo(1863,961,1)
            pyautogui.click() 
                
        elif 'open' in query:
            open_application(query)
            
 
        else:
            speak("I can search the web for you, Do you want to continue?")
            ans = takeCommand()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(query)
            else:
                speak("Couldnt quite get you sir.")

                
