"""Environment check for the DotWorld data engineering interview.

Run: python check_setup.py
If the last line says ALL GOOD, you're ready for the interview.
"""

import sys
import tempfile
from pathlib import Path

failures = []

print(f"Python {sys.version.split()[0]}", end="  ")
if sys.version_info < (3, 10):
    print("-> TOO OLD, please install Python 3.10+")
    failures.append("python")
else:
    print("-> OK")

for pkg in ("duckdb", "pandas", "jupyterlab"):
    try:
        mod = __import__(pkg)
        print(f"{pkg} {getattr(mod, '__version__', '')}".strip(), "-> OK")
    except ImportError:
        print(f"{pkg} -> MISSING (run: pip install -r requirements.txt)")
        failures.append(pkg)

if "duckdb" not in failures:
    import duckdb

    with tempfile.TemporaryDirectory() as tmp:
        csv = Path(tmp) / "smoke.csv"
        csv.write_text("id,amount\na,1\nb,2\nb,3\n")
        con = duckdb.connect(str(Path(tmp) / "smoke.duckdb"))
        con.sql("CREATE SCHEMA raw")
        con.sql(f"CREATE TABLE raw.smoke AS SELECT * FROM read_csv('{csv.as_posix()}')")
        top = con.sql("""
            SELECT id, amount FROM (
              SELECT *, row_number() OVER (PARTITION BY id ORDER BY amount DESC) rn
              FROM raw.smoke
            ) WHERE rn = 1 ORDER BY id
        """).fetchall()
        con.close()
        if top == [("a", 1), ("b", 3)]:
            print("duckdb smoke test (load CSV + query) -> OK")
        else:
            print(f"duckdb smoke test -> UNEXPECTED RESULT {top}")
            failures.append("duckdb-smoke")

print()
if failures:
    print(f"PROBLEMS FOUND: {', '.join(failures)} — see messages above.")
    print("If you can't fix it, email us before the interview and we'll sort it together.")
    sys.exit(1)
print("ALL GOOD — your machine is ready. See you at the interview!")
