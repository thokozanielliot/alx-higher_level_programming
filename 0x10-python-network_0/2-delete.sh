#!/bin/bash
# Script that sends a DELETE request to the URL passed as the
# First argument and displays the body of the response
curl -s "$1" -X DELETE
