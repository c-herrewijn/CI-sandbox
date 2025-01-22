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

# output: store in file
FUZZ_RESULT_FILE=dummy-fuzz-result.txt
echo "fuzz_result='dummy fuzz output for fuzzer: $FUZZER_NAME'" > $FUZZ_RESULT_FILE
echo "fuzz_result_file=$FUZZ_RESULT_FILE" >> "$GITHUB_OUTPUT"

exit 0
