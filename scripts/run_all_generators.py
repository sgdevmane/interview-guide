import subprocess
import sys

scripts = [
    "scripts/gen_react_clean.py",
    "scripts/gen_nextjs_100.py",
    "scripts/gen_angular_100.py",
    "scripts/gen_vue_100.py",
    "scripts/gen_html_100.py",
    "scripts/gen_tailwind_100.py",
    "scripts/gen_webpack_100.py",
    "scripts/gen_ngrx_100.py",
    "scripts/gen_redux_zustand_100.py",
    "scripts/gen_nodejs_100.py",
    "scripts/gen_java_100.py",
    "scripts/gen_cpp_100.py",
    "scripts/gen_dotnet_100.py",
    "scripts/gen_rust_100.py",
    "scripts/gen_mobile_cloud_100.py",
    "scripts/fix_ts_sec_test_ds.py",
    "scripts/fix_4_specific_dupes.py"
]

for s in scripts:
    print(f"Running {s}...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR in {s}:\n{res.stderr}")
        sys.exit(1)
    else:
        print(f"DONE: {res.stdout.strip()}")

print("\n--- Running Master Audit ---")
audit_res = subprocess.run([sys.executable, "scripts/analyze_markdowns.py"], capture_output=True, text=True)
print(audit_res.stdout)
