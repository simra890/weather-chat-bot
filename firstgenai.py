import streamlit as st
from groq import Groq 
import requests

client =Groq(api_key="")
st.subheader("welcome to")
st.title("Simra's chatbot")


    
if  "messages" not in st.session_state:
    st.session_state.messages=[]
    
user_prompt=st.text_area("Enter your prompt :",placeholder="Ask here anything....")
cities={}
def getweather(city):
    cities={
        "bangalore":(12.79,77.99),
        "mumbai":(19.0,71.1)
    }
    
    if city.lower() not in cities:
        return "city not found or defined"
    
   
        
    lat,longi=cities[city.lower()]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={longi}&current_weather=true"
    
    data = requests.get(url).json()
   
    
    return f" the current weather is {data['current_weather']['temperature']} °C"






if st.button("Generate the response"):
    if user_prompt:
        if "weather" in user_prompt.lower():
            for city in ['mumbai','bangalore']:
                if city in user_prompt.lower():
                    user_prompt = user_prompt + f" (weather data: {getweather(city)})"
                    break
    
        st.session_state.messages.append(
            {
                "role":"user",
                "content":user_prompt
            }
        )
        
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        answer=response.choices[0].message.content
        st.subheader("Response:")
        st.write(answer)
        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )
        
    else:
        st.warning("Please enter a prompt to genrate a response")
        
st.subheader("conversation history")
        
for message in st.session_state.messages:
    if message["role"]=="user":
        st.write(f" User:{message['content']}")
    elif message["role"]=="assistant":
        st.write(f" AI:{message['content']}")
    