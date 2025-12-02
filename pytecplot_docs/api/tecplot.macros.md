:::::::::: {.body role="main"}
:::::::: {#macros .section}
# Macros[¶](#macros "Link to this heading"){.headerlink}

- [tecplot.macro](#module-tecplot.macro){#id1 .reference .internal}

- [macro.execute_command()](#macro-execute-command){#id2 .reference
  .internal}

- [macro.execute_extended_command()](#macro-execute-extended-command){#id3
  .reference .internal}

- [macro.execute_file()](#macro-execute-file){#id4 .reference .internal}

- [macro.execute_function()](#macro-execute-function){#id5 .reference
  .internal}

::: {#module-tecplot.macro .section}
[]{#tecplot-macro}

## [tecplot.macro](#id1){.toc-backref role="doc-backlink"}[¶](#module-tecplot.macro "Link to this heading"){.headerlink}
:::

::: {#macro-execute-command .section}
## [macro.execute_command()](#id2){.toc-backref role="doc-backlink"}[¶](#macro-execute-command "Link to this heading"){.headerlink}

[[tecplot.macro.]{.pre}]{.sig-prename .descclassname}[[execute_command]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[command]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/macro.html#execute_command){.reference .internal}[¶](#tecplot.macro.execute_command "Link to this definition"){.headerlink}

:   Runs a series of tecplot macro commands.

    Parameters[:]{.colon}

    :   **command** ([[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}) -- The macro commands to be run.

    ::: {.admonition .warning}
    Warning

    Zero-based Indexing

    It is important to know that all indexing in PyTecplot scripts are
    zero-based. This is a departure from the macro language which is
    one-based. This is to keep with the expectations when working in the
    python language. However, PyTecplot does not modify strings that are
    passed to the Tecplot Engine. This means that one-based indexing
    should be used when running macro commands from python or when using
    [[`execute_equation()`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal}.
    :::

    This command splits the input into individual commands and runs them
    one at a time. See the [Tecplot Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for details about [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external}'s macro language.

    ::: {.admonition .warning}
    Warning

    The \$!VARSET command is not supported. Tecplot Macro variables
    should be converted to Python variables.
    :::

    ::: {.admonition .warning}
    Warning

    Intrinsic variables (that is, variables with pipes such as
    [`|DATASETFNAME|`{.docutils .literal .notranslate}]{.pre}) are not
    supported. If you need to use an intrinsic variable in the macro
    command, add the macro command to a text file and call
    [[`execute_file`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.macro.execute_file "tecplot.macro.execute_file"){.reference
    .internal}.
    :::

    See the [Tecplot Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for more information about raw data and intrinsic
    variables.

    The following command will perform the same operations as the
    [[Hello, World! example]{.std
    .std-ref}](tecplot.session.html#hello-world){.reference .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_command(r'''
        ...   $!ATTACHTEXT
        ...     ANCHORPOS { X = 35 Y = 50 }
        ...     TEXTSHAPE { HEIGHT = 35 }
        ...     TEXT = 'Hello, World!'
        ...   $!EXPORTSETUP EXPORTFNAME = 'hello_world.png'
        ...   $!EXPORT
        ...     EXPORTREGION = CURRENTFRAME
        ... ''')
    :::
    ::::
:::

::: {#macro-execute-extended-command .section}
## [macro.execute_extended_command()](#id3){.toc-backref role="doc-backlink"}[¶](#macro-execute-extended-command "Link to this heading"){.headerlink}

[[tecplot.macro.]{.pre}]{.sig-prename .descclassname}[[execute_extended_command]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[command_processor_id]{.pre}]{.n}*, *[[command]{.pre}]{.n}*, *[[raw_data]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/macro.html#execute_extended_command){.reference .internal}[¶](#tecplot.macro.execute_extended_command "Link to this definition"){.headerlink}

:   Runs a tecplot macro command defined in an addon.

    Parameters[:]{.colon}

    :   - **command_processor_id** ([[`str`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) --

          A unique string used to determine the API to call when an
          extended macro command is processed. API's are provided by
          add-ons or applications that extend the Tecplot macro
          language.

          Typically this will be the name of an add-on or application,
          followed by a version number. For example: 'CFDAnalyzer4'.

          Each application or add-on may provide one or more unique
          command processor ID strings corresponding to different API's,
          or different versions of an API.

          For example, a file converter add-on responsible for
          converting DXF files for Tecplot might provide two versions of
          an API: "DXFCONVERTTOOL-1.2", and "DXFCONVERTTOOL-2.0". In
          that case either of these strings would be passed in the
          *command_processor_id* parameter to indicate the version of
          the API to use.

        - **command** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The command to run.

        - **raw_data** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Raw data required for the command, if any
          (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}).

    ::: {.admonition .warning}
    Warning

    Zero-based Indexing

    It is important to know that all indexing in PyTecplot scripts are
    zero-based. This is a departure from the macro language which is
    one-based. This is to keep with the expectations when working in the
    python language. However, PyTecplot does not modify strings that are
    passed to the Tecplot Engine. This means that one-based indexing
    should be used when running macro commands from python or when using
    [[`execute_equation()`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal}.
    :::

    In general, the command string is formatted prior to being fed into
    the Tecplot Engine so liberal use of whitespace, including
    new-lines, are acceptable.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_extended_command(
        ...     'Multi Frame Manager',
        ...     'TILEFRAMESSQUARE')
    :::
    ::::
:::

::: {#macro-execute-file .section}
## [macro.execute_file()](#id4){.toc-backref role="doc-backlink"}[¶](#macro-execute-file "Link to this heading"){.headerlink}

[[tecplot.macro.]{.pre}]{.sig-prename .descclassname}[[execute_file]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/macro.html#execute_file){.reference .internal}[¶](#tecplot.macro.execute_file "Link to this definition"){.headerlink}

:   Run a macro file.

    Parameters[:]{.colon}

    :   **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
        .external} or [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}) -- The file to be run. (See note below concerning
        absolute and relative paths.)

    ::: {.admonition .warning}
    Warning

    Zero-based Indexing

    It is important to know that all indexing in PyTecplot scripts are
    zero-based. This is a departure from the macro language which is
    one-based. This is to keep with the expectations when working in the
    python language. However, PyTecplot does not modify strings that are
    passed to the Tecplot Engine. This means that one-based indexing
    should be used when running macro commands from python or when using
    [[`execute_equation()`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal}.
    :::

    ::: {.admonition .note}
    Note

    **Absolute and relative paths with PyTecplot**

    Relative paths, when used within the PyTecplot API are always from
    Python's current working directory which can be obtained by calling
    [[`os.getcwd()`{.xref .py .py-func .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/os.html#os.getcwd "(in Python v3.13)"){.reference
    .external}. This is true for batch and [[`connected`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
    .internal} modes. One exception to this is paths within a macro
    command or file which will be relative to the Tecplot Engine's home
    directory, which is typically the [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} installation directory. Finally, when connected to a
    remote (non-local) instance of Tecplot 360, only absolute paths are
    allowed.

    Note that backslashes must be escaped which is especially important
    for windows paths such as [`"C:\\Users"`{.docutils .literal
    .notranslate}]{.pre} or [`"\\\\server\\path"`{.docutils .literal
    .notranslate}]{.pre} which will resolve to [`"C:\Users"`{.docutils
    .literal .notranslate}]{.pre} and [`"\\server\path"`{.docutils
    .literal .notranslate}]{.pre} respectively. Alternatively, one may
    use Python's raw strings: [`r"C:\Users"`{.docutils .literal
    .notranslate}]{.pre} and [`r"\\server\path"`{.docutils .literal
    .notranslate}]{.pre}
    :::

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_file('/path/to/macro_file.mcr')
    :::
    ::::
:::

::: {#macro-execute-function .section}
## [macro.execute_function()](#id5){.toc-backref role="doc-backlink"}[¶](#macro-execute-function "Link to this heading"){.headerlink}

[[tecplot.macro.]{.pre}]{.sig-prename .descclassname}[[execute_function]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[parameters]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/macro.html#execute_function){.reference .internal}[¶](#tecplot.macro.execute_function "Link to this definition"){.headerlink}

:   Runs a macro function.

    Parameters[:]{.colon}

    :   - **name** -- ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}): Name of the macro function to run. This name is
          not case sensitive. Must be a non-zero length [[`str`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}.

        - **parameters** -- ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}): Any parameters which the quick macro requires.
          Pass [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default) for macro functions which require no
          parameters. The parameters are passed as a string which
          includes the parenthesis. For example, if the macro function
          takes a string parameter and int parameter, pass
          **'("string_parameter_name", 2)'** Default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}

    Macro functions must be defined before they are used. Typically they
    are defined in the 'tecplot.mcr' configuration file which is read
    when Tecplot Engine is initialized. Macro functions may also be
    available in the Quick Macro Panel when the Tecplot 360 GUI is
    running.

    ::: {.admonition .note}
    Note

    See the [Tecplot Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for more information about macro functions.
    :::

    Run the "Tile Frames" macro functions. This macro function is
    defined in the file "tecplot.mcr", which is located in the Tecplot
    360 installation directory:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function('Tile Frames')
    :::
    ::::

    Run a macro function named "Calculate" which takes no parameters and
    another macro function called "Display" which takes the name of a
    layout file and an integer as parameters:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.macro.execute_function('Calculate')
        >>> tp.macro.execute_function('Display', '("contour.lay", 2)')
    :::
    ::::
:::
::::::::

::: clearer
:::
::::::::::
