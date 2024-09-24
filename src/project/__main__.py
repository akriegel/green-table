# we big main
import sys
import time
from rich.progress import Progress


def main():
  minutes_on  = int(sys.argv[1])
  minutes_off = int(sys.argv[2])
  num_tomato  = int(sys.argv[3])
  with Progress() as progress:

    task = progress.add_task("tomatoes:", total=num_tomato)

    tomayto(minutes_on)
    progress.update(task, advance=1)
    while not progress.finished:
      tomahto(minutes_off)
      tomayto(minutes_on)
      progress.update(task, advance=1)
  print("lets call the whole thing off!")

def tomayto(minutes: int):
  seconds_remaining = 5 * minutes
  print("you say tom-ay-to!")
  #with Progress() as progress:
  while seconds_remaining >= 0:
  #  while not progress.finished
    print(f"{seconds_remaining}s\r", end="")
    time.sleep(1)
    seconds_remaining -= 1

def tomahto(minutes: int):
  seconds_remaining = 5 * minutes
  print("I say tom-ah-to!")
  while seconds_remaining >= 0:
    print(f"{seconds_remaining}s\r", end="")
    time.sleep(1)
    seconds_remaining -= 1

if __name__ == "__main__":
  main()
