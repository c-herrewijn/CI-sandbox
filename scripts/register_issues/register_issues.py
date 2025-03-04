#!/usr/bin/env python3

import github_helper
import os

title = f"AFL++ run {os.environ['FUZZ_RUN_ID']}: crashes or hangs found for read_{os.environ['FILE_FORMAT']}() on: {os.environ['DUCKDB_SHA']}"

num_crashes = int(os.environ['NUM_CRASHES'])
num_hangs = int(os.environ['NUM_HANGS'])
reproduction_full_path = f"https://github.com/duckdb/duckdb-fuzzer/tree/main/{os.environ['REPRODUCTION_DIR']}"
sqllogic_file_crashes = f"{reproduction_full_path}/{os.environ['FUZZ_SCENARIO']}-{os.environ['DUCKDB_SHA']}.test"
sqllogic_file_hangs = f"{reproduction_full_path}/{os.environ['FUZZ_SCENARIO']}-{os.environ['DUCKDB_SHA']}-hangs.test"

issue_desc = f"""Issue found by `{os.environ['FUZZ_SCENARIO']}` for duckdb commit hash [{os.environ['DUCKDB_SHA']}](https://github.com/duckdb/duckdb/commit/{os.environ['DUCKDB_SHA']})
- crashes found: {num_crashes}
- hangs found: {num_hangs}

"""

fuzzer_desc = f"""### Scenario
duckdb:
- SHA: `{os.environ['DUCKDB_SHA']}`
- version: `{os.environ['DUCKDB_VERSION']}`
- ref: `{os.environ['DUCKDB_REF']}`

fuzzer:
- scenrio: `{os.environ['FUZZ_SCENARIO']}`
- CI: `{os.environ['FUZZ_REPO']}` -> `{os.environ['FUZZ_WORKFLOW']}` -> [run {os.environ['FUZZ_RUN_ID']}](https://github.com/{os.environ['FUZZ_REPO']}/actions/runs/{os.environ['FUZZ_RUN_ID']})
- [reproduction files]({reproduction_full_path})
"""

reproduction = f"""### Reproduction
steps:
1. download the {os.environ['FILE_FORMAT']} files generated by the fuzzer from {reproduction_full_path}
```bash
git clone --no-checkout git@github.com:duckdb/duckdb-fuzzer.git afl_repr
cd afl_repr
git sparse-checkout set --no-cone {os.environ['REPRODUCTION_DIR']}
git checkout
```

2. copy the sqllogic test to a local duckdb repo; update the paths in the file to point to the location where you downloaded the {os.environ['FILE_FORMAT']} files
{sqllogic_file_crashes if num_crashes > 0 else ''}
{sqllogic_file_hangs if num_hangs > 0 else ''}

3. run the sqllogic tests to reproduce the error. Note that some crashes do not occur every run, so run multiple times if needed.
"""

body = issue_desc + fuzzer_desc + reproduction
github_helper.make_github_issue(title, body)
# github_helper.label_github_issue()
