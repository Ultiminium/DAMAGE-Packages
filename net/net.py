"""
DAMAGE net package v1.0
Adds HTTP GET requests to DAMAGE.

Usage:
@net,print+
     +https://api.example.com/data-
@var:create+response-
@-
"""

def register(interpreter):
    interpreter.BUILTINS.add("net")

    orig_exec_generic = interpreter._exec_generic

    def patched(funcs, content):
        if "net" in funcs:
            import urllib.request
            url = interpreter.resolve_content(content or "", funcs)
            try:
                with urllib.request.urlopen(url, timeout=10) as r:
                    result = r.read().decode()
                interpreter.last_input = result
                if "print" in funcs:
                    print(result)
            except Exception as e:
                interpreter.report_error(f"@net: request failed: {e}")
            return
        orig_exec_generic(funcs, content)

    interpreter._exec_generic = patched
