# delete-seven

Delete every third key from seven writes.

Deleting keys zero, three, and six leaves four live keys.

Family: delete. Size: 7. Deterministic seed: 910604.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case delete-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 7 |
| reads | equals 7 |
| live_keys | equals 4 |
| model_matches | equals true |
| tables | equals 0 |
| recovered | equals false |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
