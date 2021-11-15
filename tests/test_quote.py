import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
  def setUp(self):
      """
      Set up method that will run before every Test
      """
      self.random_quote = Quote("Vickie Shiraa", "Why Is The Rum Gone")

  def test_instance(self):
      self.assertTrue(isinstance(self.random_quote, Quote))

  def test_init(self):
      self.assertEqual(self.random_quote.author, "Vickie Shiraa")
      self.assertEqual(self.random_quote.quote,"Why Is The Rum Gone")