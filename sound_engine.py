import os
from gtts import gTTS
import speech_recognition as sr

def Welcome():
   welcome_msg = "Welcome to Covid-19 info system developed by Jayanti Prasad"
   language = 'en'
   myobj = gTTS(text=welcome_msg, lang=language, slow=False)
   myobj.save("data/welcome.mp3")
   os.system("mpg321 data/welcome.mp3")


def text2speech(text, cname):
   fpath = "data" + os.sep + str(cname) + ".mp3"
   language = 'en'
   myobj = gTTS(text=text, lang=language, slow=False)
   myobj.save(fpath)
   os.system("mpg321 " + fpath)


def speech2text():
   r = sr.Recognizer()
   mic = sr.Microphone()

   with mic as source:
     audio = r.listen(source)

   output = r.recognize_google(audio)

   return output


if __name__ == "__main__":

   Welcome() 
   text2speech("Here you will find some information about Covid-19 Epidemic","dummy")
   print("Please say something")

   print(speech2text())


