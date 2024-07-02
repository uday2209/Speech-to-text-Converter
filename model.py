import os
import torchaudio
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import jiwer

def load_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    if sample_rate != 16000:
        waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
    waveform = torchaudio.transforms.Vol(1.0, gain_type='amplitude')(waveform)  # Normalize audio
    return waveform.squeeze().numpy()

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def evaluate_asr_and_calculate_cer(audio_dir, text_dir, model_name='jonatasgrosman/wav2vec2-large-xlsr-53-english'):
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForCTC.from_pretrained(model_name)
    model.eval()

    cer_scores = []
    total_samples = 0

    for audio_file in os.listdir(audio_dir):
        if audio_file.endswith('.wav'):
            audio_path = os.path.join(audio_dir, audio_file)
            text_file = audio_file.replace('.wav', '.txt')
            text_path = os.path.join(text_dir, text_file)

            if os.path.exists(text_path):
                
                input_audio = load_audio(audio_path)
                input_values = processor(input_audio, sampling_rate=16000, return_tensors="pt").input_values

                
                with torch.no_grad():
                    logits = model(input_values).logits
                predicted_ids = torch.argmax(logits, dim=-1)
                transcription = processor.batch_decode(predicted_ids)[0].upper()  # Convert to uppercase

                
                reference = read_text(text_path).upper() 

                if reference and transcription:
                    cer = jiwer.cer(reference, transcription)
                    cer_scores.append(cer)
                    total_samples += 1

                    print(f"File: {audio_file}")
                    print(f"Reference: {reference}")
                    print(f"Transcription: {transcription}")
                    print(f"CER: {cer:.4f}")
                    
                else:
                    print(f"Skipping file {audio_file}: Reference or transcription is empty.")
                    

    if total_samples > 0:
        average_cer = sum(cer_scores) / total_samples
        print(f"Average CER: {average_cer:.4f}")
    else:
        print("No valid samples found to compute CER.")

# Evalution 
audio_directory = 'D:/DYSL1/DataSet/wav'
text_directory = 'D:/DYSL1/DataSet/corrected_txt'
evaluate_asr_and_calculate_cer(audio_directory, text_directory, model_name='jonatasgrosman/wav2vec2-large-xlsr-53-english')