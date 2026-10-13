#!/usr/bin/env python3
"""Gera dist/MeuQuarto.html: o quarto.html com o three.js embutido, para funcionar sem internet.

Uso: python3 build.py   (só precisa de internet na hora de gerar)
"""
import base64, json, re, urllib.request
from pathlib import Path

here = Path(__file__).parent
src = (here / 'quarto.html').read_text(encoding='utf-8')
cdn = re.search(r'"three": "(https://[^"]+/three@[^/]+)/', src).group(1)
mods = {'three': 'build/three.module.min.js'}
for p in sorted(set(re.findall(r"from 'three/addons/([^']+)'", src))):
    mods[f'three/addons/{p}'] = f'examples/jsm/{p}'  # os addons só importam de 'three', então data: URL resolve

def data_url(path):
    js = urllib.request.urlopen(f'{cdn}/{path}', timeout=60).read()
    return 'data:text/javascript;base64,' + base64.b64encode(js).decode()

imports = json.dumps({'imports': {k: data_url(v) for k, v in mods.items()}})
out, n = re.subn(r'<script type="importmap">.*?</script>', lambda _: f'<script type="importmap">{imports}</script>', src, count=1, flags=re.S)
assert n == 1, 'importmap não encontrado em quarto.html'
dst = here / 'dist' / 'MeuQuarto.html'
dst.parent.mkdir(exist_ok=True)
dst.write_text(out, encoding='utf-8')
print(f'{dst} ({dst.stat().st_size // 1024} KB, {len(mods)} módulos embutidos)')
