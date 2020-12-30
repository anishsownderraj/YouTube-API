# YouTube API
Created an application that manipulates data from the YouTube API to provide information not readily available to the user on the YouTube App. By inputting a YouTuber username, the application calculates the total duration of any specified playlist, names the videos in the playlist, and displays the shortest and longest video in the playlist. As a result, the user can decide which playlist will take up most of their time, and decide to watch it or not.

## Getting Started
## Requirements
* `python` 3.x
* `pip`
* [`virtualenv`](https://virtualenv.pypa.io/en/latest/)
## Instructions
1. Clone the Repository using the URL
```sh
$ git clone https://github.com/anishsownderraj/Sudoku-Solver
```
2. Set up an virtual environment(found below)

3. Install the requirements.txt file(found below)

## Create a new virtual environment
The following command creates a new virtual environment named `venv` in the current directory, usually this will be your project's directory.
```sh
$ virtualenv venv
```

## Activate virtual environment
The following commands [activate](https://virtualenv.pypa.io/en/latest/userguide/#activate-script) an existing virtual environment on Windows and Unix systems. The command assume that the virtual environment is named `venv` and that its location is in a subdirectory `path/to/` of the current directory. 
```sh
# Windows (CMD.exe)
$ path\to\venv\Scripts\activate.bat
# Unix
$ source path/to/venv//bin/activate
```
Once the virtual environment has been actiated your console cursor might prepend the name of the virtual environment as shown below.
```sh
$ (venv) echo 'Hello World!'
```

## Deactivate virtual environment
The following command deactivates the current virtual environment, any dependency installed after this command will be installed globally.
```sh
$ (venv) deactivate
```

## Requirements.txt
To install dependencies in the current environment from a `requirements.txt` file the command below can be used.
```sh
$ (venv) pip3 install -r requirements.txt
```
## Tests

### Sample Input #1
```sh
PewDiePie
```
### Sample Output #1
```sh

Enter the username of an Youtuber(Possible suggestions are 'PewDiePie'):
PewDiePie
Cyberpunk Playthrough | Among Us | God of War Playthrough | Ghost of Tsushima Full Playthrough | TLC |
Enter Title of Playlist you want to calculate the duration of:
Cyberpunk Playthrough
Total Duration: 8H 31M 38S
Longest Video of the Playlist is: KEANU TIME ! Cyberpunk Full Playthrough Gameplay Part 3
Shortest Video of the Playlist is: JOJO REFERENCE / Cyberpunk Full Playthrough Gameplay Part 2

```

### Sample Input #2
```sh
LinusTechTips
```

### Sample Output #2
```sh
Enter the username of an Youtuber(Possible suggestions are 'PewDiePie'):
LinusTechTips
PC Tech Support Challenge | Gaming PC Secret Shopper 2 | Virtualization | Intel Extreme Tech Upgrade | Pyramid PC | 
Enter Title of Playlist you want to calculate the duration of:
PC Tech Support Challenge
Total Duration: 5H 23M 47S
Longest Video of the Playlist is: ULTIMATE RGB PC Tech Support Challenge!!
Shortest Video of the Playlist is: ULTIMATE PC Tech Support Challenge - Jayztwocents vs Gamers Nexus
(venv) anishsownderraj@Anishs-MBP Youtube-API % 
```
### Tests of your Own
A YouTuber's username is found at the end of the URL of a YouTubers Home Page
```sh
https://www.youtube.com/user/LinusTechTips
```
Make sure the username follows after 
```sh
/user
```





