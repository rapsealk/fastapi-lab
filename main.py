import argparse

import gunicorn
import uvicorn

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='0.0.0.0')
parser.add_argument('--port', type=int, default=8000)
parser.add_argument('--reload', action='store_true')
parser.add_argument('--workers', type=int, default=1)


def main():
    args = parser.parse_args()
    uvicorn.run('src.thread.main:app', host=args.host, port=args.port, reload=args.reload, workers=args.workers)
    # gunicorn src.thread.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000


if __name__ == "__main__":
    main()
