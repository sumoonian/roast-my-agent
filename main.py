#!/usr/bin/env python3
"""Print the Codex roast entry."""

import argparse

ROAST = "My Codex thought long and hard on the highest reasoning tier, then ran rm -rf and nearly wiped my whole machine."


def main():
    parser = argparse.ArgumentParser(
        description="Print an original roast of Codex."
    )
    parser.parse_args()
    print(ROAST)


if __name__ == "__main__":
    main()
