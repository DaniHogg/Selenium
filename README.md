# Selenium Python Automation Project

This repository contains a basic Selenium automation framework using Python and pytest.

## Setup

1. Create and activate virtual environment:

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest -q
```

## Structure

- `requirements.txt` - Python dependencies
- `conftest.py` - pytest fixtures
- `tests/` - example test scripts

## Notes

- Uses `webdriver-manager` to automatically download drivers.
- Example scripts use Chrome and will open browser windows. Ensure Chrome is installed.
# Selenium
