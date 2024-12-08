'''responsible to generate the speech for the story'''

import os
import time
from system_secret import AZURE_SUBSCRIPTION_KEY
import azure.cognitiveservices.speech as speechsdk

# Initialize the Text-to-Speech service
def generate_speech(text)-> str:

    region = "northeurope" 

    file_name = f"output_file_{time.strftime('%Y%m%d-%H%M%S')}.wav"

    # Create the output folder if it doesn't exist
    os.makedirs(os.path.join(os.path.dirname(__file__), "output_files"), exist_ok=True)

    output_file = os.path.join(
        os.path.dirname(__file__),
        "output_files",
        file_name)

    # Configure the speech service
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SUBSCRIPTION_KEY, region=region)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)

    # Create the synthesizer
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    # Synthesize the text
    result = synthesizer.speak_text_async(text).get()

    # Check the result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized and saved to {output_file}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.error_details:
            print(f"Error details: {cancellation_details.error_details}")

    return f'http://localhost:8080/backend/output_files/{file_name}'


if __name__ == "__main__":
# Example Usage
    text_to_speak = "Hello, this is a demonstration of Azure Text-to-Speech!"
    generate_speech(text_to_speak)
