# flush-above

Cross the eight-entry flush threshold.

One table and a remaining memtable entry must read consistently.

Family: flush. Size: 9. Deterministic seed: 910607.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case flush-above
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 9 |
| reads | equals 9 |
| live_keys | equals 9 |
| model_matches | equals true |
| tables | equals 1 |
| recovered | equals false |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
