FROM aflplusplus/aflplusplus:stable

WORKDIR /usr/src

RUN echo "Dockerfile printing FUZZER_NAME from env: $FUZZER_NAME"

# Copy any source file(s) required for the action
COPY entrypoint.sh .

ENTRYPOINT ["/usr/src/entrypoint.sh"]
