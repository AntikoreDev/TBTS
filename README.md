# TBTS
<div align="center">
	<a href="https://github.com/AntikoreDev/TBTS" onClick = "return false"><img alt = "Repo size" src = "https://img.shields.io/github/repo-size/AntikoreDev/TBTS?style=for-the-badge"></a>
	<a href="https://github.com/AntikoreDev/TBTS/stargazers"><img alt = "Stars" src = "https://img.shields.io/github/stars/AntikoreDev/TBTS?style=for-the-badge"></a>
	<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/AntikoreDev/TBTS/total?style=for-the-badge">
	<br>
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/AntikoreDev/TBTS?style=for-the-badge">
	<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/AntikoreDev/TBTS?style=for-the-badge">
	<img alt="Made in Spain" src="https://img.shields.io/badge/Made%20in-Spain-FF0000?style=for-the-badge&labelColor=FF0000&color=FFFF00">
</div>
<br>
<div align="center"><i>TBTS stands for TBTS better than school</i></div>
<br>

**TBTS** is an open-source terminal-based solo trivia game made in [Python](https://www.python.org/) designed for those big-brained people that get sleepy on computer science classes because everything is so easy/so outdated they can't even afford to care about it.<br>
As this is a terminal-based game, it can be played kinda unnoticed by teachers (at least if you're on a computer science course), and you're going to learn more from this than whatever they're talking on class.

This game is powered by [OpenTDB](https://opentdb.com/) to get questions. I'm not responsible on what's going on there, proceed with caution, buckaroo!

### How to play
Each run is **15** questions, the highest score you can get is `45,000` as you have to be very quick with your answers. Questions itself have 
no time and you can answer whenever you want (though you may not get points at all lol)

## Installation process
You can access to any of the binaries available on this repository at [Releases](https://github.com/AntikoreDev/TBTS/releases) tab

### Running from source
If you're not a fan of binaries, here's a list of instructions on how to build the project from source. Obviously the first thing you have to do is cloning the repository on your local machine.

Once you've got a local copy of the repository, you may need to install all requirements that proceed. This can be easily done using `pip` by running the following command:
```bash
[sudo] pip install -r requirements.txt
```
Afterwards, you can quickly run the game by using the following command on the root directory of the repository:
```bash
[sudo] py main.py
```

_Note that linux may not have the `py` command itself, you may need to use `python` or `python3` in order to run python_
_Note that `keyboard` module may require of sudo permissions on linux when running from source. You may have to re-install requirements on root depending on your configuration_
_Note that `keyboard` module may have issues installing on linux, you can use `--break-system-packages` at your own risk_

### Building from Source
Using `pyinstaller` after you cloned the repository, you can simply run the following command:

```bash
[sudo] pyinstaller cli.py --onefile --name TBTS --icon=assets/icon.ico
```
This should generate a file at the new generated directory `dist/` named `TBTS.exe` if you're running on Windows.

## Contributing
As long as your additions are not _trivial_ 😉, you can always post an issue and/or making a pull request. Please be polite!

## Donating
If you want to support me and my work, consider to buy me a coffee ✨☕

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/P5P7827IB)
