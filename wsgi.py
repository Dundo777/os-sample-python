from flask import Flask
from kafka import KafkaProducer


application = Flask(__name__)

@application.route("/")
def hello():
    producer = KafkaProducer(bootstrap_servers='apache-kafka')
    for i in range(100)
        producer.send('test', bytes("hi " + str(i)))
    return "OpenShift Hello World!"

if __name__ == "__main__":
    application.run()
