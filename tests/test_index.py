import pathlib, re

def test_title_present():
    html = pathlib.Path("index.html").read_text(encoding="utf-8")
    assert re.search(r"<title>.+?</title>", html, re.I), "index.html must contain <title>"
