import os
import whisper
import google.generativeai as genai
from gtts import gTTS
import subprocess

def text_to_speech(text, filename="output.wav", lang="ja"):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    subprocess.run(
        ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", filename],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def main():
    model = whisper.load_model("base")
    api_key = "APIkey"
    if not api_key:
        raise RuntimeError("環境変数 GOOGLE_API_KEY が設定されていません。")
    genai.configure(api_key=api_key)
    gemini = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

    while True:
        text = input("音声にしたいテキストを入力してください（「終了」で終了）: ")
        if text.strip() == "終了":
            break
        tts = gTTS(text=text, lang="ja")
        tts.save("input.wav")
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", "input.wav"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        result = model.transcribe("input.wav", fp16=False)
        transcript = result["text"]
        print(f"[音声認識結果] {transcript}")
        response = gemini.generate_content(transcript)
        print(f"[Geminiの応答] {response.text}")
        text_to_speech(response.text, filename="output.wav", lang="ja")

if __name__ == "__main__":
    main()

