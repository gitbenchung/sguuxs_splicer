# sguuxs_splicer

A finite-state morphological analyser for the Sgüüx̱s language implemented in foma, adapted from [caforbes](<https://github.com/caforbes/git_fst>) Gitxsan version.

The Sgüüx̱s language (Sgüümḵ or Southern Tsimshian) is part of the linguistic and cultural heritage of the Gidestsu (Kitasoo) and Gitga'ata peoples in Klemtu and Hartley Bay, respectively. This resource was created out of respect for that heritage in collaboration with the Kitasoo, and by accessing this resource, you agree to treat that heritage and the Gidestsu and Gitga'ata peoples with respect.

This resource is available under the [Creative Commons Attribution No-Commercial 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/). You are welcome to use this resource for educational purposes and contribute to its development. Commercial use of this resource is prohibited.

I have written this README in a more casual fashion than most programming documentation. This choice is meant to try to make this package more accessible to new programmers and others who would like to replicate this tool for language revitalization uses themselves.

# How to Use

## Getting Started

### Docker Method (Recommended)

You will need to have both [foma](https://fomafst.github.io/morphtut.html) and [Python](https://www.python.org/downloads/) (Version 3.12.8 at least) installed to use this tool.

For best results, I have found to use a [Docker](https://docs.docker.com/engine/install/) workaround. You will likely need to make a Docker account too.

Unfortunately, [foma](https://fomafst.github.io/morphtut.html) does not have that robust of step-by-step instructions for new coders. If you are experiencing trouble running foma & Python locally, download and install Docker instead.

To open the package in Docker, you need to run it in a Container:

Use the command in Docker to locate wherever you keep the splicer locally as a repository:

> `cd [FILE_PATH]`

*cd* stands for 'c(hange) d(irectory)', so this command is telling Docker where we want to access our information.

Next, run:

> `docker build -t sguuxs_splicer .`

*build -t* means 'build -t(ag)'. The tag specifies what you want to build called the Image. In this case, we want to create an image called `sguuxs_splicer` using the files in the current location (called `.`).

Next, open a Python shell with `sguuxs_splicer` loaded and run:

> `docker run -it sguuxs_splicer`

*run -it* means 'run (an) -i(nteractive)t(erminal)'. You have already built the tool; now you want to test and play with it.

### Locally with Python & Foma

You should also be able to run this tool locally in your terminal without Docker. This works best on the Linux OS. However, I had issues with getting the foma subprocess to allow me to run it while using Python in Windows/Powershell. If you want to try this method, first open Command Prompt and copy the path for wherever you keep the `sguuxs_splicer` repository on your computer by inputting:

> `cd [FILE_PATH]`

Next, run Python. You can just type `python` in the next line and run it. You will need to then `import src`.

*import src* means 'import the `src` folder (source)'. This source contains the information you will need to run anything including the grammar paradigms and dictionary of words.

After importing `src' you will need to import foma as a subprocess. Try:

> `import subprocess`\
> `foma = subprocess.Popen([FILE_PATH-where-foma.exe.is...])`

Note: You will need to replace all the backslashes '\' with double backslashes '\\' in the file path.

What *subprocess.Popen()* does is create a pipe (or a means to run this other program in Python), which is defined by the file path you add into the parantheses '()'. Theoretically, it should allow you to run the package (i.e., `sguuxs_splicer`) in Python with foma.

If you experience difficulties with this method (e.g., everything is running correctly, but you can't input anything into `foma[0]:`), then use the Docker work around.

## Import the Right JSON

### Loading the Right Parser

Once the splicer is running in the Docker container, use this command:
> `fst =  src.Parser(src.FULL_SGX)`

**Note: FULL_SGX is case-sensitive**

This command takes the fst (finite-state transducer aka the transformational code to take our language and get a result) and tells the tool that ther *src* or 'source' for the Parser is the source, full_sgx.json. (`FULL_SGX` is a shortcut to get to that JSON file.) This JSON file is the keystone piece that connects our alternation rules, dictionary, and paradigms together to run.

As of 2025-03-06, you do not need to specify the configuration. You can input:
> `fst =  src.Parser()` # this command will load the preset Sgüüx̱s Parser code.

## Run the Tool

**The functions are spelled in the American English format with a 'z'.**

### Command: Analyze (aka What is this?) or Generate (aka Make this!)

When you `analyze`, the tool will take the input and derive a morphological gloss from the lexical and inflectional units stored in the dictionary and lexc files.
> Input: fst.analyze("waa")\
> Output: ['waa+N']

When you `generate`, the tool will take the input and derive a surface from from the lexical and inflectional units you provide.
> Input: fst.generate("w$aa+N-2PL.II")\
> Output: ['waasm']

**Note: You have to add the Parts of Speech (POS) and inflectional units in the way the tool understands them for Output to render:**
> +2PL.II = 2nd Person Plural, Series II Suffixes\
> +2ndPL.II ≠ Error

### Command: Lemmatize (aka What is base word?)

When you `lemmatize`, the tool will try to identify the possible stem forms from the input. The splicer will work backwards following the rules to break down a surface form to match it with something in the dictionary.
> Input: fst.lemmatize("waasm")\
> Output: ['waa+N']

# If Something Goes Wrong

Don't panic.
If you are using Docker, it is recommended to open a Bash to inspect errors or crashes in this terminal. After running:
> `docker build -t sguuxs_splicer .`

Next, run: 
> `docker run -it --rm sguuxs_splicer bash`

*docker run -it --rm sguuxs_splicer bash* means 'with Docker, run an -i(nteractive)t(erminal) --rm (delete it once it is closed) from sguuxs_splicer in a **B**ourne-**A**gain **SH**ell'.

A **bash** is allows you to monitor the coding processes in a log in the shell as they run. For example, troubleshooting is much easier if you can spot where code is crashing to debug later.

Once the bash is running, you will see a new prompt appear that looks like: *root@dd970a672a10:/app#*

Run python, import src, and then load the Parser in this order as the tool is built:
> `python`\
> `import src`\
> `fst=src.Parser()`

Then, use the *exit()* command to return to the *:/app#* stage, unless you want to play around with the Parser still.

Once it is loaded and saved, by exiting, you can inspect the lexc files and foma file for errors.

### Check the lexc files
After following the steps above, to inspect the lexc files that structure your paradigms input:
> `cat fst/foma/sgx_full.txt`

*cat fst/foma/sgx_full.txt* will cat (or concatenate), in this context *read*, the specified lexc (text) file and print it for you to review.

You will be able to read all your Lexicon entries and paradigms as compiled by the JSON. If parts of the Lexicon or paradigms are missing or mislabeled, it may mean that they are uninterpretably coded or that the JSON is misconfigured.

To inspect the alternation rules, input:
> `cat fst/foma/sgx_full.foma`

*cat fst/foma/sgx_full.foma* will cat (or concatenate), in this context *read*, the foma file and print it for you to review.

You will be able to see how your rules are structured and if the syntax is written as expected/correctly.

### Check foma file

Open foma:
> `foma`

You should be greeted with a new prompt that reads:
> `foma[0]:`

In this line, enter:
> `source fst/foma/sgx_full.foma`

*source fst/foma/sgx_full.foma* will use the source of the foma file and build and run your defined states, arcs, and paths, establishing the formalism that the Lexicon runs through.

If there are errors (e.g., cannot build the Lexicon from the lexc files, unreadable characters, misconfigured rules etc.), foma will abort at the stage it encounters the first crash. By tracing back one's steps, it is possible to diagnose and debug from the crash site.

A successful run should end with an final Output line like:
> `Writing to file /app/fst/foma/sgx_full.fomabin.`

## Current Lexicon Available

As of the last version update, I recommend testing with the following nominal lexicon with the *possessive Series II suffixes*:
|Sgüüx̱s      |Stressed Forms ($) |Surface Form | English  |
|------------|:-----------------:|:----------:|:----------:|
|nts'i'its|nts'$i'its |	nts'i'its | grandmother |
|nts'iidz|  nts'$iidz| nts'iidz| grandmother | 
|niya'ay|	n$iya'ay | niya'ay|	grandfather | 
|noo| n$oo|noo| mom |
|noho| n$oho| noho| mom |
|nigwaat|	n$igwaat|	nigwaat| father | 
|łmkdii|	łmkd$ii| łmkdii | sibling (either gender) |
|hana'ax_|h$ana'ax_ | hana'ax̱ | woman  
|'yaxwt| 'y$axwt|	'yaxwt| man |
|łgutx_a'oo|	łg$utx_a'oo| łgutx̱a'oo | cousin |
|naks|	naks|	n$aks | spouse | 
|kap|	kap|	k$ap | cup |
|daala|	d$aala| daala | dollar; money |
|waa|	w$aa| waa|	name | 
|waalp| w$aalp | waalp|	house | 
|waap| w$aap | waap| house | 

**Why the dollar ($) sign and underscore (_) next to letter?**
foma uses this $ symbol to mark stress; it precedes the character that should have the initial stress. foma also needs to read input to generate grammatical Output in a way it understands. The underscore is needed for some orthographs (special characters). foma reads the underscore better in this order: x_ [x̱].

When foma lemmatizes and analyzes Input, it also uses these symbols and rewrites the language with underscores to the right side of their letters. However, it cleans up the Output before it delivers it to you in these cases. It also will clean up the word(s) when it generates for you; however, you need to help it in the first step by providing it readable Input.

For use of the ***fst.generate()*** feature, you will need to mark stress on the word and put underscores to the right side of their letters:

> Input: fst.generate("łg$utx_a'oo+N-2PL.II")\
> Output: ['łgutx̱a'oosm']

For ***fst.lemmatize*** & ***fst.analyze***, you can input the word without symbols and the characters *with* the underscores beneath them as written in the language. 

Additional lexicon and more complex inflection to be added once test files are updated to reflect Sgüüx̱s vocabulary and rules. Current configuration is being transitioned from Gitksan.

# Version

This tool is in the development process. At the moment, it is only suitable for DP/NPs. Future versions will incorporate predicates and other complex morphology.

Last update: 2025-04-10
