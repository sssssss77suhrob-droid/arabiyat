"""Restore all 83 source-pinned originals after cloning this repository. No network/API.
Usage: python scripts/restore-original-media.py [--output media/restored]
"""
import argparse,hashlib,json,pathlib,sys
parser=argparse.ArgumentParser();parser.add_argument('--output',default='media/restored');args=parser.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
manifest=json.loads((root/'media/original-manifest.json').read_text(encoding='utf8'))
output=pathlib.Path(args.output);output=output if output.is_absolute() else root/output;output.mkdir(parents=True,exist_ok=True)
index=[]
for asset in manifest['files']:
 extension='.pdf' if asset['mime']=='application/pdf' else '.mp3'
 destination=output/(asset['id']+extension);digest=hashlib.sha256();size=0
 try:
  with destination.open('wb') as target:
   for part in asset['parts']:
    source=(root/part['path']).resolve()
    if not source.is_relative_to(root.resolve()):raise ValueError('Media part path leaves repository')
    part_hash=hashlib.sha256();part_size=0
    with source.open('rb') as stream:
     while data:=stream.read(1024*1024):target.write(data);digest.update(data);part_hash.update(data);size+=len(data);part_size+=len(data)
    if part_size!=part['size'] or part_hash.hexdigest()!=part['sha256']:raise ValueError('Media part checksum mismatch: '+part['path'])
  if size!=asset['size'] or digest.hexdigest()!=asset['sha256']:raise ValueError('Original checksum mismatch: '+asset['name'])
 except Exception:
  destination.unlink(missing_ok=True);raise
 index.append({'id':asset['id'],'name':asset['name'],'key':asset['key'],'mime':asset['mime'],'size':size,'sha256':digest.hexdigest(),'path':str(destination)})
 print(f"{len(index)}/{len(manifest['files'])}: {asset['name']}")
(output/'index.json').write_text(json.dumps({'verified':True,'files':index},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(f'All {len(index)} originals restored and verified. Import according to index.json; keep R2 keys unchanged.')
