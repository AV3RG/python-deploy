import os
import http.server
import socketserver

from http import HTTPStatus
from instagrapi import Client


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self):
        client = Client()
        client.set_proxy("https://GKDM5x6q5UxLsSGc:wifi;in;tripleplay;;@proxy.soax.com:9000")
        # client.load_settings("session.json")
        client.delay_range = [2, 5]
        client.login("rgsp.amm", "ie5HN>Z~f6AGg@#")
        client.dump_settings("session.json")
        client.get_timeline_feed()
        user_id = client.user_id_from_username("iamhardikpahwa")
        medias = client.user_medias(user_id)
        result = {}
        i = 0
        for media in medias:
            if i >= 10:
                break
            paths = []
            if media.media_type == 1:
                paths.append(client.photo_download(media.pk))
            elif media.media_type == 2 and media.product_type == "feed":
                paths.append(client.video_download(media.pk))
            elif media.media_type == 2 and media.product_type == "igtv":
                paths.append(client.video_download(media.pk))
            elif media.media_type == 2 and media.product_type == "clips":
                paths.append(client.video_download(media.pk))
            elif media.media_type == 8:
                for path in client.album_download(media.pk):
                    paths.append(path)
            result[media.pk] = paths
            print(f"https://instagram.com/p/{media.code}/", paths)
            i += 1
