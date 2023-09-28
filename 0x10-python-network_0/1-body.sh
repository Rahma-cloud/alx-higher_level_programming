#!/bin/bash
# Task 1
curl -s -o - -w "%{http_code}" "$1" | awk 'NR==1{status=$1; next} NR>1 && status==200{print}'
