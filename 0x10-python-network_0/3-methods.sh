#!/bin/bash
#task 3
curl -slX OPTIONS "$1" | grep "Allow:" | cut -d''-f 2-
