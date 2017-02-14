# TermClicker

No more copy/pasting commands when you are delivering demos to your audience, this can lead you to human mistakes, typos, confusion and undesirable stuff you don't want in your demo session. TermClicke loads commands from a text file and input them on your terminal, line by line, every time you press your clicker button. It's not a Term simulator.

## Requirements

*TermClicker* requires you to use [iTerm], or any other Terminal application that supports running co-processes whenever you press a key on your keyboard.

## Configuration

Clone the repository into a folder, open your [iTerm] App, go to Preferences > Keys, add a new Keymapping like the image below, specifying the `itermprint.py` location followed by your commands file. Usually we choose the *Page Down* key because this is the key that clickers passes to the OS when you press the buttons.

![TermClicker Configuration on iTerm](https://s3.amazonaws.com/freitasrtempfiles/TermClickeriTermConfig.png)

`/Users/freitasr/itermprint.py <commandsfile>`

### The commandsfile

Where `<commandsfile>` is the command list you want to input. You can create a text file and put the commands in it separated by line break. The first line of this file has to contain the index.

The index is an integer, that integer has to correspond to the line number you want to have the first command executed.

## Caveats and observations

Since the commands will be executed on a non-interactive way, make sure that no 




[iTerm]: https://www.iterm2.com/
