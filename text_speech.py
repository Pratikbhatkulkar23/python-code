import gtts
import playsound

text = input("enter somethinge here:")
sound = gtts.gTTS(text,lang="en")
sound.save("wel.mp3")
playsound.playsound("wel.mp3")