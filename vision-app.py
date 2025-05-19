import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
load_dotenv()

# key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = os.getenv("GEMINI_API_KEY"))
vision_model = genai.GenerativeModel(model_name="gemini-1.5-flash")
prompt = """
You are an expert ICT trader. Based on the lower timeframe chart, give me a clear trade suggestion using Smart Money Concepts (SMC) tailored for sniper entries. Do NOT say 'no trade' or 'wait for more confirmation.' You MUST give a trade setup — even if it's high risk — and explain the reasoning. Your output must include:

- Buy or Sell Signal
- Exact Entry Price or Entry Zone
- Target
- Stoploss Level
- Reason for Taking the Trade (e.g., CHoCH, BOS, Liquidity Sweep, FVG, OB) OR Reason Why You Might Avoid the Trade (e.g., low volume, counter to HTF bias)

Keep the explanation short and sharp, like a professional ICT scalper. Prioritize sniper entry setups and liquidity grabs. Assume the viewer wants an actionable signal, not theory. If image is not uploaded print this message :*Please upload the Image to get the trade*, Once image is uploaded give your trade suggestion based on the uploaded image.
"""
def get_response(image):
    # if input != "":
    #     result = vision_model.generate_content([input,image])
    # else:
    result = vision_model.generate_content([prompt,image])    
    return result.text

st.set_page_config(page_title="Vision App")
st.header("Stock Image Analyzer")
# input = st.text_input("Input Prompt", key = "input")
uploaded_image = st.file_uploader("Upload image..", type=["png","jpeg","jpg"])
image = ""
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded image", use_container_width='true')

# submit = st.button("Tell me about this image")

response = get_response(image)
st.subheader("Your Trade Suggestion is on the Way....")
st.write(response)