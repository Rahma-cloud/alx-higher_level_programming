#!/bin/bash
# Task 1
curl -s -o - -w "%{hhtp_code}" ["$1"] | awk 'NR==1 {status=$1} NR>1 && status==200 {print}'
