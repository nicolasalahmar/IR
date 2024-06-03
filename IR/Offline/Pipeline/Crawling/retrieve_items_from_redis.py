import redis
import json
import uuid

from Offline.Helper.ORM import insert_record_from_crawler


def retrieve_data_from_redis():
    redis_url = 'redis://default:PDs1KEXQm0FhdqSUp52fk3ROVMiR2vGk@redis-10178.c284.us-east1-2.gce.redns.redis-cloud.com:10178'
    redis_client = redis.StrictRedis.from_url(redis_url)

    items = redis_client.lrange('ir_crawler:items', 0, -1)
    items = [json.loads(item.decode('utf-8')) for item in items]

    counter = 0
    for item in items:
        if item is not None and 'text' in item and item['text'] and len(item['text'].strip()) > 5:
            unique_id = f"crawler_{uuid.uuid4()}"
            filtered_text = item['text'].replace('\n', ' ').replace('\r', '')
            insert_record_from_crawler(unique_id, filtered_text, model='Corpus')
            counter += 1

    print(f"Count of filtered items: {counter}")


if __name__ == "__main__":
    retrieve_data_from_redis()
