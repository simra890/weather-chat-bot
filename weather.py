import streamlit as st
from groq import Groq
import requests
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="DCL AI ASSISTANCE",
    layout="wide",
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

if "messages" not in st.session_state:
    st.session_state.messages = [ ]

st.subheader("Welcome to")
st.title("Simra's Chatbot")


def getweather(city):
    cities = {
        "visakhapatnam": (17.6868, 83.2185),
        "vijayawada": (16.5062, 80.6480),
        "guntur": (16.3067, 80.4365),
        "nellore": (14.4426, 79.9865),
        "kurnool": (15.8281, 78.0373),
        "tirupati": (13.6288, 79.4192),
        "rajahmundry": (17.0005, 81.8040),
        "amaravati": (16.5730, 80.3564),
        "itanagar": (27.0844, 93.6053),
        "naharlagun": (27.1023, 93.6942),
        "guwahati": (26.1445, 91.7362),
        "silchar": (24.8333, 92.7789),
        "dibrugarh": (27.4728, 94.9120),
        "jorhat": (26.7509, 94.2037),
        "dispur": (26.1407, 91.7882),
        "patna": (25.5941, 85.1376),
        "gaya": (24.7955, 85.0002),
        "bhagalpur": (25.2425, 86.9842),
        "muzaffarpur": (26.1209, 85.3647),
        "darbhanga": (26.1542, 85.8918),
        "purnia": (25.7771, 87.4753),
        "raipur": (21.2514, 81.6296),
        "bhilai": (21.1938, 81.3509),
        "bilaspur": (22.0797, 82.1409),
        "korba": (22.3595, 82.7501),
        "durg": (21.1904, 81.2849),
        "panaji": (15.4909, 73.8278),
        "margao": (15.2832, 73.9862),
        "vasco_da_gama": (15.3959, 73.8146),
        "ahmedabad": (23.0225, 72.5714),
        "surat": (21.1702, 72.8311),
        "vadodara": (22.3072, 73.1812),
        "rajkot": (22.3039, 70.8022),
        "gandhinagar": (23.2156, 72.6369),
        "bhavnagar": (21.7645, 72.1519),
        "jamnagar": (22.4707, 70.0577),
        "junagadh": (21.5222, 70.4579),
        "anand": (22.5645, 72.9289),
        "chandigarh": (30.7333, 76.7794),
        "faridabad": (28.4089, 77.3178),
        "gurugram": (28.4595, 77.0266),
        "ambala": (30.3752, 76.7821),
        "hisar": (29.1492, 75.7217),
        "rohtak": (28.8955, 76.6066),
        "panipat": (29.3909, 76.9635),
        "karnal": (29.6857, 76.9905),
        "shimla": (31.1048, 77.1734),
        "dharamshala": (32.2190, 76.3234),
        "mandi": (31.7040, 76.9318),
        "solan": (30.9045, 77.0967),
        "ranchi": (23.3441, 85.3096),
        "jamshedpur": (22.8046, 86.2029),
        "dhanbad": (23.7957, 86.4304),
        "bokaro": (23.6693, 86.1511),
        "bengaluru": (12.9716, 77.5946),
        "mysore": (12.2958, 76.6394),
        "hubli": (15.3647, 75.1240),
        "mangaluru": (12.9141, 74.8560),
        "belgaum": (15.8497, 74.4977),
        "davangere": (14.4644, 75.9218),
        "bellary": (15.1394, 76.9214),
        "shimoga": (13.9299, 75.5681),
        "tumkur": (13.3379, 77.1019),
        "bidar": (17.9104, 77.5199),
        "thiruvananthapuram": (8.5241, 76.9366),
        "kochi": (9.9312, 76.2673),
        "kozhikode": (11.2588, 75.7804),
        "thrissur": (10.5276, 76.2144),
        "kollam": (8.8932, 76.6141),
        "palakkad": (10.7867, 76.6548),
        "alappuzha": (9.4981, 76.3388),
        "kannur": (11.8745, 75.3704),
        "bhopal": (23.2599, 77.4126),
        "indore": (22.7196, 75.8577),
        "jabalpur": (23.1815, 79.9864),
        "gwalior": (26.2183, 78.1828),
        "ujjain": (23.1765, 75.7885),
        "sagar": (23.8388, 78.7378),
        "ratlam": (23.3315, 75.0367),
        "mumbai": (19.0760, 72.8777),
        "pune": (18.5204, 73.8567),
        "nagpur": (21.1458, 79.0882),
        "nashik": (19.9975, 73.7898),
        "aurangabad": (19.8762, 75.3433),
        "solapur": (17.6599, 75.9064),
        "kolhapur": (16.7050, 74.2433),
        "thane": (19.2183, 72.9781),
        "amravati": (20.9333, 77.7500),
        "nanded": (19.1383, 77.3210),
        "imphal": (24.8170, 93.9368),
        "shillong": (25.5788, 91.8933),
        "aizawl": (23.7271, 92.7176),
        "kohima": (25.6751, 94.1086),
        "dimapur": (25.9044, 93.7265),
        "bhubaneswar": (20.2961, 85.8245),
        "cuttack": (20.4625, 85.8828),
        "rourkela": (22.2604, 84.8536),
        "sambalpur": (21.4669, 83.9812),
        "puri": (19.8135, 85.8312),
        "berhampur": (19.3150, 84.7941),
        "ludhiana": (30.9010, 75.8573),
        "amritsar": (31.6340, 74.8723),
        "jalandhar": (31.3260, 75.5762),
        "patiala": (30.3398, 76.3869),
        "bathinda": (30.2110, 74.9455),
        "mohali": (30.7046, 76.7179),
        "jaipur": (26.9124, 75.7873),
        "jodhpur": (26.2389, 73.0243),
        "udaipur": (24.5854, 73.7125),
        "kota": (25.2138, 75.8648),
        "ajmer": (26.4499, 74.6399),
        "bikaner": (28.0229, 73.3119),
        "alwar": (27.5530, 76.6346),
        "bharatpur": (27.2152, 77.4938),
        "gangtok": (27.3314, 88.6138),
        "chennai": (13.0827, 80.2707),
        "coimbatore": (11.0168, 76.9558),
        "madurai": (9.9252, 78.1198),
        "tiruchirappalli": (10.7905, 78.7047),
        "tirunelveli": (8.7139, 77.7567),
        "salem": (11.6643, 78.1460),
        "erode": (11.3410, 77.7172),
        "vellore": (12.9165, 79.1325),
        "thoothukudi": (8.7642, 78.1348),
        "tiruppur": (11.1085, 77.3411),
        "ooty": (11.4102, 76.6950),
        "hyderabad": (17.3850, 78.4867),
        "warangal": (17.9784, 79.5941),
        "nizamabad": (18.6725, 78.0941),
        "karimnagar": (18.4386, 79.1288),
        "khammam": (17.2473, 80.1514),
        "agartala": (23.8315, 91.2868),
        "lucknow": (26.8467, 80.9462),
        "kanpur": (26.4499, 80.3319),
        "agra": (27.1767, 78.0081),
        "varanasi": (25.3176, 82.9739),
        "prayagraj": (25.4358, 81.8463),
        "meerut": (28.9845, 77.7064),
        "bareilly": (28.3670, 79.4304),
        "aligarh": (27.8974, 78.0880),
        "moradabad": (28.8386, 78.7733),
        "saharanpur": (29.9680, 77.5552),
        "gorakhpur": (26.7606, 83.3732),
        "noida": (28.5355, 77.3910),
        "mathura": (27.4924, 77.6737),
        "firozabad": (27.1591, 78.3957),
        "dehradun": (30.3165, 78.0322),
        "haridwar": (29.9457, 78.1642),
        "rishikesh": (30.0869, 78.2676),
        "haldwani": (29.2183, 79.5130),
        "roorkee": (29.8543, 77.8880),
        "kolkata": (22.5726, 88.3639),
        "howrah": (22.5958, 88.2636),
        "durgapur": (23.5204, 87.3119),
        "asansol": (23.6739, 86.9524),
        "siliguri": (26.7271, 88.3953),
        "bardhaman": (23.2324, 87.8615),
        "malda": (25.0108, 88.1415),
        "new delhi": (28.6139, 77.2090),
        "delhi": (28.7041, 77.1025),
        "port blair": (11.6234, 92.7265),
        "daman": (20.3974, 72.8328),
        "silvassa": (20.2740, 72.9970),
        "puducherry": (11.9416, 79.8083),
        "leh": (34.1526, 77.5770),
        "srinagar": (34.0837, 74.7973),
        "jammu": (32.7266, 74.8570),
        "kavaratti": (10.5626, 72.6369),
    }

    if city.lower() not in cities:
        return "City not found or not defined."

    lat, longi = cities[city.lower()]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={longi}&current_weather=true"
    data = requests.get(url).json()
    return f"The current weather is {data['current_weather']['temperature']} °C"


for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])

user_prompt = st.text_area("Enter your prompt:", placeholder="Ask anything here...")

if st.button("Generate Response"):
    if user_prompt:
        prompt_to_send = user_prompt

        if "weather" in user_prompt.lower():
            for city in  ["visakhapatnam", "vijayawada", "guntur", "nellore", "kurnool","tirupati", "rajahmundry", "amaravati", "hyderabad", "bengaluru","mumbai", "pune", "delhi", "new delhi", "chennai", "kolkata","jaipur", "lucknow", "bhopal", "patna", "ranchi", "bhubaneswar","guwahati", "shillong", "imphal", "aizawl", "kohima", "agartala","gangtok", "shimla", "chandigarh", "dehradun", "srinagar", "leh","jammu", "ahmedabad", "surat", "vadodara", "rajkot", "gandhinagar","kochi", "thiruvananthapuram", "kozhikode", "coimbatore", "madurai","nagpur", "nashik", "indore", "gwalior", "jabalpur","amritsar", "ludhiana", "jalandhar", "patiala","noida", "agra", "varanasi", "kanpur", "prayagraj","raipur", "panaji", "puducherry", "port blair"]:
                if city in user_prompt.lower():
                    prompt_to_send = user_prompt + f" (weather data: {getweather(city)})"
                    break

        st.session_state.messages.append({"role": "user", "content": prompt_to_send})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        answer = response.choices[0].message.content

        st.subheader("Response:")
        st.write(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

    else:
        st.warning("Please enter a prompt to generate a response.")
        
#this was my previous try     
# def getweather(city):
#     cities={
        
#         "visakhapatnam": (17.6868, 83.2185),
#         "vijayawada": (16.5062, 80.6480),
#         "guntur": (16.3067, 80.4365),
#         "nellore": (14.4426, 79.9865),
#         "kurnool": (15.8281, 78.0373),
#         "tirupati": (13.6288, 79.4192),
#         "rajahmundry": (17.0005, 81.8040),
#         "amaravati": (16.5730, 80.3564),
    
#         # Arunachal Pradesh
#         "itanagar": (27.0844, 93.6053),
#         "naharlagun": (27.1023, 93.6942),
    
#         # Assam
#         "guwahati": (26.1445, 91.7362),
#         "silchar": (24.8333, 92.7789),
#         "dibrugarh": (27.4728, 94.9120),
#         "jorhat": (26.7509, 94.2037),
#         "dispur": (26.1407, 91.7882),
    
#         # Bihar
#         "patna": (25.5941, 85.1376),
#         "gaya": (24.7955, 85.0002),
#         "bhagalpur": (25.2425, 86.9842),
#         "muzaffarpur": (26.1209, 85.3647),
#         "darbhanga": (26.1542, 85.8918),
#         "purnia": (25.7771, 87.4753),
    
#         # Chhattisgarh
#         "raipur": (21.2514, 81.6296),
#         "bhilai": (21.1938, 81.3509),
#         "bilaspur": (22.0797, 82.1409),
#         "korba": (22.3595, 82.7501),
#         "durg": (21.1904, 81.2849),
    
#         # Goa
#         "panaji": (15.4909, 73.8278),
#         "margao": (15.2832, 73.9862),
#         "vasco_da_gama": (15.3959, 73.8146),
    
#         # Gujarat
#         "ahmedabad": (23.0225, 72.5714),
#         "surat": (21.1702, 72.8311),
#         "vadodara": (22.3072, 73.1812),
#         "rajkot": (22.3039, 70.8022),
#         "gandhinagar": (23.2156, 72.6369),
#         "bhavnagar": (21.7645, 72.1519),
#         "jamnagar": (22.4707, 70.0577),
#         "junagadh": (21.5222, 70.4579),
#         "anand": (22.5645, 72.9289),
    
#         # Haryana
#         "chandigarh": (30.7333, 76.7794),
#         "faridabad": (28.4089, 77.3178),
#         "gurugram": (28.4595, 77.0266),
#         "ambala": (30.3752, 76.7821),
#         "hisar": (29.1492, 75.7217),
#         "rohtak": (28.8955, 76.6066),
#         "panipat": (29.3909, 76.9635),
#         "karnal": (29.6857, 76.9905),
    
#         # Himachal Pradesh
#         "shimla": (31.1048, 77.1734),
#         "dharamshala": (32.2190, 76.3234),
#         "mandi": (31.7040, 76.9318),
#         "solan": (30.9045, 77.0967),
    
#         # Jharkhand
#         "ranchi": (23.3441, 85.3096),
#         "jamshedpur": (22.8046, 86.2029),
#         "dhanbad": (23.7957, 86.4304),
#         "bokaro": (23.6693, 86.1511),
    
#         # Karnataka
#         "bengaluru": (12.9716, 77.5946),
#         "mysore": (12.2958, 76.6394),
#         "hubli": (15.3647, 75.1240),
#         "mangaluru": (12.9141, 74.8560),
#         "belgaum": (15.8497, 74.4977),
#         "davangere": (14.4644, 75.9218),
#         "bellary": (15.1394, 76.9214),
#         "shimoga": (13.9299, 75.5681),
#         "tumkur": (13.3379, 77.1019),
#         "bidar": (17.9104, 77.5199),
    
#         # Kerala
#         "thiruvananthapuram": (8.5241, 76.9366),
#         "kochi": (9.9312, 76.2673),
#         "kozhikode": (11.2588, 75.7804),
#         "thrissur": (10.5276, 76.2144),
#         "kollam": (8.8932, 76.6141),
#         "palakkad": (10.7867, 76.6548),
#         "alappuzha": (9.4981, 76.3388),
#         "kannur": (11.8745, 75.3704),
    
#         # Madhya Pradesh
#         "bhopal": (23.2599, 77.4126),
#         "indore": (22.7196, 75.8577),
#         "jabalpur": (23.1815, 79.9864),
#         "gwalior": (26.2183, 78.1828),
#         "ujjain": (23.1765, 75.7885),
#         "sagar": (23.8388, 78.7378),
#         "ratlam": (23.3315, 75.0367),
    
#         # Maharashtra
#         "mumbai": (19.0760, 72.8777),
#         "pune": (18.5204, 73.8567),
#         "nagpur": (21.1458, 79.0882),
#         "nashik": (19.9975, 73.7898),
#         "aurangabad": (19.8762, 75.3433),
#         "solapur": (17.6599, 75.9064),
#         "kolhapur": (16.7050, 74.2433),
#         "thane": (19.2183, 72.9781),
#         "amravati": (20.9333, 77.7500),
#         "nanded": (19.1383, 77.3210),
    
#         # Manipur
#         "imphal": (24.8170, 93.9368),
    
#         # Meghalaya
#         "shillong": (25.5788, 91.8933),
    
#         # Mizoram
#         "aizawl": (23.7271, 92.7176),
    
#         # Nagaland
#         "kohima": (25.6751, 94.1086),
#         "dimapur": (25.9044, 93.7265),
    
#         # Odisha
#         "bhubaneswar": (20.2961, 85.8245),
#         "cuttack": (20.4625, 85.8828),
#         "rourkela": (22.2604, 84.8536),
#         "sambalpur": (21.4669, 83.9812),
#         "puri": (19.8135, 85.8312),
#         "berhampur": (19.3150, 84.7941),
    
#         # Punjab
#         "ludhiana": (30.9010, 75.8573),
#         "amritsar": (31.6340, 74.8723),
#         "jalandhar": (31.3260, 75.5762),
#         "patiala": (30.3398, 76.3869),
#         "bathinda": (30.2110, 74.9455),
#         "mohali": (30.7046, 76.7179),
    
#         # Rajasthan
#         "jaipur": (26.9124, 75.7873),
#         "jodhpur": (26.2389, 73.0243),
#         "udaipur": (24.5854, 73.7125),
#         "kota": (25.2138, 75.8648),
#         "ajmer": (26.4499, 74.6399),
#         "bikaner": (28.0229, 73.3119),
#         "alwar": (27.5530, 76.6346),
#         "bharatpur": (27.2152, 77.4938),
    
#         # Sikkim
#         "gangtok": (27.3314, 88.6138),
    
#         # Tamil Nadu
#         "chennai": (13.0827, 80.2707),
#         "coimbatore": (11.0168, 76.9558),
#         "madurai": (9.9252, 78.1198),
#         "tiruchirappalli": (10.7905, 78.7047),
#         "tirunelveli": (8.7139, 77.7567),
#         "salem": (11.6643, 78.1460),
#         "erode": (11.3410, 77.7172),
#         "vellore": (12.9165, 79.1325),
#         "thoothukudi": (8.7642, 78.1348),
#         "tiruppur": (11.1085, 77.3411),
#         "ooty": (11.4102, 76.6950),
    
#         # Telangana
#         "hyderabad": (17.3850, 78.4867),
#         "warangal": (17.9784, 79.5941),
#         "nizamabad": (18.6725, 78.0941),
#         "karimnagar": (18.4386, 79.1288),
#         "khammam": (17.2473, 80.1514),
    
#         # Tripura
#         "agartala": (23.8315, 91.2868),
    
#         # Uttar Pradesh
#         "lucknow": (26.8467, 80.9462),
#         "kanpur": (26.4499, 80.3319),
#         "agra": (27.1767, 78.0081),
#         "varanasi": (25.3176, 82.9739),
#         "prayagraj": (25.4358, 81.8463),
#         "meerut": (28.9845, 77.7064),
#         "bareilly": (28.3670, 79.4304),
#         "aligarh": (27.8974, 78.0880),
#         "moradabad": (28.8386, 78.7733),
#         "saharanpur": (29.9680, 77.5552),
#         "gorakhpur": (26.7606, 83.3732),
#         "noida": (28.5355, 77.3910),
#         "mathura": (27.4924, 77.6737),
#         "firozabad": (27.1591, 78.3957),
    
#         # Uttarakhand
#         "dehradun": (30.3165, 78.0322),
#         "haridwar": (29.9457, 78.1642),
#         "rishikesh": (30.0869, 78.2676),
#         "haldwani": (29.2183, 79.5130),
#         "roorkee": (29.8543, 77.8880),
    
#         # West Bengal
#         "kolkata": (22.5726, 88.3639),
#         "howrah": (22.5958, 88.2636),
#         "durgapur": (23.5204, 87.3119),
#         "asansol": (23.6739, 86.9524),
#         "siliguri": (26.7271, 88.3953),
#         "bardhaman": (23.2324, 87.8615),
#         "malda": (25.0108, 88.1415),
    
#         # Union Territories
#         "new_delhi": (28.6139, 77.2090),
#         "delhi": (28.7041, 77.1025),
#         "port_blair": (11.6234, 92.7265),
#         "daman": (20.3974, 72.8328),
#         "silvassa": (20.2740, 72.9970),
#         "puducherry": (11.9416, 79.8083),
#         "leh": (34.1526, 77.5770),
#         "srinagar": (34.0837, 74.7973),
#         "jammu": (32.7266, 74.8570),
#         "kavaratti": (10.5626, 72.6369),
#         "chandigarh_ut": (30.7333, 76.7794),
            
        
#     }
    
    
#     if city.lower() not in cities:
#         return "city not found or defined"
    
   
        
#     lat,longi=cities[city.lower()]
#     url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={longi}&current_weather=true"
    
#     data = requests.get(url).json()
   
    
#     return f" the current weather is {data['current_weather']['temperature']} °C"
