from typing import Final


PROMPT_ARROW: Final[str] = "->"


def input_data(exploit_name: str, prompt_title: str) -> str:
    return input(f"Apophis({exploit_name}) ~ {prompt_title} {PROMPT_ARROW} ").strip()


def print_success(message: str) -> None:
    print(f"[SUCCESS] {message}")


def print_error(message: str) -> None:
    print(f"[ERROR] {message}")


def print_status(message: str) -> None:
    print(f"[STATUS] {message}")

