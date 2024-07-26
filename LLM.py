import httpx
import ollama
import time
import spacy
import string
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Spacy model not found. Downloading the model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_text(path):
    with open(path, 'r') as file:
        text = file.read()
    
    return text
    

def score_applicant_responses(questions, answers):
    try:
        # Concatenate questions and answers
        input_text = ""
        for question, answer in zip(questions, answers):
            input_text += f"Q: {question}\nA: {answer}\n\n"
        
        
        response = ollama.chat(model='llama3', messages=[
            {
                "role": "user", 
                "content": 'The following text contains questions asked to an applicant and the applicant\'s transcribed answers. I want you to provide a score from 0 to 100 for the quality of the applicant\'s answers. Do a thorough analysis before coming up with your final scores. Provide a single score in the format: "Score: X". Nothing else should be output. Here is the data: ' + input_text,
            },
        ])
        return response['message']['content']
    except httpx.RequestError as e:
        print(f"An HTTP request error occurred: {e}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"An HTTP status error occurred: {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while scoring the responses: {e}")
        return None

def parse(keywords, textfile):
    foundwords = set()
    doc = nlp(textfile)
    for token in doc:
        if token.text.lower() in keywords:
            foundwords.add(token.text)
    
    score = len(foundwords)/len(keywords)
    
    return score*100
    
    
           
        

if __name__ == "__main__":
    # Example input
    questions = ["What is your experience with data analysis?"]
    answers = ["I have over 3 years of experience in data analysis, working with tools like SQL, Python, and Excel to analyze and interpret data."]

    key_words = ["python","machine", "learning","data science","sql"]
    
    start_time = time.time()
    

    text = extract_text("/Users/keshavgoel/Desktop/Vdart-1/ Python, Python, Python, SQL, machine learning.")

    score = score_applicant_responses(questions, text).split(':')[1]
    
    print(f"Applicant's Answer Quality Score: {score}")

    
    print(parse(key_words,text))

    
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time} seconds")
