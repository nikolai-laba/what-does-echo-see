"""Checks on the ECHO extractor's suppression and the cached snapshot.
Adapted from data/scripts/tests/test_audit_corrections.py in the CISC repo.
Run: python3 -m unittest discover -s tests -v   (standard library only)
"""
import csv
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


echo = module('fetch_echo_activity')


class Suppression(unittest.TestCase):
    def test_complementary_suppression_is_not_a_less_than_five_bound(self):
        cells = {('A', 'X'): 2, ('A', 'Y'): 12, ('B', 'X'): 8, ('B', 'Y'): 30}
        result = echo.suppress(cells)
        self.assertEqual(set(result.values()), {'suppressed'})
        self.assertEqual(echo.suppress({('A', 'X'): 0, ('A', 'Y'): 7}), {('A', 'X'): 0, ('A', 'Y'): 7})


class CachedData(unittest.TestCase):
    def test_echo_preserves_published_monthly_totals_and_neutral_marker(self):
        with (ROOT / 'data/echo-activity-oak-park.csv').open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(sum(r['count'] == 'suppressed' for r in rows), 73)
        self.assertFalse(any(r['count'] == '<5' for r in rows))
        for breakdown in ('service_by_month', 'referral_by_month'):
            self.assertEqual(sum(int(r['count']) for r in rows if r['breakdown'] == breakdown), 1598)

    def test_call_volume_files_match_the_board_deck(self):
        with (ROOT / 'data/police-calls-echo-relevant-2025.csv').open() as f:
            rows = list(csv.DictReader(f))
        totals = {}
        for r in rows:
            totals[r['call_group']] = totals.get(r['call_group'], 0) + int(r['calls_2025'])
            self.assertIn(r['match_confidence'], {'high', 'medium', 'low'})
        self.assertEqual(totals, {'Call Type 1 (mental health)': 341,
                                  'Call Type 2 (domestic/abuse)': 670,
                                  'Community Response': 5214})


if __name__ == '__main__':
    unittest.main()
