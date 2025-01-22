#!/bin/sh -l

# input: use some var
echo "ENV content:"
echo $ENV

echo "entrypoint received fuzzer name: $FUZZER_NAME"

# output: set some var
echo "fuzz_result='dummy fuzz output for fuzzer: $FUZZER_NAME'" >> "$GITHUB_OUTPUT"

exit 0
