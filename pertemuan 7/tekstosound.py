from gtts import gTTS 
from playsound import playsound

mytext = '화이팅!'
language = 'ko'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("semangat.mp3") 
playsound("semangat.mp3", True)
