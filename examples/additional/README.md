# Additional scenarios for lsm-storage-engine

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case overwrite-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| overwrite-single | overwrite | 1 | Write and read a single key. |
| overwrite-seven | overwrite | 7 | Overwrite one key seven times. |
| delete-single | delete | 1 | Delete the only written key. |
| delete-seven | delete | 7 | Delete every third key from seven writes. |
| flush-below | flush | 7 | Write below the eight-entry flush threshold. |
| flush-exact | flush | 8 | Reach the eight-entry flush threshold. |
| flush-above | flush | 9 | Cross the eight-entry flush threshold. |
| compact-nine | compact | 9 | Compact nine writes spanning two tables. |
| recover-three | recover | 3 | Recover three writes, append a key, and restart again. |
| torn-wal-five | torn-wal | 5 | Recover after a truncated final WAL frame. |

Scope: Single-writer storage in temporary directories.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
