from extract_data_youtube import extractID, extractTitleChannel, extractTranscripts
from summarize_vid import summarizeVideo

def summarize_youtube_video(youtube_url, language='en'):
    try:
        video_id = extractID(youtube_url);

        title, channel = extractTitleChannel(youtube_url)
        print(f"\nVideo: {title}")
        print(f"Channel: {channel}")

        print("\nExtracting transcripts...")
        transcript = extractTranscripts(video_id, language)

        if transcript:
            #Summarize the Content
            print("\nGenerating summary...")
            summary = summarizeVideo(transcript, language)
            
            #Result of Summary
            print("\n=== SUMMARY ===")
            print(summary)
        else:
            print("No transcripts available for summarization.")

    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_url = input("Enter YouTube URL: ")
    language = input("Enter language code for summary (e.g., 'en', 'es'): ") or 'en'
    summarize_youtube_video(youtube_url, language)