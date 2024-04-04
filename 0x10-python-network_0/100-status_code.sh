#!/bin/bash
# Send a costum header request
curl -so /dev/null -w "%{http_code}" $1 
