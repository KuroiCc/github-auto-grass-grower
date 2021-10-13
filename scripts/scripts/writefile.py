from datetime import datetime
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    text = datetime.now().strftime("%Y-%m-%d %X") + "\n"

    with open(path, "a") as file:
        file.write(text)
