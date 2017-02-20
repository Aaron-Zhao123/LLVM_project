#!/bin/bash
cd /Users/aaron/llvm/build
(time make) 2> buildtime.txt
cp buildtime.txt /Users/aaron/Projects/L25_miniproject/test
rm buildtime.txt
cd /Users/aaron/Projects/L25_miniproject/test
