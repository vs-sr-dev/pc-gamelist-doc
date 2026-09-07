#!/usr/bin/env python3
"""rowlen.py -- measure the titles table in README.md against the row format.

    python tools/rowlen.py            # column statistics and any violations
    python tools/rowlen.py --quiet    # exit 1 if a row is over budget, no output

The budgets are the ones written above the table. A row that carries an
argument instead of a value is a row whose argument belongs in the repository
the title links to, and this tool is what says so before a commit does.
"""
import os
import re
import sys

COLUMNS = ["Title", "Year", "Studio", "Saga", "What it is"]
BUDGET = {"Year": 4, "Studio": 60, "Saga": 40, "What it is": 200}
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")


def rows(path):
    """The titles table, found by its header rather than by being the first.

    The README holds more than one table -- the row-format table above the
    titles is itself a table -- so a tool that took the first one would measure
    the documentation of the rule instead of the rows the rule governs.
    """
    got = []
    header = None
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\r\n")
        if not line.startswith("|"):
            if header is not None and got:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            if cells == COLUMNS:
                header = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        got.append((n, cells))
    if header is None:
        sys.exit("no table headed %s in %s" % (" | ".join(COLUMNS), path))
    return header, got


def main():
    quiet = "--quiet" in sys.argv
    cols, data = rows(README)
    if not data:
        sys.exit("the titles table has a header and no rows -- refusing to "
                 "report a clean run over an empty population")
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
        if not re.fullmatch(r"\d{4}", cells[1]):
            bad.append((n, "%s: Year is %r, not four digits" % (who, cells[1])))
    if not quiet:
        print("%-12s %5s %5s %5s %7s" % ("column", "min", "med", "max", "total"))
        for i, name in enumerate(cols):
            lens = sorted(len(c[i]) for _, c in data if len(c) > i)
            print("%-12s %5d %5d %5d %7d"
                  % (name, lens[0], lens[len(lens) // 2], lens[-1], sum(lens)))
        print("\n%d rows, %d over budget" % (len(data), len(bad)))
        for n, msg in bad:
            print("  README.md:%d  %s" % (n, msg))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
