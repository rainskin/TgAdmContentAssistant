import pymongo

db_client = pymongo.MongoClient()
images_db = db_client['images']
ecchi_col = images_db['reddit ecchi']
hentai_coll = images_db['Hentai']
blacklist = images_db['blacklist']
cute_pics = images_db['Cute_pics']
avatars = images_db['Avatars']
irl_pics = images_db['irl_pics']
zxc = images_db['ZXC']
yuri = images_db['yuri']
bubblecum = images_db['bubblecum']