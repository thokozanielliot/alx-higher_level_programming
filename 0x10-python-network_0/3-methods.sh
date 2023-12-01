#!/bin/bash
# Script that takes in a URL and displays all HTTP methods
# The server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
