import time as t
import random as r
import datetime as dt
import pygame as pg
from pygame import mixer
print(t.ctime())
q=["Every morning, you have two choices: continue to sleep with your dreams or wake up and chase them.",
   "The best way to start the day is with a grateful heart.",
   "Every sunrise is an invitation to brighten someone's day.",
   "Good morning! Start your day with a smile and positive thoughts.",
   "A beautiful morning starts with a beautiful mindset.",
   "Rise up and attack the day with enthusiasm.",
   "Every day is a new beginning. Take a deep breath, smile, and start again.",
   "Let today be the day you give up who you’ve been for who you can become.",
   "Wake up with determination and go to bed with satisfaction.",
   "Good morning! Believe in yourself and make it happen.",
   "Today is a new day. Make it count.",
   "May your day be filled with good thoughts, kind people, and happy moments.",
   "Good morning! Your future is created by what you do today.",
   "Every morning is a chance to start anew.",
   "Embrace the glorious mess that you are.",
   "Let your soul expand, let your heart reach out to others in loving and generous warmth.",
   "A positive attitude will lead to positive outcomes.",
   "Good morning! You have the power to make this day amazing.",
   "Let the light of a new day inspire you to achieve greatness.",
   "May your day be as bright as your smile.",
   "Good morning! Let’s make today the best day ever.",
   "Success is waking up every day and finding peace of mind.",
   "Opportunities are like sunrises. If you wait too long, you miss them.",
   "The early bird gets the worm, but the second mouse gets the cheese.",
   "Today is a new day. Even if you were wrong yesterday, you can get it right today.",
   "Your day is only as good as you make it.",
   "Good morning! The secret of getting ahead is getting started.",
   "Wake up with determination. Go to bed with satisfaction.",
   "The best preparation for tomorrow is doing your best today.",
   "Every morning is a fresh start. It is never too late to dig in and begin a new journey of success.",
   "The future depends on what you do today.",
   "Good morning! Don’t watch the clock; do what it does. Keep going.",
   "Set a goal that makes you want to jump out of bed in the morning.",
   "Each morning we are born again. What we do today is what matters most.",
   "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
   "Good morning! The only limit to our realization of tomorrow is our doubts of today.",
   "Dream big and dare to fail.",
   "Your big opportunity may be right where you are now.",
   "Success is not the key to happiness. Happiness is the key to success.",
   "Good morning! Success is going from failure to failure without losing your enthusiasm.",
   "Do something today that your future self will thank you for."
   "நம்பிக்கையே எல்லாம், வழிகாட்டும் பொன்மொழிகள்",
   "எத்தனை இலக்குகளை அடைந்திருந்தாலும், அடுத்த இலக்கை அமைத்துக்கொள்.",
   "ஏழ்மைதான் என் வாழ்வின் மிகப்பெரிய உந்துதலாக இருந்தது."]
#print(r.choice(q))

AT=input("Enter the time(HH:MM:SS AM/PM)")
print("Alarm Set Successfully")

while True:
    CT=dt.datetime.now().strftime("%H:%M:%S %p")

    if CT==AT:
        print("Wake up! Alarm Ringing...")
        print("Motive of the Day")
        print(r.choice(q))
        pg.init()
        mixer.music.load("Mouth Organ Bgm.Mp3")
        mixer.music.play()
        break
    t.sleep(1)
'''
q=["நம்பிக்கையே எல்லாம், வழிகாட்டும் பொன்மொழிகள்","எத்தனை இலக்குகளை அடைந்திருந்தாலும், அடுத்த இலக்கை அமைத்துக்கொள்.","ஏழ்மைதான் என் வாழ்வின் மிகப்பெரிய உந்துதலாக இருந்தது."]
print(r.choice(q))
'''
