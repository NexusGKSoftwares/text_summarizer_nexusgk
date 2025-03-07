import unittest
from main.summarizer import extractive_summary, abstractive_summary

class TestSummarizer(unittest.TestCase):
    def test_extractive_summary(self):
        text = "This is a long text that needs to be summarized."
        summary = extractive_summary(text, 1)
        self.assertTrue(len(summary) > 0)

    def test_abstractive_summary(self):
        text = "This is a long text that needs to be summarized."
        summary = abstractive_summary(text)
        self.assertTrue(len(summary) > 0)

if __name__ == "__main__":
    unittest.main()
