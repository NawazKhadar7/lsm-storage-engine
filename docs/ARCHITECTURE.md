# Architecture

Mutation → durable WAL → MemTable. Flush → immutable SST → durable manifest checkpoint. Get merges memtable/table versions. Recovery replays WAL records newer than the checkpoint.
