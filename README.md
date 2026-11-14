# Interval Coverage Ledger

Merge overlapping numeric intervals and report total coverage and gaps.

![Sample run from Interval Coverage Ledger](docs/demo.webp)

## Run

Install Python 3.11 or newer. Run these commands from the repository root.

```sh
python app.py sample.json
```

Replace `sample.json` with a JSON file following the same structure. The app prints a JSON report to standard output.

Use finite numbers and strictly increasing start and end endpoints. Intervals are treated as half-open and touching intervals are merged.

## Verify

Run `python check.py` with Python 3.11 or newer after the build step when applicable. The check verifies the bundled scenario and confirms that an invalid input returns an error.
