#!/bin/bash
# Send a JSON POST request to a URL
curl -s "@$2" -H "Content-Type: application/json" $1 
