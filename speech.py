import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    speech = r.listen(source)
try:
    print('Output:\n'+r.recognize_google(speech))
except:
    pass
