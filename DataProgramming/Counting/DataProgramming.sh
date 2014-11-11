#!/bin/sh
# Data Streaming
echo ./Mapper.py | ./hadoop-sort-and-shuffle | ./Reducer.py | ./top10words
./Mapper.py | ./hadoop-sort-and-shuffle | ./Reducer.py | ./top10words
