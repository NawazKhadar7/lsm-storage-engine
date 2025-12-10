# Data Model

WAL record = sequence, key, value, deleted. SST payload includes sorted key versions and a Bloom bitmap. Manifest lists authoritative tables, checkpoint and generation.
