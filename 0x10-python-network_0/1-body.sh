#!/bin/bash
# print ip address content length
curl -o /dev/null -s -w "%{http_code}\n" $1
