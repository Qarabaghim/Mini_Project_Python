import time


def format_time(seconds):

    hours = seconds // 3600

    minutes = (seconds % 3600) // 60

    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"


def countdown(seconds):

    while seconds >= 0:

        print(
            "\rTime Remaining:",
            format_time(seconds),
            end=""
        )

        time.sleep(1)

        seconds -= 1

    print("\nTime's Up!")


def get_time():

    while True:

        try:

            seconds = int(
                input("Enter Time in Seconds: ")
            )

            if seconds > 0:
                return seconds

            print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def main():

    seconds = get_time()

    countdown(seconds)


if __name__ == "__main__":
    main()