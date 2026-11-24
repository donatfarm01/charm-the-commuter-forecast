"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast for the invented city of
Drizzlewick to /output/entry.txt. The line is a single constant so
the program's output is identical on every run.
"""

import os

ENTRY = "Good morning, Drizzlewick: light rain until nine, then sunshine, and the 8:15 bus will actually be on time for once."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
