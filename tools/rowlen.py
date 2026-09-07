#!/usr/bin/env python3
"""rowlen.py -- measure the table in README.md against the row format.

    python tools/rowlen.py            # column statistics and any violations
    python tools/rowlen.py --quiet    # exit 1 if a row is over budget, no output

The budgets are the ones written above the table. A row that carries an
argument instead of a value is a row whose argument belongs in the repository
the title links to, and this tool is what says so before a commit does.
"""
import os
import re
import sys

BUDGET = {"Year": 4, "Studio": 60, "Saga": 40, "What it is": 200}
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")


def rows(path):
    got = []
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if not line.startswith("|"):
            continue
        got.append((n, [c.strip() for c in line.rstrip("\n").strip().strip("|").split("|")]))
    if len(got) < 3:
        sys.exit("no table in %s" % path)
    return got[0][1], got[2:]


def main():
    quiet = "--quiet" in sys.argv
    cols, data = rows(README)
    if len(data) == 0:
        sys.exit("table has a header and no rows -- refusing to report a clean run "
                 "over an empty population")
    bad = []
    for n, cells in data:
        if len(cells) != len(cols):
            bad.append((n, "row has %d cells, header has %d" % (len(cells), len(cols))))
            continue
        slug = re.search(r"vs-sr-dev/([A-Za-z0-9._-]+)", cells[0])
        who = slug.group(1) if slug else cells[0][:40]
        for i, name in enumerate(cols):
            limit = BUDGET.get(name)
            if limit is not None and len(cells[i]) > limit:
                bad.append((n, "%s: %s is %d characters, budget %d"
                            % (who, name, len(cells[i]), limit)))
        if len(cells) > 1 and not re.fullmatch(r"\d{4}", cells[1]):
            bad.append((n, "%s: Year is %r, not four digits" % (who, cells[1])))
    if not quiet:
        print("%-12s %5s %5s %5s %7s" % ("column", "min", "med", "max", "total"))
        for i, name in enumerate(cols):
            lens = sorted(len(c[i]) for _, c in data if len(c) > i)
            med = lens[len(lens) // 2]
            print("%-12s %5d %5d %5d %7d"
                  % (name, lens[0], med, lens[-1], sum(lens)))
        print("\n%d rows, %d over budget" % (len(data), len(bad)))
        for n, msg in bad:
            print("  README.md:%d  %s" % (n, msg))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
