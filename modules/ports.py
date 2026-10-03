import socket


COMMON_PORTS = [
    21,
    22,
    25,
    53,
    80,
    110,
    143,
    443,
    465,
    587,
    993,
    995,
    8080,
    8443
]


def check_ports(hostname):

    results = []

    for port in COMMON_PORTS:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.5)

        try:

            if sock.connect_ex(
                (hostname, port)
            ) == 0:

                results.append(port)

        except Exception:
            pass

        finally:
            sock.close()

    return results
