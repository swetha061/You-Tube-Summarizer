# Youtube Summarizer
This project is a YouTube summarizer that accepts user-input YouTube video links and presents the YouTube video summary within 250 words. By seamlessly integrating the YouTube Transcript API and harnessing Gemini Pro's AI model, I've crafted a tool for distilling key insights from long videos, improving comprehension and accessibility.
## Steps
- Configure the Gemini API key and store it in a variable in the .env file.
- Create and activate the environment :
  `condo create -p venv python==3.10 -y`
  `conda activate venv/`
- Once the Environment is created, install all the requirements, listed in the requirements.txt. The following command can be used:
  `pip install -r requirements.txt`
  (Note: Ensure your file is saved before running the above command. If downloads fail to start, check your file's status)
- Develop functionalities for the project.
- Develop the Streamlit app interface to accept YouTube video links and display the generated summary.
- Run the app:
  `streamlit run app.py`
