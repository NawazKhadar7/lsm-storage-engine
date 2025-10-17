# recover-048-03

Restart using the WAL and append another durable record.

Input scale: 48; deterministic random seed: 227.
Run `python scripts/demo.py --case workloads/recover-048-03.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
