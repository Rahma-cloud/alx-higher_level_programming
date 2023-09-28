#!/bin/bash
#task 3
curl -sL "$1" | grep "Allow:" | cut-d ' '-f 2-
