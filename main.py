from __future__ import annotations
def run(text):
 import re
 return re.findall(r"\[[^\]]*\]\(([^)]+)\)",text)
