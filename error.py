from urllib import request
import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclibrary
import requests

url = "https://api.football-data.org/v4/competitions/CL/matches"

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi =" 9e53f84ef38742b982a9a6eb05ecb92a"

def speak(text):
   engine.say(text)
   engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
      webbrowser.open("https://google.com")
    elif "open hotstar" in c.lower():
      webbrowser.open("https://hotstar.com") 
    elif "open netflix" in c.lower():
      webbrowser.open("https://netflix.com") 
    elif "open twitter" in c.lower():
      webbrowser.open("https://twitter.com") 
    elif "open primevideo" in c.lower():
      webbrowser.open("https://primevideo.com") 
    elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")   
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = musiclibrary.music[song]
       webbrowser.open(link)
    elif "news" in c.lower():
      
          headers = {
              "X-Auth-Token": " 9e53f84ef38742b982a9a6eb05ecb92a"  # Replace with your actual API key
          }

          # Make the GET request
          response = requests.get(url, headers=headers)

          # Check if the request was successful
          if response.status_code == 200:
              data = response.json()  # Convert response to JSON
              speak(data)  # Print the data
          else:
              speak(f"Error {response.status_code}: {response.text}")  # Print error message
          
if __name__ == "__main__":
     speak("I'm On")
     while True:
      #Listen for the wake word "J"  
      # obtain audio from the microphone
      r = sr.Recognizer()
     
      # recognize speech using Sphinx
      print("recognizing....")
      try:
          with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=1,phrase_time_limit=1)
          word = r.recognize_google(audio)
          if (word.lower() == "hello"):
            speak("Yes Sir")
            #listen for command
            with sr.Microphone() as source:
              print("Jarvis Active...")
              audio = r.listen(source)
              command = r.recognize_google(audio)

              processCommand(command)

      except Exception as e:
          print("Error; {0}".format(e))
