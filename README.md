# Squawk Decoder

Small CLI to tell you what a Mode 3/A squawk means—common VFR codes, special-purpose codes, and which U.S. ARTCC owns a block. Data is embedded; no downloads required.

## Usage
- Run commands from the repo root.
- Any code ending in `00` is treated as the full block (e.g., `1300` covers 1300-1377).

### Examples
Summary lookup:
```
$ ./squawk 1200
Squawk 1200
Status: allocation found
Allocations:
  - 1200: Visual Flight Rules (VFR) aircraft that may or may not be in contact with ATC.
ARTCC assignments:
  - none
```

ARTCC block and assignments:
```
$ ./squawk 0700
Squawk 0700
Status: allocation found
Allocations:
  - 0700-0777: External ARTCC code blocks and code subsets, consisting of the discrete codes of the blocks except for the nondiscrete code of the first primary block, which is used as the ARTCC nondiscrete external code if all discrete external codes are assigned.
ARTCC assignments:
  - ZAB (Albuquerque, KZAB) | 0700-0777 | EP-1 | External Departures; Primary code block or subset; order 1
  - ZJX (Jacksonville, KZJX) | 0700-0777 | EP-1 | External Departures; Primary code block or subset; order 1
  - ZME (Memphis, KZME) | 0700-0777 | ES-1 | External Departures; Secondary code block or subset; order 1
  - ZOB (Cleveland, KZOB) | 0700-0777 | ET-3 | External Departures; Tertiary code block or subset; order 3
```

Invalid input hinting:
```
$ ./squawk 8888
Squawk 8888: invalid Mode 3/A (Mode 3/A codes are octal; use digits 0-7 only.)
  Closest known range: 7777 in allocations (distance 1111).
```

JSON output:
```
$ ./squawk 7500 --json
{
  "input": "7500",
  "code": "7500",
  "valid": true,
  "error": null,
  "table_a": [
    {
      "range": "7500",
      "allocation": "Hijack/Unlawful Interference - reserved internationally."
    }
  ],
  "artcc": [],
  "closest": null
}
```

## Files
- `squawk`: Bash wrapper that calls the CLI.
- `squawk_cli.py`: CLI entry point.
- `squawk_data.py`: Embedded data and lookup API.
- `resources/FAA_Order_JO_7110.66G_NBCAP.pdf`: Source order for U.S. beacon code allocations.
- `resources/ARTCC_Location_Identifiers.csv`: ARTCC names with FAA/ICAO identifiers (U.S. centers).
