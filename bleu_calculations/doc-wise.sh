#!/bin/bash

# args format :  <csv_file> <targets_output_file> <predictions_output_file>


if [ $# -eq 0 ]; then
    echo "args format :  <csv_file> <targets_output_file> <predictions_output_file>"
    exit 1
fi

# extract the csv into a reference file and a hypothesis file
python3 extract_csv.py $1 $2 $3

# run perl script to extract author's blue calculation
perl multi-bleu-detok.pl -lc $2 < $3



