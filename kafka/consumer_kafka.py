from __future__ import annotations

from confluent_kafka import Consumer

c = Consumer(
    {
        "bootstrap.servers": "localhost:9093",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)

c.subscribe(["mytopic"])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    print("Received message: {}".format(msg.value().decode("utf-8")))

c.close()
