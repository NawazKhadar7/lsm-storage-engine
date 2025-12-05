# flush-exact

Reach the eight-entry flush threshold.

Exactly one immutable table is produced.

Family: flush. Size: 8. Deterministic seed: 910606.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case flush-exact
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 8 |
| reads | equals 8 |
| live_keys | equals 8 |
| model_matches | equals true |
| tables | equals 1 |
| recovered | equals false |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
