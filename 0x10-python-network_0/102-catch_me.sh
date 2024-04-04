#!/bin/bash
# Makes the server to responese with you got me message 
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
