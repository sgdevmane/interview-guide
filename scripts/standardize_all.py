import os
import re

def standardize_markdown(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split by <a id="q
    parts = re.split(r'<a id="q\d+"></a>', content)
    if len(parts) <= 1:
        return
    
    header = parts[0]
    # Keep header up to ## Table of Contents\n\n
    toc_pos = header.find("## Table of Contents")
    if toc_pos != -1:
        clean_header = header[:toc_pos] + "## Table of Contents\n\n"
    else:
        clean_header = header + "\n## Table of Contents\n\n"
    
    questions = []
    seen_titles = set()
    
    for p in parts[1:]:
        q_match = re.search(r'### Q\d+:\s*(.*?)\n\*\*Difficulty\*\*:\s*<span class="(.*?)">(.*?)</span>', p)
        if not q_match:
            continue
        title = q_match.group(1).strip()
        badge_cls = q_match.group(2).strip()
        badge_txt = q_match.group(3).strip()
        
        # Deduplicate title
        norm_title = title.lower().replace("`", "").replace(" ", "")
        if norm_title in seen_titles:
            continue
        seen_titles.add(norm_title)
        
        # Re-number question inside p
        # Replace ### Q\d+: with placeholder
        rest_of_p = re.sub(r'### Q\d+:', '### Q_NUM_PLACEHOLDER:', p, count=1)
        questions.append((title, badge_cls, badge_txt, rest_of_p))
    
    print(f"{filepath}: Extracted {len(questions)} unique questions.")
    
    # Build TOC and Body
    toc_lines = []
    body_blocks = []
    for idx, (title, badge_cls, badge_txt, block) in enumerate(questions, 1):
        toc_lines.append(f"{idx}. [{title}](#q{idx}) <span class=\"{badge_cls}\">{badge_txt}</span>")
        fixed_block = block.replace('### Q_NUM_PLACEHOLDER:', f'### Q{idx}:')
        body_blocks.append(f'<a id="q{idx}"></a>' + fixed_block.rstrip())
    
    new_toc = "\n".join(toc_lines) + "\n\n---\n\n"
    new_body = "\n\n---\n\n".join(body_blocks) + "\n"
    
    final_content = clean_header + new_toc + new_body
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)

for root, _, files in os.walk("markdowns"):
    for f in files:
        if f.endswith(".md") and not "part" in f and not "angular14" in f:
            standardize_markdown(os.path.join(root, f))

print("All markdowns standardized successfully!")
