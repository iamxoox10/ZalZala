def discover_from_certificate_data(data):
    """
    Extract hostnames from certificate/transparency
    data supplied by an authorized workflow.
    """

    names = set()

    for item in data:
        if isinstance(item, str):
            names.add(item.strip())

    return sorted(
        name for name in names
        if name
    )
