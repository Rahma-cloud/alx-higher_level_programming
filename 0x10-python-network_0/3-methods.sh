#!/bin/bash
#task 3
curl -sLX OPTIONS "$1" | grep "Allow:" | cut -d' '-f2-
