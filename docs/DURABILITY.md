# Durability ordering

WAL fsync precedes acknowledgment. Table fsync and directory sync precede manifest publication. Manifest publication and directory sync precede WAL reset or old-table deletion. Power-loss guarantees depend on filesystem and device behavior; this bundle does not test sudden power loss.
