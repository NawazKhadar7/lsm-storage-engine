# recover-016-01

Restart using the WAL and append another durable record.

Input scale: 16; deterministic random seed: 225.
Run `python scripts/demo.py --case workloads/recover-016-01.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
