import os
import re

def rebuild_file_toc(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract header up to ## Table of Contents
    toc_match = re.search(r'(.*?## Table of Contents\s*\n)(.*?)(\n---\s*\n\s*<a id="q1">|<a id="q1">)', content, flags=re.DOTALL)
    if not toc_match:
        return
    
    header_part = toc_match.group(1)
    body_part = content[content.find('<a id="q1">'):]
    
    # Parse all questions in body
    q_blocks = re.findall(r'<a id="q(\d+)"></a>\s*\n### Q\d+:\s*(.*?)\n\*\*Difficulty\*\*:\s*<span class="(.*?)">(.*?)</span>', body_part)
    
    if not q_blocks:
        return
    
    # Rebuild clean TOC
    toc_lines = []
    seen_titles = set()
    new_body_blocks = []
    
    for idx, (q_num, title, badge_class, badge_text) in enumerate(q_blocks, 1):
        clean_title = title.strip()
        toc_lines.append(f"{idx}. [{clean_title}](#q{idx}) <span class=\"{badge_class}\">{badge_text}</span>")
    
    new_toc = "\n".join(toc_lines) + "\n\n---\n\n"
    
    # Write back
    new_content = header_part + new_toc + body_part
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Rebuilt clean TOC for {filepath} ({len(q_blocks)} items)")

for cat in ["git", "linux", "database", "design-patterns", "golang", "graphql", "algorithms", "python", "css", "svelte", "microfrontend", "microservices", "kubernetes", "material-radix-ui", "system-design"]:
    md_files = [f for f in os.listdir(f"markdowns/{cat}") if f.endswith(".md") and not "part" in f]
    for mf in md_files:
        rebuild_file_toc(f"markdowns/{cat}/{mf}")

print("TOC rebuilding complete.")
