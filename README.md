# DotWorld — interview environment check

Hi! Before our technical interview, please make sure your machine can run the tools we'll
use live. This takes ~5 minutes. **Please do this a few days ahead**, so if anything fails
we can fix it together before the interview instead of losing time during it.

You need: **Python 3.10+** and **git**.

## 1. Clone and install

macOS / Linux:

```bash
git clone <this-repo-url>
cd <repo-folder>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows (PowerShell):

```powershell
git clone <this-repo-url>
cd <repo-folder>
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> Windows note: if activation is blocked, run
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once, or use
> `.venv\Scripts\activate.bat` from cmd instead.

## 2. Run the check

```bash
python check_setup.py
```

You should see `ALL GOOD` at the end.

## 3. Check Jupyter starts

```bash
jupyter lab hello.ipynb
```

Run the cell (Shift+Enter) — it should print `ALL GOOD` too. Then you're done.

**Anything red or broken?** Reply to our email with the error message and your OS —
we'll sort it out before the day.

At the interview you'll receive a link to a small repo with the exercise; it uses exactly
this stack (Python + DuckDB + SQL in a Jupyter notebook), so nothing new to install.
