import os
from openai import OpenAI

def summarizeVideo(text, lang='en'):
    # api_key = os.getenv("OPENAI_API_KEY");

    # if not api_key:
    #     return "Summarization unavailable - no OpenAI API key provided";
    
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  
    )
    
    prompt = f'''Following text is in the original language from the video. Provide the output in this language: {lang}.
    Format the output as follows:
    
    Summary:
    (short summary of the video)
     
    Key Points:
    (List of Bullet Points about the video)

    Conclusion:
    (Conclusion about the video)
     
    Input text: {text}'''

    response = client.chat.completions.create(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content