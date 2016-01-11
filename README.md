# django-aashe-theme
Unify, themed for AASHE

The unify theme's core theme is made available as a django app with accessible
static files and a custom scss override file.

## Installation

Add the repo to your requirements.txt:

Add to `INSTALLED_APPS`:

    'aashe_theme',

## Usage

Simply add the theme to your templates:

    <!-- CSS Theme -->
    {% include 'aashe_theme/styles.html' %}

    <!-- JS Theme -->
    {% include 'aashe_theme/javascript.html' %}
