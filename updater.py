import os
import sys
from threading import Thread, currentThread
import json
from kafka import KafkaConsumer
import django


def consumer(canonical_source):
    from Sync.models import CanonicalUpdate, ENUM_UpdateStatus
    
    consumer = KafkaConsumer(canonical_source.name,

                            bootstrap_servers=['localhost:9092'])
    print( f"Subscribed to { canonical_source.name }" )
    
    done = False
    current_thread = currentThread()
    while not getattr(current_thread, "done", False):
        message = next(consumer)
        print ("%s:%d:%d: key=%s value=%s" % (  message.topic, message.partition,
                                                message.offset, message.key,
                                                message.value.decode('utf-8')))

        update = CanonicalUpdate(canonical_source=canonical_source, status=ENUM_UpdateStatus.IN_PROGRESS, json=json.loads(message.value))
        update.save()


def setup():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitchen_sync.settings')
    django.setup()


def main():
    from Sync.models import CanonicalSource

    sources = CanonicalSource.objects.all()
    threads = []
    done = False
    for source in sources:
        thread = Thread(target=consumer, args=(source,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    setup()
    main()
