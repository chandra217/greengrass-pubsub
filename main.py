import sys
import time
from src.publisher import Publisher


def main():
    args = sys.argv[1:]
    client = Publisher(args[0])

    while True:
        client.tick()
        time.sleep(1)


if __name__ == "__main__":
    main()
