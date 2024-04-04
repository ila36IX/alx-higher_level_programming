#!/bin/bash
# Display all HTTP methods a server accepts
curl -s -X OPTIONS $1
