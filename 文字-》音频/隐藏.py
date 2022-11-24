

import wave 

with open('txt.txt', 'rb') as f:
    txt_data = f.read()
    file_len = len(txt_data)
    txt_data = file_len.to_bytes(3, byteorder = 'little') + txt_data

with wave.open("音乐.wav", "rb") as f:
    attrib = f.getparams() 
    wav_data = bytearray( f.readframes(-1) )


for index in range(len(txt_data)):
    wav_data[index * 4] = txt_data[index]
    

with wave.open("隐藏后-音乐.wav", "wb") as f:
    f.setparams(attrib)  
    f.writeframes(wav_data)


