# Compaction

Merge every manifest-listed table using the highest sequence for each key. Retain tombstones. Publish one new table atomically through the manifest, then remove obsolete files. This is full compaction, not a leveled policy.
