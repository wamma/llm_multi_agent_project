# scripts/analyze_mcp_logs.py
import json
from collections import Counter
from datetime import datetime, timedelta

LOG_FILE = "logs/mcp_requests.log"

def analyze(log_file=LOG_FILE, since_days=7):
    cutoff = datetime.now().timestamp() - since_days*86400
    task_cnt = Counter()
    key_cnt  = Counter()

    with open(log_file, encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            if entry["ts"] < cutoff:
                continue
            task_cnt[entry["task"]] += 1
            for k in entry["keys"]:
                key_cnt[k] += 1

    print("🔝 Top Tasks:")
    for t, c in task_cnt.most_common(10):
        print(f"  {t}: {c}회")

    print("\n🔑 Top Context Keys:")
    for k, c in key_cnt.most_common(10):
        print(f"  {k}: {c}회")

if __name__ == "__main__":
    analyze()
