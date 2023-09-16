#pip3 install SpeechRecognition pydub

import speech_recognition as sr


#Work for English

#Function Using Filename
def reco (filename):

    r = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        #Listen data from file
        audio_data = r.record(source)
        #Recognize and transcribe
        text = r.recognize_google(audio_data)
        print(text)
        print("Done")
        return text 


#test 

file = "Enregistrement (3).wav"
reco(file)