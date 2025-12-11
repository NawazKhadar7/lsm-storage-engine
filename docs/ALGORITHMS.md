# Algorithms

Sequence numbers select the newest version. WAL persists before memtable mutation. Flush publishes the durable SST then updates the manifest before resetting the WAL. Compaction writes a replacement and publishes the manifest before deleting old tables. Reference: https://www.cs.umb.edu/~poneil/lsmtree.pdf .
