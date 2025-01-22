#!/bin/sh -l

# where are we?
echo "ENV content:"
env
echo "ls output:"
ls

# input: use some var
echo "entrypoint received fuzzer name: $FUZZER_NAME"

# output: set some var
echo "fuzz_result='dummy fuzz output for fuzzer: $FUZZER_NAME'" >> "$GITHUB_OUTPUT"

exit 0
