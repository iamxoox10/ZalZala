import socket


def analyze_dns(hostname):

    result = {
        "hostname": hostname,
        "addresses": []
    }

    try:

        records = socket.getaddrinfo(
            hostname,
            None
        )

        addresses = sorted({
            record[4][0]
            for record in records
        })

        result["addresses"] = addresses

    except Exception as e:

        result["error"] = str(e)

    return result
