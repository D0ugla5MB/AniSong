from re import compile
from datetime import datetime
from typing import Tuple
from bs4 import BeautifulSoup
URL_OPT = -1
SOUNDTRACK_OPT = -1
beauty = lambda html : BeautifulSoup(html, 'html.parser')
mal_urls = {
    'all': 'https://myanimelist.net/topanime.php',
    'airing': 'https://myanimelist.net/topanime.php?type=airing',
    'upcoming': 'https://myanimelist.net/topanime.php?type=upcoming',
    'tv': 'https://myanimelist.net/topanime.php?type=tv',
    'movie': 'https://myanimelist.net/topanime.php?type=movie',
    'ova': 'https://myanimelist.net/topanime.php?type=ova',
    'ona': 'https://myanimelist.net/topanime.php?type=ona',
    'special': 'https://myanimelist.net/topanime.php?type=special',
    'pop': 'https://myanimelist.net/topanime.php?type=bypopularity',
    'fav': 'https://myanimelist.net/topanime.php?type=favorite'
}
# api_platform = ['spotify','youtube','yt_music'] # `youtube` depends if it is possible to use a reverse engineering to extract only the audio from the returned video
# search_engine_therms = ('anime', 'artist', 'song')


def check_song_type(param: Tuple[str, ...]): 
    class SizeError(Exception): pass
    class TupleElementsError(Exception): pass
    
    expect = ('opening','ending','other')
    
    if len(param) != len(expect): raise SizeError("The tuples size differ")
    if not all(elem in expect for elem in param): raise TupleElementsError(f"The elements from param: {param} are NOT the expected ones: {expect}") 
    return True 
# search_engine_filters = song_type if check_song_type(song_type) else ('opening','ending','other')

def error_opt(): raise ValueError('Invalid option')

def choose_sountrack_fetching_way(opt:int):
    
    def opt0(): ""
    def opt1(): ""
    
    if opt == 0: return opt0
    if opt == 1: return opt1
    return error_opt

def choose_sountrack_fetching_way(opt:int):
    
    def opt0(): ""
    def opt1(): ""
    
    if opt == 0: return opt0
    if opt == 1: return opt1
    return error_opt
     



def main():
    return 0


if __name__ =='__main__':
    main()