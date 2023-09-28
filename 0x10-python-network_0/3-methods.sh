#!/bin/bash
#task 3
curl -sl "$1" | grep "Allow:" | cut -d'' -f2-
