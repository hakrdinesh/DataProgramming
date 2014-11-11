#!/bin/sh
# Data Streaming
./MapperBig.py | ./hadoop-sort-and-shuffle | ./Reducer.py | ./top10words
