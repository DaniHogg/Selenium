# Selenium Python Automation (Pytest)

This repository contains **focused Selenium automation examples using Python and pytest**.

It is intentionally lightweight and exists to demonstrate:
- Core Selenium concepts
- Pytest fixture usage
- Basic project structure for browser automation

> For a production-ready, CI-enabled automation framework, see:
> **qa-automation-template**
``

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
- `tests/` - test scripts

## Notes

- Uses `webdriver-manager` to automatically download drivers.
- Scripts use Chrome and will open browser windows. Ensure Chrome is installed.



## Purpose of This Repository

This repo intentionally focuses on **Selenium fundamentals** without the additional complexity of full framework abstraction.

It is designed to:
- Show clear, readable Selenium tests
- Demonstrate pytest fixtures via `conftest.py`
- Serve as a reference implementation for small-scale UI automation
