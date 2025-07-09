# The 'GET_' refers to HTTP GET request the respective function performs
from typing import NewType
from re import match
from .const import *

# Function: check_args
"""
Check if the given argument matches any of the predefined patterns.
"""
"check_args(args: str) -> bool"

# Function: get
"""
Perform an HTTP GET request to the given URL and validate the response.
"""
"get(url: str) -> str"

# Function: treat_res
"""
Process the HTML response and extract relevant elements.
"""
"treat_res(res: str) -> list"

# Function: check_urls_list
"""
Validate a list of URLs to ensure they match the expected format.
"""
"check_urls_list(data: list) -> bool"

# Function: fetch_urls
"""
Fetch URLs based on the provided arguments or predefined URL lists.
"""
"fetch_urls(args: str = '')"

# Function: build_csv
"""
Build a CSV file from the provided data source.
"""
"build_csv(src: __file__)"