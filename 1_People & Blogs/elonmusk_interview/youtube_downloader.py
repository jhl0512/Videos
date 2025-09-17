import pandas as pd
import os
import yt_dlp

# CSV 불러오기
df = pd.read_csv("일론머스크인터뷰.csv")

# 저장할 폴더
save_path = "downloads"
os.makedirs(save_path, exist_ok=True)

# yt-dlp 옵션
ydl_opts = {
    'outtmpl': os.path.join(save_path, '%(autonumber)s_%(title).200B.%(ext)s'),
    'format': 'mp4/bestvideo+bestaudio/best',
}

for idx, row in df.iterrows():
    url = row['OG URL']
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"[완료] {url}")
    except Exception as e:
        print(f"[실패] {url} - {e}")