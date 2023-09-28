#!/bin/bash
#task 3
curl -sIX OPTIONS $1 | grep "Allow:" | cut -d ' ' -f 2-
