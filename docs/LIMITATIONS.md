# Limitations

Python single-writer reference, not a distributed C++/Rust database. SST files are JSON and read in full, so lookup performance is intentionally limited. No cross-process locking, replication, snapshots, concurrent reads during writes, memory mapping or background compaction. Incomplete final WAL frames are truncated; complete checksum corruption fails closed.
