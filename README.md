# Stay In Tarkov Documentation
 
This is the Stay In Tarkov documentation Repo, if you're looking for the docs, go here: https://docs.stayintarkov.com/

# Compiling 

- Install Visual Studio Code
- Install Python
- Clone this project to a local folder
- Open workspace file SITDocs.code-workspace
- Open Terminal 
- `pip install -U sphinx`
- `pip install pyyaml`
- `pip install sphinxcontrib-video`
- `pip install sphinx_rtd_theme`
- Install VSCode Extension `Run on Save` by emeraldwalk
- Restart VSCode
- Open workspace file SITDocs.code-workspace
- Open Terminal
- `cd docs`
- `.\make.bat html`

# Localisation

If you want to help localise Stay In Tarkov, check if the langauge you want to translate is already there, under the Locales folder. If it is you can edit the .po files and make a push request when done, otherwise you'll need to let someone in the Discord know so we can add it.

* If you know how to use Sphinx and Sphinx-Intl to make locale files from the build, you can pull this project and make the locales yourself.