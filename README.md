# Overview

MoviesWebsite is a website that displays the poster art and trailers of your favorite movies.

# Requirements

This website was written using HTML, JavaScript, and Python.  Users should ensure they have Python 2.7 installed on their machine before attempting to run the code.

# Getting and Using the Code

You can download the source code for MoviesWebsite at [this GitHub repo from ToolsForInsight](https://github.com/ToolsForInsight/MoviesWebsite).  You should unzip all the files in this repo to the same directory on your computer.


**Explanation and Use of Important Files**

The files in this repo include:

1. fresh_tomatoes.py
	- This script contains the layout (HTML), styling (CSS), and interactivity (JavaScript) for the website.
	- If you want to change the layout, styling, or interactivity for the entertainment center webpage, you should modify this file.
2. media.py
	- This file defines the different types of media that can be included in the entertainment center website.
	- If you want to modify what a "movie" means in the context of your entertainment center website or add different media to the website (e.g., "book"), you should modify this file.
3. entertainment_center.py
	- This script creates the objects (from media.py) that will be added to the entertainment center website, then runs the script (fresh_tomatoes.py) that creates and opens the website.
	- You can customize the movies added to suit your taste.
	- If you modify the media.py file to include media besides moveis (e.g., books), you should modify this script to include the new type(s) of media.

**Running the Code / Viewing the Website**

To view the website (either as-provided or after making changes), you should:

1. Open the command line.
2. From the command line, navigate to the directory into which you unzipped all the files from this repo.
3. Enter the following command at the command line (without quotes): "python entertainment_center.py"

# License

This software is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl.html).  Accordingly, you are free to run, study, share, and modify this software only if you give these same freedoms to users of *your* implementation of this software.