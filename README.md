## About

# Files
- Main.py
  A fastapi project to allow users to upload an audio file and then proceed to provide a transcription. The fastapi uses the get method to automatically redirect users to the Docs page where
  they can easily upload their own audio file and view trancription in the post section
- LLM.py
  A LLM that utilizes Ollama to rate a user's quality based on their answers to questions. Allows users to input their own questions and answers. 

# How to Run
- Create and start a Virtual Environment
- Install necessary packages (whisperx, fastapi, torch, etc)

FOR main.py
- Make sure virtual environment is running
- In terminal type fastapi dev main.py
    -  If an error occurs check imports/package installation
- The program will then redirect you to the docs page
- Click on Post -> try it out -> choose file -> select audio file -> execute
- Under responses and code response you should see the transcription of your audio

FOR LLM.py
- Make sure virtual environment is running
- In terminal type python LLM.py
- It should output a user quality score from 1-100
- In the code body you can experiment with different questions/answers/Ollama prompts
  
