from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json
from PIL import Image
root=Path(__file__).resolve().parents[1]
class Check(HTMLParser):
 def __init__(self): super().__init__(); self.ids=set();self.refs=[];self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   assert a['id'] not in self.ids;self.ids.add(a['id'])
  for key in ('href','src'):
   if key in a:self.refs.append(a[key])
  if tag=='img':
   assert a.get('alt') and a.get('width') and a.get('height');self.images.append(a['src'])
p=Check();p.feed((root/'index.html').read_text());m=json.loads((root/'archive.json').read_text())
assert m['complete'] is False
assert [e['date_start'] for e in m['entries']]==sorted(e['date_start'] for e in m['entries'])
assert len(m['entries'])==len(p.images)
for ref in p.refs:
 u=urlsplit(ref)
 if u.scheme: assert u.scheme=='https';continue
 if u.path: assert (root/unquote(u.path)).is_file(),ref
 if u.fragment: assert u.fragment in p.ids,ref
for e in m['entries']:
 f=root/e['image'];assert hashlib.sha256(f.read_bytes()).hexdigest()==e['sha256'];Image.open(f).verify()
 assert e['thumbnail'] in p.images;Image.open(root/e['thumbnail']).verify()
 assert e['source_url'] in p.refs
assert not any('2026-08-29' in e['file'] for e in m['entries'])
print(f"PASS: {len(m['entries'])} originals, previews, hashes, chronology, links, anchors and alt text")
