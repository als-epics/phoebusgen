# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'phoebusgen'
copyright = '2022, Lawrence Berkeley National Laboratory'
author = 'Tynan Ford'

# The full version, including alpha/beta/rc tags
release = '2.3.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.githubpages', 'sphinx_autodoc_typehints']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_options = {
        'members': 'widgets, screen, widget, properties',
        'private-members': 'widgets, screen',
        'inherited-members': 'widgets',
        'exclude-members': '_prettify, _add_action, _add_font_style, _add_rotation_step, _get_font_element, _add_mode, _add_horizontal_alignment, _add_vertical_alignment, _add_file_component, _add_resize_behavior, _add_state, _add_style'
        }


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
