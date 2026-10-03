import json
import re
from datetime import datetime
from pathlib import Path


def safe_name(value):

    return re.sub(
        r"[^a-zA-Z0-9_.-]",
        "_",
        value
    )


def save_report(target, results):

    output = Path("reports")
    output.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )

    name = safe_name(target)

    filename = (
        output /
        f"{name}-{timestamp}.html"
    )

    data = json.dumps(
        results,
        indent=2,
        ensure_ascii=False
    )

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ZalZala Report</title>
<style>
body {{
    font-family: monospace;
    background: #111;
    color: #eee;
    padding: 30px;
}}
pre {{
    white-space: pre-wrap;
    background: #181818;
    padding: 20px;
    border-radius: 8px;
}}
h1 {{
    color: #ff3333;
}}
</style>
</head>

<body>

<h1>ZALZALA SECURITY REPORT</h1>

<p><b>Target:</b> {target}</p>

<p>
<b>Made by Pakistan ORAKXAI Anonymous</b>
</p>

<pre>{data}</pre>

</body>
</html>
"""

    filename.write_text(
        html,
        encoding="utf-8"
    )

    return str(filename)