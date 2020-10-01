import argparse

from djm_client import client


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="The IP of the expose backend api.", default="127.0.0.1",)
    parser.add_argument("--port", help="The PORT of the expose backend api.", default="8000")
    args = parser.parse_args()

    api_ip = args.host
    port = args.port


    app = client.MainCmdLine()
    app.cmdloop()

    