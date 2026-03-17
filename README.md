# System Operations Toolkit

A collection of Python CLI security and operations tools I made to understand scripting.

## Tools

- **Log Parser** — parses server logs, extracts errors and warnings, outputs a JSON report
- **Port Scanner** — checks which TCP ports are open on a host
- **DNS Lookup** — queries A, MX, and TXT DNS records for any domain
- **API Client** — looks up a GitHub user and their top repositories

## Installation
```bash
git clone https://github.com/qaicore/sysops-toolkit.git
cd sysops-toolkit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

**Log Parser**
```bash
python tools/log_parser.py --file sample_data/sample.log --output report.json
```

**Port Scanner**
```bash
python tools/port_scanner.py --host google.com --ports 80,443,9999
```

**DNS Lookup**
```bash
python tools/dns_lookup.py --domain google.com --type MX
```

**GitHub API Client**
```bash
python tools/api_client.py --user torvalds
```

## Running Tests
```bash
python -m pytest tests/ -v
```