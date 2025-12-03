# torn-wal-five

Recover after a truncated final WAL frame.

The valid prefix and the later append must remain readable.

Family: torn-wal. Size: 5. Deterministic seed: 910610.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case torn-wal-five
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 5 |
| reads | equals 5 |
| live_keys | equals 6 |
| model_matches | equals true |
| tables | equals 1 |
| recovered | equals true |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
