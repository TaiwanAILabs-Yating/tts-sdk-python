# -*- coding:utf-8 -*-
# Author: AILabs-TTS
from os.path import abspath, join, dirname
from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="Yating TTS SDK",
    version="0.1.2",
    author="pinkeyu7",
    author_email="pinke.yu7@gmail.com",
    description="Yating TTS SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TaiwanAILabs-Yating/tts-sdk-python",
    keywords="text to speech",
    packages=find_packages(exclude=["docs", "test*"]),
    include_package_data=True,
    install_requires=[
        "requests >= 2.22.0"
    ],
    python_requires=">=3.6",
)
