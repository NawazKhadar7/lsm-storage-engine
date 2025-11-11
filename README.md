# Log-Structured Merge-Tree Storage Engine

A durable local single-writer engine with checksummed WAL frames, immutable tables, Bloom filters and manifest-based compaction.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

POSIX-style fsync, checksummed framed WAL, in-memory latest records, sorted checksummed SST files, Bloom lookups, atomic manifest updates, full-table compaction and restart recovery.

## Limits and optional runtimes

Python single-writer reference, not a distributed C++/Rust database. SST files are JSON and read in full, so lookup performance is intentionally limited. No cross-process locking, replication, snapshots, concurrent reads during writes, memory mapping or background compaction. Incomplete final WAL frames are truncated; complete checksum corruption fails closed.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
