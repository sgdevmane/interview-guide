import os
import sys
sys.path.append(os.path.dirname(__file__))
from writer_helper import write_category_file

# ==============================================================================
# Helper to build clean 100 questions
# ==============================================================================
def create_100_qnas(topic_name, file_name, title, subtitle, icon, curated_list):
    """
    curated_list: list of tuples (title, difficulty, strategy, code)
    Ensures exactly 100 unique questions with complete details.
    """
    assert len(curated_list) >= 100, f"Need at least 100 questions for {topic_name}, got {len(curated_list)}"
    
    questions = []
    seen = set()
    for item in curated_list:
        clean_title = item[0].strip()
        norm = clean_title.lower()
        if norm not in seen and len(questions) < 100:
            seen.add(norm)
            questions.append({
                "title": clean_title,
                "difficulty": item[1],
                "strategy": item[2],
                "code": item[3]
            })
            
    assert len(questions) == 100, f"Expected 100 questions for {topic_name}, got {len(questions)}"
    write_category_file(topic_name, file_name, title, subtitle, icon, questions)
    print(f"[SUCCESS] Generated 100 QnAs for {topic_name}")

if __name__ == '__main__':
    print("Batch generator base ready.")
