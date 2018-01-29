Python 3.6.2 |Anaconda, Inc.| (default, Sep 19 2017, 08:03:39) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pyttsx3
>>> def text_to_speech(text):
	eng=pyttsx3.init()
	eng.say(text)
	eng.runAndWait()

	
>>> 
