import ollama
import os

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

    
if __name__ == "__main__":
    print(process_query("Tell me a joke!"))