def extract_username(url):
    return url.rstrip("/").split("/")[-1]
