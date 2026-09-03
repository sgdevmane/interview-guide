import os
import re

def fix_file_toc(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    header = content[:content.find("## Table of Contents")] + "## Table of Contents\n\n"
    body_start = content.find('<a id="q1">')
    body = content[body_start:]
    
    # Match questions in body
    q_matches = re.finditer(r'<a id="q(\d+)"></a>\s*\n### Q\d+:\s*(.*?)\n+(?:\*\*Difficulty\*\*:\s*([^\n]+))?', body)
    
    toc_lines = []
    for m in q_matches:
        idx = int(m.group(1))
        title = m.group(2).strip()
        diff_raw = m.group(3) or "Intermediate"
        # Extract badge class and clean diff text
        if "span" in diff_raw:
            diff_text_match = re.search(r'>([^<]+)<', diff_raw)
            diff_text = diff_text_match.group(1).strip() if diff_text_match else "Intermediate"
        else:
            diff_text = diff_raw.strip()
        
        diff_cls = diff_text.lower()
        if "adv" in diff_cls:
            diff_cls = "advanced"
            diff_text = "Advanced"
        elif "beg" in diff_cls:
            diff_cls = "beginner"
            diff_text = "Beginner"
        else:
            diff_cls = "intermediate"
            diff_text = "Intermediate"
        
        toc_lines.append(f"{idx}. [{title}](#q{idx}) <span class=\"{diff_cls}\">{diff_text}</span>")
    
    new_toc = "\n".join(toc_lines) + "\n\n---\n\n"
    new_content = header + new_toc + body
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Fixed TOC for {filepath} with {len(toc_lines)} items.")

fix_file_toc("markdowns/git/git-questions.md")
fix_file_toc("markdowns/linux/linux-questions.md")
