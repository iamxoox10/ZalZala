import socket
import ssl


def analyze_tls(hostname):

    result = {
        "hostname": hostname
    }

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=10
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure:

                result["version"] = secure.version()
                result["cipher"] = secure.cipher()[0]

                certificate = secure.getpeercert()

                result["subject"] = str(
                    certificate.get("subject")
                )

                result["issuer"] = str(
                    certificate.get("issuer")
                )

    except Exception as e:

        result["error"] = str(e)

    return result
