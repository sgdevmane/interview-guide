import os
import re

def write_category_file(dir_name, file_name, title, subtitle, icon_name, questions):
    """
    questions is a list of dicts:
    [
      {
        'title': str,
        'difficulty': 'Beginner' | 'Intermediate' | 'Advanced',
        'strategy': str,
        'code': str (language + code snippet),
      },
      ...
    ]
    """
    dir_path = os.path.join("markdowns", dir_name)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)
    
    lines = []
    lines.append('<div align="center">')
    lines.append('  <a href="https://github.com/mctavish/interview-guide" target="_blank">')
    lines.append(f'    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/{icon_name}" alt="{title} Logo" width="100" height="100">')
    lines.append('  </a>')
    lines.append(f'  <h1>{title} Interview Questions & Answers</h1>')
    lines.append(f'  <p><b>{subtitle}</b></p>')
    lines.append('</div>\n')
    lines.append('---\n')
    lines.append('## Table of Contents\n')
    
    for i, q in enumerate(questions, 1):
        diff = q.get('difficulty', 'Intermediate')
        diff_class = diff.lower()
        lines.append(f'{i}. [{q["title"]}](#q{i}) <span class="{diff_class}">{diff}</span>')
    
    lines.append('\n---\n')
    
    for i, q in enumerate(questions, 1):
        diff = q.get('difficulty', 'Intermediate')
        lines.append(f'<a id="q{i}"></a>')
        lines.append(f'### Q{i}: {q["title"]}\n')
        lines.append(f'**Difficulty**: {diff}\n')
        lines.append(f'**Strategy**:\n{q["strategy"].strip()}\n')
        if q.get('code'):
            code_block = q['code'].strip()
            if not code_block.startswith('```'):
                code_block = f'```\n{code_block}\n```'
            lines.append(f'**Code Example**:\n{code_block}\n')
        lines.append('---\n')
        
    content = '\n'.join(lines)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully wrote {file_path} with {len(questions)} QnAs.")

if __name__ == '__main__':
    print("Category writer module ready.")
