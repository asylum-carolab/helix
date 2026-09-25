"""Regenerate conventional Android resources from catalog.json and app-map.csv."""
import csv, json
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr
P=Path(__file__).resolve().parents[1]; M=P/'app/src/main'
catalog=json.loads((P/'catalog.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((P/'app-map.csv').open(encoding='utf-8')))
def write(path,text):path.write_text(text+'\n',encoding='utf-8')
items='\n'.join('    <item component='+quoteattr('ComponentInfo{'+r['package_name']+'/'+r['component']+'}')+' drawable='+quoteattr(r['asset'])+'/>' for r in rows)
appfilter='<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'+items+'\n</resources>'
items='\n'.join('    <item drawable='+quoteattr(a['asset'])+'/>' for a in catalog)
drawable='<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <category title="HELIX — 38 icônes"/>\n'+items+'\n</resources>'
for directory in ['assets','res/xml']:
 write(M/directory/'appfilter.xml',appfilter);write(M/directory/'drawable.xml',drawable)
write(M/'res/values/iconpack.xml','<resources>\n    <string-array name="icon_pack">\n'+'\n'.join('        <item>'+a['asset']+'</item>' for a in catalog)+'\n    </string-array>\n</resources>')
write(M/'res/values/drawables.xml','<resources>\n    <!-- ICONS01: real PNG resources in drawable-nodpi replace the five pilot aliases. -->\n</resources>')
manifest=(M/'AndroidManifest.xml').read_text(encoding='utf-8')
start=manifest.index('    <!-- Visibility');end=manifest.index('    <application')
queries='    <!-- Visibility limited to the 38 requested application packages. -->\n    <queries>\n'+'\n'.join('        <package android:name='+quoteattr(p)+'/>' for p in sorted({a['package'] for a in catalog}))+'\n    </queries>\n'
write(M/'AndroidManifest.xml',manifest[:start]+queries+manifest[end:].rstrip())
print('Synced',len(catalog),'catalog icons and',len(rows),'component mappings')
