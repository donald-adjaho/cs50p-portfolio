# CS50P Week7
# Objective: Extract YouTube video ID from HTML <iframe> and return short URL
# Features:
#   - Uses regex to detect <iframe> with YouTube embed link
#   - Supports case-insensitive matching
#   - Outputs short YouTube URL format
# Usage:
#   - Prompt: "HTML: "
#   - Output: "https://youtu.be/VIDEO_ID" or None if not found
# Notes:
#   - Only works with embed URLs from youtube.com
#   - Ignores extra attributes inside <iframe>
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe.*?src="https?://?(?:www\.)?youtube\.com/embed/([\w-]+)".*?</iframe>'
    matches = re.search(pattern, s, re.IGNORECASE)
    if matches:
        videoId = matches.group(1)
        return f"https://youtu.be/{videoId}"
    else:
        return None


if __name__ == "__main__":
    main()
