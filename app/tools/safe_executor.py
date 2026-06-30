import ast
import pandas as pd
import numpy as np


ALLOWED_GLOBALS = {
    "__builtins__": {},
    "pd": pd,
    "np": np
}

BLOCKED_NAMES = {
    "eval",
    "exec",
    "open",
    "compile",
    "__import__",
    "input"
}

BLOCKED_MODULES = {
    "os",
    "sys",
    "subprocess",
    "shutil",
    "pathlib",
    "socket",
    "requests"
}


def validate_code(code):
    tree = ast.parse(code)

    for node in ast.walk(tree):

        if isinstance(node, (ast.Import, ast.ImportFrom)):
            raise ValueError("Imports are not allowed")

        if isinstance(node, ast.Name) and node.id in BLOCKED_NAMES:
            raise ValueError(f"{node.id} is not allowed")

        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            raise ValueError("Dunder methods are not allowed")

        if isinstance(node, ast.Name) and node.id in BLOCKED_MODULES:
            raise ValueError(f"{node.id} is not allowed")


def execute_code(code, df):
    validate_code(code)

    local_vars = {"df": df.copy()}

    try:
        exec(code, ALLOWED_GLOBALS, local_vars)

        if "result" not in local_vars:
            raise ValueError("Code must store output in 'result'")

        return local_vars["result"]

    except Exception as e:
        raise RuntimeError(f"Execution failed: {e}")