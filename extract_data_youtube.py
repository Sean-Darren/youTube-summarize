import re
import requests
import bs4
from youtube_transcript_api import YouTubeTranscriptApi

def extractID(link):
    ID_url = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", link)
    if ID_url:
        print("Video ID: ", ID_url.group(1))
        return ID_url.group(1)
    raise ValueError("Invalid Youtube URL")

def extractTitleChannel(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    raw = requests.get(link, headers=headers, timeout=10)
    raw.raise_for_status()
    
    tag = bs4.BeautifulSoup(raw.text, features="html.parser")
    title_video = tag.find("title").text.strip()
    channel_meta = tag.find("meta", {"itemprop": "name"})
    channel_video = channel_meta["content"] if channel_meta else "Unknown Channel"
    return title_video, channel_video

def extractTranscripts(video_id, language='en'):
    try:
        ytt_api = YouTubeTranscriptApi()
        
        transcript_list = ytt_api.list(video_id)
        
        try:
            transcript = transcript_list.find_manually_created_transcript([language, 'en'])
        except:
            transcript = transcript_list.find_generated_transcript([language, 'en'])
        
        fetched = transcript.fetch()
        return ' '.join([snippet.text for snippet in fetched])
        
    except Exception as e:
        print(f"Error getting transcripts: {e}")
        
        try:
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.list(video_id)
            transcript = transcript_list.find_transcript([language, 'en'])
            
            if transcript.is_translatable:
                translated = transcript.translate(language)
                fetched = translated.fetch()
            else:
                fetched = transcript.fetch()
            return ' '.join([snippet.text for snippet in fetched])
        except Exception as e2:
            print(f"Fallback failed: {e2}")
            return None