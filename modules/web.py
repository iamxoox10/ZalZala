import ssl
import urllib.request
import urllib.error
from html.parser import HTMLParser


class TitleParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.title = ""
        self.active = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.active = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.title += data.strip()


def scan_web(url):

    result = {
        "url": url,
        "status": None,
        "final_url": None,
        "server": None,
        "content_type": None,
        "title": None,
        "headers": {},
        "body_sample": ""
    }

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ZalZala/1.0"
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

            result["headers"] = dict(response.headers.items())

            text = body.decode(
                "utf-8",
                errors="ignore"
            )

            result["body_sample"] = text[:50000]

            parser = TitleParser()
            parser.feed(text)

            result["title"] = parser.title.strip()

    except urllib.error.HTTPError as e:

        result["status"] = e.code
        result["error"] = str(e)

    except Exception as e:

        result["error"] = str(e)

    return result