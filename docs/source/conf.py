# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import yaml

project = 'SIT.Documentation'
copyright = '2024, Stay In Tarkov Team'
author = 'Stay In Tarkov Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.video']
templates_path = ['../templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
locale_dirs = ['../locales']
html_scaled_image_link = False

# Same as in build_docs.py, set a lang array, starting with en since that will always build, and adding all other avalible locales to it after
langs = ["en"]
langs += os.listdir("../locales")

# get the environment variable build_all_docs and pages_root
build_all_docs = os.environ.get("build_all_docs", str(True))
pages_root = os.environ.get("pages_root", "https://cyrogon.github.io/TestLocaleSIT")

# Get the current language and version from the OS enviroment variables set in the build_docs.py
current_language = os.environ.get("current_language", "en")
current_version = os.environ.get("current_version", "latest")

# Initialize the HTML context for later use
html_context = {
  'current_language' : current_language,
  'languages' : [],
  'current_version' : current_version,
  'versions' : [],
}

# Checks if we are currently building the latest version, and if so, appends only the lang identifier to the language redirects from all avalible locales
if (current_version == 'latest'):
  for lang in langs:
    html_context['languages'].append([lang, "{}/{}".format(pages_root, lang)])

html_context['versions'].append(['latest', "{}/{}".format(pages_root, current_language)])


# Open the versions.yaml to see what versions to build and what langs they supported, commented out as currently unused
"""
with open("../versions.yaml", "r") as yaml_file:
  docs = yaml.safe_load(yaml_file)

# if the current version isn't latest, append the version to the redirect string of the page, so that it links to the correct locale

if (current_version != 'latest'):
  for language in docs[current_version].get('languages', []):
    html_context['languages'].append([language, "{}/{}/{}".format(pages_root, current_version, language)])



for version, details in docs.items():
  html_context['versions'].append([version, "{}/{}/{}".format(pages_root, version, current_language)])
"""