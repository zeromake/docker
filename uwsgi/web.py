app = Flask(__name__)

@app.route('/')
def main():
    return 'Test'
