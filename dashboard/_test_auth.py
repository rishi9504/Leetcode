"""Quick test for LeetCode API authentication."""
import json
import secrets
from urllib.request import Request, urlopen

# Load session cookie
with open("dashboard/.env", "r") as f:
    for line in f:
        if line.strip().startswith("LEETCODE_SESSION="):
            session = line.strip().split("=", 1)[1].strip()
            break

print(f"Cookie length: {len(session)}")

# Generate a CSRF token (LeetCode just checks cookie == header match)
csrf = secrets.token_hex(32)

## Test submission detail (code)
query1 = """
query submissionDetail($submissionId: Int!) {
    submissionDetails(submissionId: $submissionId) {
        code
        lang { name verboseName }
        timestamp
        statusDisplay
        runtime
        memory
    }
}
"""

payload = json.dumps({
    "query": query1,
    "variables": {"submissionId": 1872987728}
}).encode("utf-8")

req = Request("https://leetcode.com/graphql", data=payload, method="POST")
req.add_header("Content-Type", "application/json")
req.add_header("Cookie", f"LEETCODE_SESSION={session}; csrftoken={csrf}")
req.add_header("x-csrftoken", csrf)
req.add_header("Referer", "https://leetcode.com")
req.add_header("Origin", "https://leetcode.com")
req.add_header("User-Agent",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

try:
    with urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("SUCCESS:", json.dumps(data, indent=2)[:1000])
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, "read"):
        body = e.read().decode("utf-8", errors="replace")[:500]
        print(f"Response body: {body}")
