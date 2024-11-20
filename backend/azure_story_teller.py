import os
import time
import azure.cognitiveservices.speech as speechsdk

# Initialize the Text-to-Speech service
def azure_tts(text)-> bool:
    # Replace these with your Azure TTS credentials
    subscription_key = "37QUuC4eUTVLa5UP2U4DHFRVvUSrGF0tAttG9P3GiQVIhQGdTj19JQQJ99AKACi5YpzXJ3w3AAAYACOGfGVC"
    region = "northeurope" 

    file_name = f"output_file_{time.strftime('%Y%m%d-%H%M%S')}.wav"

    output_file = os.path.join(
        os.path.dirname(__file__),
        "output_files",
        file_name)

    # Configure the speech service
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
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

# Example Usage
text_to_speak = "Hello, this is a demonstration of Azure Text-to-Speech!"
azure_tts(text_to_speak)
