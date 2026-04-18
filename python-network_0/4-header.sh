#!/bin/bash
# This script sends a GET request with a custom header and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
