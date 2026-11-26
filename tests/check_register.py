from pathlib import Path
import csv
from urllib.parse import unquote
from html.parser import HTMLParser

class Download(HTMLParser):
    def handle_starttag(self, tag, attrs):
        url = dict(attrs).get('href', '')
        if tag == 'a' and url.startswith('data:text/csv'):
            self.rows = list(csv.reader(unquote(url.split(',', 1)[1]).splitlines()))

root = Path(__file__).resolve().parents[1]
page = Download()
page.feed((root / 'index.html').read_text())
with (root / 'data/annual-results.csv').open() as stream:
    register = list(csv.reader(stream))
assert register == page.rows
data = register[1:]
assert len(set((r[0], r[1]) for r in data)) == len(data) == 8
for year, measure, actual, target, gap, source in data:
    assert source.startswith('https://')
    assert 0 <= float(actual) <= 100 and abs(float(target)-float(actual)-float(gap)) < .05
latest = [r for r in data if r[0] == '2025–26']
assert sorted(float(r[4]) for r in latest) == [0, 9.7, 19.2, 25.2]
assert sum(float(r[2]) >= float(r[3]) for r in latest) == 1
series = {name: [float(r[2]) for r in sorted(data) if r[1] == name] for name in {r[1] for r in data}}
assert series['Handover within 40 min'] == [64.9, 67.7, 70.8]
assert series['ED stay under 4 hours'] == [54, 53.6, 49.8]
assert round(100-series['ED stay under 4 hours'][-1],1) == 50.2
print('Register, dashboard download and headline calculations agree.')
