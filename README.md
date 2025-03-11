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

As of 2025-03-06, be sure to specify the configuration. Do not input:
> `fst =  src.Parser()` # this command will load the most complete fst file

This method is not recommended as there are two jsons in the package: the *full_sgx.json* and the *full_dialectal.json*. The latter json is the mother file of the Sgüüx̣s one and is configured for Gitxsan. In this development stage, this other json is kept for reference. As it is more complete than the Sgüüx̣s one, it may run automatically if the command is unspecified. In later stages, the command will be runnable without specification once the Sgüüx̣s json is fuller and the Gitxsan one is removed.

## Run the Tool

**The functions are spelled in the American English format with a 'z'.**

### Command: Analyze (aka What is this?) or Generate (aka Make this!)

When you `analyze`, the tool will take the input and derive a morphological gloss from the lexical and inflectional units stored in the dictionary and lexc files.
> Input: fst.analyze("waap")\
> Output: ['waap+N']

When you `generate`, the tool will take the input and derive a surface from from the lexical and inflectional units you provide.
> Input: fst.generate("waap+2PL.II")\
> Output: ['na waapsm']

**Note: You have to add the Parts of Speech (POS) and inflectional units in the way the tool understands them for Output to render:**
> +2PL.II = 2nd Person Plural, Series II Suffixes\
> +2ndPL.II ≠ Error

### Command: Lemmatize (aka What is base word?)

When you `lemmatize`, the tool will try to identify the possible stem forms from the input. The splicer will work backwards following the rules to break down a surface form to match it with something in the dictionary.
> Input: fst.lemmatize("na waalbm")\
> Output: ['waap+N']

# Version

This tool is in the development process. At the moment, it is only suitable for DP/NPs. Future versions will incorporate predicates and other complex morphology.

Last update: 2025-03-06
