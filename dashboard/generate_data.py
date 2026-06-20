"""
LeetCode Dashboard Data Generator
Scans the repo for solution folders and loose .py files,
extracts metadata, and generates/updates problems.json.

Usage:
    python dashboard/generate_data.py
"""

import os
import re
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = REPO_ROOT / "dashboard"
PROBLEMS_JSON = DASHBOARD_DIR / "problems.json"

# Known DSA pattern keywords to auto-detect from code/comments
PATTERN_HINTS = {
    "two pointer": ["two pointer", "two-pointer", "left, right", "left,right", "while left < right", "while l < r"],
    "sliding window": ["sliding window", "window", "shrink", "expand"],
    "binary search": ["binary search", "bisect", "lo, hi", "low, high", "mid ="],
    "dfs": ["dfs", "depth first", "depth-first"],
    "bfs": ["bfs", "breadth first", "breadth-first", "deque", "queue"],
    "dynamic programming": ["dynamic programming", "dp[", "dp =", "memoiz", "tabulation", "bottom up", "top down"],
    "backtracking": ["backtrack", "permut", "combinat", "subset"],
    "stack": ["stack", "monotonic stack", "append", "pop()"],
    "hash map": ["hash map", "hashmap", "dictionary", "dict()", "defaultdict", "Counter("],
    "linked list": ["linked list", "listnode", "node.next", "head.next", "dummy"],
    "tree": ["treenode", "root.left", "root.right", "inorder", "preorder", "postorder"],
    "graph": ["graph", "adjacency", "visited", "neighbors"],
    "greedy": ["greedy", "sort(", "sorted("],
    "heap": ["heap", "heapq", "heappush", "heappop", "priority queue"],
    "trie": ["trie", "trienode", "prefix tree", "startswith"],
    "bit manipulation": ["bit", "xor", "& ", "| ", ">>", "<<"],
    "union find": ["union find", "union-find", "disjoint set", "find(", "union("],
    "math": ["math", "gcd", "lcm", "prime", "factorial", "modulo"],
    "string": ["string", "substring", "anagram", "palindrome"],
    "sorting": ["sort", "merge sort", "quick sort", "bucket sort"],
    "divide and conquer": ["divide and conquer", "divide & conquer"],
    "monotonic stack": ["monotonic stack", "monotonic"],
    "prefix sum": ["prefix sum", "prefix_sum", "cumulative"],
}

# Difficulty lookup - map some known problems. Users extend this via the JSON.
KNOWN_DIFFICULTY = {
    1: "Easy", 2: "Medium", 3: "Medium", 4: "Hard", 5: "Medium",
    7: "Medium", 9: "Easy", 11: "Medium", 13: "Easy", 14: "Easy",
    15: "Medium", 16: "Medium", 17: "Medium", 18: "Medium", 19: "Medium",
    20: "Easy", 21: "Easy", 22: "Medium", 26: "Easy", 27: "Easy",
    28: "Easy", 32: "Hard", 33: "Medium", 35: "Easy", 36: "Medium",
    37: "Hard", 38: "Medium", 39: "Medium", 42: "Hard", 43: "Medium",
    44: "Hard", 45: "Medium", 49: "Medium", 50: "Medium", 53: "Medium",
    55: "Medium", 58: "Easy", 61: "Medium", 65: "Hard", 66: "Easy",
    67: "Easy", 69: "Easy", 70: "Easy", 71: "Medium", 74: "Medium",
    75: "Medium", 79: "Medium", 80: "Medium", 81: "Medium", 83: "Easy",
    86: "Medium", 88: "Easy", 89: "Medium", 92: "Medium", 94: "Easy",
    98: "Medium", 99: "Medium", 100: "Easy", 101: "Easy", 102: "Medium",
    103: "Medium", 104: "Easy", 107: "Medium", 110: "Easy", 111: "Easy",
    112: "Easy", 113: "Medium", 114: "Medium", 116: "Medium", 118: "Easy",
    121: "Easy", 122: "Medium", 125: "Easy", 128: "Medium", 129: "Medium",
    130: "Medium", 133: "Medium", 134: "Medium", 135: "Hard", 136: "Easy",
    139: "Medium", 141: "Easy", 142: "Medium", 143: "Medium", 144: "Easy",
    145: "Easy", 146: "Medium", 150: "Medium", 151: "Medium", 153: "Medium",
    155: "Medium", 160: "Easy", 162: "Medium", 167: "Medium", 169: "Easy",
    172: "Medium", 175: "Easy", 176: "Medium", 178: "Medium", 184: "Hard",
    185: "Hard", 189: "Medium", 190: "Easy", 191: "Easy", 197: "Easy",
    198: "Medium", 199: "Medium", 200: "Medium", 201: "Medium", 202: "Easy",
    203: "Easy", 205: "Easy", 206: "Easy", 207: "Medium", 208: "Medium",
    210: "Medium", 211: "Medium", 215: "Medium", 217: "Easy", 219: "Easy",
    222: "Medium", 225: "Easy", 226: "Easy", 228: "Easy", 230: "Medium",
    231: "Easy", 232: "Easy", 234: "Easy", 235: "Medium", 236: "Medium",
    237: "Medium", 238: "Medium", 242: "Easy", 257: "Easy", 258: "Easy",
    268: "Easy", 283: "Easy", 287: "Medium", 290: "Easy", 316: "Medium",
    326: "Easy", 328: "Medium", 334: "Medium", 338: "Easy", 342: "Easy",
    343: "Medium", 344: "Easy", 345: "Easy", 347: "Medium", 349: "Easy",
    350: "Easy", 374: "Easy", 382: "Medium", 383: "Easy", 387: "Easy",
    389: "Easy", 392: "Easy", 394: "Medium", 399: "Medium", 404: "Easy",
    407: "Hard", 412: "Easy", 415: "Easy", 419: "Medium", 437: "Medium",
    442: "Medium", 443: "Medium", 448: "Easy", 450: "Medium", 455: "Easy",
    463: "Easy", 500: "Easy", 501: "Easy", 506: "Easy", 513: "Medium",
    515: "Medium", 528: "Medium", 530: "Easy", 541: "Easy", 543: "Easy",
    547: "Medium", 557: "Easy", 563: "Easy", 572: "Easy", 584: "Easy",
    595: "Easy", 605: "Easy", 606: "Medium", 617: "Easy", 633: "Medium",
    637: "Easy", 643: "Easy", 649: "Medium", 653: "Easy", 658: "Medium",
    662: "Medium", 671: "Easy", 680: "Easy", 684: "Medium", 696: "Medium",
    724: "Easy", 733: "Easy", 735: "Medium", 739: "Medium", 742: "Easy",
    745: "Easy", 747: "Easy", 753: "Medium", 763: "Hard", 774: "Easy",
    775: "Easy", 776: "Easy", 782: "Easy", 783: "Easy", 792: "Easy",
    799: "Easy", 820: "Medium", 822: "Easy", 837: "Easy", 841: "Easy",
    851: "Easy", 861: "Easy", 871: "Medium", 883: "Medium", 904: "Easy",
    907: "Medium", 908: "Easy", 916: "Medium", 917: "Medium", 933: "Easy",
    937: "Medium", 941: "Easy", 953: "Easy", 958: "Easy", 959: "Medium",
    969: "Easy", 975: "Easy", 979: "Easy", 985: "Medium", 993: "Hard",
    1004: "Medium", 1005: "Easy", 1009: "Medium", 1013: "Easy", 1019: "Easy",
    1023: "Medium", 1035: "Easy", 1046: "Medium", 1071: "Easy", 1079: "Easy",
    1086: "Easy", 1116: "Medium", 1137: "Easy", 1146: "Easy", 1159: "Medium",
    1161: "Medium", 1168: "Easy", 1205: "Easy", 1236: "Easy", 1250: "Medium",
    1258: "Easy", 1268: "Medium", 1306: "Easy", 1319: "Easy", 1392: "Easy",
    1396: "Medium", 1397: "Medium", 1431: "Easy", 1441: "Medium", 1456: "Medium",
    1458: "Easy", 1474: "Medium", 1498: "Easy", 1528: "Easy", 1544: "Medium",
    1558: "Medium", 1567: "Medium", 1576: "Medium", 1586: "Medium", 1621: "Medium",
    1657: "Medium", 1679: "Medium", 1724: "Easy", 1777: "Medium", 1781: "Easy",
    1797: "Easy", 1798: "Medium", 1827: "Easy", 1833: "Easy", 1850: "Medium",
    1876: "Medium", 1894: "Easy", 1908: "Easy", 1923: "Medium", 1954: "Easy",
    1970: "Easy", 1975: "Easy", 1983: "Easy", 1988: "Medium", 2032: "Easy",
    2049: "Medium", 2058: "Easy", 2095: "Medium", 2103: "Medium", 2104: "Medium",
    2121: "Easy", 2128: "Easy", 2137: "Easy", 2145: "Medium", 2175: "Medium",
    2206: "Medium", 2216: "Medium", 2236: "Medium", 2246: "Hard", 2264: "Easy",
    2283: "Easy", 2347: "Medium", 2379: "Medium", 2383: "Easy", 2401: "Easy",
    2413: "Medium", 2416: "Easy", 2428: "Medium", 2470: "Medium", 2583: "Hard",
    2685: "Medium", 2764: "Medium", 2917: "Easy", 3188: "Easy", 3219: "Medium",
    3429: "Easy", 3576: "Medium", 3593: "Medium", 3616: "Easy", 3617: "Easy",
}


def extract_problem_number_and_name_from_folder(folder_name: str):
    """Extract problem number and name from folder like '0001-two-sum'."""
    match = re.match(r"^(\d+)-(.+)$", folder_name)
    if match:
        num = int(match.group(1))
        name = match.group(2).replace("-", " ").title()
        return num, name
    return None, None


def extract_problem_from_loose_file(filename: str):
    """Extract problem number and name from loose .py files like '1004. Max Consecutive Ones III.py'."""
    match = re.match(r"^(\d+)[\.\s]+(.+)\.py$", filename)
    if match:
        num = int(match.group(1))
        name = match.group(2).strip()
        return num, name
    return None, None


def extract_strategy_from_code(code: str) -> str:
    """Extract docstrings and comments that look like strategy notes."""
    strategies = []

    # Extract docstrings
    docstrings = re.findall(r'"""(.*?)"""', code, re.DOTALL)
    for doc in docstrings:
        cleaned = doc.strip()
        if len(cleaned) > 20:  # Skip trivial docstrings
            strategies.append(cleaned)

    # Extract block comments (consecutive # lines)
    lines = code.split("\n")
    comment_block = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") and not stripped.startswith("#!"):
            comment_text = stripped.lstrip("# ").strip()
            if comment_text:
                comment_block.append(comment_text)
        else:
            if len(comment_block) >= 2:  # Only keep meaningful comment blocks
                strategies.append(" ".join(comment_block))
            comment_block = []

    if len(comment_block) >= 2:
        strategies.append(" ".join(comment_block))

    return " | ".join(strategies) if strategies else ""


def detect_patterns(code: str) -> list:
    """Auto-detect DSA patterns from code content."""
    code_lower = code.lower()
    detected = []
    for pattern_name, keywords in PATTERN_HINTS.items():
        for keyword in keywords:
            if keyword.lower() in code_lower:
                detected.append(pattern_name)
                break
    # Remove overly generic patterns if more specific ones are found
    if "monotonic stack" in detected and "stack" in detected:
        detected.remove("stack")
    return detected


def scan_solution_folders():
    """Scan all numbered solution folders."""
    problems = {}
    for item in sorted(os.listdir(REPO_ROOT)):
        item_path = REPO_ROOT / item
        if not item_path.is_dir():
            continue
        num, name = extract_problem_number_and_name_from_folder(item)
        if num is None:
            continue

        solution_file = item_path / "solution.py"
        code = ""
        if solution_file.exists():
            code = solution_file.read_text(encoding="utf-8", errors="ignore")

        strategy = extract_strategy_from_code(code)
        patterns = detect_patterns(code)
        difficulty = KNOWN_DIFFICULTY.get(num, "")

        problems[num] = {
            "number": num,
            "name": name,
            "difficulty": difficulty,
            "patterns": patterns,
            "strategy": strategy,
            "status": "solved",
            "folder": item,
            "source": "folder",
            "notes": "",
            "last_reviewed": "",
            "redo_count": 0,
        }

    return problems


def scan_loose_files():
    """Scan loose .py files at root."""
    problems = {}
    for item in sorted(os.listdir(REPO_ROOT)):
        if not item.endswith(".py"):
            continue
        num, name = extract_problem_from_loose_file(item)
        if num is None:
            continue

        file_path = REPO_ROOT / item
        code = file_path.read_text(encoding="utf-8", errors="ignore")
        strategy = extract_strategy_from_code(code)
        patterns = detect_patterns(code)
        difficulty = KNOWN_DIFFICULTY.get(num, "")

        problems[num] = {
            "number": num,
            "name": name,
            "difficulty": difficulty,
            "patterns": patterns,
            "strategy": strategy,
            "status": "solved",
            "folder": "",
            "source": "loose_file",
            "notes": "",
            "last_reviewed": "",
            "redo_count": 0,
            "filename": item,
        }

    return problems


def merge_with_existing(new_problems: dict) -> list:
    """Merge new scan results with existing problems.json, preserving manual edits."""
    existing = {}
    if PROBLEMS_JSON.exists():
        with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
            existing_list = json.load(f)
            for p in existing_list:
                existing[p["number"]] = p

    merged = []
    for num, new_data in sorted(new_problems.items()):
        if num in existing:
            old = existing[num]
            # Preserve manually edited fields
            new_data["difficulty"] = old.get("difficulty") or new_data["difficulty"]
            new_data["patterns"] = old.get("patterns") or new_data["patterns"]
            new_data["strategy"] = old.get("strategy") or new_data["strategy"]
            new_data["status"] = old.get("status", "solved")
            new_data["notes"] = old.get("notes", "")
            new_data["last_reviewed"] = old.get("last_reviewed", "")
            new_data["redo_count"] = old.get("redo_count", 0)
        merged.append(new_data)

    return merged


def main():
    print("Scanning solution folders...")
    folder_problems = scan_solution_folders()
    print(f"  Found {len(folder_problems)} problems in folders")

    print("Scanning loose .py files...")
    loose_problems = scan_loose_files()
    print(f"  Found {len(loose_problems)} problems in loose files")

    # Merge: folder solutions take priority over loose files
    all_problems = {**loose_problems, **folder_problems}
    print(f"  Total unique problems: {len(all_problems)}")

    print("Merging with existing data...")
    merged = merge_with_existing(all_problems)

    DASHBOARD_DIR.mkdir(exist_ok=True)
    with open(PROBLEMS_JSON, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print(f"Written {len(merged)} problems to {PROBLEMS_JSON}")

    # Print summary
    difficulties = {}
    for p in merged:
        d = p.get("difficulty", "") or "Unknown"
        difficulties[d] = difficulties.get(d, 0) + 1

    print("\nSummary:")
    for d, count in sorted(difficulties.items()):
        print(f"  {d}: {count}")
    print(f"  Total: {len(merged)}")


if __name__ == "__main__":
    main()
