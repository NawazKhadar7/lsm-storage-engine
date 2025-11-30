# overwrite-seven

Overwrite one key seven times.

Key-space rounding retains the last written value.

Family: overwrite. Size: 7. Deterministic seed: 910602.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case overwrite-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 7 |
| reads | equals 7 |
| live_keys | equals 1 |
| model_matches | equals true |
| tables | equals 0 |
| recovered | equals false |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
