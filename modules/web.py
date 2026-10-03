import ssl
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urlparse


class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()


def analyze(url):
    result = {
        "url": url,
        "status": None,
        "server": None,
        "content_type": None,
        "final_url": None,
        "title": None,
        "headers": {}
    }

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ZalZala/0.1 Security Assessment"
        }
    )

    try:
        context = ssl.create_default_context()

        with urllib.request.urlopen(
            request,
            timeout=10,
            context=context
        ) as response:

            body = response.read(200000)

            result["status"] = response.status
            result["final_url"] = response.geturl()
            result["server"] = response.headers.get("Server")
            result["content_type"] = response.headers.get("Content-Type")

            for key, value in response.headers.items():
                result["headers"][key] = value

            if "text/html" in (result["content_type"] or "").lower():
                parser = TitleParser()

                try:
                    parser.feed(body.decode("utf-8", errors="ignore"))
                    result["title"] = parser.title.strip()
                except Exception:
                    pass

    except urllib.error.HTTPError as error:
        result["status"] = error.code
        result["final_url"] = url

    except Exception as error:
        result["error"] = str(error)

    return result
