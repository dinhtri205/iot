import json
import paho.client as mqtt # hoặc paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"📥 Received from MQTT: {data}")
        # Ở đây bạn có thể tích hợp lưu vào InfluxDB Cloud miễn phí hoặc ghi file log CSV tạm thời
    except Exception as e:
        print("Error:", e)

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("broker.hivemq.com", 1883, 60)
mqtt_client.subscribe("iot/sensor/data")

print("🚀 MQTT Collector is running inside GitHub Codespaces...")
mqtt_client.loop_forever()