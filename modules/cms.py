def detect_cms(web_result):

    body = (
        web_result.get("body_sample", "")
        .lower()
    )

    headers = {
        key.lower(): value.lower()
        for key, value
        in web_result.get("headers", {}).items()
    }

    detected = []

    fingerprints = {
        "WordPress": [
            "wp-content",
            "wp-includes",
            "wordpress"
        ],
        "Drupal": [
            "drupal-settings-json",
            "drupal"
        ],
        "Joomla": [
            "joomla"
        ],
        "Shopify": [
            "cdn.shopify.com",
            "shopify"
        ]
    }

    for name, indicators in fingerprints.items():

        for indicator in indicators:

            if indicator in body:
                detected.append(name)
                break

    server = headers.get("server")

    if server:
        detected.append(
            f"Server: {server}"
        )

    return sorted(set(detected))
