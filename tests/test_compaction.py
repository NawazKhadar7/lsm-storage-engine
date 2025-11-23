import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.lsm import LSM
class CompactTests(unittest.TestCase):
    def test_delete_not_resurrected(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=LSM(tmp,1);d.put('a',1);d.put('b',2);d.delete('a');d.compact();self.assertIsNone(d.get('a'));self.assertEqual(LSM(tmp).get('b'),2);self.assertEqual(len(d.tables),1)
    def test_invalid_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):LSM(tmp).put('',1)
