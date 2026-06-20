"""
LeetCode Data Fetcher
Fetches your solved problems, accepted solutions, and question details
from LeetCode using your session cookie.

Setup:
    1. Log into leetcode.com in your browser
    2. Open DevTools (F12) -> Application -> Cookies -> leetcode.com
    3. Copy the value of the 'LEETCODE_SESSION' cookie
    4. Set it as an environment variable or pass it as an argument:
       
       Option A (env var):
         set LEETCODE_SESSION=your_cookie_value_here
         python dashboard/fetch_leetcode.py

       Option B (argument):
         python dashboard/fetch_leetcode.py --session your_cookie_value_here

       Option C (.env file):
         Create dashboard/.env with:
         LEETCODE_SESSION=your_cookie_value_here
         Then run: python dashboard/fetch_leetcode.py

Notes:
    - The session cookie expires periodically; refresh it if you get auth errors.
    - Rate-limited to ~1 request/sec to be respectful to LeetCode's servers.
    - Fetches only Accepted submissions (your latest accepted code per problem).
    - Run generate_data.py first, then this script to enrich the data.
"""

import json
import os
import secrets
import sys
import time
import argparse
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

DASHBOARD_DIR = Path(__file__).resolve().parent
PROBLEMS_JSON = DASHBOARD_DIR / "problems.json"
ENV_FILE = DASHBOARD_DIR / ".env"
LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
LEETCODE_BASE = "https://leetcode.com"

# Rate limit: seconds between API calls
RATE_LIMIT = 1.5

# CSRF token — LeetCode just checks that cookie value == header value
_CSRF_TOKEN = secrets.token_hex(32)


def load_env_file():
    """Load variables from dashboard/.env file if it exists."""
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and value:
                        os.environ.setdefault(key, value)


def get_session_cookie(args_session=None):
    """Get LEETCODE_SESSION from args, env, or .env file."""
    if args_session:
        return args_session
    load_env_file()
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    if not session:
        print("ERROR: No LEETCODE_SESSION cookie provided.")
        print()
        print("How to get your session cookie:")
        print("  1. Log into https://leetcode.com in your browser")
        print("  2. Open DevTools (F12) -> Application -> Cookies -> leetcode.com")
        print("  3. Copy the value of 'LEETCODE_SESSION'")
        print()
        print("Then either:")
        print('  set LEETCODE_SESSION=<value>')
        print("  python dashboard/fetch_leetcode.py")
        print()
        print("Or:")
        print("  python dashboard/fetch_leetcode.py --session <value>")
        print()
        print("Or create dashboard/.env with:")
        print("  LEETCODE_SESSION=<value>")
        sys.exit(1)
    return session


def graphql_request(session_cookie, query, variables=None):
    """Make a GraphQL request to LeetCode."""
    payload = json.dumps({
        "query": query,
        "variables": variables or {}
    }).encode("utf-8")

    req = Request(LEETCODE_GRAPHQL, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Cookie", f"LEETCODE_SESSION={session_cookie}; csrftoken={_CSRF_TOKEN}")
    req.add_header("x-csrftoken", _CSRF_TOKEN)
    req.add_header("Referer", LEETCODE_BASE)
    req.add_header("Origin", LEETCODE_BASE)
    req.add_header("User-Agent",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "errors" in data:
                print(f"  GraphQL errors: {data['errors']}")
                return None
            return data.get("data")
    except HTTPError as e:
        if e.code == 401 or e.code == 403:
            print(f"  AUTH ERROR ({e.code}): Session cookie may be expired. Refresh it.")
        else:
            print(f"  HTTP Error {e.code}: {e.reason}")
        return None
    except URLError as e:
        print(f"  Network error: {e.reason}")
        return None


# ─── Queries ──────────────────────────────────────────────────────────

QUERY_USER_PROFILE = """
query userProfile {
    matchedUser(username: "") {
        username
        submitStats {
            acSubmissionNum {
                difficulty
                count
            }
        }
    }
}
"""

QUERY_ALL_SOLVED = """
query userSolvedProblems($limit: Int!, $skip: Int!) {
    problemsetQuestionListV2(
        categorySlug: ""
        limit: $limit
        skip: $skip
    ) {
        questions {
            questionFrontendId
            title
            titleSlug
            difficulty
            topicTags {
                name
                slug
            }
            acRate
            paidOnly
            status
        }
    }
}
"""

QUERY_QUESTION_DETAIL = """
query questionDetail($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
        content
        topicTags {
            name
            slug
        }
        hints
        stats
        acRate
        paidOnly
    }
}
"""

QUERY_SUBMISSIONS = """
query submissionList($questionSlug: String!, $limit: Int, $offset: Int, $status: Int) {
    questionSubmissionList(
        questionSlug: $questionSlug
        limit: $limit
        offset: $offset
        status: $status
    ) {
        submissions {
            id
            lang
            timestamp
            statusDisplay
            runtime
            memory
        }
    }
}
"""

QUERY_SUBMISSION_DETAIL = """
query submissionDetails($submissionId: Int!) {
    submissionDetails(submissionId: $submissionId) {
        code
        lang {
            name
            verboseName
        }
        timestamp
        statusDisplay
        runtime
        memory
    }
}
"""


# ─── Fetchers ─────────────────────────────────────────────────────────

def fetch_all_solved_problems(session):
    """Fetch all problems the user has solved (AC status)."""
    print("Fetching all solved problems from LeetCode...")
    all_questions = []
    skip = 0
    limit = 100  # LeetCode allows up to 100 per page

    while True:
        data = graphql_request(session, QUERY_ALL_SOLVED, {
            "limit": limit,
            "skip": skip
        })
        if not data or "problemsetQuestionListV2" not in data:
            print("  Failed to fetch problem list. Check your session cookie.")
            break

        plist = data["problemsetQuestionListV2"]
        questions = plist.get("questions", [])

        if not questions:
            break

        # Filter to only solved problems (V2 API returns all, status field indicates solve state)
        solved_page = [q for q in questions if q.get("status") == "SOLVED"]
        all_questions.extend(solved_page)
        skip += limit
        print(f"  Page {skip // limit}: {len(solved_page)} solved out of {len(questions)} (total so far: {len(all_questions)})")

        # If we got fewer than limit, we've reached the end
        if len(questions) < limit:
            break

        time.sleep(RATE_LIMIT)

    print(f"  Total solved problems fetched: {len(all_questions)}")
    return all_questions


def fetch_submission_for_problem(session, title_slug):
    """Fetch the latest accepted Python3 submission for a problem.
    Falls back to any language if no Python3 submission found."""
    # Fetch latest accepted submission (status: 10 = Accepted)
    data = graphql_request(session, QUERY_SUBMISSIONS, {
        "questionSlug": title_slug,
        "limit": 1,
        "offset": 0,
        "status": 10,
    })

    submissions = []
    if data and "questionSubmissionList" in data:
        sub_list = data["questionSubmissionList"]
        if sub_list:
            submissions = sub_list.get("submissions", [])

    if not submissions:
        return None

    # Get the actual code from the submission
    sub = submissions[0]
    sub_id = int(sub["id"])
    lang_short = sub.get("lang", "unknown")
    runtime_short = sub.get("runtime", "")
    memory_short = sub.get("memory", "")
    time.sleep(RATE_LIMIT)

    detail_data = graphql_request(session, QUERY_SUBMISSION_DETAIL, {
        "submissionId": sub_id
    })

    if detail_data and "submissionDetails" in detail_data:
        detail = detail_data["submissionDetails"]
        if detail:
            lang_info = detail.get("lang") or {}
            return {
                "code": detail.get("code", ""),
                "language": lang_info.get("verboseName", lang_short),
                "runtime": detail.get("runtime", runtime_short),
                "memory": detail.get("memory", memory_short),
                "timestamp": detail.get("timestamp", ""),
            }

    # Fallback: return metadata without code
    return {
        "code": "",
        "language": lang_short,
        "runtime": runtime_short,
        "memory": memory_short,
        "timestamp": sub.get("timestamp", ""),
    }


def fetch_question_detail(session, title_slug):
    """Fetch detailed question info including description and hints."""
    data = graphql_request(session, QUERY_QUESTION_DETAIL, {
        "titleSlug": title_slug
    })
    if data and "question" in data:
        return data["question"]
    return None


# ─── Main Logic ───────────────────────────────────────────────────────

def map_topic_tags_to_patterns(tags):
    """Map LeetCode topic tags to our DSA pattern categories."""
    tag_to_pattern = {
        "array": "array",
        "hash-table": "hash map",
        "linked-list": "linked list",
        "math": "math",
        "two-pointers": "two pointer",
        "string": "string",
        "binary-search": "binary search",
        "divide-and-conquer": "divide and conquer",
        "dynamic-programming": "dynamic programming",
        "backtracking": "backtracking",
        "stack": "stack",
        "heap-priority-queue": "heap",
        "greedy": "greedy",
        "sorting": "sorting",
        "graph": "graph",
        "depth-first-search": "dfs",
        "breadth-first-search": "bfs",
        "tree": "tree",
        "binary-tree": "tree",
        "binary-search-tree": "binary search",
        "trie": "trie",
        "bit-manipulation": "bit manipulation",
        "union-find": "union find",
        "sliding-window": "sliding window",
        "monotonic-stack": "monotonic stack",
        "prefix-sum": "prefix sum",
        "recursion": "recursion",
        "memoization": "dynamic programming",
        "matrix": "matrix",
        "simulation": "simulation",
        "counting": "counting",
        "design": "design",
        "queue": "bfs",
    }

    patterns = []
    for tag in tags:
        slug = tag.get("slug", "")
        mapped = tag_to_pattern.get(slug)
        if mapped and mapped not in patterns:
            patterns.append(mapped)
    return patterns


def merge_leetcode_data(solved_questions, session, fetch_solutions=True, max_solutions=None):
    """Merge LeetCode API data into existing problems.json."""
    # Load existing data
    existing = {}
    if PROBLEMS_JSON.exists():
        with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
            for p in json.load(f):
                existing[p["number"]] = p

    updated_count = 0
    new_count = 0
    solution_count = 0

    for i, q in enumerate(solved_questions):
        num = int(q["questionFrontendId"])
        title = q["title"]
        slug = q["titleSlug"]
        # V2 API returns uppercase difficulty (EASY, MEDIUM, HARD) — normalize to title case
        difficulty = q["difficulty"].capitalize()
        tags = q.get("topicTags", [])
        ac_rate = q.get("acRate")
        # V2 API returns acRate as decimal (0-1), convert to percentage
        ac_pct = round(ac_rate * 100, 1) if ac_rate and ac_rate < 1 else (round(ac_rate, 1) if ac_rate else None)

        patterns = map_topic_tags_to_patterns(tags)
        tag_names = [t["name"] for t in tags]

        if num in existing:
            p = existing[num]
            # Update difficulty from LeetCode (authoritative source)
            p["difficulty"] = difficulty
            # Merge patterns: keep existing + add new from LeetCode tags
            existing_patterns = set(p.get("patterns", []))
            existing_patterns.update(patterns)
            p["patterns"] = list(existing_patterns)
            # Add LeetCode metadata
            p["leetcode_tags"] = tag_names
            p["leetcode_slug"] = slug
            p["acceptance_rate"] = ac_pct
            p["name"] = title  # Use exact LeetCode title
            updated_count += 1
        else:
            # New problem not in local repo
            existing[num] = {
                "number": num,
                "name": title,
                "difficulty": difficulty,
                "patterns": patterns,
                "strategy": "",
                "status": "solved",
                "folder": "",
                "source": "leetcode_api",
                "notes": "",
                "last_reviewed": "",
                "redo_count": 0,
                "leetcode_tags": tag_names,
                "leetcode_slug": slug,
                "acceptance_rate": ac_pct,
            }
            new_count += 1

    print(f"\n  Updated {updated_count} existing problems with LeetCode data")
    print(f"  Added {new_count} new problems from LeetCode")

    # Fetch actual solutions (code) — this is slower, one API call per problem
    if fetch_solutions:
        # Prioritize problems without local folders (new from LeetCode)
        existing_folders = get_existing_folders()
        no_folder = []
        has_folder = []
        for num, p in sorted(existing.items()):
            if p.get("leetcode_slug") and not p.get("leetcode_solution"):
                if num not in existing_folders:
                    no_folder.append((num, p))
                else:
                    has_folder.append((num, p))
        # Fetch no-folder problems first, then existing-folder ones
        to_fetch = no_folder + has_folder

        if max_solutions:
            to_fetch = to_fetch[:max_solutions]

        if to_fetch:
            print(f"\nFetching accepted solutions for {len(to_fetch)} problems...")
            print("  (This takes ~3 sec per problem due to rate limiting)")
            print(f"  Estimated time: ~{len(to_fetch) * 3 // 60} min {len(to_fetch) * 3 % 60} sec")
            print()

            for i, (num, p) in enumerate(to_fetch):
                slug = p["leetcode_slug"]
                print(f"  [{i+1}/{len(to_fetch)}] Fetching solution for #{num} {p['name']}...", end=" ")

                sub = fetch_submission_for_problem(session, slug)
                if sub:
                    p["leetcode_solution"] = sub["code"]
                    p["solution_language"] = sub["language"]
                    p["solution_runtime"] = sub["runtime"]
                    p["solution_memory"] = sub["memory"]
                    solution_count += 1
                    print(f"OK ({sub['language']}, {sub['runtime']})")
                else:
                    print("No submission found")

                time.sleep(RATE_LIMIT)

            print(f"\n  Fetched {solution_count} solutions")

    # Write back
    merged = sorted(existing.values(), key=lambda p: p["number"])
    with open(PROBLEMS_JSON, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print(f"\nWritten {len(merged)} problems to {PROBLEMS_JSON}")
    return merged


# ─── Folder Sync ──────────────────────────────────────────────────────

REPO_ROOT = DASHBOARD_DIR.parent

LANG_EXTENSIONS = {
    "python": ".py",
    "python3": ".py",
    "java": ".java",
    "c++": ".cpp",
    "c": ".c",
    "javascript": ".js",
    "typescript": ".ts",
    "go": ".go",
    "rust": ".rs",
    "ruby": ".rb",
    "swift": ".swift",
    "kotlin": ".kt",
    "scala": ".scala",
    "c#": ".cs",
    "php": ".php",
    "dart": ".dart",
}


def get_existing_folders():
    """Scan repo root for existing NNNN-slug/ folders and return set of problem numbers."""
    existing = {}
    for item in REPO_ROOT.iterdir():
        if item.is_dir() and item.name[:4].isdigit():
            try:
                num = int(item.name[:4])
                existing[num] = item
            except ValueError:
                pass
    return existing


def sync_folders(session=None, fetch_descriptions=True):
    """Create solution folders for all problems in problems.json that have code.

    Creates:
      NNNN-slug-name/
        solution.py   (or .java, .cpp, etc. based on submission language)
        README.md     (problem description from LeetCode if available)
    """
    if not PROBLEMS_JSON.exists():
        print("No problems.json found. Run the fetcher first.")
        return

    with open(PROBLEMS_JSON, "r", encoding="utf-8") as f:
        problems = json.load(f)

    existing_folders = get_existing_folders()

    created = 0
    updated = 0
    skipped = 0
    desc_fetched = 0

    problems_with_code = [p for p in problems if p.get("leetcode_solution") or p.get("folder")]

    print(f"\nSyncing folders for {len(problems_with_code)} problems with solution code...")
    print(f"  Existing folders found: {len(existing_folders)}")

    for p in sorted(problems_with_code, key=lambda x: x["number"]):
        num = p["number"]
        slug = p.get("leetcode_slug", "")
        name = p.get("name", "")
        code = p.get("leetcode_solution", "")
        lang = p.get("solution_language", "python3").lower()

        if not slug:
            # Build slug from name
            slug = name.lower().replace(" ", "-").replace("(", "").replace(")", "")
            slug = "".join(c for c in slug if c.isalnum() or c == "-")
            slug = slug.strip("-")

        folder_name = f"{num:04d}-{slug}"
        folder_path = REPO_ROOT / folder_name

        # Check if folder already exists (by number)
        if num in existing_folders:
            existing_path = existing_folders[num]
            # Update solution file if we have code and existing folder has no solution
            solution_files = list(existing_path.glob("solution.*"))
            if code and not solution_files:
                ext = LANG_EXTENSIONS.get(lang, ".py")
                sol_file = existing_path / f"solution{ext}"
                sol_file.write_text(code, encoding="utf-8")
                print(f"  + Added solution to existing {existing_path.name}/")
                updated += 1
            else:
                skipped += 1
            # Update the folder path in problems.json
            p["folder"] = existing_path.name
            continue

        if not code:
            skipped += 1
            continue

        # Create new folder
        folder_path.mkdir(exist_ok=True)

        # Write solution file
        ext = LANG_EXTENSIONS.get(lang, ".py")
        sol_file = folder_path / f"solution{ext}"
        sol_file.write_text(code, encoding="utf-8")

        # Fetch and write README.md (problem description)
        readme_content = ""
        if fetch_descriptions and session and slug:
            time.sleep(RATE_LIMIT)
            detail = fetch_question_detail(session, slug)
            if detail and detail.get("content"):
                readme_content = detail["content"]
                desc_fetched += 1

        if not readme_content:
            # Minimal README with problem title and link
            readme_content = (
                f"<h2>{num}. {name}</h2>\n"
                f'<p><a href="https://leetcode.com/problems/{slug}/">View on LeetCode</a></p>\n'
                f"<p>Difficulty: {p.get('difficulty', 'Unknown')}</p>\n"
            )

        readme_file = folder_path / "README.md"
        readme_file.write_text(readme_content, encoding="utf-8")

        p["folder"] = folder_name
        created += 1
        print(f"  + Created {folder_name}/ ({lang})")

    # Write updated problems.json with folder references
    with open(PROBLEMS_JSON, "w", encoding="utf-8") as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)

    print(f"\nFolder sync complete:")
    print(f"  Created: {created} new folders")
    print(f"  Updated: {updated} existing folders (added solution)")
    print(f"  Skipped: {skipped} (already complete or no code)")
    if fetch_descriptions:
        print(f"  Descriptions fetched: {desc_fetched}")


def main():
    parser = argparse.ArgumentParser(description="Fetch LeetCode solved problems and solutions")
    parser.add_argument("--session", type=str, help="LEETCODE_SESSION cookie value")
    parser.add_argument("--no-solutions", action="store_true",
                        help="Skip fetching individual solution code (faster)")
    parser.add_argument("--max-solutions", type=int, default=None,
                        help="Max number of solutions to fetch (for testing, e.g. --max-solutions 5)")
    parser.add_argument("--problems-only", action="store_true",
                        help="Only fetch problem list, skip solutions entirely")
    parser.add_argument("--sync-folders", action="store_true",
                        help="Create NNNN-slug/ folders with solution files and README.md")
    parser.add_argument("--sync-only", action="store_true",
                        help="Only sync folders from existing problems.json (no LeetCode fetch)")
    parser.add_argument("--no-descriptions", action="store_true",
                        help="Skip fetching problem descriptions for README.md during sync")
    args = parser.parse_args()

    session = get_session_cookie(args.session)

    # --sync-only: just create folders from existing data, no LeetCode fetch
    if args.sync_only:
        print("Syncing folders from existing problems.json (no LeetCode fetch)...")
        sync_folders(session=session, fetch_descriptions=not args.no_descriptions)
        print("\nDone!")
        return

    # Test authentication first
    print("Testing LeetCode session...")
    test_data = graphql_request(session, QUERY_ALL_SOLVED, {"limit": 1, "skip": 0})
    if not test_data or "problemsetQuestionListV2" not in test_data:
        print("\nFailed to authenticate. Please check your LEETCODE_SESSION cookie.")
        sys.exit(1)

    questions = test_data["problemsetQuestionListV2"].get("questions", [])
    print(f"  Authenticated! Connection successful (got {len(questions)} test record).\n")

    # Fetch all solved problems
    solved = fetch_all_solved_problems(session)
    if not solved:
        print("No solved problems found. Exiting.")
        sys.exit(1)

    # Merge into problems.json
    fetch_solutions = not args.no_solutions and not args.problems_only
    merge_leetcode_data(
        solved,
        session,
        fetch_solutions=fetch_solutions,
        max_solutions=args.max_solutions,
    )

    # Sync folders if requested
    if args.sync_folders:
        sync_folders(session=session, fetch_descriptions=not args.no_descriptions)

    print("\nDone! Refresh your dashboard to see the updated data.")
    if args.no_solutions or args.problems_only:
        print("Tip: Run without --no-solutions to also fetch your accepted code.")
    if not args.sync_folders:
        print("Tip: Run with --sync-folders to create solution folders in your repo.")


if __name__ == "__main__":
    main()
