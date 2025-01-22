#!/bin/sh -l

# where are we?
echo "ENV content:"
env
echo "pwd:"
pwd
echo "ls -la ."
ls -la .
echo "ls -la /"
ls -la /

# input: use some var
echo "entrypoint received fuzzer name: $FUZZER_NAME"

# output: set some var
echo "fuzz_result='dummy fuzz output for fuzzer: $FUZZER_NAME'" >> "$GITHUB_OUTPUT"

exit 0
