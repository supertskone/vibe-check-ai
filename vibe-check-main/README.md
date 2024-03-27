# VibeCheckAI

VibeCheckAI is a sentiment analysis web application that allows users to upload either text or audio files for sentiment analysis using OpenAI's models:

<img width="100%" alt="image" src="https://github.com/nemanyas/vibe-check/assets/151020880/587e00f5-06cd-405a-9eb1-137df329d6cb">

## Features

- **Explorer Level:** Allows users to upload text files and receive sentiment analysis insights.
- **Hero Level:** Supports audio file uploads, transcribes them using the Deepgram API, and performs sentiment analysis on the transcribed text.
- **Future Improvements for Master and Grandmaster level:** Integration with Google Cloud Platform for scalable processing and exploration of alternative transcription services like Whisper for Grandmaster Level.

## Installation

1. Clone this repository to your local machine.
2. OpenAI and Deepgram API keys are inside the repository.
4. Run the Flask application using `python app.py` or using ▶️.

## Usage

1. Navigate to the web interface hosted at `http://127.0.0.1:5000`.
2. Upload a text or audio file using the provided form.
3. Receive sentiment analysis insights on the uploaded content.

## Code Overview

- The main application logic is contained in `app.py`.
- HTML templates for the web interface are located in the `templates/` directory.
- CSS styles for the web interface are located in the `static/style.css` file.
- Sentiment analysis is performed using OpenAI's babbage-002 model.

## Future Improvements

- Integration with Google Cloud Platform for scalable processing - it would take a bit more time to implement but should be easy to add:

  ### Initialize Google Cloud Storage client
    ```
    storage_client = storage.Client()
    bucket_name = 'vibe-check-bucket'
    ```
  ### Use it in the upload_file() method:
    ```
    bucket = storage_client.bucket(bucket_name)
          blob = bucket.blob(file.filename)
          blob.upload_from_file(file)
          return blob.path
    ```
- Exploration of alternative transcription services like Whisper for improved accuracy and reliability. 
  It is expected to yield superior results; however, from a code perspective, it appears quite similar.
