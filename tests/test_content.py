from threeza.content import threeza_template

def test_threeza_template():
    html = threeza_template("unclaimed.html")
    assert "Threeza" in html
    assert "<html>" in html
