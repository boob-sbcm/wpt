def main(request, response):
    headers = [("Content-Type", "application/x-blink-test-plugin")]

    return headers, "This is a mock plugin. It does pretty much nothing."
