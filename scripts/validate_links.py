#!/usr/bin/env python3
"""Validate paper and code URLs stored in papers.csv."""

from __future__ import annotations

import csv
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


TIMEOUT_SECONDS = 15
USER_AGENT = "awesome-causal-tsad-link-checker/1.0"


def check_url(url: str) -> tuple[bool, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return 200 <= response.status < 400, str(response.status)
    except urllib.error.HTTPError as exc:
        # Some websites reject HEAD requests. Retry with a small GET request.
        if exc.code in {403, 405, 429}:
            get_request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Range": "bytes=0-512",
                },
                method="GET",
            )
            try:
                with urllib.request.urlopen(
                    get_request, timeout=TIMEOUT_SECONDS
                ) as response:
                    return 200 <= response.status < 400, str(response.status)
            except Exception as retry_exc:
                return False, f"{type(retry_exc).__name__}: {retry_exc}"
        return False, f"HTTP {exc.code}"
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    csv_path = repo_root / "papers.csv"

    if not csv_path.exists():
        print(f"Missing file: {csv_path}", file=sys.stderr)
        return 2

    failures = 0
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        method = row.get("method", "Unknown")
        for field in ("paper_url", "code_url"):
            url = (row.get(field) or "").strip()
            if not url:
                continue
            ok, status = check_url(url)
            label = "OK" if ok else "FAIL"
            print(f"{label:4}  {method:12}  {field:10}  {status:20}  {url}")
            if not ok:
                failures += 1
            time.sleep(0.2)

    print(f"\nChecked {len(rows)} entries; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
