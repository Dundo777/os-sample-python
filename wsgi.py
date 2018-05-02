from flask import Flask
from kafka import KafkaProducer


application = Flask(__name__)

@application.route("/")
def hello():
    producer = KafkaProducer(bootstrap_servers='apache-kafka:9092')
    for i in range(100):
        txt = "Hiii " + str(i)
        producer.send('test', bytes(txt.encode('ASCII')))
    producer.flush()
    return "OpenShift Hello World!"

if __name__ == "__main__":
    application.run()
