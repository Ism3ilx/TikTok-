from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, AudioFileClip
from gtts import gTTS
import os

def create_video(text, output_name="output.mp4"):
    # 1. تحويل النص لصوت
    tts = gTTS(text=text, lang='ar')
    tts.save("voice.mp3")
    audio = AudioFileClip("voice.mp3")
    
    # 2. إنشاء خلفية (أو استخدام فيديو جاهز من المجلد)
    bg = ColorClip(size=(720, 1280), color=(30, 30, 30), duration=audio.duration)
    
    # 3. إضافة النص
    txt_clip = TextClip(text, fontsize=50, color='white', size=(600, None), method='caption')
    txt_clip = txt_clip.set_start(0).set_duration(audio.duration).set_position('center')
    
    # 4. دمج الكل
    video = CompositeVideoClip([bg, txt_clip])
    video = video.set_audio(audio)
    
    video.write_videofile(output_name, fps=24, codec="libx264")
    return output_name
  
