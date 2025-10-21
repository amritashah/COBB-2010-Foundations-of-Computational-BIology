#!/bin/bash
for line in $(cat "$1"); do
    grep -q "$line" "$2" || echo "$line"
done
        