import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.nlp.preprocessing import clean_text


def test_clean_text_lowercase():
    assert clean_text("HELLO WORLD") == "hello world"


def test_clean_text_removes_numbers_and_symbols():
    assert clean_text("News 2024!!!") == "news"


def test_clean_text_removes_extra_spaces():
    assert clean_text("  World     News   ") == "world news"


def test_clean_text_removes_urls():
    assert clean_text("Read https://example.com now") == "read now"