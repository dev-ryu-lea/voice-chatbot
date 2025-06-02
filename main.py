import os
import whisper
import google.generativeai as genai
from gtts import gTTS

def text_to_speech(text, filename="input.wav", lang="ja"):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"音声ファイル '{filename}' を作成しました。")

def main():

    text = input("音声にしたいテキストを入力してください: ")


    text_to_speech(text, filename="input.wav", lang="ja")

    model = whisper.load_model("base")
    audio_path = "input.wav"

    print("[*] 音声を認識中...")
    result = model.transcribe(audio_path, fp16=False)
    transcript = result["text"]
    print(f"[音声認識結果] {transcript}")

    
    api_key = os.getenv("GOOGLE_API_KEY", "APIkey")
    genai.configure(api_key=api_key)

    print("[*] Geminiに問い合わせ中...")
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(transcript)

    print(f"\n[Geminiの応答] {response.text}")

if __name__ == "__main__":
    main()
