#!/bin/bash
# send a json file to the web address
curl -sX POST -F 'file=@'$2 $1
