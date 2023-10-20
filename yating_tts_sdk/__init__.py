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

    MODEL_ZHEN_FEMALE_1 = "zh_en_female_1"
    MODEL_ZHEN_FEMALE_2 = "zh_en_female_2"
    MODEL_ZHEN_MALE_1 = "zh_en_male_1"
    MODEL_TAI_FEMALE_1 = "tai_female_1"
    MODEL_TAI_FEMALE_2 = "tai_female_2"
    MODEL_TAI_MALE_1 = "tai_male_1"

    ENCODING_MP3 = "MP3"
    ENCODING_LINEAR16 = "LINEAR16"

    SAMPLE_RATE_16K = "16K"
    SAMPLE_RATE_22K = "22K"

    RANGE_MAX = 1.5
    RANGE_MIN = 0.5

    def __init__(self, url, key):
        """
        Args:
        url (str): An API endpoint to a service provider.
        key (str): An auth key licenced from a service provider.
        """

        self._url = url
        self._key = key

    def synthesize(self, text: str, text_type: str, model: str, speed: float, pitch: float, energy: float, encoding: str, sample_rate: str, file_name: str):
        """
        text        (str): the text that you want to generate audio. If text_type is ssml, then sentence has 5000 length limit. Otherwise, it has 100 length limit.
        text_type   (str): determine the input text format.
        model       (str): the speaker that you want whom to speak your audio in specific language.
        speed       (float): voice speed, from 0.5-1.5.
        pitch       (float): voice pitch, from 0.5-1.5.
        energy      (float): voice energy, from 0.5-1.5.
        encoding    (str): audio file format.
        sample_rate (str): the sample rate for your generate audio.
        filename    (str): the filename for audio file.
        """

        self.validate(text, text_type, model, speed, pitch, energy, encoding, sample_rate)

        dto = self.generator(text, text_type, model, speed, pitch, energy, encoding, sample_rate)

        headers = dict()
        headers["key"] = self._key
        headers["Content-Type"] = "application/json"

        payload = json.dumps(dto)

        with requests.post(self._url, headers=headers, data=payload) as response:
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

    def validate(self, text: str, text_type: str, model: str, speed: float, pitch: float, energy: float, encoding: str, sample_rate: str):
        """
        Validate parameter for below:
        text        (str): should not be empty
        text_type   (str): ssml, text
        model       (str): zh_en_female_1, zh_en_female_2, zh_en_male_1, tai_female_1, tai_female_2, tai_male_1
        speed       (float): default 1, from 0.5 to 1.5
        pitch       (float): default 1, from 0.5 to 1.5
        energy      (float): default 1, from 0.5 to 1.5
        encoding    (str): MP3, LINEAR16
        sample_rate (str): 16K (22K not support yet)
        """

        type_list = [self.TYPE_SSML, self.TYPE_TEXT]
        model_list = [self.MODEL_ZHEN_FEMALE_1,
                      self.MODEL_ZHEN_FEMALE_2, self.MODEL_ZHEN_MALE_1,self.MODEL_TAI_FEMALE_1,
                      self.MODEL_TAI_FEMALE_2, self.MODEL_TAI_MALE_1]
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
        if speed < self.RANGE_MIN or speed > self.RANGE_MAX:
            raise Exception(f"speed: {speed} out of range")
        if pitch < self.RANGE_MIN or pitch > self.RANGE_MAX:
            raise Exception(f"pitch: {pitch} out of range")
        if energy < self.RANGE_MIN or energy > self.RANGE_MAX:
            raise Exception(f"energy: {energy} out of range")

    def generator(self, text: str, text_type: str, model: str, speed: float, pitch: float, energy: float, encoding: str, sample_rate: str):
        """
        Generate request body for api call.
        """

        return {
            "input": {
                "text": text,
                "type": text_type
            },
            "voice": {
                "model": model,
                "speed": speed,
                "pitch": pitch,
                "energy": energy
            },
            "audioConfig": {
                "encoding": encoding,
                "sampleRate": sample_rate
            }
        }
