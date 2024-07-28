import re

def validate_youtube_link(link):
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')
    return youtube_regex.match(link)

def validate_link(link):
    return link.startswith("http://") or link.startswith("https://")
