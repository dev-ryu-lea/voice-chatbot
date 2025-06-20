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
## 特徴

- 音声認識（Whisper）
- ChatGPTによる応答生成
- 音声合成（pyttsx3）

## 処理の流れ

1. **入力したテキストを音声ファイルに変換**（gTTS）
2. **音声を Whisper により文字起こし**
3. **Gemini API により応答を生成**
4. **応答をコンソールに出力**

## 環境・前提条件
Python 3.8 以上
Windows / Mac / Linux いずれでもOK（推奨：Windows）
マイク付きのPC

## セットアップ手順

### 1. リポジトリをダウンロード
```bash
git clone https://github.com/dev-ryu-lea/voice-chatbot.git
cd voice-chatbot
```
### 2.必要なライブラリのインストール
```
pip install -r requirements.txt
```
### 3.OpenAI APIキーの設定
main.pyに自分のAPIKEYを直接書き込んでください
### 注意：情報漏洩が怖い場合プロジェクトフォルダに.envというファイルを作成しその中に記述し環境変数としてエクスポートしてください

## 今後の展望
今現在WebSocketを用いたリアルタイム音声対話を開発中
使っているPCのスペック上TTSによる音声発話はいったん保留とし、マイクで入力リアルタイムで文字お越しを想定しています







