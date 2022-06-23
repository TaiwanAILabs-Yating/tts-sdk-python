"""
Example code for yating tts api call.
"""

from yating_tts_sdk import YatingClient as ttsClient

URL = "TTS_ENDPOINT"
KEY = "PUT_YOUR_API_KEY_HERE"


TEXT = "歡迎收聽雅婷文字轉語音"
TEXT_TYPE = ttsClient.TYPE_TEXT
MODEL = ttsClient.MODEL_FEMALE_1
ENCODING = ttsClient.ENCODING_MP3
SAMPLE_RATE = ttsClient.SAMPLE_RATE_16K
FILE_NAME = "example"


client = ttsClient(URL, KEY)
client.synthesize(TEXT, TEXT_TYPE, MODEL,
                  ENCODING, SAMPLE_RATE, FILE_NAME)
