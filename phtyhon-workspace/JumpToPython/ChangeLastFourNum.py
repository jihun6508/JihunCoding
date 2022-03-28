import re

originalText = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
a = re.compile(r"(?P<Origin>\w+\s+\d+[-]\d+[-])(?P<lastNum>\d+)")

print(a.sub("\g<Origin>####", originalText))