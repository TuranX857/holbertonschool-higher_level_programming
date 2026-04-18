#!/bin/bash
# This script lists allowed HTTP methods
curl -sI -X OPTIONS "$1" | awk -F': ' '/Allow/ {print $2}'
