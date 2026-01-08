# Log-Structured Merge-Tree Storage Engine

A durable local single-writer engine with checksummed WAL frames, immutable tables, Bloom filters and manifest-based compaction.

## 1. Overview

A storage engine must reconcile recent writes, immutable tables and recovery after interruption. This single-writer reference exposes durability boundaries with a framed write-ahead log, atomic manifest updates and an independent dictionary oracle.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Durable mutation log:** Writes checksummed WAL frames and uses fsync-style durability.
- **Immutable tables:** Flushes sorted records into checksummed SST files.
- **Lookup and compaction:** Uses Bloom filters and merges table records with version/tombstone handling.
- **Recovery checks:** Exercises restart recovery, torn final log frames and checksum corruption handling.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Execution | Python 3.10+ standard library | Runnable single-writer engine |
| Durability | Local files, fsync-style operations and atomic manifest replacement | Implemented for the local reference |
| Storage format | Framed WAL, JSON SST files and Bloom filters | Inspectible formats; SST files are read in full |

### How the components fit together

A mutation reaches the durable WAL before the MemTable. Flush creates immutable SST files and publishes a manifest checkpoint. Reads reconcile current and table records; restart recovery replays WAL entries newer than the checkpoint.

| Component | Responsibility |
| --- | --- |
| [src/syslab/wal.py](src/syslab/wal.py) | Framed log checksums and replay. |
| [src/syslab/sstable.py](src/syslab/sstable.py) | Sorted immutable table representation. |
| [src/syslab/bloom.py](src/syslab/bloom.py) | Bloom membership filter. |
| [src/syslab/lsm.py](src/syslab/lsm.py) | Engine operations, compaction and recovery orchestration. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

Python single-writer reference, not a distributed C++/Rust database. SST files are JSON and read in full, so lookup performance is intentionally limited. No cross-process locking, replication, snapshots, concurrent reads during writes, memory mapping or background compaction. Incomplete final WAL frames are truncated; complete checksum corruption fails closed.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `lsm-storage-engine` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **24 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "overwrite",
  "id": "overwrite-016-01",
  "seed": 101,
  "size": 16
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/overwrite-016-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "live_keys": 4,
    "model_matches": true,
    "reads": 16,
    "recovered": false,
    "tables": 0,
    "writes": 16
  }
}
```

Sixteen writes overwrite four keys, and all reads agree with the independent model. recovered=false means this particular example does not exercise a restart; separate bundled workloads cover recovery.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=overwrite-016-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Durable mutation log | [src/syslab/wal.py](src/syslab/wal.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects database internals, crash consistency and systems correctness. It provides concrete evidence for discussing write ordering, atomic publication and the tradeoffs of a simplified table format.

**A question to investigate:** How do flush thresholds, Bloom-filter parameters and compaction policies change write amplification, lookup cost and recovery time?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
