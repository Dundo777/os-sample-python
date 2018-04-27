from flask import Flask
from kafka import KafkaProducer


application = Flask(__name__)

@application.route("/")
def hello():
    producer = KafkaProducer(bootstrap_servers='apache-kafka')
    for i in range(100):
        txt = "Hi " + str(i)
        producer.send('test', bytes(txt.encode('ASCII')))
    return "OpenShift Hello World!"

if __name__ == "__main__":
    application.run()
