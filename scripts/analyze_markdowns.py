import os
import glob
import re

markdowns_dir = 'markdowns'
dirs = sorted([d for d in os.listdir(markdowns_dir) if os.path.isdir(os.path.join(markdowns_dir, d))])

print("Total categories:", len(dirs))
print("=" * 100)

summary = []

for d in dirs:
    dpath = os.path.join(markdowns_dir, d)
    mdfiles = sorted(glob.glob(os.path.join(dpath, '*.md')))
    for f in mdfiles:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        
        # Extract headers
        q_headers = re.findall(r'^###\s+(?:Q\d+[:.]|\d+[\.:])?\s*(.+)$', content, re.MULTILINE)
        
        # Extract TOC items
        toc_items = re.findall(r'^\d+\.\s+\[([^\]]+)\]', content, re.MULTILINE)
        
        # Check duplicates in questions
        q_titles = [re.sub(r'[^a-z0-9]', '', q.strip().lower()) for q in q_headers]
        seen = {}
        dupes = []
        for idx, t in enumerate(q_titles):
            if len(t) > 3:
                if t in seen:
                    dupes.append((seen[t], idx+1, q_headers[idx]))
                else:
                    seen[t] = idx+1
            
        has_difficulty = len(re.findall(r'\*\*Difficulty\*\*:', content))
        has_strategy = len(re.findall(r'\*\*(?:Strategy|Core Concept|Explanation)\*\*:', content))
        code_blocks = len(re.findall(r'```', content)) // 2
        back_to_top = len(re.findall(r'Back to Top', content, re.IGNORECASE))
        
        summary.append({
            'dir': d,
            'file': os.path.basename(f),
            'qs': len(q_headers),
            'toc': len(toc_items),
            'diff': has_difficulty,
            'strat': has_strategy,
            'code': code_blocks,
            'btt': back_to_top,
            'dupes': dupes,
            'path': f
        })

print(f"{'Directory / File':<45} | {'Qs':<4} | {'TOC':<4} | {'Diff':<4} | {'Strat':<5} | {'Code':<4} | {'BTT':<4} | {'Dupes'}")
print("-" * 100)
for s in summary:
    fname = f"{s['dir']}/{s['file']}"
    dupe_info = f"{len(s['dupes'])} dupes" if s['dupes'] else "None"
    print(f"{fname:<45} | {s['qs']:<4} | {s['toc']:<4} | {s['diff']:<4} | {s['strat']:<5} | {s['code']:<4} | {s['btt']:<4} | {dupe_info}")
    if s['dupes']:
        for d1, d2, title in s['dupes'][:3]:
            print(f"    - Dupe Q{d1} vs Q{d2}: {title}")
