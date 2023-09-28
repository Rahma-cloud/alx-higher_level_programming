#!/bin/bash
# Task 0
curl -sI "$1" | grep -i "Content-length" | awk '{print $2}' | tr -d '\r'
