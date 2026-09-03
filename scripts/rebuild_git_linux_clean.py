import os
import re

def clean_file_to_100(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    header = content[:content.find("## Table of Contents")] + "## Table of Contents\n\n"
    
    # Split content by <a id="q
    parts = re.split(r'<a id="q\d+"></a>', content)
    
    unique_questions = []
    seen_titles = set()
    
    for p in parts[1:]:
        q_match = re.search(r'### Q\d+:\s*(.*?)\n', p)
        if not q_match:
            continue
        raw_title = q_match.group(1).strip()
        norm_title = raw_title.lower().replace("`", "").replace(" ", "").replace("?", "").replace(":", "")
        
        if norm_title in seen_titles:
            continue
        seen_titles.add(norm_title)
        
        # Extract difficulty
        diff_match = re.search(r'\*\*Difficulty\*\*:\s*([^\n]+)', p)
        diff_raw = diff_match.group(1).strip() if diff_match else "Intermediate"
        if "span" in diff_raw:
            span_txt = re.search(r'>([^<]+)<', diff_raw)
            diff_text = span_txt.group(1).strip() if span_txt else "Intermediate"
        else:
            diff_text = diff_raw
        
        diff_cls = diff_text.lower()
        if "adv" in diff_cls or "exp" in diff_cls:
            diff_cls = "advanced"
            diff_text = "Advanced"
        elif "beg" in diff_cls:
            diff_cls = "beginner"
            diff_text = "Beginner"
        else:
            diff_cls = "intermediate"
            diff_text = "Intermediate"
        
        # Strip old ### Q\d+: ... from p
        cleaned_body = re.sub(r'### Q\d+:.*?\n', '', p, count=1).strip()
        # Ensure difficulty tag is standardized
        cleaned_body = re.sub(r'\*\*Difficulty\*\*:.*?\n', '', cleaned_body, count=1).strip()
        
        unique_questions.append((raw_title, diff_cls, diff_text, cleaned_body))
        if len(unique_questions) >= 100:
            break
    
    print(f"{filepath}: gathered {len(unique_questions)} unique questions.")
    
    toc_lines = []
    body_blocks = []
    
    for idx, (title, diff_cls, diff_txt, body) in enumerate(unique_questions, 1):
        toc_lines.append(f"{idx}. [{title}](#q{idx}) <span class=\"{diff_cls}\">{diff_txt}</span>")
        q_block = f"""<a id="q{idx}"></a>
### Q{idx}: {title}
**Difficulty**: <span class="{diff_cls}">{diff_txt}</span>  

{body}"""
        body_blocks.append(q_block)
    
    new_toc = "\n".join(toc_lines) + "\n\n---\n\n"
    new_body = "\n\n---\n\n".join(body_blocks) + "\n"
    
    final_content = header + new_toc + new_body
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"Successfully cleaned {filepath} to 100 unique Qs.")

clean_file_to_100("markdowns/git/git-questions.md")
clean_file_to_100("markdowns/linux/linux-questions.md")
