import ollama
import os

def configure_system():
    # Check if ollama is running
    # if yes
    # check if a model is available
    # if yes
    pass

def process_query(user_query) -> str:
    messages = [
        {
            'role': 'system',
            'content' : 'you only talk like a teacher teaching kids less than 8 years of age and limit your answers to 20 words'
        
        },
        {
            'role' : 'user',
            'content' : user_query
        }
    ]
    response = ollama.chat(model='llama3.2', messages=messages)
    return response['message']['content'] 

def main(msg):
    configure_system()
    print(process_query(msg))
    
if __name__ == "__main__":
    main("I am feeling lucky !")