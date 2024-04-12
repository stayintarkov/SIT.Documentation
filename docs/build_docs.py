import os
import subprocess
import yaml

# Define an array with en inside since en will always build
langs = ["en"]

# Create a fucntion that makes a shorthand for the make command as well as setting OS vars
# before execution
def build_doc(version, language):
    os.environ["current_version"] = version
    os.environ["current_language"] = language
    os.environ['SPHINXOPTS'] = "-D language='{}'".format(language)
    subprocess.run("make html", shell=True)

os.environ["build_all_docs"] = str(True)
os.environ["pages_root"] = "https://docs.stayintarkov.com/"

# Create a shorthand for making and moving a directory
def move_dir(src, dst):
  subprocess.run(["mkdir", "-p", dst])
  subprocess.run("mv "+src+'* ' + dst, shell=True)

# List all Langs in the Locales folder for building
langs += os.listdir("locales")

# Iterate over all found languages and build then move each one to it's designated dir
for i in langs:
   build_doc("latest", i)
   move_dir("./build/html/", "../pages/{}".format(i))

# Move the index.html to the root pages directory so it redirects to the en docs
subprocess.run("mv ./templates/index.html ../pages/index.html", shell=True)

# Open the versions files to see what versions to build and what langs they supported, currently commented out as we don't have alternate versions yet#
"""
with open("versions.yaml", "r") as yaml_file:
  docs = yaml.safe_load(yaml_file)
"""

# Loop over all the values and build the versions with their respective language, currently commented out as we don't have alternate versions yet
"""
for version, details in docs.items():
  tag = details.get('tag', '')
  for language in details.get('languages', []): 
    build_doc(version, language)
    move_dir("./build/html/", "../pages/"+version+'/'+language+'/')
"""