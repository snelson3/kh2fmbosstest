This is a Python script meant to help reduce friction when it comes to testing Boss Replacement codes in Kingdom Hearts 2 Final Mix, with the goal of gathering information to improve/stabilize the boss randomizer created by Valaxor

Many thanks to SonicShadowSilver2 for having detailed pastebins of information on KH2FM, as well as Valaxor for creating his randomizer and having the code for that be open source.

## Known Issues

There are a few bosses that softlock or crash when teleporting to them using the codes this script generates, I haven't been able to figure out why. They hopefully will load properly when you go to them normally in the game (this workaround was only tested with Pete (Past))

* teleporting to Hades 2nd visit & Paradox cup doesn't work
* Replacing any of the STT Day 4 fights will result in a crash
* Teleporting to the Volcanic Lord/Blizzard Lord fight softlocks
* Teleporting to Sephiroth will hard crash PCSX
* Teleporting to Riku? fight will softlock
* Teleporting to Pete (Past) will softlock

## Installation

First make sure to have set up an environment for Valaxor's Randomizer (if you are reading this you probably have done this)

Easy
Make sure to have the Anaconda Python installed
Download the release for this project (https://github.com/snelson3/kh2fmbosstest/releases/tag/v1.0), and unzip the contents into the pcsx folder

Hard
Clone this repository
Change the out_fn path to be wherever your pcsx cheats folder is

## Usage

The easiest way to use this helper is to open the jupyter notebook, and make changes to the existing cell and run it

By default the cell only replaces the specified original boss with another specified new boss (these id numbers correspond with the row number where the boss is listed in bosstable.csv).
It will also enable a code where holding R2 while doing a level transition will load the replaced boss fight, although you can also test without doing this (there is an option to disable this code from being added)

There are a number of commented lines which apply extra codes, which can be helpful in preparing a save file for testing, or if you are bad at fighting the bosses and don't want that to hinder testing

If you are interesting in helping complete testing of the different boss replacement options (there are 3-5 thousand, although large swaths of that are unimportant/redundant), visit this google doc for instructions (https://docs.google.com/spreadsheets/d/1XgqwB4SrBDu5nxFoXYipn-pvP0Z_6b7QRIk7aH1ObSQ/edit?usp=sharing)

If you have any problems with this script (most likely issues will be incorrect values in the bosstable.csv), feel free to create a github issue or DM me (thundrio) in the KH2 Rando Discord