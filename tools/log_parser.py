import argparse
import json
from datetime import datetime

datetime.now().isoformat()

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True, help="Input file")
parser.add_argument("--output", default="report.json", help="Output file")
args = parser.parse_args()

filepath = args.file  # now it comes from the command line

findings = []

with open(filepath, "r") as f:
    for line_number, line in enumerate(f, start=1):
        if "ERROR" in line:
            findings.append({"line_number": line_number, "severity": "ERROR", "message": line.split("] ")[-1].strip()})
        if "WARN" in line:
            findings.append({"line_number": line_number, "severity": "WARN", "message": line.split("] ")[-1].strip()})

print(findings)

generation_time = datetime.now().isoformat()
total_errors = sum(1 for f in findings if f["severity"] == "ERROR")
total_warnings = sum(1 for f in findings if f["severity"] == "WARN")
findings_json = json.dumps({
    "generated_at": generation_time,
    "total_errors": total_errors,
    "total_warnings": total_warnings,
    "findings": findings
}, indent=4)

with open(args.output, "w") as f:
    f.write(findings_json)
    
