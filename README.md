# Stopwatch & Countdown Timer

**Completed:** July 30, 2025

A command-line stopwatch and countdown timer built with Python. The program offers two modes for measuring elapsed time or counting down from a specified number of seconds, with a readable display that automatically formats durations into hours, minutes, and seconds.

I built this project at age 16 after one school year of learning programming with Raptor, as a way to put those skills into practice in Python.

## Features

- **Stopwatch mode:** Measure the time between entering `start` and `end`.
- **Countdown mode:** Enter a whole number of seconds and watch the remaining time count down.
- **Readable time formatting:** Shows hours, minutes, and seconds only when needed (for example, `2 min 5 sec`).
- **Input validation:** Prompts again when an invalid mode, command, or countdown value is entered.
- **Menu navigation:** Return to the mode-selection menu after finishing either mode.
- **Exit command:** Type `exit` at supported prompts to close the program.

## Requirements

- Python 3
- No third-party packages — uses Python's built-in `time` and `math` modules.

## Getting Started

1. Download `Stop_Watch.py` from this repository.
2. Open a terminal in the folder containing the file.
3. Run:

   `python Stop_Watch.py`

   On systems that use `python3`, run `python3 Stop_Watch.py` instead.

## How to Use

When the program starts, choose a mode:

- Enter `1` for Stopwatch.
- Enter `2` for Countdown Timer.

### Mode 1 — Stopwatch

1. Enter `1` at the mode-selection prompt.
2. Type `start` and press Enter to begin timing.
3. When you're ready to stop, type `end` and press Enter.
4. The elapsed time is displayed in hours, minutes, and seconds, as applicable.
5. Type `menu` to choose another mode or `exit` to close the program.

**Example output:**

`Time: 1 min 12 sec`

The stopwatch measures from when `start` is accepted until `end` is accepted; it doesn't show a live, continuously updating display while waiting for `end`.

### Mode 2 — Countdown Timer

1. Enter `2` at the mode-selection prompt.
2. Enter a non-negative whole number of seconds (for example, `65`).
3. The program displays the remaining duration once per second.
4. When the countdown finishes, it prints `Time is up!!!`.
5. Type `menu` or `exit` at the completion prompt.

**Example for 3 seconds:**

- `Time: 3 sec`
- `Time: 2 sec`
- `Time: 1 sec`
- `Time is up!!!`

## How It Works

The program uses a main `while True` loop to return to the mode menu after each completed session.

- The `time_function()` function converts a duration in seconds into hours, minutes, and seconds using integer division (`//`) and the remainder operator (`%`). It omits zero-valued units for clearer output.
- **Stopwatch mode** calls `time.time()` at the start and end, calculates the elapsed duration, and normally displays whole seconds. For a duration shorter than one second, it displays a value truncated to one decimal place.
- **Countdown mode** validates the input with `isdigit()`, converts it to an integer, and decrements the counter after each one-second `time.sleep(1)` delay.
- Input loops keep asking for supported commands instead of immediately ending the program when a user makes a mistake.

## Current Limitations

- The countdown cannot be paused or cancelled with an in-program command after it starts; you must stop the running process to interrupt it.
- Entering `0` for the countdown finishes immediately.
- The stopwatch reports elapsed time only when it is stopped, not continuously while it runs.
- Stopwatch results are primarily displayed in whole seconds, so this is not intended for high-precision timing.

**Author:** [Nik Berginc](https://github.com/nikberginc)
