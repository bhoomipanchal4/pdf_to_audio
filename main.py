from twilio.rest import Client
import os
from PyPDF2 import PdfReader
from gtts import gTTS
from twilio.twiml.voice_response import VoiceResponse

from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Fetch account information
account = client.api.accounts(account_sid).fetch()

print(account.friendly_name)
print(account.status)


reader = PdfReader("book.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

# Convert text to speech.

tts = gTTS(text=text)

tts.save("speech.mp3")

# Use Twilio to play audio.

response = VoiceResponse()

response.play("https://yourwebsite.com/speech.mp3")

print(response)