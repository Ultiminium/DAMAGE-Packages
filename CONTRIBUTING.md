# Contributing to DAMAGE-Packages

Thank you for wanting to contribute. This is the official community package registry for the DAMAGE programming language. Anyone can submit a package — if it's useful and follows the rules, it gets merged.

---

## What is a DAMAGE package?

A package is a collection of DAMAGE functions and variables that users can install with a single command:

```bash
damage install packagename
```

Once installed, everything in the package auto-loads every time a `.damg` program runs. No import needed.

---

## Before you start

- Packages must be written in **pure DAMAGE** — no Python, no other languages
- Your package must not conflict with any DAMAGE built-in function name
- Function names must be unique — check existing packages before naming yours
- Package names must be **lowercase with no spaces**

Built-in names you cannot use:
`print` `var` `math` `loop` `user` `addfunc` `output` `dyn` `gui` `random` `text` `clear` `import` `enc` `dec` `fetch`

---

## Package structure

Every package lives in its own folder named after the package:

```
mypackage/
  package.json     — required, metadata
  mypackage.damg   — required, your DAMAGE code
  mypackage.zip    — required, zip of all files above
```

---

## Writing package.json

```json
{
  "name": "mypackage",
  "version": "1.0",
  "description": "A short description of what your package does",
  "author": "your-github-username",
  "functions": ["@myfunc", "@myotherfunc"]
}
```

All fields are required. `functions` is a list of every function your package adds.

---

## Writing your .damg file

Use standard DAMAGE syntax. Define all your functions with `@addfunc`. Variables set at the top level are available globally after the package loads.

```
| mypackage.damg

@addfunc+
@print+
     +Hello from mypackage!-
@-
@addfunc:createname"myfunc"
@---

@addfunc+
| set @var n+(value)- before calling this
@print,var+
     +The value is (n)-
@-
@addfunc:createname"myotherfunc"
@---
```

**Document your functions with comments.** Tell users what variables to set before calling each function, and what variables the function produces as output.

---

## Variable conventions

Since DAMAGE variables are shared globally, use a prefix to avoid conflicts:

```
| good — prefixed with package name
@var+
     dice_result+0-
@-

| bad — too generic, might conflict
@var+
     result+0-
@-
```

---

## Creating the zip file

The `.zip` must contain all your files at the **root level** — not inside a subfolder.

```bash
cd mypackage/
zip -j mypackage.zip package.json mypackage.damg
```

Verify the zip contains the right files:

```bash
unzip -l mypackage.zip
```

---

## Submitting your package

1. **Fork** this repository on GitHub
2. **Create a folder** with your package name — when creating a new file, type `mypackage/package.json` to create the folder automatically
3. **Upload all three files** — `package.json`, `mypackage.damg`, `mypackage.zip`
4. **Open a pull request** with a short description of what your package does

---

## What happens next

Your pull request will be reviewed for:

- Does it work correctly in DAMAGE?
- Does it follow naming conventions?
- Is it actually useful?
- Is the code readable and documented?

If it passes review, it gets merged and immediately becomes available via `damage install mypackage`.

---

## Updating a package

To release a new version:

1. Fork and update your package files
2. Bump the version in `package.json` (e.g. `"version": "1.1"`)
3. Rebuild the zip
4. Open a pull request

---

## Example packages

Look at the existing packages for reference:

| Package | What it does |
|---------|-------------|
| `dice` | Roll d6, d20, d100, or custom dice |
| `cards` | Draw random cards from a standard deck |
| `math` | Square root, absolute value, rounding |
| `color` | Colored terminal output |
| `table` | Formatted tables and dividers |
| `format` | Currency display, zero padding |
| `validate` | Password strength, range checking |
| `string` | Repeat strings, trim |

---

## Questions?

Open an issue on the [DAMAGE repository](https://github.com/Ultiminium/DAMAGE).
