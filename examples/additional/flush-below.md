# flush-below

Write below the eight-entry flush threshold.

All entries remain readable before any table is produced.

Family: flush. Size: 7. Deterministic seed: 910605.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case flush-below
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 7 |
| reads | equals 7 |
| live_keys | equals 7 |
| model_matches | equals true |
| tables | equals 0 |
| recovered | equals false |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
