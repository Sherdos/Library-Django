
def icon_url(objects):
    urls = []
    for object in objects:
        url = object.icon.url
        urls.append(url)
    return urls