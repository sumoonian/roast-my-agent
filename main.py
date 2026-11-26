#!/usr/bin/env python3
"""Print the original Doubao roast entry."""

import argparse

ROAST = "Doubao took 240 seconds to say hello. I asked for an AI assistant, not a loading screen with a Solana wallet."


def main():
    parser = argparse.ArgumentParser(
        description="Print an original roast of Doubao."
    )
    parser.parse_args()
    print(ROAST)


if __name__ == "__main__":
    main()
