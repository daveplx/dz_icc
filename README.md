# dz_icc

Simple script to go through log files of a disctinct (selfmade) format looking for what happened with a certain item at certain coordinates (**I**tem **C**oordinate **C**rawler)

Far from perfect, could be improved in many areas like making code less redundant in places and serializing objects instead of the string-format-split-array shenanigans that are taking place but alas, time is limited and it works.

----
# How to use

1. Download Python with a version of *at least* 3.8 from the official website (https://www.python.org/downloads/)

2. Install it, making sure you select "Add to Path". After you did this, you should be able to open a Powershell/CMD window, type "python --version" and see a version being shown instead of an error akin to "python is not recognized yada yada". If you don't, fix it before going forward (Most likely adding Python to your system PATH)

3. Download the script in this repository. It's called "icc.py" but you can call it however you'd like. Put it somewhere that makes sense to you (C:\scripts\icc\ or something alike if you want to keep it a little bit tidy)

4. Open up a Powershell/CMD window if you haven't already so that you can type the following commands. Move to the directory where your "icc.py" lies. Here's a little trick under Windows 10: In Windows Explorer, hold "Shift" while right-clicking the empty space in the folder and select "Open Powershell window here". Otherwise, learn how to move through directories ("cd" is the command for it)

5. Run "python -m pip install --upgrade pip" (just good practice AFAIK) followed by "pip  install prettytable". Now you have everything installed and ready to run the script.

6. Before actually launching it, open the "icc.py" in a text editor of your choice (notepad *works* but I would recommend at least Notepad++ or something like VSCode, Atom, Sublime that have proper Syntax Highlighting from the get go)

7. Ignoring the very first blob of imports, you can see some variables written in UPPER CASE. These are static variables that you can change before running your script and that it depends on. I will go through them one by one below.
    
    * *First things first, you can put a "#" in front of a line of code to ignore it (comment). When you try things out, simply duplicate a line and # one of them so you can simply go back to how it was*

    * OUT_FILE_NAME defines the name of the txt file that holds your results. No need to change it unless you want to.
    * ALLOWED_COORD_DEVIATION defines how much of a +/- it will accept when looking for things that happened with the item of your choice. If this is 5, an X of "316" that you entered will still lead to a result if the item was moved at ~"321". Can be left as-is.
    * LOG_FILE_NAME defines the name of the log files that are to be searched. This can probably be kept as-is but just in case it ever changes, all you need is turn this knob.
    * DEFAULT_LOG_DIR_PATH is where it gets interesting. Depending on which (OS) drive letter you took when mirroring the GDrive and how exactly you did it, this might have to be changed. You want this to point to the folder where all the subfolders are then contained, which in turn hold the log files. If it's mirrored the "normal" way, you might just have to change the letter at the front of the string. Otherwise you might want to copy&paste from Windows Explorer to this variable and double any "\" (that is because "\" is an escape character). **This is probably the most important variable to look at for you**
    * FOLDERS_ TO_SKIP defines the names of folders that you don't want to look into. There were some issues when "\_current" was being written so the option exists to ignore it. If you want to add more, just make it look like this afterwards: \['\_current', 'foldername2', 'foldername3'\]
    * SKIP_FOLDERS simply enables or disables the abovementioned skipping. Do what you want with is.

8. Run the script by entering the command "python icc.py" in your Powershell/CMD. It should tell you what to do. With nothing else, it just asks for an item name. When you give it an item name and X coordinate as parameters (for example "python icc.py woodaxe 318"), it will go right ahead without prompting. If for some reason you want to search a different log folder without re-writing the script, you can use one of the last two options where you give it a path to search which it will then use instead of DEFAULT_LOG_DIR_PATH. Might be useful if you're looking through logs on the second server but that is less often the case.

9. You should find a "item_coordinate_result.txt" (or whatever your LOG_FILE_NAME is set to) in the folder with "icc.py" that holds your results in a PrettyTable (easier to read)

## Have fun!
