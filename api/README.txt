to run dev flask server:
    macos: 
        export FLASK_APP=main.py
        flask run --port=5000
    linux:
        set FLASK_APP=main.py
        flask run --port=5000

to run test query:
    macos/linux:
        curl http://localhost:5000/test
    or
    go to web browser > http://localhost:5000/test