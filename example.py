from maga import Maga

import logging
logging.basicConfig(level=logging.INFO)


# class Crawler(Maga):
#     async def handler(self, infohash, addr):
#         logging.info(infohash)
#
# crawler = Crawler()
# crawler.run(6881)
#
# from maga import Maga
#
# import logging
#
# logging.basicConfig(level=logging.INFO)
#
#
# class Crawler(Maga):
#     async def handler(self, infohash, addr):
#         logging.info(addr)
#         logging.info(infohash)


# Or, if you want to have more control

class Crawler(Maga):
    async def handle_get_peers(self, infohash, addr):
        logging.info(
            "Receive get peers message from DHT {}. Infohash: {}.".format(
                addr, infohash
            )
        )

    async def handle_announce_peer(self, infohash, addr, peer_addr):
        logging.info(
            "Receive announce peer message from DHT {}. Infohash: {}. Peer address:{}".format(
                addr, infohash, peer_addr
            )
        )


crawler = Crawler()
# Set port to 0 will use a random available port
crawler.run(port=0)