#!/bin/bash
# Send a costum header request
curl -s -d email=test@gmail.com -d subject="I will always be here for PLD" $1 
