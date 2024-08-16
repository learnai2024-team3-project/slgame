# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Sphinx 資源
# 1. https://chwang12341.medium.com/d35640a33ffe (繁中)

# ReStructuredText（縮寫為 reST 或 RST）是一種輕量級標記語言，主要用於撰寫技術文檔和生成格式化文件。
# reST 最初是為了 Python 社群開發的，並廣泛應用於 Sphinx 等文檔生成工具，用於生成 HTML、PDF、LaTeX 等格式的文檔。

import os
import sys
sys.path.insert(0, os.path.abspath('../../backend'))

project = 'slgame'
copyright = '2024, Bill Lin et al.'
author = 'Bill Lin et al.'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh-TW'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'haiku'
# 其他主題：
# alabaster, classic, sphinxdoc, scrolls, agogo, 
# traditional, nature, haiku, pyramid, bizstyle, default

html_static_path = ['_static']
