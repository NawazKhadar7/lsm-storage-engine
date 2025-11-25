import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.wal import WAL
class WalTests(unittest.TestCase):
    def test_torn_append_then_new_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'wal';w=WAL(p);w.append({'x':1});p.write_bytes(p.read_bytes()+b'xx');self.assertEqual(w.recover(),[{'x':1}]);w.append({'x':2});self.assertEqual(len(w.recover()),2)
    def test_corrupt_complete_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'wal';w=WAL(p);w.append({'x':1});b=bytearray(p.read_bytes());b[-1]^=1;p.write_bytes(b)
            with self.assertRaises(ValueError):w.recover()
