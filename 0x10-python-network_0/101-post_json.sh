#!/bin/bash
# send a json file to the web address
curl -sH "Content-Type: application/json" -d "$(cat $2)" $1
