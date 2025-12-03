import sys, unittest, json, math, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from syslab.core import run_case
from syslab.common import validate_case,check,dumps,atomic_json,finite_numbers
from syslab.cli import evaluate,cases
from syslab.bloom import Bloom
class BloomTests(unittest.TestCase):
    def test_no_false_negatives(self):
        b=Bloom()
        for i in range(100):b.add(str(i))
        self.assertTrue(all(b.may_contain(str(i)) for i in range(100)))
    def test_roundtrip(self):
        b=Bloom();b.add('a');other=Bloom(b.bits,b.hashes,b.bitmap);self.assertTrue(other.may_contain('a'))
