# Disk format

WAL uses big-endian uint32 payload length and CRC32, followed by UTF-8 JSON (maximum 1 MiB). SST and manifest use SHA-256 envelopes over canonical JSON. CRC/checksums detect corruption, not malicious modification.
