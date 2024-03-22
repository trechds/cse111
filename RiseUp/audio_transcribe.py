import whisper

modelo = whisper.load_model("base")

transcription = modelo.transcribe("nome do arqvuido.mp4")

print(transcription)