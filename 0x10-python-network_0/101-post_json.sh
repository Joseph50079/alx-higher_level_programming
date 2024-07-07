#!/bin/bash
# send a json file to the web address
curl -X POST -F 'file=@'$2 $1
