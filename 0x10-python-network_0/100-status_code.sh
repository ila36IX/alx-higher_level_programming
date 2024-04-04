#!/bin/bash
# Send a costum header request
curl -s o /dev/null -w "%{http_code}" $1 
