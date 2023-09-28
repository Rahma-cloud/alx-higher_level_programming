#!/bin/bash
# Task 0
url="$1"
curl -sI "$url" | grep -i "Content-length" | awk '{print $2}' | tr -d '\r'
