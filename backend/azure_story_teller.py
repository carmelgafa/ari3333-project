'''responsible to generate the speech for the story'''

import os
import time
from system_secret import AZURE_SUBSCRIPTION_KEY
import azure.cognitiveservices.speech as speechsdk

class AzureAIStoryTeller():

    def __init__(self):
        '''
        Initializes the AzureAIStoryTeller.

        Sets up the speech configuration for the Azure Cognitive Service Speech
        with the subscription key and region from the system_secret file.
        '''
        region = "northeurope"
        self.speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_SUBSCRIPTION_KEY,
            region=region)

    def generate_speech(self, text)-> str:
        '''
        Generates the speech for the story.

        Given a text, it generates a audio file 
        using the Azure Cognitive Service Speech 
        and saves it to the output_files folder.

        Returns the URL of the generated audio file.
        '''

        file_name = f"output_file_{time.strftime('%Y%m%d-%H%M%S')}.wav"

        # Create the output folder if it doesn't exist
        os.makedirs(os.path.join(os.path.dirname(__file__), "output_files"), exist_ok=True)

        output_file = os.path.join(
            os.path.dirname(__file__),
            "output_files",
            file_name)

        # Configure the speech service
        audio_config = speechsdk.audio.AudioOutputConfig(
            filename=output_file)

        # Create the synthesizer
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config,
            audio_config=audio_config)

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

    teller = AzureAIStoryTeller()
    text_to_speak = "Hello, this is a demonstration of Azure Text-to-Speech!"
    teller.generate_speech(text_to_speak)
