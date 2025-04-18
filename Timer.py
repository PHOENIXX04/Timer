import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    try:
        seconds = int(input("Enter time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid number of seconds.")

if __name__ == "__main__":
    main()
