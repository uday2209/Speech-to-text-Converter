# Speech-to-Text Converter

This repository hosts a robust speech-to-text conversion model utilizing the Word2Vec algorithm. It excels in accurately transcribing spoken language, 
adeptly handling diverse accents including Indian accents, and varying noise levels. Implemented in Python, this model is ideal for integrating into voice assistants, transcription services, and other speech recognition systems.

**Installation**<br>
To install the necessary dependencies and set up the environment, follow these steps:

Create and activate a virtual environment (optional but recommended):<br>
python3 -m venv venv<br>
cd venv\Scripts\activate

Install the required dependencies:<br>
pip install -r requirements.txt

**Dataset**

Nptel pure data of used in this model.<br>
https://github.com/AI4Bharat/NPTEL2020-Indian-English-Speech-Dataset<br>

**Results**

**Average Character Error Rate (ACER) :-  0.1966**

**Examples**


1)<br>
[INFO]  Processing file: 00003068300b3a77cfdd0208addd752f26c0c084963a1cdc0b4459ec.wav<br>
    Reference    : DENSITY PROFILE AND THIS HAS BEEN FOUND TO BE VERY SUITABLE FOR GUIDING THE LASER SO<br>
    Transcription: DENSELY PROFILE AND THIS HAS BEEN FOUND TO BE VERY SUITABLE FOR GUIDING THE LAZER SO<br>
    **CER          : 0.0357**<br>
2)<br>
[INFO] Processing file: 0000381573d407fe83934438efd5d2c0727766e4e14a79eca4aeb7f6.wav<br>
    Reference    : X NONNEGATIVE AND A IS A M BY N MATRIX AND RANK OF A IS EQUAL<br>
    Transcription: EXTNONIGAT YOU AND AZA EMBINMATRIX AN RANK OF AS EQUAL<br>
    **CER          : 0.3279**<br>
3)<br>
[INFO] Processing file: 0000381573d407fe83934438efd5d2c0727766e4e14a79eca4aeb7f6.wav<br>
    Reference    : X NONNEGATIVE AND A IS A M BY N MATRIX AND RANK OF A IS EQUAL<br>
    Transcription: EXTNONIGAT YOU AND AZA EMBINMATRIX AN RANK OF AS EQUAL<br>
    **CER          : 0.3279**<br>
