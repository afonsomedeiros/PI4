from CONST import DEBUG, RELOADER
from api import create_app


def main():
    app = create_app()
    app.run(debug=DEBUG, reloader=RELOADER)

if __name__ == '__main__':
    main()