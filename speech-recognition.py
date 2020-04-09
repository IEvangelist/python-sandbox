import os
import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = os.environ['SPEECH__SERVICE__KEY'], os.environ['SPEECH__SERVICE__REGION']

def recognize_speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print('Say something...')
    result = speech_recognizer.recognize_once()
    print(get_result_text(reason=result.reason, result=result))

def get_result_text(reason, result):
    reason_format = {
        speechsdk.ResultReason.RecognizedSpeech: 'Recognized: "{}"'.format(result.text),
        speechsdk.ResultReason.NoMatch: 'No speech could be recognized: {}'.format(result.no_match_details),
        speechsdk.ResultReason.Canceled: 'Speech Recognition canceled: {}'.format(result.cancellation_details)
    }
    return reason_format.get(reason, 'Unable to recognize speech')


recognize_speech_to_text()