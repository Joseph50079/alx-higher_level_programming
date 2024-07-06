#!/bin/bash
# displays allowed methods
curl -Is -X OPTIONS $1 | grep 'Allow:' | awk '{ $1=""; sub(/^ /, ""); print $0 }'
