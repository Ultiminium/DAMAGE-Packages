# Contributing to DAMAGE-Packages

Anyone can submit a package. Packages are installed via `damage install name` and auto-load on every program run.

---

## How to submit a package

1. Fork this repository
2. Create a folder with your package name (e.g. `mypackage/`)
3. Add the required files (see below)
4. Open a pull request

Once reviewed and merged, it's available to all DAMAGE users via `damage install mypackage`.

---

## Package structure

```
mypackage/
  package.json     required — metadata
  mypackage.damg   required — your DAMAGE code
  mypackage.zip    required — zip of the files above
```

---

## package.json format

```json
{
  "name": "mypackage",
  "version": "1.0",
  "description": "What your package does",
  "author": "your-github-username",
  "functions": ["@funcname"]
}
```

---

## Writing your package

Packages are written in standard DAMAGE syntax. Define functions with `@addfunc` — they'll be available in any program after install.

```
@addfunc+
@print+
     +Hello from mypackage!-
@-
@addfunc:createname"myfunc"
@---
```

Anything valid in DAMAGE is valid in a package — variables, conditions, loops, functions. The package runs once on load, so anything defined at the top level is immediately available.

---

## The zip file

The `.zip` must contain all your package files at the root level (not in a subfolder):

```bash
cd mypackage/
zip -j mypackage.zip *
```

---

## Rules

- Packages must be written in DAMAGE only — no Python or other languages
- No malicious code
- No packages that conflict with DAMAGE built-in names
- Name must be lowercase, no spaces
- Keep it useful — packages should add real functionality
- No adult or otherwise inappropriate content

---

## Questions?

Open an issue on the [DAMAGE repo](https://github.com/Ultiminium/DAMAGE).
