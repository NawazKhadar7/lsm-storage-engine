import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.sstable import read_table,write_table
class SstTests(unittest.TestCase):
    def test_lookup_and_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'sst';write_table(p,{'a':[1,2,False]});rows,b=read_table(p);self.assertTrue(b.may_contain('a'));self.assertEqual(rows['a'][1],2)
    def test_corrupt_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'sst';write_table(p,{'a':[1,2,False]});d=json.loads(p.read_text());d['payload']['records']['a'][1]=5;p.write_text(json.dumps(d))
            with self.assertRaises(ValueError):read_table(p)
