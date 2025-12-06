# Design

Keep tombstones during compaction to make deletion semantics explicit. Orphan files are ignored; only manifest-listed tables are authoritative. A torn tail differs from corruption of a complete frame.
