# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Stay In Tarkov'
copyright = '2024, Paulov'
author = 'Paulov'

release = '0.1'
version = '0.5.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

## -- Custom CSS Overrides
html_css_files = ['css/custom.css']

## -- Copy to HTML output
html_static_path = ['_static']