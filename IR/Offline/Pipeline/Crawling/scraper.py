import redis
from scrapy.utils.project import get_project_settings
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from items import TextItem
from itemadapter import ItemAdapter

r = redis.StrictRedis.from_url(
    'redis://default:PDs1KEXQm0FhdqSUp52fk3ROVMiR2vGk@redis-10178.c284.us-east1-2.gce.redns.redis-cloud.com:10178')

r.lpush('ir_crawler:start_urls', 'https://www.bbc.com/')

settings = get_project_settings()


class IrSpider(RedisCrawlSpider):
    name = 'IR-project-spider'

    allowed_domains = ["bbc.com"]
    redis_key = 'ir_crawler:start_urls'

    redis_batch_size = 1
    max_idle_time = 7
    item_count = 0

    rules = (
        Rule(LinkExtractor(allow=(), deny=('tag/',), tags=('a',), unique=True, deny_extensions=(".jpg", ".pdf")),
             callback='parse', follow=True),
    )

    custom_settings = {
        'HTTPCACHE_ENABLED': False,
        'DOWNLOAD_DELAY': 2,
        'SCHEDULER': 'scrapy_redis.scheduler.Scheduler',
        'DUPEFILTER_CLASS': 'scrapy_redis.dupefilter.RFPDupeFilter',
        'REDIS_URL': 'redis://default:PDs1KEXQm0FhdqSUp52fk3ROVMiR2vGk@redis-10178.c284.us-east1-2.gce.redns.redis-cloud.com:10178',
        'SCHEDULER_PERSIST': True,
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 300
        },
        'REDIS_ITEMS_KEY': 'quote_spider:items',
        'REDIS_ITEMS_SERIALIZER': 'json.dumps',
        "CLOSESPIDER_ITEMCOUNT": 100000,
    }

    def parse(self, response):
        for header in response.css('h1, h2, h3, p'):
            item = TextItem()
            item['text'] = header.css('::text').get()
            yield ItemAdapter(item).asdict()
