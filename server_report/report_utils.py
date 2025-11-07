import os

def write_html(content, path):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\n")
