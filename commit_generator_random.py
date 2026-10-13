import os
import random
import time
from datetime import datetime, timedelta

# -------- USER INPUT --------

start_date = "2026-05-01"
end_date = "2026-10-14"

skip_weekdays = [6]  # Sunday mostly skip

skip_dates = [
    "2025-12-10"
]

# probability of commit day
commit_probability = 0.65

min_commits = 1
max_commits = 4

file_name = "activity_log.txt"

messages = [
    "fix bug",
    "update code",
    "refactor logic",
    "improve script",
    "add feature",
    "cleanup",
    "minor improvement",
    "update docs",
    "optimize code"
]

# ----------------------------

start = datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.strptime(end_date, "%Y-%m-%d")

current = start

while current <= end:

    date_str = current.strftime("%Y-%m-%d")

    # skip weekday
    if current.weekday() in skip_weekdays:
        current += timedelta(days=1)
        continue

    # skip specific date
    if date_str in skip_dates:
        current += timedelta(days=1)
        continue

    # randomly skip some days
    if random.random() > commit_probability:
        current += timedelta(days=1)
        continue

    commits_today = random.randint(min_commits, max_commits)

    for i in range(commits_today):

        # realistic coding hours
        hour = random.randint(10, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        commit_time = f"{date_str}T{hour:02d}:{minute:02d}:{second:02d}"

        with open(file_name, "a") as f:
            f.write(commit_time + "\n")

        os.system(f"git add {file_name}")

        msg = random.choice(messages)

        os.system(
            f'GIT_AUTHOR_DATE="{commit_time}" '
            f'GIT_COMMITTER_DATE="{commit_time}" '
            f'git commit -m "{msg}"'
        )

        # small delay to avoid git lock
        time.sleep(random.uniform(0.5, 1.5))

    current += timedelta(days=1)

print("Done creating commits")
print("Run: git push origin main")