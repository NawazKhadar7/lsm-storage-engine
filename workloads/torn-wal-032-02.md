# torn-wal-032-02

Discard only an incomplete trailing WAL frame and preserve subsequent recovery.

Input scale: 32; deterministic random seed: 257.
Run `python scripts/demo.py --case workloads/torn-wal-032-02.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
