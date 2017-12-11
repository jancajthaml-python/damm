import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import damm

class TestDamm(unittest.TestCase):

  def test_digit(self):
    tests = [
      ("0012301476470096832", 5),
      ("xy-1", None)
    ]

    for t in tests:
      number, expected = t
      valid = damm.Digit(number)
      self.assertEqual(valid, expected, "damm.Digit?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

  def test_validate(self):
    tests = [
      ("00123014764700968325", True),
      ("1234567812345678", False),
      ("xy-1", False)
    ]

    for t in tests:
      number, expected = t
      valid = damm.Validate(number)
      self.assertEqual(valid, expected, "damm.Validate?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

  def test_generate(self):
    tests = [
      ("0012301476470096832", "00123014764700968325")
    ]

    for t in tests:
      number, expected = t
      valid = damm.Generate(number)
      self.assertEqual(valid, expected, "damm.Generate?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

if __name__ == '__main__':
  unittest.main()
