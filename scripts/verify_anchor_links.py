import os
import re
import sys

MARKDOWNS_DIR = "markdowns"

def verify_all_anchors():
    print("=== Comprehensive Anchor Link Verifier ===")
    total_files = 0
    total_links_verified = 0
    errors = []

    for root, dirs, files in os.walk(MARKDOWNS_DIR):
        for f in files:
            if f.endswith("-questions.md"):
                total_files += 1
                file_path = os.path.join(root, f)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()

                # Extract TOC links: (#q1), (#q2), etc.
                toc_links = re.findall(r'\[.*?\]\(#(q\d+)\)', content)
                # Extract Target anchors: <a id="q1"></a> or <a name="q1"></a>
                target_anchors = set(re.findall(r'<a\s+(?:id|name)=["\'](q\d+)["\']', content))

                missing_anchors = []
                for q_id in toc_links:
                    total_links_verified += 1
                    if q_id not in target_anchors:
                        missing_anchors.append(q_id)

                if missing_anchors:
                    errors.append((file_path, missing_anchors))

    print(f"Verified {total_links_verified} TOC anchor links across {total_files} categories.")
    if errors:
        print(f"❌ Found {len(errors)} files with missing target anchors:")
        for fp, missing in errors:
            print(f"  - {fp}: missing {len(missing)} anchors -> {missing[:5]}...")
        sys.exit(1)
    else:
        print("✅ 100% of TOC anchor links have exact matching target <a id=\"qX\"> anchors in markdown body!")

if __name__ == "__main__":
    verify_all_anchors()
