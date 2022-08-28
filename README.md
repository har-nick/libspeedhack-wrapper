# libspeedhack-wrapper

A simple Python script to use with hotkeys to increase/decrease a game's speed to your liking.

## Description

libspeedhack-wrapper takes two arguments, an operation, and an amount.

It runs through libspeedhack's log output to find the game's current speed, does some magic with floats, and echoes it back out automatically.

Notifications are also ran using notify-send. They *should* fail silently if you don't have them installed.

## Getting Started

### Installing

* Git clone, save the raw file, do as you like!

### Executing program

You're best using this alongside some sort of hotkey program, like KDE's Shortcuts.

To increase the speed, use a command like so:

```
python libspeedhack-hotkeys.py -o increase -a 0.5
```

To decrease, simply replace increase with decrease

Minus values haven't been tested. Since oldSpeed and newSpeed values are only added or subtracted, I assume they'd work how you'd expect them to.

## Help

If you find something is wrong, please let me know. Or make a pull request! This is my first ever Python script, so any help goes a long way!

## Todo:

- [ ] Create a silent mode
- [ ] Look at minus values
- [ ] Fix bugs?
