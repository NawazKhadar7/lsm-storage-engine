# delete-single

Delete the only written key.

The tombstone leaves no live keys and reads match the model.

Family: delete. Size: 1. Deterministic seed: 910603.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case delete-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 1 |
| reads | equals 1 |
| live_keys | equals 0 |
| model_matches | equals true |
| tables | equals 0 |
| recovered | equals false |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
