#!/bin/bash
# Task5
email="test@gmail.com"
subject="I will always be here for PLD"
curl -sX POST "$1" -d "email=$email&subject=$subject"
