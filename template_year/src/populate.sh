#!/bin/bash
# Use in WSL terminal
# Usage: ./populate.sh [number of copies]

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [number of copies]"
    exit 1
fi

input_file="template.py"
num_copies=$1

for ((i=1; i<=num_copies; i++))
do
    new_file="day_$i.py"
    cp "$input_file" "$new_file"
    sed -i "s/day_1/day_$i/g" "$new_file"
done
