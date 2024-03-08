# m12-draft-class

A collection of scripts with the purpose of automatically generating a draft class for Madden 12 Franchise Mode.

## How to import a custom draft class into Madden 12

This requires a PS3 or Xbox 360 version of Madden 12. I personally tested this using the RPCS3 emulator.

First, save your franchise. If you're using a physical PS3 or Xbox 360, you will need to save onto a flash drive and connect the flash drive to your computer. If you're using an Xbox 360, use [Horizon](https://www.wemod.com/horizon) to extract the relevant data. You can follow some of the steps listed [here](https://forums.operationsports.com/forums/madden-nfl-old-gen-rosters/579625-madden-roster-editor-v1.html) (but do not use Xanthanol's editor for this purpose. Also do not change file extensions to .MC02).

If you're using a PS3, the folder should be named "BLUS30770-FRANCHISE-{FILE NAME}". If you're using an Xbox 360, the save file/folder should be named "FRANCHISE-{FILE NAME}".

Next, you will need to download the [Madden Xtreme DB Editor (MXDBE)](https://www.footballidiot.com/forum/viewtopic.php?t=21400) if you haven't already. I believe this program only works on Windows.

Using MXDBE, find your save file and open "USR-DATA" (no file extension). 

Navigate to record number 170 named "PLAY" and click on it. This table should have 212 fields with a capacity of 3,273 records.

From here, click on "CSV" at the top and then "Export PLAY". **DO NOT RENAME THIS FILE.** Save this file in the same directory as this repo. Keep MXDBE open for now.

In command prompt, navigate to this repo's directory (which should contain all python .py files as well as "USR-DATA - PLAY.csv". 

Run the command `python franchise_gen.py`.

After running, you will notice two files have been added into the directory: "PLAY-UPDATED.csv" and "GUIDE.csv".

In MXDBE, make sure you are still on record 170 PLAY. Click on "CSV" at the top and then "Import PLAY". Find the "PLAY-UPDATED.csv" file from the repo directory and import it. This will take a while to load.

Once it has loaded, go to "File" at the top then "Save". Once MXDBE has saved the file, you can exit MXDBE.

If you're using a physical console, you will have to then inject this file back onto your flash drive using Horizon (360).

Load the franchise file in Madden 12. You can check if this worked in a few ways:

1. By opening "GUIDE.csv" and ensuring the player names are consistent between the CSV and your franchise. (**NOTE: CONTAINS SPOILERS**)
2. By checking if there are exactly 3 players listed as fullbacks, kickers, and punters.
3. If any player in the draft class is 20 years old or over 24.
4. By comparing the draft class to the [Madden 12 Draft Class Guide](https://forums.operationsports.com/forums/madden-nfl-old-gen/508269-spoilers-madden-12-complete-draft-class-guide.html). If the highest rated punter is not in the table of contents, the injection worked successfully.

"GUIDE.csv" contains a list of all players in the draft class with their overall ratings and potential ratings, akin to the Madden 12 Draft Class Guide.

## Known issues

### Pro Bowl Glitch

On occasion, simulating/playing the Pro Bowl will glitch and you might get stuck on the Pro Bowl week.

To fix this, open your franchise file in MXDBE as earlier. **DO NOT REGENERATE THE DRAFT CLASS**. Instead of using record 170 PLAY, navigate to record 185 SCHD. Look for the row where "GATG"=1010 and "GHTG"=1011 (often the second row from the top). This is the Pro Bowl. On this row, change the field value under "SEWN" from 20 to 19. This effectively moves the Pro Bowl a week earleir so you can continue simulating the rest of the season and enter the offseason.

### Overall Ratings

Some positions, namely defensive backs, have incorrectly calculated overall ratings. The issue stems from the source I found that calculates Madden 12 overall ratings. This will only change if I can find a more reliable formula. Otherwise, if you want to ensure all players are rated correctly in-game, just use "Edit Player" on each player you want to correct and save their proper overall ratings.

## Attributions

The formulas for calculating player ratings came from [Xanthanol's Madden Roster Editor](https://forums.operationsports.com/forums/madden-nfl-old-gen-rosters/579625-madden-roster-editor-v1.html).

The randomly generated first names come from [this dataset](https://github.com/hadley/data-baby-names/blob/master/baby-names.csv).

The randomly generated last names come from [this dataset](https://github.com/fivethirtyeight/data/blob/master/most-common-name/surnames.csv).
