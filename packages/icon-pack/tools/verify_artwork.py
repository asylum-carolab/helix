"""Verify packaged raster assets against the approved extraction record."""
import hashlib,json
from pathlib import Path
import numpy as np
from PIL import Image
P=Path(__file__).resolve().parents[1];R=P.parents[1];A=R/'icons/helix-icons01'
catalog=json.loads((P/'catalog.json').read_text(encoding='utf-8'))
layout=json.loads((A/'artwork-layout.json').read_text(encoding='utf-8'))
assert hashlib.sha256((A/'reference-grid.png').read_bytes()).hexdigest()==layout['source_sha256']
assert len(catalog)==len(layout['icons'])==38
frame=np.array(Image.open(A/'frame-master.png'))
y,x=np.mgrid[:512,:512];outer=(x<85)|(x>=426)|(y<85)|(y>=426)
hashes=set();report=[]
for asset,record in zip(catalog,layout['icons']):
 assert record['key']==asset['key']
 path=P/'app/src/main/res/drawable-nodpi'/f"{asset['asset']}.png"
 im=Image.open(path); pixels=np.array(im)
 assert im.size==(512,512) and im.mode=='RGBA'
 assert np.array_equal(pixels[outer],frame[outer]),f"Frame mismatch: {asset['key']}"
 assert pixels[0,0,3]==0 and pixels[-1,-1,3]==0
 box=record['output_box'];assert min(box[:2])>85 and max(box[2:])<426
 digest=hashlib.sha256(path.read_bytes()).hexdigest();hashes.add(digest)
 report.append(dict(asset=asset['asset'],sha256=digest,frame_identical=True,canvas=[512,512],glyph_box=box))
assert len(hashes)==38,'Duplicate artwork'
(A/'artwork-checks.json').write_text(json.dumps(dict(icon_count=38,unique_count=38,frame_border_identical=True,transparent_corners=True,safe_glyph_bounds=True,icons=report),indent=2)+'\n',encoding='utf-8')
print('PASS: 38 unique RGBA PNGs, identical outer frame, transparent corners, safe glyph bounds, matching source hash')
