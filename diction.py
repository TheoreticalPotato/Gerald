'''Take Voice Command'''
import speech_recognition as sr

def remove_before_word(string, word):
    # Split the string by the word
    parts = string.split(word)
    
    # Get the second part of the split
    if len(parts) > 1:
        result = ''.join(parts[1:])
    else:
        result = string
    
    return result

# Example usage
string = "This is a sample string. I want to remove everything before the word 'sample'."
word = "sample"

new_string = remove_before_word(string, word)
print(new_string)

# Takes command
def takeCommand():
    
    r = sr.Recognizer()
    # Uses default system microphone
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # Tries to do recognize your voice
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    # If voice can't be recognized
    except Exception as e:
        print(e)   
        print("Unable to recognize your goofy ass voice") 
        return "None"
    # Replaces 'gerald' and 'hey' so it doesnt mess up the command
    if 'Gerald' in query:
        query =  remove_before_word(query, "Gerald")
        return query
    
    # Will not register if query does not incklude "Gerald"
    else:
        query = ""
        return query 