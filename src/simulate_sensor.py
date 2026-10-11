
import json
import random
import time
from datetime import datetime, timezone

while True:
    sensor = {
        "device_id": "esp32_01",
        "temperature": round(random.uniform(24, 34), 2),
        "humidity": round(random.uniform(45, 85), 2),
        "light": random.randint(100, 1000),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    print(json.dumps(sensor, ensure_ascii=False))
    time.sleep(5)