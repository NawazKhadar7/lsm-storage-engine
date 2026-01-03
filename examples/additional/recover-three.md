# recover-three

Recover three writes, append a key, and restart again.

Original keys and the recovery append survive both restarts.

Family: recover. Size: 3. Deterministic seed: 910609.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case recover-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| writes | equals 3 |
| reads | equals 3 |
| live_keys | equals 4 |
| model_matches | equals true |
| tables | equals 1 |
| recovered | equals true |

Scope: Single-writer storage in temporary directories.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
