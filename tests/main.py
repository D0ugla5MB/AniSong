import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / '.env')
    
header_f = PROJECT_ROOT / os.getenv('HEADERS_FILE')

beauty = lambda f_html: BeautifulSoup(f_html, 'html.parser')

def read_page(path:str) -> str:
    with open(path, 'r',encoding='utf-8') as f:
        return f.read()
html_files_dict = {
    "songs_link": beauty(read_page("tests/html/anime_with_songs_link.html")),
    "without_index": beauty(read_page("tests/html/anime_without_index.html")),
    "op_end": beauty(read_page("tests/html/animw_without_op_end.html")),
    "archive": beauty(read_page("tests/html/archive.html")),
    "season_year": beauty(read_page("tests/html/season_year.html")),
    "top": beauty(read_page("tests/html/top.html")),
}

def check_resp_headers(f_path: str = header_f):
    if f_path is None: 
        raise Exception('File not found')
    
    with open(f_path, 'r', encoding='utf-8') as f:
        headers = f.readlines()
    
    headers_dict = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in headers if ":" in line}
    
    status_code = headers_dict.get("Status", None)
    if status_code != "200":
        raise Exception(f"Invalid status code: {status_code}")
    
    content_type = headers_dict.get("Content-Type", None)
    if content_type != "text/html":
        raise Exception(f"Invalid content type: {content_type}")
    
    content_length = headers_dict.get("Content-Length", None)
    if content_length is None or int(content_length) <= 0:
        raise Exception(f"Invalid content length: {content_length}")
    
    
def main():
    check_resp_headers()
    
if __name__ =='__main__':
    main()