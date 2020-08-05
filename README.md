This is a Python script meant to help reduce friction when it comes to testing Boss Replacement codes in Kingdom Hearts 2 Final Mix, with the goal of helping improve/stabilize the boss randomizer created by Valaxor

Many thanks to SonicShadowSilver2 for having detailed pastebins of information on KH2FM, as well as Valaxor for creating his randomizer and having the code for that be open source.

## Installation

Easy
Make sure to have the Anaconda Python installed
Download the release for this project (), and unzip the contents into the pcsx folder

Hard
Clone this repository
Change the out_fn path to be wherever your pcsx cheats folder is

## Usage

The easiest way to use this helper is to open the jupyter notebook, and make changes to the existing cell and run it

By default the cell only replaces the specified original boss with another specified new boss (these id numbers correspond with the row number where the boss is listed in bosstable.csv)

There are a number of commented lines which apply extra codes, which can be helpful in preparing a save file for testing, or if you are bad at fighting the bosses and don't want that to hinder testing

If you are interesting in helping complete testing of the different boss replacement options (there are 3-5 thousand, although large swaths of that are unimportant/redundant), visit this google doc for instructions (https://docs.google.com/spreadsheets/d/1XgqwB4SrBDu5nxFoXYipn-pvP0Z_6b7QRIk7aH1ObSQ/edit?usp=sharing)