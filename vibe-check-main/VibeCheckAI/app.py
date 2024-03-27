import openai
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

openai.api_key = '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'
deepgram_api_key = '817843e6c5a9d5ac17dae5f89a5aa3e51bede179'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        if is_text_file(file.filename):
            text = file.read().decode('utf-8')
            return analyze_text_with_openai(text)
        elif is_audio_file(file.filename):
            transcript = transcribe_audio(file)
            if transcript:
                return analyze_text_with_openai(transcript)
            else:
                return 'Transcription failed'
    else:
        return 'Invalid file type'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'txt', 'mp3', 'wav'}


def is_text_file(filename):
    return filename.rsplit('.', 1)[1].lower() == 'txt'


def is_audio_file(filename):
    return filename.rsplit('.', 1)[1].lower() in {'mp3', 'wav'}


def analyze_text_with_openai(text):
    prompt = (
        f"Return the sentiment or psychological insights derived from the conversation, some insights about speakers: \n\n\n\n {text}"
    )
    try:
        response = openai.completions.create(
            model="babbage-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return format_dialogue(response.choices[0].text.strip())
    except Exception as e:
        error_message = str(e)
        if "429" in error_message:
            return "Looks like we've hit our quota limit for now."
        else:
            return error_message


def transcribe_audio(file):
    headers = {
        'Authorization': f'Token {deepgram_api_key}',
        'Content-Type': 'audio/wav'
    }
    try:
        response = requests.post(
            'https://api.deepgram.com/v1/listen',
            headers=headers,
            files={'file': file}
        )
        if response.status_code == 200:
            transcript = response.json()['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript
        else:
            return f"Error transcribing file: {response.text}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


def format_dialogue(insights):
    return insights.replace("\n", "<br /><br />")


if __name__ == '__main__':
    app.run(debug=True)
