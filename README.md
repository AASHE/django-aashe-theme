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

If you are using django-compressor, simply use the '_compressed' versions instead:

    <!-- CSS Theme -->
    {% include 'aashe_theme/styles_compressed.html' %}

    <!-- JS Theme -->
    {% include 'aashe_theme/javascript_compressed.html' %}

You may also simply extend the base templates:

    {% extends 'aashe_theme/base.html %}
    
    or
    
    {% extends 'aashe_theme/base_compressed.html %}

These already include the styles and javascript templates, to add additional scripts just extend the css and javascript blocks in your own templates using {{ block.super }}.
