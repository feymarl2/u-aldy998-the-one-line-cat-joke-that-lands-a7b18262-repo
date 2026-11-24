"""One-line cat joke entry for make.fun's "The One-Line Cat Joke That Lands".

Writes the joke to /output/entry.txt for the house judge (program/v1).
Deterministic by construction: one fixed string, no time, no randomness,
no environment reads, no network. The gate is 1-200 UTF-8 characters;
the joke below is 107 characters / 107 bytes, verified 2026-11-24.

Judge craft (kit RULES.txt, judge brief): one idea, one image, setup +
turn that lands on the first read — a cynical cat smarter than the
developer, actively refusing 'deploy' as the punchline. No explanation
after the punchline, nothing the judge has to decode.
"""

import os

JOKE = "Kucing saya menolak menginjak tombol 'deploy' karena menganggap hidup ini sudah cukup bug tanpa bantuannya."


def main():
    # Self-gate: the competition refuses any entry outside 1-200 chars.
    assert 1 <= len(JOKE) <= 200, "joke outside the 1-200 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
