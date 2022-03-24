import speech_recognition as sr

def speech2txt():
   r = sr.Recognizer()
   mic = sr.Microphone()

   with mic as source:
     audio = r.listen(source)

   output = r.recognize_google(audio)
   #output =  r.recognize_sphinx(audio)


   with open("output.txt","w") as fp:
     fp.write(output)

   return output


if __name__ == "__main__":

   print(speech2txt())              
