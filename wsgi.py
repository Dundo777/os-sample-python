from flask import Flask
from kafka import KafkaProducer


application = Flask(__name__)

@application.route("/")
def hello():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('test', 'hi!')
    return "OpenShift Hello World!"

if __name__ == "__main__":
    application.run()
