"""
Student Performance Analyser
Subject: Fundamentals of AI-ML
- Prints statistics to console
- Bar graph for Marks (clean plot)
- Scatter graph for Attendance (clean plot)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────

marks_df      = pd.read_csv("student_marks.csv")
attendance_df = pd.read_csv("student_attendance.csv")

names  = marks_df["StudentName"].str.split().str[0]
scores = marks_df["Marks_AIML"]

att_names = attendance_df["StudentName"].str.split().str[0]
att_pct   = attendance_df["AttendancePercent"]

# ─────────────────────────────────────────────
# 2. STATISTICS — PRINTED TO CONSOLE ONLY
# ─────────────────────────────────────────────

print("=" * 50)
print("  MARKS STATISTICS — Fundamentals of AI-ML")
print("=" * 50)
print(f"  Total Students  : {len(scores)}")
print(f"  Mean            : {scores.mean():.2f}")
print(f"  Median          : {scores.median():.2f}")
print(f"  Std Deviation   : {scores.std():.2f}")
print(f"  Min Score       : {scores.min()}")
print(f"  Max Score       : {scores.max()}")
print(f"  Pass (>= 40)    : {(scores >= 40).sum()}")
print(f"  Fail  (< 40)    : {(scores < 40).sum()}")
print("=" * 50)

print()

print("=" * 50)
print("  ATTENDANCE STATISTICS  (2 Weeks / 10 Days)")
print("=" * 50)
print(f"  Mean Attendance   : {att_pct.mean():.2f}%")
print(f"  Median Attendance : {att_pct.median():.2f}%")
print(f"  Std Deviation     : {att_pct.std():.2f}%")
print(f"  Highest           : {att_pct.max()}%")
print(f"  Lowest            : {att_pct.min()}%")
print(f"  Regular (>= 75%)  : {(att_pct >= 75).sum()}")
print(f"  Shortage (< 75%)  : {(att_pct < 75).sum()}")
print("=" * 50)

# ─────────────────────────────────────────────
# 3. BAR GRAPH — MARKS (clean, no stats on plot)
# ─────────────────────────────────────────────

fig1, ax1 = plt.subplots(figsize=(12, 5))

ax1.bar(names, scores, color="steelblue", edgecolor="navy", width=0.6)

ax1.set_xlabel("Students")
ax1.set_ylabel("Marks (out of 100)")
ax1.set_title("Student Marks — Fundamentals of AI-ML")
ax1.set_ylim(0, 110)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("marks_bar_graph.png", dpi=150, bbox_inches="tight")
plt.show()

# ─────────────────────────────────────────────
# 4. SCATTER GRAPH — ATTENDANCE (clean, no stats on plot)
# ─────────────────────────────────────────────

x_pos = np.arange(len(att_names))

fig2, ax2 = plt.subplots(figsize=(12, 5))

ax2.scatter(x_pos, att_pct, color="darkorange", s=100, zorder=5, edgecolors="black", linewidth=0.6)

ax2.set_xticks(x_pos)
ax2.set_xticklabels(att_names, rotation=30, ha="right")
ax2.set_ylim(0, 110)
ax2.set_xlabel("Students")
ax2.set_ylabel("Attendance (%)")
ax2.set_title("Student Attendance — 2 Weeks (10 Working Days)")
plt.tight_layout()
plt.savefig("attendance_scatter_graph.png", dpi=150, bbox_inches="tight")
plt.show()
