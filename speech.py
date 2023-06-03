'''Speech Engine'''
import pyttsx3
import azure.cognitiveservices.speech as speechsdk

# TTS setup
engine = pyttsx3.init('sapi5')                    
engine.setProperty('rate', 230)     
engine.setProperty('volume', 1.0)    
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)

# azure config
speech_key = "Azure api key"
service_region = "region"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_synthesis_voice_name = "en-AU-NielNeural"
speech_config.speech_synthesis_speeed = 0.5
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def speak(text):
    result = speech_synthesizer.speak_text_async(text).get()

speak('hello, I am gerald, how can I help you today?')