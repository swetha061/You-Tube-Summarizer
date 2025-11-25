import streamlit as st
from dotenv import load_dotenv 
load_dotenv() #load all environment variables

import os
import google.generativeai as genai
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

from youtube_transcript_api import YouTubeTranscriptApi

prompt = "You are a Youtube video Summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points within 250 words. Please provide summary of the text given here: "

#function for getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript=""
        for i in transcript_text:
            transcript+=" "+i["text"]

        return transcript

    except Exception as e:
        raise e
    

#function for getting summary based on prompt from google gemini pro
def generate_gemini_content(transcript_text,prompt):

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text

#building a streamlit app
st.title("Youtube Summarizer")
youtube_link = st.text_input("Enter Youtube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]

if st.button("Get Summary"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        summary = generate_gemini_content(transcript_text,prompt)
        st.markdown("#SUMMARY#")
        st.write(summary)