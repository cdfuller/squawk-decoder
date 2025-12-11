"""CLI wrapper for squawk lookups."""

import argparse
import json

from squawk_data import SquawkDatabase


def parse_args():
    """Build and parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Look up squawk code allocations from FAA Order JO 7110.66G (NBCAP)."
    )
    parser.add_argument("code", help="Four-digit Mode 3/A squawk code (octal digits 0-7).")
    parser.add_argument(
        "--json", dest="as_json", action="store_true", help="Return the raw lookup payload as JSON."
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Include legend and contextual notes in text output."
    )
    return parser.parse_args()


def main():
    """Entrypoint for the squawk CLI."""
    args = parse_args()
    database = SquawkDatabase()
    lookup = database.lookup(args.code)

    if args.as_json:
        print(json.dumps(lookup, indent=2))
    else:
        print(database.format_summary(lookup, verbose=args.verbose))

    return 0 if lookup["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
