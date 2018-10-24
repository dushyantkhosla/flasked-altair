# Flask + Jinja2 + Altair

- In a nutshell, Jinja2 just generates text files dynamically and allows you to generate elaborate web pages that have a complex structure and many dynamic components

**Templates**
- We fill/replace placeholders in *template* files with values passed to it
  - for example, with Flask's `render_template` function
- In addition to boilerplate code, Templates contain *variables*, *expressions* and *tags*
  - Variables get replaced with values when a template is rendered
  - Expressions are used for applying conditional logic/looping constructs
  - Tags control the logic of the template

- **Delimiters**
  - these placeholders represent the parts of the page that are variable and will only be known at runtime.
  - `{% ... %}` for Statements
  - `{{ ... }}` for Expressions to print to the template output
  - `{# ... #}` for Comments not included in the template output
  - `#  ... ##` for Line Statements

- **Variables**
  - Template variables are defined by the context dictionary passed to the template.
  - The attributes or sub-elements of variables are accessible via the dot accessor `.` or via square brackets subscripting `[]`
    - For example, `{{ foo.bar }}` and `{{ foo['bar'] }}`
    - If you try to access an attribute that doesn't exist, you get an empty string if printed/iterated over and an error for all other operations

- **Filters**
  - are used to *modify* variables as `{{ variable | filter_1 | filter_2 ... }}`
  - some filters accept arguments
  - available filters - `abs, attr, batch, capitalize, center, default, dictsort, escape, filesizeformat, first, float, forceescape, format, groupby, indent, int, join, last, length, list, lower, map, max, min, pprint, random, reject, rejectattr, replace, reverse, round, safe, select, selectattr, slice, sort, string, striptags, sum, title, tojson, trim, truncate, unique, upper, urlencode, urlize, wordcount, wordwrap, xmlattr`
  - See [List of Builtin Filters](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters) for definitions

- **Tests**
  - constructed using the `is` keyword and a function
  - can accept arguments
  - for example, `{% if loop.index is divisibleby(3) %}` or `{% extends layout_template if layout_template is defined else 'master.html' %}`
  - available tests - `callable, defined, divisibleby, eq, escaped, even, ge, gt, in, iterable, le, lower, lt, mapping, ne, none, number, odd, sameas, sequence, string, undefined upper`
  - See [List of Builtin Tests](http://jinja.pocoo.org/docs/2.10/templates/#builtin-tests)

- **Whitespace Control**
  - By default, single trailing newlines are stripped and spaces/tabs/newlines are returned as-are
  - Behavior is controlled by the options
    - `trim_blocks` removes the first newline after a template tag  
    - `lstrip_blocks` removes tabs and spaces from the beginning of a line to the start of a block
  - with both options enabled, the block lines are removed and other whitespace is preserved
    - can manually disable the `lstrip_blocks` behavior by putting a plus sign `(+)` at the start of a block
      - for example, `{%+ if something %}yay{% endif %}`
    - whitespaces before or after a block can be removed by using a minus sign `(-)` to the start or end of a block
      - for example,

      ```
      {% for item in seq -%}
        {{ item }}
      {%- endfor %}
      ```

- **Escaping**
  - to use curly braces as a string, try `{{ '{{' }}` or mark the block as `{% raw %} ... {% endraw %}`

- **Template Inheritance**
  - most powerful part of Jinja
  - allows you to build
    - **base** template that contains all the *common elements* of your site and
    - **child** templates that *override* placeholder blocks in the base
  - the `{% block %}` tags define spaces that child templates can fill in
    - put name of the block after the end tag for better readability, as `{% block NAME %} ... {% endblock NAME %}`
    - You can’t define multiple `{% block %}` tags with the same name in the same template.
  - the `{% extends %}` tag tells the engine that this template builds on another, so it first finds that one
    -  it should be the first tag in a child template
  - Example 1: `base.html`, note the *head, title, content, footer* blocks
    ```
    <!DOCTYPE html>
  <html lang="en">
  <head>
      {% block head %}
      <link rel="stylesheet" href="style.css" />
      <title>{% block title %}{% endblock title %} - My Webpage</title>
      {% endblock head %}
  </head>
  <body>
      <div id="content">{% block content %}{% endblock content %}</div>
      <div id="footer">
          {% block footer %}
          &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
          {% endblock footer%}
      </div>
  </body>
  </html>
    ```
  - Example 2: 'child-1.html'
  ```
  {% extends "base.html" %}
  {% block title %}Index{% endblock %}
  {% block head %}
      {{ super() }}
      <style type="text/css">
          .important { color: #336699; }
      </style>
  {% endblock %}
  {% block content %}
      <h1>Index</h1>
      <p class="important">
        Welcome to my awesome homepage.
      </p>
  {% endblock %    
  ```
  - The two templates have matching block statements with name `content`, and this is how `Jinja2` knows how to combine the two templates into one.

- **Block Nesting**
  - Blocks can be nested for more complex layouts.
  - By default, the inner blocks do not have access to the variables available to the outer blocks
  - But you can explicitly specify that variables are available in a block by setting the block to “scoped”
  - For example,
  ```
  {% for item in seq %}
      <li>{% block loop_item scoped %}{{ item }}{% endblock %}</li>
  {% endfor %}  
  ```

- **For Loops**
  - example
  ```
  <h1>Members</h1>
  <ul>
  {% for user in users %}
    <li>{{ user.username|e }}</li>
  {% endfor %}
  </ul>  
  ```
  - Can also iterate over dicts, as `{% for key, value in my_dict.iteritems() %}`
  - Use if- for skipping objects, as `{% for user in users if not user.hidden %}`
  - If an empty sequence was passed, or the sequence was emptied by a previous iteration of the loop, use `else`
  ```
  <ul>
  {% for user in users %}
      <li>{{ user.username|e }}</li>
  {% else %}
      <li><em>no users found</em></li>
  {% endfor %}
  </ul>  
  ```
  - Some special variables are available inside the loop providing metadata
    - available via the dot `.` on the loop variable, ex `loop.index`
    - list of variables - `first, last, cycle, depth, previtem, nextitem`
  ```
  {% for user in users %}
      {%- if loop.index >= 10 %}{% break %}{% endif %}
  {%- endfor %}  
  ```
- **If statements**
  - In the simplest form, you can use it to test if a variable is defined, not empty and not false
  - Example, `{% if users %} {% for i in users %} ... {% endfor %} {% endif %}`
  - Complex logic via `elif`
  ```
  {% if kenny.sick %}
      Kenny is sick.
  {% elif kenny.dead %}
      You killed Kenny!  You bastard!!!
  {% else %}
      Kenny looks okay --- so far
  {% endif %}  
  ```
  - can also be used inline
    - `{% extends layout_template if layout_template is defined else 'master.html' %}`
  - useful for filtering loops

- **Include**
  - useful to include a template and return the rendered contents of that file into the current namespace
  ```
  {% include 'header.html' %}
      Body
  {% include 'footer.html' %}  
  ```

- **Macros**
  - like functions
  - need to be imported, if defined in another file
  - defined as
  ```
  {% macro NAME(PARAMETERS) -%}
    ...
  {%- endmacro %}
  ```
  - Inside macros, you have access to three special variables
    - `varargs` - similar to args in Python, extra positional arguments are collected into a list
    - `kwargs` - all unconsumed keyword arguments are stored here
    - `caller` - name of the caller if the macro was called using a `call` tag

- **Call**
  - Used to pass a macro to another macro using a special `call` block
  - example
  ```
  {% macro render_dialog(title, class='dialog') -%}
      <div class="{{ class }}">
          <h2>{{ title }}</h2>
          <div class="contents">
              {{ caller() }}
          </div>
      </div>
  {%- endmacro %}

  {% call render_dialog('Hello World') %}
      This is a simple dialog rendered by using a macro and
      a call block.
  {% endcall %}  
  ```

- **Filters**
  - allow you to apply regular Jinja2 filters on a block of template data.
  - Just wrap the code in the special `filter` block:
  ```
  {% filter upper %}
      This text becomes uppercase
  {% endfilter %}
  ```

- **Assignments**
  - assign values to variables using `{% set var = val %}`
  - Assignments at top level (globals; i.e., outside of blocks, macros or loops) can be imported by other templates

- **Block Assignments**
  - to capture the contents of a block into a variable name
  - just write the variable name and then everything until {% endset %} is captured.
  - example
  ```
  {% set navigation %}
      <li><a href="/">Index</a>
      <li><a href="/downloads">Downloads</a>
  {% endset %}  
  ```

- **Include**
  - to include a template and return the rendered contents of that file into the current namespace
  - by default, included templates have access to the variables of the active context
  - allowed to mark an include with options such as
  ```
  {% include "sidebar.html" ignore missing %}
  {% include "sidebar.html" ignore missing with context %}
  {% include "sidebar.html" ignore missing without context %}  
  ```
  - can also provide a list of templates that are checked for existence before inclusion.
  ```
  {% include ['page_detailed.html', 'page.html'] %}
  {% include ['special_sidebar.html', 'sidebar.html'] ignore missing %}  
  ```

- **Import**
  - works similarly to the import statements in Python
  - by default, imported templates don’t have access to the current template variables, just the globals
  - two ways to import templates
    - import a complete template into a variable, as `{% import 'forms.html' as forms %}` and then use the dot accessor to use macros/variables defined inside it
    - request specific macros / exported variables from it, as `{% from 'forms.html' import input as input_field, textarea %}`

- **Modifying Import Context Behavior**
  - By default, *included templates are passed the current context* and **imported templates are not**
    - this is because imports, unlike includes, are cached; as imports are often used just as a module that holds macros.
  - This behavior can be changed explicitly: by adding `with context` or `without context` to the import/include directive
  ```
  {% from 'forms.html' import input with context %}
  {% include 'header.html' without context %}  
  ```

- **Literals**
  - basic expressions to create objects with atomic or complex types
  - Everything between two double or single quotes is a **string.**, as `Hello there!`
  - Integers and floating point numbers are created by just writing the number down. as `42` or `3.142`
  - Everything between two square brackets is a list, as `['apples', 'mangoes', 'oranges']`
  - Tuples are like lists that cannot be modified (“immutable”), created as `('apples', 'oranges')`
  - The special constants `true, false`, and `none` are written in lowercase
  - Arithmetic operators (`+ - * / // % **`)
  - Comparison operators (`== != > >= < <=`)
  - Logical operators (`and or not`)
  - Others (`in is | ~ [] .`)

- **Global Functions**
  - [Reference](http://jinja.pocoo.org/docs/2.10/templates/#list-of-global-functions)
  - `range, lipsum, dict`
  - `cycler`
  - `joiner`, used to “join” multiple sections.        
  - `namespace`, creates a new global container that allows attribute assignment using the `{% set %}` tag
    - main purpose of this is to allow carrying a value from within a loop body to an outer scope
  ```
  {% set ns = namespace() %}
  {% set ns.foo = 'bar' %}  
  ```

- **WITH statement**
  - to create a new inner scope.
  - Variables set within this scope are not visible outside of the scope.
  ```
  {% with foo = 42 %}
      ... {{ foo }} ...
  {% endwith %}
  ```

- **Autoescape**
  - activate and deactivate the autoescaping from within the templates.
  ```
  {% autoescape true %}
      Autoescaping is active within this block
  {% endautoescape %}

  {% autoescape false %}
      Autoescaping is inactive within this block
  {% endautoescape %}  
  ```
