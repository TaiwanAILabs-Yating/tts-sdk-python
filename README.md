# Yating TTS SDK - Python version

## Install

Initial Install

```bash
pip install Yating-TTS-SDK
```

Upgrade existed package

```bash
pip install Yating-TTS-SDK --upgrade
```

## PyPI Link

[Yating-TTS-SDK](https://pypi.org/project/Yating-TTS-SDK/)

## Available Key

- Please contact Yating TTS

### Input

```JSON
{
    "input": {
        "text": "sentence, the text that you want to generate audio",
        "type": "text"
    },
    "voice": {
        "model": "zh_en_female_1",
        "speed": 1,
        "pitch": 1,
        "energy": 1
    },
    "audioConfig": {
        "encoding": "LINEAR16",
        "sampleRate": "16K"
    }
}
```

## Available Variable

### Input Type

| Name | Description                          |
| ---- | ------------------------------------ |
| text | Recognize input.text as pure text.   |
| ssml | Recognize input.text in ssml format. |

### Voice Setting

| Name   | Type   | Value Limit  | Description                      |
| ------ | ------ | :----------: | -------------------------------- |
| model  | string | Table bellow | Voice Model                      |
| speed  | float  |  0.5 - 1.5   | Voice Speed, faster slower       |
| pitch  | float  |  0.5 - 1.5   | Voice Pitch, higher or lower     |
| energy | float  |  0.5 - 1.5   | Voice Energy, stronger or weaker |

### Voice Model

| Name           | Sample Rate | Description                        |
| -------------- | ----------- | ---------------------------------- |
| zh_en_female_1 | 16k,22k     | Yating speak Mandarin and English  |
| zh_en_female_2 | 16k,22k     | Yiqing speak Mandarin and English  |
| zh_en_male_1   | 16k,22k     | Jiahao speak Mandarin and English  |
| zh_en_male_2   | 22k         | Zhiming speak Mandarin and English |
| tai_female_1   | 16k,22k     | Yating speak Taiwanese             |
| tai_female_2   | 16k,22k     | Yiqing speak Taiwanese             |
| tai_male_1     | 16k,22k     | Jiahao speak Taiwanese             |

### Encoding Format

| Name     | File Extension | Description                 |
| -------- | -------------- | --------------------------- |
| MP3      | .mp3           | Compressed audio            |
| LINEAR16 | .wav           | Uncompromised audio quality |

### Sampling Rate

| Name | Description            |
| ---- | ---------------------- |
| 16K  | Sampling rate in 16khz |
| 22K  | Sampling rate in 22khz |
