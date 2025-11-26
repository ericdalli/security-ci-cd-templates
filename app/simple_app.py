"""
Very small demo application to illustrate how security checks
(Bandit, dependency scanning) can be wired into CI/CD pipelines.

This is not a real application – just enough code to give tools
something to analyze.
"""

import os
from hashlib import sha256


def hash_value(value: str) -> str:
    """Return a simple SHA-256 hash of the given string."""
    return sha256(value.encode("utf-8")).hexdigest()


def get_config() -> dict:
    """
    Example config loader.

    In a real-world app you’d read from environment variables,
    config files, or a secret manager – *not* hard-code secrets.
    """
    return {
        "ENV": os.getenv("APP_ENV", "dev"),
        "DEBUG": os.getenv("APP_DEBUG", "false").lower() == "true",
    }


def main() -> None:
    config = get_config()
    print(f"Running in environment: {config['ENV']}")
    print(f"Debug mode: {config['DEBUG']}")
    print(f"Hash of 'example': {hash_value('example')}")


if __name__ == "__main__":
    main()
