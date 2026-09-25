"""Reference-pixel extraction, no generative redraw. Requires Pillow and NumPy."""
import argparse, hashlib, json, shutil
from pathlib import Path
from collections import deque
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
P=Path(__file__).resolve().parents[1]; R=P.parents[1]
parser=argparse.ArgumentParser(); parser.add_argument('reference',type=Path); args=parser.parse_args()
im=Image.open(args.reference).convert('RGB'); assert im.size==(1536,1024)
catalog=json.loads((P/'catalog.json').read_text(encoding='utf-8'))
# Independent source box, optical longest edge, and center offsets for EACH icon.
settings=[
('phone',(61,53,157,151),286,0,0),('messages',(250,57,342,148),284,0,3),
('contacts',(444,55,532,148),284,0,0),('calendar',(630,50,723,148),286,0,0),
('camera',(815,51,913,150),289,0,0),('gallery',(1006,57,1103,148),286,0,0),
('files',(1194,61,1288,146),279,0,2),('settings',(1382,55,1477,149),285,0,0),
('chrome',(60,246,159,345),288,0,0),('google',(252,252,341,339),276,0,0),
('play_store',(448,246,532,345),296,6,0),('youtube',(630,259,723,333),285,0,0),
('spotify',(818,256,913,339),290,0,0),('tiktok',(1011,245,1097,348),294,1,0),
('chatgpt',(1195,247,1290,345),301,0,0),('gemini',(1383,246,1477,345),308,0,0),
('outlook',(57,443,155,538),293,0,0),('gmail',(249,451,343,533),281,0,0),
('drive',(438,444,535,539),292,0,0),('photos',(628,441,724,542),294,0,0),
('maps',(828,441,902,540),304,0,-2),('google_tv',(1007,454,1096,529),295,0,0),
('shazam',(1196,443,1289,541),284,0,0),('youtube_music',(1381,442,1480,542),287,0,0),
('samsung_notes',(59,641,148,735),286,0,0),('clock',(249,639,346,740),303,0,0),
('calculator',(441,639,536,738),288,0,0),('bixby',(632,646,719,737),280,0,0),
('samsung_health',(819,640,913,739),294,0,0),('galaxy_store',(1010,639,1097,740),286,0,0),
('good_lock',(1198,646,1285,735),281,0,0),('samsung_members',(1387,650,1473,730),285,0,0),
('meet',(59,841,157,923),282,0,0),('vlc',(441,831,536,931),302,0,0),
('linkedin',(632,838,714,925),282,0,0),('alexa',(812,842,915,924),302,0,0),
('leboncoin',(1205,844,1284,925),272,0,0),('icon_pack_studio',(1382,837,1480,930),300,0,0)]
assert [s[0] for s in settings]==[a['key'] for a in catalog]
# Use the exact same frame for every output. Restore the dark inner plate with
# dark RGB triplets selected from aligned reference tiles, removing Phone's glyph.
xs=[31,220,408,598,787,977,1165,1355]; ys=[27,224,419,617,811]
stack=np.stack([np.asarray(im.crop((xs[a['source_cell']%8]-8,ys[a['source_cell']//8]-8,xs[a['source_cell']%8]+162,ys[a['source_cell']//8]+162))) for a in catalog])
master=stack[0].copy()
order=np.argsort(stack.max(axis=3),axis=0)
plate=np.take_along_axis(stack,order[0:1,:,:,None],axis=0)[0]
region=Image.new('L',(170,170),0); d=ImageDraw.Draw(region)
d.rounded_rectangle((28,26,141,137),radius=17,fill=255)
region=region.filter(ImageFilter.GaussianBlur(3))
base=Image.composite(Image.fromarray(plate).filter(ImageFilter.MedianFilter(3)),Image.fromarray(master),region).convert('RGBA')
alpha=Image.new('L',(170,170));d=ImageDraw.Draw(alpha)
d.rounded_rectangle((7,6,165,160),radius=37,fill=255)
alpha=alpha.filter(ImageFilter.GaussianBlur(2));base.putalpha(alpha)
base=base.resize((512,512),Image.Resampling.LANCZOS)
out=R/'icons/helix-icons01';out.mkdir(parents=True,exist_ok=True)
source=out/'reference-grid.png'
if not source.exists(): shutil.copyfile(args.reference,source)
base.save(out/'frame-master.png')
drawable=P/'app/src/main/res/drawable-nodpi';drawable.mkdir(exist_ok=True)
records=[]
for key,box,target,dx,dy in settings:
 crop=im.crop(box); rgb=np.asarray(crop).astype(float)
 strength=np.maximum(rgb[:,:,1],rgb[:,:,2])
 seed=(strength>75)&(rgb[:,:,2]>rgb[:,:,0]*1.12)
 h,w=seed.shape;seen=np.zeros_like(seed);keep=np.zeros_like(seed)
 for y,x in zip(*np.where(seed)):
  if seen[y,x]:continue
  q=deque([(y,x)]); seen[y,x]=1; comp=[]
  while q:
   yy,xx=q.popleft();comp.append((yy,xx))
   for ny,nx in [(yy-1,xx),(yy+1,xx),(yy,xx-1),(yy,xx+1)]:
    if 0<=ny<h and 0<=nx<w and seed[ny,nx] and not seen[ny,nx]:seen[ny,nx]=1;q.append((ny,nx))
  if len(comp)>=12:
   for yy,xx in comp:keep[yy,xx]=1
 mask=Image.fromarray((keep*255).astype('uint8')).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
 a=np.asarray(mask).astype(float)/255*np.clip((strength-24)/35,0,1)
 glyph=Image.fromarray(np.dstack([rgb,a*255]).astype('uint8'))
 bounds=glyph.getbbox(); assert bounds,key
 glyph=glyph.crop(bounds)
 scale=target/max(glyph.size);size=tuple(round(v*scale) for v in glyph.size)
 glyph=glyph.resize(size,Image.Resampling.LANCZOS)
 pos=(round(256-size[0]/2+dx),round(253-size[1]/2+dy))
 assert min(pos)>85 and pos[0]+size[0]<426 and pos[1]+size[1]<426,(key,pos,size)
 icon=base.copy();icon.alpha_composite(glyph,pos)
 icon.save(drawable/f'helix_{key}.png',optimize=True)
 records.append(dict(key=key,source_box=box,segmented_bounds=bounds,target_long_edge=target,offset=[dx,dy],scale=round(scale,5),output_box=[*pos,pos[0]+size[0],pos[1]+size[1]]))
sheet=Image.new('RGB',(1600,1100),(7,13,20));d=ImageDraw.Draw(sheet)
font_path=Path('C:/Windows/Fonts/arial.ttf')
font=ImageFont.truetype(str(font_path),17) if font_path.exists() else ImageFont.load_default(size=17)
for i,a in enumerate(catalog):
 x=(i%8)*200;y=(i//8)*220
 pic=Image.open(drawable/f"{a['asset']}.png").resize((184,184),Image.Resampling.LANCZOS)
 sheet.paste(pic,(x+8,y+4),pic)
 d.text((x+100,y+193),a['label'],font=font,fill='#eefcff',anchor='mt')
sheet.save(out/'contact-sheet.png')
(out/'artwork-layout.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(args.reference.read_bytes()).hexdigest(),canvas=[512,512],method='Reference-pixel extraction with identical common frame; individual proportional optical scaling and positioning; no generative redraw',icons=records),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared',len(records),'RGBA PNGs and contact sheet')
