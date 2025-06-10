# 音声認識チャットボット (Whisper + Gemini)

このプロジェクトは、以下の処理を自動で行う Python スクリプトです。
main.pyは一回限りの対話、test.pyは"終了"と入力するまで終わらない対話になるようにしました。



## このプロジェクトの目的

今後、音声認識AIを開発していくうえでの **土台となるもの** を作りたいと考え、本スクリプトを制作しました。  
将来的には以下のような拡張を予定しています：

- マイクによるリアルタイム音声入力
- Geminiの応答をTTSで音声出力
- AR/MR表示や対話型AIへの応用

---

## 🔁 処理の流れ

1. **入力したテキストを音声ファイルに変換**（gTTS）
2. **音声を Whisper により文字起こし**
3. **Gemini API により応答を生成**
4. **応答をコンソールに出力**

##環境・前提条件
Python 3.8 以上
Windows / Mac / Linux いずれでもOK（推奨：Windows）
マイク付きのPC

##セットアップ手順
1.このリポジトリをダウンロード
```git clone https://github.com/dev-ryu-lea/voice-chatbot.git
  cd voice-chatbot
```
