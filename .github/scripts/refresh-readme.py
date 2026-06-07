#!/usr/bin/env python3
"""Refresh time-based fields in README.md (years of experience).

Keeps the hardcoded year mentions in sync with CAREER_START so the profile
never goes stale. Idempotent — only writes (and the workflow only commits)
when the computed value actually changes.
"""
import datetime
import re

CAREER_START = datetime.date(2019, 9, 1)
today = datetime.date.today()
years = int((today - CAREER_START).days / 365.25)

with open('README.md', encoding='utf-8') as f:
    s = f.read()
orig = s

# Typing SVG (URL-encoded): "...6%2B+Years..."  -> "<years>%2B+Years"
s = re.sub(r'\d+%2B\+Years', f'{years}%2B+Years', s)
# Japanese: "経験6年以上" -> "経験<years>年以上"
s = re.sub(r'経験\d+年以上', f'経験{years}年以上', s)

if s != orig:
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'README years refreshed -> {years}+')
else:
    print(f'README already current ({years}+ years)')
