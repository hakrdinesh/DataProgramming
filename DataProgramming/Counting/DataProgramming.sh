#!/bin/sh
# Data Streaming
./Mapper.py | ./hadoop-sort-and-shuffle | ./Reducer.py | ./top10words
