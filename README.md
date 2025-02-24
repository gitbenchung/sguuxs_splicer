# sguuxs_splicer
A finite-state morphological analyser for the Sgüüx̣s language implemented in foma, adapted from [caforbes](<https://github.com/caforbes/git_fst>) Gitxsan version.

The Sgüüx̣s language (Sgüümk or Southern Tsimshian) is part of the linguistic and cultural heritage of the Gidestsu (Kitasoo) and Gitga'ata peoples in Klemtu and Hartley Bay, respectively. This resource was created out of respect for that heritage in collaboration with the Kitasoo, and by accessing this resource, you agree to treat that heritage and the Gidestsu and Gitga'ata peoples with respect.

This resource is available under the [Creative Commons Attribution No-Commercial 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/). You are welcome to use this resource for educational purposes and contribute to its development. Commercial use of this resource is prohibited.

I have written this README in a more casual fashion than most programming documentation. This choice is meant to try to make this package more accessible to new programmers and others who would like to replicate this tool for language revitalization uses themselves.
# How to Use
## Getting Started
### Docker Method (Recommended)
You will need to have both [foma](https://fomafst.github.io/morphtut.html) and [Python](https://www.python.org/downloads/) (Version 3.12.8 at least) installed to use this tool.

For best results, I have found to use a [Docker](https://docs.docker.com/engine/install/) work around. You will likely need to make a Docker account too.

Unfortunately, [foma](https://fomafst.github.io/morphtut.html) does not have that robust of step-by-step instructions for new coders. If you are experiencing trouble running foma & Python locally, download and install Docker instead.

To open the package in Docker, you need to run it in a Container:

> `docker build -t sguuxs_splicer .`

*build -t* means 'build -t(ag)'. The tag specifies what you want to build called the Image. In this case, we want to open `sguuxs_splicer`.

Next, open a Python shell with `sguuxs_splicer` loaded and run: 

> `docker run -it sguuxs_splicer`

*run -it* means 'run (an) -i(nteractive)t(erminal)'. You have already built the tool; now you want to test and play with it.

### Locally with Python & Foma
You should also be able to run this tool locally in a Terminal. However, I had issues with getting the foma subprocess to allow me to run it while using Python. If you want to try this method, first open Command Prompt and copy the path for wherever you keep the `sguuxs_splicer` repository on your computer by inputting:

> `cd [FILE_PATH]`

Next, run Python. You can just type `python` in the next line and run it. You will need to then `import src`.

*import src* means 'import the source'. This source contains the information you will need to run anything including the grammar paradigms and dictionary of words.

After importing `src' you will need to import foma as a subprocess. Try:

> `import subprocess`\
> `foma = subprocess.Popen([FILE_PATH-where-foma.exe.is...])`

Note: You will need to replace all the backslashes '\' with double backslashes '\\' in the file path.
What *subprocess.Popen()* does is creates a pipe (or means to fun this other program in Python), which is defined by the file path you add into the parantheses '()'. Theoretically, it should allow you to run the package (i.e., `sguuxs_splicer`) in Python with foma.

If you experience difficulties with this method (e.g., everything is running correctly, but you can't input anything into `foma[0]:`), then use the Docker work around.

# Version
This tool is in the development process. At the moment, it is only suitable for DP/NP morphology. Future versions will incorporate predicates and other complex morphology.

Last update: 2025-02-06
