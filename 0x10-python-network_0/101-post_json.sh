#!/bin/bash
# send a json file to the web address
curl -sX POST -F 'key1=value1' -F 'file=@'$2 $1
