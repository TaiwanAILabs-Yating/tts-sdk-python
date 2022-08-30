"""
Yating TTS SDK
"""

import base64
import json
from urllib.error import HTTPError
import requests


class YatingClient:
    """
    YatingClient provide TTS synthesize service via api call.
    """

    TYPE_SSML = "ssml"
    TYPE_TEXT = "text"

    MODEL_FEMALE_1 = "zh_en_female_1"
    MODEL_FEMALE_2 = "zh_en_female_2"
    MODEL_MALE_1 = "zh_en_male_1"

    ENCODING_MP3 = "MP3"
    ENCODING_LINEAR16 = "LINEAR16"

    SAMPLE_RATE_16K = "16K"

    def __init__(self, url, key):
        """
        Args:
        url (str): An API endpoint to a service provider.
        key (str): An auth key licenced from a service provider.
        """

        self._url = url
        self._key = key

    def synthesize(self, text: str, text_type: str, model: str, encoding: str, sample_rate: str, file_name: str):
        """
        text        (str): the text that you want to generate audio.
        text_type   (str): determine the input text format.
        model       (str): the speaker that you want whom to speak your audio in specific language.
        encoding    (str): audio file format.
        sample_rate (str): the sample rate for your generate audio.
        filename    (str): the filename for audio file.
        """

        self.validate(text, text_type, model, encoding, sample_rate)

        dto = self.generator(text, text_type, model, encoding, sample_rate)

        headers = dict()
        headers["key"] = self._key
        headers["Content-Type"] = "application/json"

        payload = json.dumps(dto)

        with requests.post(self._url,  headers=headers, data=payload,) as response:
            if response.ok:
                result = response.json()

                if result["audioConfig"]["encoding"] == self.ENCODING_MP3:
                    file_name = f"{file_name}.mp3"
                else:
                    file_name = f"{file_name}.wav"

                data = base64.b64decode(result["audioContent"])

                audio_file = open(file_name, "wb")
                audio_file.write(data)
                audio_file.close()
            else:
                result = response.json()
                reason = " ".join(result["message"])
                raise HTTPError(self._url, response.status_code,
                                reason, response.headers, None)

    def validate(self, text: str, text_type: str, model: str, encoding: str, sample_rate: str):
        """
        Validate parameter for below:
        text        (str): should not be empty
        text_type   (str): ssml, text
        model       (str): zh_en_female_1, zh_en_female_2, zh_en_male_1
        encoding    (str): MP3, LINEAR16
        sample_rate (str): 16K
        """

        type_list = [self.TYPE_SSML, self.TYPE_TEXT]
        model_list = [self.MODEL_FEMALE_1,
                      self.MODEL_FEMALE_2, self.MODEL_MALE_1]
        encoding_list = [self.ENCODING_MP3, self.ENCODING_LINEAR16]
        sample_rate_list = [self.SAMPLE_RATE_16K]

        if text == "":
            raise Exception("text is empty")
        if text_type not in type_list:
            raise Exception(f"{text_type} not in type_list")
        if model not in model_list:
            raise Exception(f"{model} not in model_list")
        if encoding not in encoding_list:
            raise Exception(f"{encoding} not in encoding_list")
        if sample_rate not in sample_rate_list:
            raise Exception(f"{sample_rate} not in sample_rate_list")

    def generator(self, text: str, text_type: str, model: str, encoding: str, sample_rate: str):
        """
        Generate request body for api call.
        """

        return {
            "input": {
                "text": text,
                "type": text_type
            },
            "voice": {
                "model": model
            },
            "audioConfig": {
                "encoding": encoding,
                "sampleRate": sample_rate
            }
        }
