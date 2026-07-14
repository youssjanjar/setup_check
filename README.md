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

## 3. Run the notebook

Open `hello.ipynb` in your editor and run the cell (Shift+Enter). You should see `ALL GOOD`.

**Use the venv kernel:** whichever IDE you use (VS Code, Cursor, PyCharm, etc.), make sure the notebook is using the Jupyter kernel / Python interpreter from the `.venv` you created above — not your system Python. On macOS/Linux that's typically `.venv/bin/python`; on Windows, `.venv\Scripts\python.exe`. If it doesn't appear in the kernel list, use "Select Kernel" / "Select Python Interpreter" and browse to that path.

Alternatively, from the terminal (with `.venv` activated):

```bash
jupyter lab hello.ipynb
```

Run the cell there too — it should also print `ALL GOOD`. Then you're done.

**Anything red or broken?** Reply to our email with the error message and your OS —
we'll sort it out before the day.

**If you want to commit anything** (here or in the exercise repo): `main` is protected —
create your own branch first, named `candidat_<yourname>`:

```bash
git checkout -b candidat_yourname
```

At the interview you'll receive a link to a small repo with the exercise; it uses exactly
this stack (Python + DuckDB + SQL in a Jupyter notebook), so nothing new to install.
