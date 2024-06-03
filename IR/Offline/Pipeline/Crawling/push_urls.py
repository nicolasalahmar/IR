import redis

r = redis.StrictRedis.from_url(
    'redis://default:PDs1KEXQm0FhdqSUp52fk3ROVMiR2vGk@redis-10178.c284.us-east1-2.gce.redns.redis-cloud.com:10178')

f = open('collected_urls', 'r')
start_urls = f.readlines();
start_urls = [url.strip() for url in start_urls]
for url in start_urls:
    r.lpush('ir_crawler:start_urls', url)
