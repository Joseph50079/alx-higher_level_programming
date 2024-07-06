#!/bin/bash
# print ip address content length
curl -Is -X GET $1 | grep -i 'status' | awk '{print $2 " " $3}' | grep -i 200
