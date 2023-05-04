from init import *
from apis import *


if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost", port=5000, debug=True, threaded=True)
