RECOMMENDED_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


def analyze_headers(headers):

    normalized = {
        key.lower(): value
        for key, value in headers.items()
    }

    findings = []

    for header in RECOMMENDED_HEADERS:

        if header.lower() not in normalized:
            findings.append(
                f"Missing: {header}"
            )
        else:
            findings.append(
                f"Present: {header}"
            )

    return findings
