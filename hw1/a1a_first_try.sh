#!/bin/bash
for i in $(cat "$1"); do
    grep -F "$i" "$2"
done | sort -u
        