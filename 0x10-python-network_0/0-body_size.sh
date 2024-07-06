#!/usr/bin/env bash
# print ip address content length

curl -Is $1 | grep -i Content-Length | awk '{print $2}'
