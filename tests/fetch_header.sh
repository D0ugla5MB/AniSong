#!/bin/bash

url=${1:-"localhost"}

if [ -z "$url" ]; then
    echo 'provide a url.'
    exit 1
fi
if !command -v curl &> /dev/null; then 
    echo 'curl is not installed'
    exit 1
fi

curl -I "$url"