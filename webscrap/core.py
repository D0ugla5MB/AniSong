# guide on .header.py
from re import match
from .const import *

def check_args(args: str) -> bool:  # from get_urls' args
    if args == '':
        return True
    if PATTERNS["base_url"].match(args) or PATTERNS["anime_url"].match(args) or PATTERNS["default_redirect"].match(args):
        return True

    return False


def get(url:str) -> str:
    import requests
    
    res = requests.get(url, headers={
        "Accept": "text/html",
        "Referer": GET_TARGET
    })
    is_html_content = "text/html" in res.headers.get("Content-Type", "")
    is_status_ok = res.status_code == 200

    return res.text if is_html_content and is_status_ok else f'FAILED AT{res}'

def treat_res(res:str) -> list: # returns a list containg str elements
    if not isinstance(res, str):
        return []
    
    from html.parser import HTMLParser
    
    class CustomHtmlParser(HTMLParser):
        selectors_name = ['hoverinfo_trigger','hoverinfo_trigger fl-l ml12 mr8', 'a', 'href']
    
        def __init__(self):
            super().__init__()
            self.filtered_content = []
            self.is_highlight = False
            
        """
            search/get html elements using the class name defined in 'selectors_name'
            if only the `hoverinfo_trigger` is provided, will happen a dupe return since there are subclassess
                then access and/or filter by odd/even indexes numbers OR access directly by the 2nd selector
            the elements are a tags so extract the the href prop
                
        """
        
        def handle_startendtag(self, tag, attrs):
            return super().handle_startendtag(tag, attrs)
        
        def handle_data(self, data):
            return super().handle_data(data)
        
        """
            treat the html content returned by the parser;
            check 
            if it is a whole a tag with href OR only the href BOTH are valid
                if whole a tag, extract the href
            else
                rewrite the parser code
        """

    return
    
def check_urls_list(data: list) -> bool: 
    """
        expect receive: a list whose all elements are str each matching `https://myanimelist.net/anime/<int>/<slug>`
    """
    
    pass



def fetch_urls(args: str = ''):
    """
        args might be from GET_URL_LIST or some referenced url of the previous mentioned value using ['tv','movie','ova','ona','special']
    """
    if not check_args(args=args):
        return False
    
    
    pass

def build_csv(src: __file__):
    pass