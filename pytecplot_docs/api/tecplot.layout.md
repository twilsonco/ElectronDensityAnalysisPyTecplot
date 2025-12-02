::::::::::::::::::::: {.body role="main"}
::::::::::::::::::: {#layout .section}
# Layout[¶](#layout "Link to this heading"){.headerlink}

- [tecplot.layout](#module-tecplot.layout){#id2 .reference .internal}

- [active_frame()](#active-frame){#id3 .reference .internal}

- [active_page()](#active-page){#id4 .reference .internal}

- [add_page()](#add-page){#id5 .reference .internal}

- [delete_page()](#delete-page){#id6 .reference .internal}

- [next_page()](#next-page){#id7 .reference .internal}

- [new_layout()](#new-layout){#id8 .reference .internal}

- [load_layout()](#load-layout){#id9 .reference .internal}

- [page()](#page){#id10 .reference .internal}

- [pages()](#pages){#id11 .reference .internal}

- [frames()](#frames){#id12 .reference .internal}

- [save_layout()](#save-layout){#id13 .reference .internal}

- [layout.aux_data()](#layout-aux-data){#id14 .reference .internal}

- [Frame](#frame){#id15 .reference .internal}

- [Page](#id1){#id16 .reference .internal}

- [Paper](#paper){#id17 .reference .internal}

::: {#module-tecplot.layout .section}
[]{#tecplot-layout}

## [tecplot.layout](#id2){.toc-backref role="doc-backlink"}[¶](#module-tecplot.layout "Link to this heading"){.headerlink}

Pages, frames and other layout-related operations.

The "layout" consists of a stack of [[`Pages`{.xref .any .py .py-class
.docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
.internal} identified by index or [[`name`{.xref .any .py .py-attr
.docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Page.name "tecplot.layout.Page.name"){.reference
.internal}. Each [[`Page`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
.internal} consists of a single "workspace" which holds a collection of
[[`Frames`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
.internal} that are laid out in relation to an area called the
[[`Paper`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
.internal}.

The Tecplot Engine is guaranteed to have at least one [[`Page`{.xref
.any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
.internal} which is holding onto at least one [[`Frame`{.xref .any .py
.py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
.internal}. It also has the concept of an active [[`Frame`{.xref .any
.py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
.internal} and by extension, an active [[`Page`{.xref .any .py .py-class
.docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
.internal}. Most, if not all operations that require a handle to a
[[`Frame`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
.internal} will use the active [[`Frame`{.xref .any .py .py-class
.docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
.internal} by default. This includes any function that operates on
objects held by a [[`Frame`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
.internal} such as a [[`Cartesian3DFieldPlot`{.xref .any .py .py-class
.docutils .literal
.notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot "tecplot.plot.Cartesian3DFieldPlot"){.reference
.internal} or [[`Dataset`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
.internal}.
:::

::: {#active-frame .section}
## [active_frame()](#id3){.toc-backref role="doc-backlink"}[¶](#active-frame "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[active_frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#active_frame){.reference .internal}[¶](#tecplot.active_frame "Link to this definition"){.headerlink}

:   Returns the active frame.

    Returns[:]{.colon}

    :   [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} -- Currently active frame.
:::

::: {#active-page .section}
## [active_page()](#id4){.toc-backref role="doc-backlink"}[¶](#active-page "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[active_page]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#active_page){.reference .internal}[¶](#tecplot.active_page "Link to this definition"){.headerlink}

:   Returns the currently active page.

    Returns[:]{.colon}

    :   [[`Page`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} -- The currently active page.

    Only one [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} can be active at any given time. As long as the page is
    not deleted (through a call to [[`new_layout`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.new_layout "tecplot.new_layout"){.reference
    .internal} or [[`load_layout`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.load_layout "tecplot.load_layout"){.reference
    .internal} for example) this can be used to bring it back to the
    active state:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        page1 = tecplot.active_page()
        page2 = tecplot.add_page()

        # page2 is now active
        assert page2.active

        # we can bring page1 back to the front:
        page1.activate()
        assert page1.active
    :::
    ::::
:::

::: {#add-page .section}
## [add_page()](#id5){.toc-backref role="doc-backlink"}[¶](#add-page "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[add_page]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#add_page){.reference .internal}[¶](#tecplot.add_page "Link to this definition"){.headerlink}

:   Adds a [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} to the layout.

    Returns[:]{.colon}

    :   [[`Page`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} -- The newly created page.

    This will implicitly activate the newly created page:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        page1 = tecplot.active_page()
        page2 = tecplot.add_page()
        # page2 is now active
        assert page2.active
    :::
    ::::
:::

::: {#delete-page .section}
## [delete_page()](#id6){.toc-backref role="doc-backlink"}[¶](#delete-page "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[delete_page]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[page_to_delete]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#delete_page){.reference .internal}[¶](#tecplot.delete_page "Link to this definition"){.headerlink}

:   Removes a [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} from the layout.

    This will render any [[`Page`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} object pointing to the deleted [[`Page`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} useless. The unique ID will not be used again in the
    active session and it is up to the user to clear the python object
    using [[`The`{.docutils .literal .notranslate}]{.pre}` `{.docutils
    .literal .notranslate}[`del`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`statement`{.docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/reference/simple_stmts.html#del "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.exception import TecplotRuntimeError

        page = tp.add_page()
        tp.delete_page(page)

        next_page = tp.active_page()

        assert page != next_page
        assert not page.active

        try:
            # the page is gone so activating
            # will produce an exception
            page.activate()
        except TecplotRuntimeError as e:
            print(e)

        del page # clear the python object
    :::
    ::::
:::

::: {#next-page .section}
## [next_page()](#id7){.toc-backref role="doc-backlink"}[¶](#next-page "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[next_page]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#next_page){.reference .internal}[¶](#tecplot.next_page "Link to this definition"){.headerlink}

:   Activates and returns the next page.

    Returns[:]{.colon}

    :   [[`layout.Page`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} -- The next page in the layout.

    [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} objects are stored in an ordered stack in the Tecplot
    Engine. This method rotates the stack and returns the resulting
    active [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.layout import next_page

        page1 = tecplot.active_page()
        page2 = tecplot.add_page()
        page3 = next_page()

        # page1 is now the active page
        # and is the same as page3
        assert page1.active
        assert page3 == page1
    :::
    ::::
:::

::: {#new-layout .section}
## [new_layout()](#id8){.toc-backref role="doc-backlink"}[¶](#new-layout "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[new_layout]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#new_layout){.reference .internal}[¶](#tecplot.new_layout "Link to this definition"){.headerlink}

:   Clears the current layout and creates a blank frame.

    This will invalidate any object instances previously obtained:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        frame = tecplot.active_frame()
        tecplot.new_layout()

        # frame object is no longer usable.
        # the following will print:
        #       <class 'ValueError'> 255 is not a valid PlotType
        try:
            frame.plot_type
        except Exception as e:
            print(type(e),e)
    :::
    ::::
:::

::: {#load-layout .section}
## [load_layout()](#id9){.toc-backref role="doc-backlink"}[¶](#load-layout "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[load_layout]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#load_layout){.reference .internal}[¶](#tecplot.load_layout "Link to this definition"){.headerlink}

:   Reads a layout file and replaces the active frame.

    Parameters[:]{.colon}

    :   **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
        .external} or [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}) -- The file name of the layout to be loaded. (See
        note below conerning absolute and relative paths.)

    Raises[:]{.colon}

    :   - [**TecplotOSError**](tecplot.exceptions.html#tecplot.exception.TecplotOSError "tecplot.exception.TecplotOSError"){.reference
          .internal} -- If file can not be found.

        - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- If the file could not be loaded.

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

    This will replace the current layout and therefore will invalidate
    any object instances previously obtained:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot as tp

        frame = tp.active_frame()

        examples = tp.session.tecplot_examples_directory()
        layoutfile = os.path.join(examples, 'SimpleData', 'F18.lay')
        tp.load_layout(layoutfile)

        # frame object is no longer usable.
        # the following will print:
        #       <class 'ValueError'> 255 is not a valid PlotType
        try:
            frame.plot_type
        except Exception as e:
            print(type(e),e)
    :::
    ::::
:::

::: {#page .section}
## [page()](#id10){.toc-backref role="doc-backlink"}[¶](#page "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[page]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#page){.reference .internal}[¶](#tecplot.page "Link to this definition"){.headerlink}

:   Returns the page by name.

    Parameters[:]{.colon}

    :   **pattern** ([[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`re.Pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external}) -- Case-insensitive [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} or a compiled [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} used to match the page by name.

    Returns[:]{.colon}

    :   [[`Page`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} -- The first page identified by *pattern*.

    ::: {.admonition .note}
    Note

    A layout can contain [[`pages`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} with identical names and only the first match found is
    returned. This is not guaranteed to be deterministic and care should
    be taken to have only [[`pages`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} with unique names when this feature is used.
    :::

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        page11 = tecplot.add_page()
        page11.name = 'Page 11'
        page12 = tecplot.add_page()
        page12.name = 'Page 12'
        assert page12 == tecplot.page('Page 1*')
    :::
    ::::
:::

::: {#pages .section}
## [pages()](#id11){.toc-backref role="doc-backlink"}[¶](#pages "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[pages]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#pages){.reference .internal}[¶](#tecplot.pages "Link to this definition"){.headerlink}

:   Yields pages matching a specified pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`re.Pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external}, optional) -- Case-insensitive [[`glob-style`{.xref
        .any .docutils .literal .notranslate}]{.pre}` `{.xref .any
        .docutils .literal .notranslate}[`pattern`{.xref .any .docutils
        .literal .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} or a compiled [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} used to match page names.

    Returns[:]{.colon}

    :   [[`Page`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} -- Generator of pages identified by *pattern* or all
        pages if no *pattern* is specified.

    This function returns a generator which can only be iterated over
    once. It can be converted to a [[`list`{.xref .any .docutils
    .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} for persistence:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        # iterate over all frames in
        # all pages and print their names
        for page in tecplot.pages():
            for frame in page.frames():
                print(frame.name)

        # store a persistent list of pages
        pages = list(tecplot.pages())
    :::
    ::::
:::

::: {#frames .section}
## [frames()](#id12){.toc-backref role="doc-backlink"}[¶](#frames "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[frames]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame_pattern]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[page_pattern]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#frames){.reference .internal}[¶](#tecplot.frames "Link to this definition"){.headerlink}

:   Returns a generator of frames matching the specified pattern.

    Parameters[:]{.colon}

    :   - **frame_pattern** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`re.Pattern`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
          .external}) -- Case-insensitive [[`glob-style`{.xref .any
          .docutils .literal .notranslate}]{.pre}` `{.xref .any
          .docutils .literal .notranslate}[`pattern`{.xref .any
          .docutils .literal .notranslate}]{.pre}` `{.xref .any
          .docutils .literal .notranslate}[`string`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
          .external} or a compiled [[`regex`{.xref .any .docutils
          .literal .notranslate}]{.pre}` `{.xref .any .docutils .literal
          .notranslate}[`pattern`{.xref .any .docutils .literal
          .notranslate}]{.pre}` `{.xref .any .docutils .literal
          .notranslate}[`instance`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
          .external} used to match the frame by name. All frames are
          returned if no pattern is specified.

        - **page_pattern** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`re.Pattern`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
          .external}) -- Case-insensitive [[`glob-style`{.xref .any
          .docutils .literal .notranslate}]{.pre}` `{.xref .any
          .docutils .literal .notranslate}[`pattern`{.xref .any
          .docutils .literal .notranslate}]{.pre}` `{.xref .any
          .docutils .literal .notranslate}[`string`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
          .external} or a compiled [[`regex`{.xref .any .docutils
          .literal .notranslate}]{.pre}` `{.xref .any .docutils .literal
          .notranslate}[`pattern`{.xref .any .docutils .literal
          .notranslate}]{.pre}` `{.xref .any .docutils .literal
          .notranslate}[`instance`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
          .external} used to match the page by name. All pages are
          included if no pattern is specified.

    Returns[:]{.colon}

    :   [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} -- Generator of frames identified by name patterns.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        # print name of all frames on all pages
        for frame in tecplot.frames():
            print(frame.name)
    :::
    ::::
:::

::: {#save-layout .section}
## [save_layout()](#id13){.toc-backref role="doc-backlink"}[¶](#save-layout "Link to this heading"){.headerlink}

[[tecplot.]{.pre}]{.sig-prename .descclassname}[[save_layout]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[include_data]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_preview]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[use_relative_paths]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[post_layout_commands]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[pages]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#save_layout){.reference .internal}[¶](#tecplot.save_layout "Link to this definition"){.headerlink}

:   Writes the current layout to a file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The path to the output filename. (See note
          below conerning absolute and relative paths.)

        - **include_data** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Associated value indicates if the
          layout should be saved as a layout package where the data is
          included with the style information or if it should reference
          linked data. If 'include_data' is None and the filename ends
          with '.lpk', then the file will be saved as a layout package
          file. (default: None)

        - **include_preview** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Associated value indicates if the
          layout package should also include a preview image. This
          argument only applies if the include data option is True.
          (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **use_relative_paths** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Associated value indicates if the
          layout should be saved using relative paths. This argument
          only applies if the include data option is [[`False`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **post_layout_commands** ([[`str`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- A character string containing a set
          of Tecplot macro commands that are appended to the layout or
          layout package file. These can be almost anything and are
          generally used to store add-on specific state information
          using [`$!EXTENDEDCOMMAND`{.docutils .literal
          .notranslate}]{.pre} commands. (default: [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **pages** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Page`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
          .internal} objects, optional) -- If [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, all pages are written to the layout, otherwise the
          specified subset of pages are written. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

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

    ::: {.admonition .note}
    Note

    If you receive an exception with the error message "Journal should
    be valid in all frames", then you must save a data file using
    [[`save_tecplot_ascii`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.save_tecplot_ascii "tecplot.data.save_tecplot_ascii"){.reference
    .internal} or [[`save_tecplot_plt`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.save_tecplot_plt "tecplot.data.save_tecplot_plt"){.reference
    .internal} before saving the layout.
    :::

    In this example, we load an example layout file and then save it as
    a packaged layout file:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot

        examples_dir = tecplot.session.tecplot_examples_directory()
        infile = os.path.join(examples_dir, 'SimpleData', 'F18.lay')

        tecplot.load_layout(infile)
        tecplot.save_layout('output.lpk')
    :::
    ::::
:::

::: {#layout-aux-data .section}
## [layout.aux_data()](#id14){.toc-backref role="doc-backlink"}[¶](#layout-aux-data "Link to this heading"){.headerlink}

[[tecplot.layout.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/layout.html#aux_data){.reference .internal}[¶](#tecplot.layout.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for the current layout.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the entire layout containing
    all frames and datasets currently held by the Tecplot Engine. Such
    data is written to the layout file by default and can be retrieved
    later. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        aux = tp.layout.aux_data()
        aux['info'] = '''        This layout contains a lot of things:
            1. Something
            2. Something else
            3. Also this'''

        '''
        The following will print (including newlines):
            This layout contains a lot of things:
                1. Something
                2. Something else
                3. Also this
        '''
        print(aux['info'])
    :::
    ::::
:::

::: {#frame .section}
## [Frame](#id15){.toc-backref role="doc-backlink"}[¶](#frame "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.layout.]{.pre}]{.sig-prename .descclassname}[[Frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[page]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame){.reference .internal}[¶](#tecplot.layout.Frame "Link to this definition"){.headerlink}

:   [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} object within a [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}, holding onto a [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} and a [[Plot]{.std
    .std-ref}](tecplot.plot.html#plot){.reference .internal}.

    Parameters[:]{.colon}

    :   - **uid** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- This must be a *valid* unique ID
          number pointing internally to a Frame object or [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}. A new [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is created if set to [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}. (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **page** ([[`Page`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
          .internal}, optional) -- The destination [[`Page`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
          .internal} of this newly created [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Page`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

    ::: {.admonition .warning}
    Warning

    Though it is possible to create a [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} object using the constructor, it is usually sufficient to
    obtain a frame through [[`tecplot.active_frame()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.active_frame "tecplot.active_frame"){.reference
    .internal} or [[`Page.frame()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page.frame "tecplot.layout.Page.frame"){.reference
    .internal}. One can also create a [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} using a [[`Page`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} handle with [[`Page.add_frame()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page.add_frame "tecplot.layout.Page.add_frame"){.reference
    .internal}.
    :::

    The concept of the [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} is central to understanding the Tecplot Engine. The
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} is what connects a [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} to a [[Plot]{.std
    .std-ref}](tecplot.plot.html#plot){.reference .internal} handle from
    which one manipulates the desired image as well as accessing the
    attached data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        frame = tecplot.active_frame()

        # will print: 'Frame "Frame 001"'
        print(frame)
    :::
    ::::

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.active "tecplot.layout.Frame.active"){.reference .internal}                                                      Checks if this [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} is active.
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.aux_data "tecplot.layout.Frame.aux_data"){.reference .internal}                                                Auxiliary data for this frame.
      [[`background_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.background_color "tecplot.layout.Frame.background_color"){.reference .internal}                        Color of the background.
      [[`border_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.border_thickness "tecplot.layout.Frame.border_thickness"){.reference .internal}                        The border thickness in units of [[`Frame.size_pos_units`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference .internal}.
      [[`dataset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.dataset "tecplot.layout.Frame.dataset"){.reference .internal}                                                   The [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal} belonging to this Frame.
      [[`has_dataset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.has_dataset "tecplot.layout.Frame.has_dataset"){.reference .internal}                                       [[`bool`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference .external}: Checks to see if the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} as an attached [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}
      [[`header_background_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.header_background_color "tecplot.layout.Frame.header_background_color"){.reference .internal}   The header\'s background color.
      [[`height`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.height "tecplot.layout.Frame.height"){.reference .internal}                                                      The height in units of [[`Frame.size_pos_units`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference .internal}.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.name "tecplot.layout.Frame.name"){.reference .internal}                                                            Returns or sets the name.
      [[`page`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.page "tecplot.layout.Frame.page"){.reference .internal}                                                            The [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal} containing this Frame.
      [[`plot_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.plot_type "tecplot.layout.Frame.plot_type"){.reference .internal}                                             Returns or sets the current plot type.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.position "tecplot.layout.Frame.position"){.reference .internal}                                                [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: [`(x,y)`{.docutils .literal .notranslate}]{.pre} position of the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} in inches.
      [[`show_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.show_border "tecplot.layout.Frame.show_border"){.reference .internal}                                       [[`bool`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference .external}: Show or hide the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}\'s border.
      [[`show_header`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.show_header "tecplot.layout.Frame.show_header"){.reference .internal}                                       [[`bool`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference .external}: Show or hide the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}\'s header in the border.
      [[`size_pos_units`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference .internal}                              The units used for size properties.
      [[`transparent`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.transparent "tecplot.layout.Frame.transparent"){.reference .internal}                                       [[`bool`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference .external}: Use transparency within this [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`width`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.width "tecplot.layout.Frame.width"){.reference .internal}                                                         The width in units of [[`Frame.size_pos_units`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference .internal}.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.activate "tecplot.layout.Frame.activate"){.reference .internal}()                                                                    Causes this [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} to become active.
      [[`activated`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.activated "tecplot.layout.Frame.activated"){.reference .internal}()                                                                 Context for temporarily activating this [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`active_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.active_zones "tecplot.layout.Frame.active_zones"){.reference .internal}(\*zones)                                                 Returns or sets the active [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal}.
      [[`add_circle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_circle "tecplot.layout.Frame.add_circle"){.reference .internal}(center, radius, coord_sys)                                     Place a circle annotation on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_ellipse`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_ellipse "tecplot.layout.Frame.add_ellipse"){.reference .internal}(center, size, coord_sys)                                    Place an ellipse annotation on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_georeferenced_image`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_georeferenced_image "tecplot.layout.Frame.add_georeferenced_image"){.reference .internal}(image_filename, \...)   Add a geographic reference image and world file to the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_image`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_image "tecplot.layout.Frame.add_image"){.reference .internal}(filename, position, height)                                       Add an image to the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_latex`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_latex "tecplot.layout.Frame.add_latex"){.reference .internal}(text\[, position, coord_sys, \...\])                              Adds a [[`LaTeX`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}` `{.xref .any .py .py-class .docutils .literal .notranslate}[`text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} annotation to the Frame.
      [[`add_polyline`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference .internal}(\*points, \*\*kwargs)                                    Create a polyline annotation on this [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_rectangle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_rectangle "tecplot.layout.Frame.add_rectangle"){.reference .internal}(corner, size, coord_sys)                              Place a rectangle annotation on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_square`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_square "tecplot.layout.Frame.add_square"){.reference .internal}(corner, size, coord_sys)                                       Place a square annotation on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.add_text "tecplot.layout.Frame.add_text"){.reference .internal}(text\[, position, coord_sys, \...\])                                 Adds a [[`text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} to a [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`create_dataset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.create_dataset "tecplot.layout.Frame.create_dataset"){.reference .internal}(name\[, var_names, reset_style\])                  Create an empty [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`delete_geometry`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.delete_geometry "tecplot.layout.Frame.delete_geometry"){.reference .internal}(geom)                                           Delete a geometry or image annotation object from the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`delete_image`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.delete_image "tecplot.layout.Frame.delete_image"){.reference .internal}(img)                                                     Delete an image annotation object from the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`delete_text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.delete_text "tecplot.layout.Frame.delete_text"){.reference .internal}(text)                                                       Delete a [[`text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object from a frame.
      [[`geometries`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference .internal}()                                                              Get an iterator for all geometry objects in the frame.
      [[`images`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference .internal}()                                                                          Get an iterator for all image objects in the frame.
      [[`load_stylesheet`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.load_stylesheet "tecplot.layout.Frame.load_stylesheet"){.reference .internal}(filename\[, plot_style, \...\])                 Apply a stylesheet settings file to this frame.
      [[`move_to_bottom`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.move_to_bottom "tecplot.layout.Frame.move_to_bottom"){.reference .internal}()                                                  Moves [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} behind all others in [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal}.
      [[`move_to_top`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.move_to_top "tecplot.layout.Frame.move_to_top"){.reference .internal}()                                                           Moves [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} in front of all others in [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal}.
      [[`plot`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.plot "tecplot.layout.Frame.plot"){.reference .internal}(\[plot_type\])                                                                   The primary [[Plot]{.std .std-ref}](tecplot.plot.html#plot){.reference .internal} style-control object.
      [[`save_stylesheet`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.save_stylesheet "tecplot.layout.Frame.save_stylesheet"){.reference .internal}(filename\[, plot_style, \...\])                 Save the frame\'s current style to a file.
      [[`texts`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame.texts "tecplot.layout.Frame.texts"){.reference .internal}()                                                                             Get an iterator for all [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} objects in the frame.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.activate){.reference .internal}[¶](#tecplot.layout.Frame.activate "Link to this definition"){.headerlink}

:   Causes this [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} to become active.

    The parent [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} is implicitly "activated" as a side-effect of this
    operation:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        page1 = tecplot.active_page()
        frame1 = page1.active_frame()
        page2 = tecplot.add_page()
        frame2 = page2.active_frame()
        assert not (frame1.active and page1.active)
        assert frame2.active and page2.active

        frame1.activate()
        assert not (frame2.active or page2.active)
        assert frame1.active and page1.active
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[activated]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.activated){.reference .internal}[¶](#tecplot.layout.Frame.activated "Link to this definition"){.headerlink}

:   Context for temporarily activating this [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        page = tecplot.active_page()
        frame1 = page.active_frame()
        frame2 = page.add_frame()

        assert frame2.active

        with frame1.activated():
            # frame1 is active only during this context
            assert frame1.active
            # there is only one frame active at a time
            assert not frame2.active

        assert frame2.active
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.active "Link to this definition"){.headerlink}

:   Checks if this [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} is active.

    Returns[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}: [[`True`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} if this [[`Frame`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} is the active [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[active_zones]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.active_zones){.reference .internal}[¶](#tecplot.layout.Frame.active_zones "Link to this definition"){.headerlink}

:   Returns or sets the active [[Zones]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    Parameters[:]{.colon}

    :   **zones** ([[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal},
        optional) -- The [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        objects, which must be in the [[`Dataset`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} attached to this [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}, that will be activated. All other [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        will be deactivated.

    Returns[:]{.colon}

    :   [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        -- This will return a generator of active [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        in this [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}.

    This should only be used on frames with an active plot type that
    contains a dataset with at least one zone.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_circle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[center]{.pre}]{.n}*, *[[radius]{.pre}]{.n}*, *[[coord_sys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_circle){.reference .internal}[¶](#tecplot.layout.Frame.add_circle "Link to this definition"){.headerlink}

:   Place a circle annotation on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **center** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Position [\\((x, y)\\)]{.math .notranslate
          .nohighlight} of the center of the circle in the coordinates
          specified by **coord_sys**.

        - **radius** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- The size of the radius in the coordinates
          specified by **coord_sys**.

        - **coord_sys** ([[`CoordSys`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
          .internal}) -- The coordinate system to use for position and
          size of this annotation.

    Returns[:]{.colon}

    :   [[`annotation.Circle`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Circle "tecplot.annotation.Circle"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.constant import CoordSys

        frame = tecplot.active_frame()
        circle = frame.add_circle((0.2, 0.2), 0.1, CoordSys.Frame)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_ellipse`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_ellipse "tecplot.layout.Frame.add_ellipse"){.reference
    .internal}, [[`add_rectangle`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_rectangle "tecplot.layout.Frame.add_rectangle"){.reference
    .internal}, [[`add_square`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_square "tecplot.layout.Frame.add_square"){.reference
    .internal}, [[`add_polyline`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_ellipse]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[center]{.pre}]{.n}*, *[[size]{.pre}]{.n}*, *[[coord_sys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_ellipse){.reference .internal}[¶](#tecplot.layout.Frame.add_ellipse "Link to this definition"){.headerlink}

:   Place an ellipse annotation on the [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **center** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Position [\\((x, y)\\)]{.math .notranslate
          .nohighlight} of the ellipse in the coordinates specified by
          **coord_sys**.

        - **size** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Lengths [\\((h\_{axis}, v\_{axis})\\)]{.math
          .notranslate .nohighlight} of the horizontal and vertical axes
          in the coordinates specified by **coord_sys**. Both lengths
          must be non-zero.

        - **coord_sys** ([[`CoordSys`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
          .internal}) -- The coordinate system to use for position and
          size of this annotation.

    Returns[:]{.colon}

    :   [[`annotation.Ellipse`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Ellipse "tecplot.annotation.Ellipse"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.constant import CoordSys

        frame = tecplot.active_frame()
        ellipse = frame.add_ellipse((0.5, 0.5), (0.1, 0.2), CoordSys.Frame)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_circle`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_circle "tecplot.layout.Frame.add_circle"){.reference
    .internal}, [[`add_rectangle`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_rectangle "tecplot.layout.Frame.add_rectangle"){.reference
    .internal}, [[`add_square`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_square "tecplot.layout.Frame.add_square"){.reference
    .internal}, [[`add_polyline`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_georeferenced_image]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[image_filename]{.pre}]{.n}*, *[[world_filename]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_georeferenced_image){.reference .internal}[¶](#tecplot.layout.Frame.add_georeferenced_image "Link to this definition"){.headerlink}

:   Add a geographic reference image and world file to the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **image_filename** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The image source file.

        - **world_filename** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The world file associated with the image.

    Returns[:]{.colon}

    :   [[`annotation.GeoreferencedImage`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.GeoreferencedImage "tecplot.annotation.GeoreferencedImage"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> imgfile = 'region.png'
        >>> worldfile = 'region.pgw'
        >>> geoimg = frame.add_georeferenced_image(imgfile, worldfile)
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_image]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[position]{.pre}]{.n}*, *[[height]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_image){.reference .internal}[¶](#tecplot.layout.Frame.add_image "Link to this definition"){.headerlink}

:   Add an image to the [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The image source file. The format of this file
          must be Microsoft Windows Bitmap (*.bmp), JPEG (*.jpg or
          *.jpeg) or Portable Network Graphics (*.png).

        - **position** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Position [\\((x, y)\\)]{.math .notranslate
          .nohighlight} of the image in percentage frame coordinates.

        - **height** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- The initial size, or height, of the image in
          percentage frame units. The initial width in frame units is
          set automatically based on the width to height aspect ratio of
          the image.

    Returns[:]{.colon}

    :   [[`annotation.Image`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Image "tecplot.annotation.Image"){.reference
        .internal}

    This example adds an image to the upper left quadrant of the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> img = frame.add_image('myimage.png', (0, 50), 50)
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_latex]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[text]{.pre}]{.n}*, *[[position]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[coord_sys]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[size_units]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[size]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[anchor]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zone]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_latex){.reference .internal}[¶](#tecplot.layout.Frame.add_latex "Link to this definition"){.headerlink}

:   Adds a [[`LaTeX`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}` `{.xref .any .py .py-class .docutils .literal
    .notranslate}[`text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} annotation to the Frame.

    LaTeX is a computer language designed for typesetting. The most
    popular use of LaTeX is math and Greek fonts for technical purposes.
    See the User Manual for instruction on how to setup LaTeX for use
    with Tecplot 360. Once LaTeX is configured for the GUI version of
    Tecplot 360 no additional changes are needed for PyTecplot.

    Parameters[:]{.colon}

    :   - **text** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The text string must have a non-zero length.

        - **position** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} (x,y), optional) -- The position of the anchor as a
          percentage of the specified coordinates. (default: (0,0))

        - **coord_sys** ([[`CoordSys`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
          .internal}, optional) -- Coordinate system used to position
          the anchor of the text object. The possible values are:
          [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
          .internal} or [[`CoordSys.Frame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
          .internal}. (default: [[`CoordSys.Frame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
          .internal})

        - **size_units** ([[`Units`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units "tecplot.constant.Units"){.reference
          .internal}, optional) -- Text sizing units. Possible values
          are: [[`Units.Grid`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Grid "tecplot.constant.Units.Grid"){.reference
          .internal}, [[`Units.Frame`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Frame "tecplot.constant.Units.Frame"){.reference
          .internal} or [[`Units.Point`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
          .internal}. (default: [[`Units.Point`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
          .internal})

        - **size** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Text height in the specified units.
          (default: 14)

        - **anchor** ([[`TextAnchor`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor "tecplot.constant.TextAnchor"){.reference
          .internal}, optional) -- Anchor position with respect to the
          text box. Possible values are: [[`TextAnchor.Left`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Left "tecplot.constant.TextAnchor.Left"){.reference
          .internal}, [[`TextAnchor.Center`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Center "tecplot.constant.TextAnchor.Center"){.reference
          .internal}, [[`TextAnchor.Right`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Right "tecplot.constant.TextAnchor.Right"){.reference
          .internal}, [[`TextAnchor.MidLeft`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.MidLeft "tecplot.constant.TextAnchor.MidLeft"){.reference
          .internal}, [[`TextAnchor.MidCenter`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.MidCenter "tecplot.constant.TextAnchor.MidCenter"){.reference
          .internal}, [[`TextAnchor.MidRight`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.MidRight "tecplot.constant.TextAnchor.MidRight"){.reference
          .internal}, [[`TextAnchor.HeadLeft`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.HeadLeft "tecplot.constant.TextAnchor.HeadLeft"){.reference
          .internal}, [[`TextAnchor.HeadCenter`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.HeadCenter "tecplot.constant.TextAnchor.HeadCenter"){.reference
          .internal}, [[`TextAnchor.HeadRight`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.HeadRight "tecplot.constant.TextAnchor.HeadRight"){.reference
          .internal}, [[`TextAnchor.OnSide`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.OnSide "tecplot.constant.TextAnchor.OnSide"){.reference
          .internal} (default: [[`TextAnchor.Left`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Left "tecplot.constant.TextAnchor.Left"){.reference
          .internal})

        - **zone** ([[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal}, optional) -- [[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal} or [[`XYLinemap`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
          .internal} to which the text will be attached. (default: None)

    Returns[:]{.colon}

    :   [[`annotation.Text`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
        .internal}: The resulting [[`text`{.xref .any .py .py-class
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
        .py-class .docutils .literal .notranslate}[`box`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
        .internal} object.

    Example

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import TextAnchor

        frame = tp.active_frame()
        frame.add_latex(r'$$\zeta(s) = \sum_{n=1}^\infty\frac{1}{n^s}$$',
                        (50,50), size=64, anchor=TextAnchor.Center)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/frame_add_latex.png"
    class="reference internal image-reference"><img
    src="../_images/frame_add_latex.png" style="width: 300px;"
    alt="../_images/frame_add_latex.png" /></a>
    </figure>

    ::: {.admonition .seealso}
    See also

    [[`add_text`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_text "tecplot.layout.Frame.add_text"){.reference
    .internal}, [[`delete_text`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.delete_text "tecplot.layout.Frame.delete_text"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_polyline]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[points]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_polyline){.reference .internal}[¶](#tecplot.layout.Frame.add_polyline "Link to this definition"){.headerlink}

:   Create a polyline annotation on this [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **\*points** ([[`lists`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of points) -- Arrays of [\\((x, y)\\)]{.math
        .notranslate .nohighlight} or [\\((x, y, z)\\)]{.math
        .notranslate .nohighlight} positions of the points along this
        polyline in the coordinate system specified by **coord_sys**. If
        multiple lists are provided, they must be of the same dimension
        (2D or 3D), though they may be of different lengths.

    Keyword Parameters:

    :   

        coord_sys ([[`CoordSys`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference .internal}, optional): The coordinate system to use for

        :   the positions of this annotation. Only 2D polylines may use
            a coordinate system other than the data-coordinates
            ("grid"). (default: [[`CoordSys.Grid`{.xref .any .py
            .py-attr .docutils .literal
            .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
            .internal})

    Returns[:]{.colon}

    :   One of [[`annotation.Polyline2D`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Polyline2D "tecplot.annotation.Polyline2D"){.reference
        .internal}, [[`annotation.Polyline3D`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Polyline3D "tecplot.annotation.Polyline3D"){.reference
        .internal}, [[`annotation.MultiPolyline2D`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.MultiPolyline2D "tecplot.annotation.MultiPolyline2D"){.reference
        .internal} or [[`annotation.MultiPolyline3D`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.MultiPolyline3D "tecplot.annotation.MultiPolyline3D"){.reference
        .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        points = [ [1, 2,  3],
                   [2, 4,  9],
                   [3, 8, 27], ]

        frame = tecplot.active_frame()
        polyline = frame.add_polyline(points)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_circle`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_circle "tecplot.layout.Frame.add_circle"){.reference
    .internal}, [[`add_ellipse`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_ellipse "tecplot.layout.Frame.add_ellipse"){.reference
    .internal}, [[`add_rectangle`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_rectangle "tecplot.layout.Frame.add_rectangle"){.reference
    .internal}, [[`add_square`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_square "tecplot.layout.Frame.add_square"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_rectangle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[corner]{.pre}]{.n}*, *[[size]{.pre}]{.n}*, *[[coord_sys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_rectangle){.reference .internal}[¶](#tecplot.layout.Frame.add_rectangle "Link to this definition"){.headerlink}

:   Place a rectangle annotation on the [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **center** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Position [\\((x, y)\\)]{.math .notranslate
          .nohighlight} of the rectangle in the coordinates specified by
          **coord_sys**.

        - **size** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Size [\\((width, height)\\)]{.math .notranslate
          .nohighlight} of the rectangle in the coordinates specified by
          **coord_sys**.

        - **coord_sys** ([[`CoordSys`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
          .internal}) -- The coordinate system to use for position and
          size of this annotation.

    Returns[:]{.colon}

    :   [[`annotation.Rectangle`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Rectangle "tecplot.annotation.Rectangle"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.constant import CoordSys

        frame = tecplot.active_frame()
        rectangle = frame.add_rectangle((0.5, 0.5), (0.1, 0.2), CoordSys.Frame)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_circle`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_circle "tecplot.layout.Frame.add_circle"){.reference
    .internal}, [[`add_ellipse`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_ellipse "tecplot.layout.Frame.add_ellipse"){.reference
    .internal}, [[`add_square`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_square "tecplot.layout.Frame.add_square"){.reference
    .internal}, [[`add_polyline`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_square]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[corner]{.pre}]{.n}*, *[[size]{.pre}]{.n}*, *[[coord_sys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_square){.reference .internal}[¶](#tecplot.layout.Frame.add_square "Link to this definition"){.headerlink}

:   Place a square annotation on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **corner** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Position [\\((x, y)\\)]{.math .notranslate
          .nohighlight} of the lower-left corner of the square in the
          coordinates specified by **coord_sys**.

        - **size** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Side-length of the square in the coordinates
          specified by **coord_sys**.

        - **coord_sys** ([[`CoordSys`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
          .internal}) -- The coordinate system to use for position and
          size of this annotation.

    Returns[:]{.colon}

    :   [[`annotation.Square`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Square "tecplot.annotation.Square"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.constant import CoordSys

        frame = tecplot.active_frame()
        square = frame.add_square((0.2, 0.2), 0.1, CoordSys.Frame)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_circle`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_circle "tecplot.layout.Frame.add_circle"){.reference
    .internal}, [[`add_ellipse`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_ellipse "tecplot.layout.Frame.add_ellipse"){.reference
    .internal}, [[`add_rectangle`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_rectangle "tecplot.layout.Frame.add_rectangle"){.reference
    .internal}, [[`add_polyline`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[add_text]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[text]{.pre}]{.n}*, *[[position]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[coord_sys]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[text_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[typeface]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[bold]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[italic]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[size_units]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[size]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[color]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[angle]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[line_spacing]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[anchor]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[box_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[line_thickness]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[box_color]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[fill_color]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[margin]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zone]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.add_text){.reference .internal}[¶](#tecplot.layout.Frame.add_text "Link to this definition"){.headerlink}

:   Adds a [[`text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} to a [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **text** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The text string must have a non-zero length.

        - **position** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} (x,y), optional) -- The position of the anchor as a
          percentage of the specified coordinates. (default: (0,0))

        - **coord_sys** ([[`CoordSys`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
          .internal}, optional) -- Coordinate system used to position
          the anchor of the text object. The possible values are:
          [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
          .internal} or [[`CoordSys.Frame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
          .internal}. (default: [[`CoordSys.Frame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
          .internal})

        - **text_type** ([[`TextType`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType "tecplot.constant.TextType"){.reference
          .internal}, optional) -- Type of text object to create.
          Options are [[`TextType.Regular`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType.Regular "tecplot.constant.TextType.Regular"){.reference
          .internal} (default) and [[`TextType.LaTeX`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType.LaTeX "tecplot.constant.TextType.LaTeX"){.reference
          .internal}. If set to [[`TextType.LaTeX`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType.LaTeX "tecplot.constant.TextType.LaTeX"){.reference
          .internal}, most style-related options will be saved but
          ignored when the text is rendered. These options will only be
          used if the type of the text object is later changed to
          [[`TextType.Regular`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType.Regular "tecplot.constant.TextType.Regular"){.reference
          .internal}.

        - **typeface** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- The typeface name. For consistency
          across various platforms, Tecplot guarantees that the
          following standard typeface names are available: "Helvetica",
          "Times", "Courier", "Greek", "Math", and "User Defined". Other
          typefaces may or may not be available depending on the
          TrueType fonts available. If the typeface name or style is not
          available, a suitable replacement will be selected. (default:
          "Helvetica")

        - **bold** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Use the bold variation of the
          specified typeface. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **italic** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Use the italic variation of the
          specified typeface. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **size_units** ([[`Units`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units "tecplot.constant.Units"){.reference
          .internal}, optional) -- Text sizing units. Possible values
          are: [[`Units.Grid`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Grid "tecplot.constant.Units.Grid"){.reference
          .internal}, [[`Units.Frame`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Frame "tecplot.constant.Units.Frame"){.reference
          .internal} or [[`Units.Point`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
          .internal}. (default: [[`Units.Point`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
          .internal})

        - **size** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Text height in the specified units.
          (default: 14)

        - **color** ([[`Color`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
          .internal}, optional) -- Color of the text (default:
          [[`Color.Black`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color.Black "tecplot.constant.Color.Black"){.reference
          .internal})

        - **angle** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Angle of the text baseline in degrees
          from -360 to 360. (default: 0)

        - **line_spacing** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Line spacing in units of line size.
          Can take values from 0 to 50. (default: 1)

        - **anchor** ([[`TextAnchor`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor "tecplot.constant.TextAnchor"){.reference
          .internal}, optional) -- Anchor position with respect to the
          text box. Possible values are: [[`TextAnchor.Left`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Left "tecplot.constant.TextAnchor.Left"){.reference
          .internal}, [[`TextAnchor.Center`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Center "tecplot.constant.TextAnchor.Center"){.reference
          .internal}, [[`TextAnchor.Right`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Right "tecplot.constant.TextAnchor.Right"){.reference
          .internal}, [[`TextAnchor.MidLeft`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.MidLeft "tecplot.constant.TextAnchor.MidLeft"){.reference
          .internal}, [[`TextAnchor.MidCenter`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.MidCenter "tecplot.constant.TextAnchor.MidCenter"){.reference
          .internal}, [[`TextAnchor.MidRight`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.MidRight "tecplot.constant.TextAnchor.MidRight"){.reference
          .internal}, [[`TextAnchor.HeadLeft`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.HeadLeft "tecplot.constant.TextAnchor.HeadLeft"){.reference
          .internal}, [[`TextAnchor.HeadCenter`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.HeadCenter "tecplot.constant.TextAnchor.HeadCenter"){.reference
          .internal}, [[`TextAnchor.HeadRight`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.HeadRight "tecplot.constant.TextAnchor.HeadRight"){.reference
          .internal}, [[`TextAnchor.OnSide`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.OnSide "tecplot.constant.TextAnchor.OnSide"){.reference
          .internal} (default: [[`TextAnchor.Left`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Left "tecplot.constant.TextAnchor.Left"){.reference
          .internal})

        - **box_type** ([[`constant.TextBox`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox "tecplot.constant.TextBox"){.reference
          .internal}, optional) -- Type of text box can be one of:
          [[`constant.TextBox.None_`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox.None_ "tecplot.constant.TextBox.None_"){.reference
          .internal}, [[`constant.TextBox.Filled`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox.Filled "tecplot.constant.TextBox.Filled"){.reference
          .internal} or [[`constant.TextBox.Hollow`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox.Hollow "tecplot.constant.TextBox.Hollow"){.reference
          .internal}. (default: [[`constant.TextBox.None_`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox.None_ "tecplot.constant.TextBox.None_"){.reference
          .internal})

        - **line_thickness** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Text box boarder line thickness may
          be a value in the range from 0.0001 to 100. (default: 0.1)

        - **box_color** ([[`Color`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
          .internal}, optional) -- Text box border line color. See
          [[`Color`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
          .internal} for possible values. (default:
          [[`Color.Black`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color.Black "tecplot.constant.Color.Black"){.reference
          .internal})

        - **fill_color** ([[`Color`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
          .internal}, optional) -- Text box fill color. See
          [[`Color`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
          .internal} for possible values. (default: [[`White`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color.White "tecplot.constant.Color.White"){.reference
          .internal})

        - **margin** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Margin between the text and text box.
          May be in the range from 0 to 2000. (default: 20)

        - **zone** ([[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal}, optional) -- [[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal} or [[`XYLinemap`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
          .internal} to which the text will be attached. (default: None)

    Returns[:]{.colon}

    :   [[`annotation.Text`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
        .internal}: The resulting [[`text`{.xref .any .py .py-class
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
        .py-class .docutils .literal .notranslate}[`box`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
        .internal} object.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.constant import Color

        frame = tecplot.active_frame()
        frame.add_text('Hello, World!', position=(35, 50),
                       bold=True, italic=False, color=Color.Blue)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_latex`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_latex "tecplot.layout.Frame.add_latex"){.reference
    .internal}, [[`delete_text`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.delete_text "tecplot.layout.Frame.delete_text"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this frame.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the frame. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> aux = tp.active_frame().aux_data
        >>> aux['Result'] = '3.14159'
        >>> print(aux['Result'])
        3.14159
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[background_color]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.background_color "Link to this definition"){.headerlink}

:   Color of the background.

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[border_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.border_thickness "Link to this definition"){.headerlink}

:   The border thickness in units of [[`Frame.size_pos_units`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference
    .internal}.

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[create_dataset]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[var_names]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.create_dataset){.reference .internal}[¶](#tecplot.layout.Frame.create_dataset "Link to this definition"){.headerlink}

:   Create an empty [[`Dataset`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This will create a new [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} and replace the existing one, destroying all data
    associated with it.

    Parameters[:]{.colon}

    :   - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- have to be unique.

        - **var_names** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`strings`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- [[`Variable`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal} names. This only sets the names and not the data
          type or location. See [[`add_variable`{.xref .any .py .py-meth
          .docutils .literal
          .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset.add_variable "tecplot.data.Dataset.add_variable"){.reference
          .internal}. (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}) -- before loading the [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The newly created [[`Dataset`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal}.

    ::: {.admonition .note}
    Note

    Relationships between [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} and [[`Dataset`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}

    A [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} may only hold a single [[`Dataset`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}, though this [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} may be shared between several [[`Frames`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. Therefore, this method will only *replace* the current
    dataset when **reset_style** is set to [[`True`{.xref .any .docutils
    .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external} and will fail otherwise. If this [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} already has a [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}, it may be more efficient to do one of the following
    instead:

    > <div>
    >
    > - Add a new (blank) frame with [[`Page.add_frame()`{.xref .any .py
    >   .py-meth .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.layout.Page.add_frame "tecplot.layout.Page.add_frame"){.reference
    >   .internal} and create a [[`Dataset`{.xref .any .py .py-class
    >   .docutils .literal
    >   .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    >   .internal} for this.
    >
    > - Add new zones to the existing [[`Dataset`{.xref .any .py
    >   .py-class .docutils .literal
    >   .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    >   .internal} with [[`Dataset.add_ordered_zone()`{.xref .any .py
    >   .py-meth .docutils .literal
    >   .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset.add_ordered_zone "tecplot.data.Dataset.add_ordered_zone"){.reference
    >   .internal}, [[`Dataset.add_fe_zone()`{.xref .any .py .py-meth
    >   .docutils .literal
    >   .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset.add_fe_zone "tecplot.data.Dataset.add_fe_zone"){.reference
    >   .internal} or [[`Dataset.add_poly_zone()`{.xref .any .py
    >   .py-meth .docutils .literal
    >   .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset.add_poly_zone "tecplot.data.Dataset.add_poly_zone"){.reference
    >   .internal}.
    >
    > - Change the existing data [[`in-place`{.xref .any .py .py-attr
    >   .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArgListArgType.Array "tecplot.constant.ArgListArgType.Array"){.reference
    >   .internal}.
    >
    > </div>
    :::

    ::: {.admonition .note}
    Note

    **Performance considerations for data manipulations.**

    When performing many data-manipulation operations including adding
    zones, adding variables, modifying field data or connectivity, and
    especially in connected mode, it is recommended to do this all with
    the [[`tecplot.session.suspend()`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.suspend "tecplot.session.suspend"){.reference
    .internal}. This will prevent the Tecplot engine from trying to
    "keep up" with the changes. Tecplot will be notified of all changes
    made upon exit of this context. This may result in significant
    performance gains for long operations.
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[dataset]{.pre}]{.sig-name .descname}*[[:]{.pre}]{.p}[ ]{.w}[[Dataset]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}*[¶](#tecplot.layout.Frame.dataset "Link to this definition"){.headerlink}

:   The [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} belonging to this Frame.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[delete_geometry]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[geom]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.delete_geometry){.reference .internal}[¶](#tecplot.layout.Frame.delete_geometry "Link to this definition"){.headerlink}

:   Delete a geometry or image annotation object from the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **geom** ([[`Circle`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Circle "tecplot.annotation.Circle"){.reference
        .internal}, [[`Image`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Image "tecplot.annotation.Image"){.reference
        .internal} or similar instance) -- The annotation instance to be
        removed from the [[`Frame`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}.

    ::: {.admonition .warning}
    Warning

    After the annotation is deleted, all handles to it will no longer be
    valid and all accessing any properties of the object will result in
    a [[`TecplotLogicError`{.xref .any .py .py-exc .docutils .literal
    .notranslate}]{.pre}](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
    .internal} being raised.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        from tecplot.constant import CoordSys

        frame = tecplot.active_frame()
        rectangle = frame.add_rectangle((0.5, 0.5), (0.1, 0.2), CoordSys.Frame)
        frame.delete_geometry(rectangle)
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[delete_image]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[img]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.delete_image){.reference .internal}[¶](#tecplot.layout.Frame.delete_image "Link to this definition"){.headerlink}

:   Delete an image annotation object from the [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **img** ([[`Image`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Image "tecplot.annotation.Image"){.reference
        .internal} or [[`GeoreferencedImage`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.GeoreferencedImage "tecplot.annotation.GeoreferencedImage"){.reference
        .internal}) -- The annotation instance to be removed from the
        [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}.

    ::: {.admonition .warning}
    Warning

    After the annotation is deleted, all handles to it will no longer be
    valid and all accessing any properties of the object will result in
    a [[`TecplotLogicError`{.xref .any .py .py-exc .docutils .literal
    .notranslate}]{.pre}](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
    .internal} being raised.
    :::

    ::: {.admonition .seealso}
    See also

    [[`delete_geometry()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.delete_geometry "tecplot.layout.Frame.delete_geometry"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[delete_text]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[text]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.delete_text){.reference .internal}[¶](#tecplot.layout.Frame.delete_text "Link to this definition"){.headerlink}

:   Delete a [[`text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object from a frame.

    When deleted, the text object is no longer displayed in the frame
    and is permanently invalid. To display the text in the frame again,
    a new text object must be created by calling [[`add_text`{.xref .any
    .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_text "tecplot.layout.Frame.add_text"){.reference
    .internal}.

    ::: {.admonition .warning}
    Warning

    Use this method with care. After a text object has been deleted by
    calling this method, it is no longer valid, and all properties of
    the deleted text object will throw [[`TecplotLogicError`{.xref .any
    .py .py-exc .docutils .literal
    .notranslate}]{.pre}](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
    .internal} when accessed.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        text = tp.active_frame().add_text("abc")
        tp.active_frame().delete_text(text)

        # The text object is no longer valid.
        # Any property access will throw TecplotLogicError
        try:
            print(text.text_string)
        except tp.exception.TecplotLogicError as e:
            print(e)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`add_text`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.add_text "tecplot.layout.Frame.add_text"){.reference
    .internal}
    :::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[geometries]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.geometries){.reference .internal}[¶](#tecplot.layout.Frame.geometries "Link to this definition"){.headerlink}

:   Get an iterator for all geometry objects in the frame.

    This method provides access to all geometric shape instances
    attached to this [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. This includes [[`Circle`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Circle "tecplot.annotation.Circle"){.reference
    .internal}, [[`Polyline2D`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Polyline2D "tecplot.annotation.Polyline2D"){.reference
    .internal}, [[`Polyline3D`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Polyline3D "tecplot.annotation.Polyline3D"){.reference
    .internal} and all similar objects:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for geom in frame.geometries():
        ...     print(type(geom))
        <class 'tecplot.annotation.geometry.Circle'>
        <class 'tecplot.annotation.polyline.Polyline2D'>
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[has_dataset]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.has_dataset "Link to this definition"){.headerlink}

:   [[`bool`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
    .external}: Checks to see if the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} as an attached [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> if not frame.has_dataset:
        ...     dataset = frame.create_dataset('Dataset', ['x','y','z','p'])
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[header_background_color]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.header_background_color "Link to this definition"){.headerlink}

:   The header's background color.

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[height]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.height "Link to this definition"){.headerlink}

:   The height in units of [[`Frame.size_pos_units`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference
    .internal}.

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[images]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.images){.reference .internal}[¶](#tecplot.layout.Frame.images "Link to this definition"){.headerlink}

:   Get an iterator for all image objects in the frame.

    This method provides access to all [[`Image`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Image "tecplot.annotation.Image"){.reference
    .internal} and [[`GeoreferencedImage`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.GeoreferencedImage "tecplot.annotation.GeoreferencedImage"){.reference
    .internal} instances attached to this [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for image in frame.images():
        ...     print(image.filename)
        image1.png
        image2.png
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[load_stylesheet]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[plot_style]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[text]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[geom]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[streams]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[contours]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[frame_geom]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[merge]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.load_stylesheet){.reference .internal}[¶](#tecplot.layout.Frame.load_stylesheet "Link to this definition"){.headerlink}

:   Apply a stylesheet settings file to this frame.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The path to a stylesheet file. (See note below
          conerning absolute and relative paths.)

        - **plot_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Apply the stylesheet's plot style.
          (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **text** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include the stylesheet's text
          objects. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **geom** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include the stylesheet's geometry
          objects. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **streams** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include the stylesheet's stream
          traces. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **contours** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include the stylesheet's contour
          levels. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **frame_geom** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Apply the stylesheet's frame position
          and size. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **merge** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Merge with the frame's current style.
          (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

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

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tecplot.active_frame()
        >>> frame.load_stylesheet('my_style.sty')
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[move_to_bottom]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.move_to_bottom){.reference .internal}[¶](#tecplot.layout.Frame.move_to_bottom "Link to this definition"){.headerlink}

:   Moves [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} behind all others in [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[move_to_top]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.move_to_top){.reference .internal}[¶](#tecplot.layout.Frame.move_to_top "Link to this definition"){.headerlink}

:   Moves [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in front of all others in [[`Page`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.name "Link to this definition"){.headerlink}

:   Returns or sets the name.

    This is the name used when searching for [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} objects in [[`Page.frames`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page.frames "tecplot.layout.Page.frames"){.reference
    .internal} and [[`Page.frame`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page.frame "tecplot.layout.Page.frame"){.reference
    .internal}. It does not have to be unique, even for multiple frames
    in a single [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        frame = tecplot.active_frame()
        frame.name = '3D Data View'

        # will print: "this frame: 3D Data View"
        print('this frame:', frame.name)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[page]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.page "Link to this definition"){.headerlink}

:   The [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} containing this Frame.

    This provides access to the parent [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        frame = tecplot.active_frame()
        page = frame.page

        # Will print: "Page 001"
        print(page.name)
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[plot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PlotType.Automatic]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.plot){.reference .internal}[¶](#tecplot.layout.Frame.plot "Link to this definition"){.headerlink}

:   The primary [[Plot]{.std
    .std-ref}](tecplot.plot.html#plot){.reference .internal}
    style-control object.

    Returns[:]{.colon}

    :   [[Plot]{.std .std-ref}](tecplot.plot.html#plot){.reference
        .internal} -- One of the possible [[Plot]{.std
        .std-ref}](tecplot.plot.html#plot){.reference .internal}
        subclasses, depending on the [`plot_type`{.docutils .literal
        .notranslate}]{.pre} specified. By default, the active plot
        type, obtained from [[`Frame.plot_type`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame.plot_type "tecplot.layout.Frame.plot_type"){.reference
        .internal}, is used.

    The [[Plot]{.std .std-ref}](tecplot.plot.html#plot){.reference
    .internal} object is the handle through which one can manipulate the
    style and visual representation of the [[`Dataset`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}. Possible return types are: [[`SketchPlot`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.SketchPlot "tecplot.plot.SketchPlot"){.reference
    .internal}, [[`Cartesian2DFieldPlot`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian2DFieldPlot "tecplot.plot.Cartesian2DFieldPlot"){.reference
    .internal}, [[`Cartesian3DFieldPlot`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot "tecplot.plot.Cartesian3DFieldPlot"){.reference
    .internal}, [[`PolarLinePlot`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.PolarLinePlot "tecplot.plot.PolarLinePlot"){.reference
    .internal} and [[`XYLinePlot`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinePlot "tecplot.plot.XYLinePlot"){.reference
    .internal}. Each of these have their own specific set of attributes
    and methods:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot
        from tecplot.constant import PlotType

        install_dir = tecplot.session.tecplot_install_directory()
        infile = os.path.join(install_dir, 'examples', 'SimpleData', 'SpaceShip.lpk')
        tecplot.load_layout(infile)

        frame = tecplot.active_frame()
        assert frame.plot_type is PlotType.Cartesian3D

        plot3d = frame.plot()
        plot3d.show_contour = True
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[plot_type]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.plot_type "Link to this definition"){.headerlink}

:   Returns or sets the current plot type.

    A [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} can have only one active plot type at any given time. The
    types are enumerated by [[`constant.PlotType`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot
        from tecplot.constant import PlotType

        frame = tecplot.active_frame()
        assert frame.plot_type is PlotType.Sketch

        install_dir = tecplot.session.tecplot_install_directory()
        infile = os.path.join(install_dir, 'examples', 'SimpleData', 'SpaceShip.lpk')
        tecplot.load_layout(infile)

        frame = tecplot.active_frame()
        assert frame.plot_type is PlotType.Cartesian3D

        frame.plot_type = PlotType.Cartesian2D
        assert frame.plot_type is PlotType.Cartesian2D
    :::
    ::::

    ::: {.admonition .note}
    Note

    Plot type cannot be set to [[`constant.PlotType.Automatic`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
    .internal}.
    :::

    Type[:]{.colon}

    :   [[`constant.PlotType`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
        .internal}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: [`(x,y)`{.docutils .literal .notranslate}]{.pre}
    position of the [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in inches.

    The [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} x position is relative to the left side of the paper. The
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} y position is relative to the top of the paper.

    If x is [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}, the [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} x position is not changed. If y is [[`None`{.xref .any
    .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}, the [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} y position is not changed.

    Set [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} position 1 inch from the left side of the paper and two
    inches from the top of the paper:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.active_frame().position=(1.0, 2.0)
    :::
    ::::

    Move the active [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} one inch to the right:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.active_frame().position=(tp.active_frame().position.x+1, None)
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[save_stylesheet]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[plot_style]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[aux_data]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[text]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[geom]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[streams]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[contours]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[defaults]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[relative_paths]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[compress]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.save_stylesheet){.reference .internal}[¶](#tecplot.layout.Frame.save_stylesheet "Link to this definition"){.headerlink}

:   Save the frame's current style to a file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The path to a stylesheet file. (See note below
          conerning absolute and relative paths.)

        - **plot_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include the frame's plot style.
          (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **aux_data** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include auxiliary data. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **text** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include text objects. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **geom** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include geometry objects. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **streams** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include stream traces. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **contours** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include contour levels. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **defaults** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Include all factory defaults used by
          the current style. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **relative_paths** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Use relative paths. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **compress** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Compress the output of the style.
          (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

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

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tecplot.active_frame()
        >>> frame.save_stylesheet('my_style.sty')
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[show_border]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.show_border "Link to this definition"){.headerlink}

:   [[`bool`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
    .external}: Show or hide the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}'s border.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[show_header]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.show_header "Link to this definition"){.headerlink}

:   [[`bool`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
    .external}: Show or hide the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}'s header in the border.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[size_pos_units]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.size_pos_units "Link to this definition"){.headerlink}

:   The units used for size properties.

    Possible values: [[`Paper`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
    .internal}, [[`Workspace`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FrameSizePosUnits.Workspace "tecplot.constant.FrameSizePosUnits.Workspace"){.reference
    .internal}.

    Type[:]{.colon}

    :   [[`FrameSizePosUnits`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FrameSizePosUnits "tecplot.constant.FrameSizePosUnits"){.reference
        .internal}

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[texts]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/frame.html#Frame.texts){.reference .internal}[¶](#tecplot.layout.Frame.texts "Link to this definition"){.headerlink}

:   Get an iterator for all [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} objects in the frame.

    This example shows how to obtain a list of all red [[`Text`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.annotations.html#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} objects:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> all_red_text_objects = [T for T in tp.active_frame().texts()
        ...                         if T.color == Color.Red]
    :::
    ::::

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[transparent]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.transparent "Link to this definition"){.headerlink}

:   [[`bool`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
    .external}: Use transparency within this [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

<!-- -->

[[Frame.]{.pre}]{.sig-prename .descclassname}[[width]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Frame.width "Link to this definition"){.headerlink}

:   The width in units of [[`Frame.size_pos_units`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame.size_pos_units "tecplot.layout.Frame.size_pos_units"){.reference
    .internal}.

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::

::: {#id1 .section}
## [Page](#id16){.toc-backref role="doc-backlink"}[¶](#id1 "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.layout.]{.pre}]{.sig-prename .descclassname}[[Page]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page){.reference .internal}[¶](#tecplot.layout.Page "Link to this definition"){.headerlink}

:   [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} object within a layout, holding onto one or more
    [[`Frames`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **uid** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, optional) -- This must be a *valid* unique ID number
        pointing internally to a [[`Page`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} object or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}. A new [[`Page`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
        .internal} is created if set to [[`None`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}. (default: [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external})

    ::: {.admonition .warning}
    Warning

    Though it is possible to create a [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} object using the constructor, it is usually sufficient to
    obtain a page through [[`tecplot.add_page`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.add_page "tecplot.add_page"){.reference
    .internal}, [[`tecplot.active_page`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.active_page "tecplot.active_page"){.reference
    .internal}, [[`tecplot.page`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.page "tecplot.page"){.reference
    .internal} or [[`tecplot.pages`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.pages "tecplot.pages"){.reference
    .internal}.
    :::

    A [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} can be thought of like a canvas onto which one or more
    [[`Frames`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} can be laid out. The engine guarantees there will always
    be at least one [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} in the layout which can be accessed via
    [[`tecplot.active_page`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.active_page "tecplot.active_page"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        page = tecplot.active_page()
        page.name = 'Page 001'

        # prints: "Page 001"
        print(page.name)

        # prints: "Frame 001"
        for frame in page.frames():
            print(frame.name)
    :::
    ::::

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.active "tecplot.layout.Page.active"){.reference .internal}         Checks if this [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal} is active.
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.aux_data "tecplot.layout.Page.aux_data"){.reference .internal}   Auxiliary data for this page.
      [[`exists`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.exists "tecplot.layout.Page.exists"){.reference .internal}         Checks if the [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal} exists in the current layout.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.name "tecplot.layout.Page.name"){.reference .internal}               Name of the page.
      [[`paper`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.paper "tecplot.layout.Page.paper"){.reference .internal}            [[`Paper`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference .internal}: The [[`Paper`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference .internal} defined in this [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal}.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.position "tecplot.layout.Page.position"){.reference .internal}   Index of the Page
      ------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.activate "tecplot.layout.Page.activate"){.reference .internal}()                        Activates the [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal}.
      [[`active_frame`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.active_frame "tecplot.layout.Page.active_frame"){.reference .internal}()            Returns the active [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`add_frame`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.add_frame "tecplot.layout.Page.add_frame"){.reference .internal}(\[position, size\])   Creates a new [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} in this [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal}.
      [[`delete_frame`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.delete_frame "tecplot.layout.Page.delete_frame"){.reference .internal}(frame)       Removes the frame from this [[`Page`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference .internal}.
      [[`frame`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.frame "tecplot.layout.Page.frame"){.reference .internal}(pattern)                          Returns the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} by name.
      [[`frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.frames "tecplot.layout.Page.frames"){.reference .internal}(\[pattern\])                   Returns a [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of [[`Frames`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal} matching the specified pattern.
      [[`tile_frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Page.tile_frames "tecplot.layout.Page.tile_frames"){.reference .internal}(\[mode\])       Tile frames based on a certain mode.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.activate){.reference .internal}[¶](#tecplot.layout.Page.activate "Link to this definition"){.headerlink}

:   Activates the [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}.

    Raises[:]{.colon}

    :   - [**TecplotRuntimeError**](tecplot.exceptions.html#tecplot.exception.TecplotRuntimeError "tecplot.exception.TecplotRuntimeError"){.reference
          .internal} -- Page does not exist.

        - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- Could not activate the page.

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Page.active "Link to this definition"){.headerlink}

:   Checks if this [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} is active.

    Returns[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external} -- [[`True`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} if active.

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[active_frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.active_frame){.reference .internal}[¶](#tecplot.layout.Page.active_frame "Link to this definition"){.headerlink}

:   Returns the active [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    Returns[:]{.colon}

    :   [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} -- The active [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}.

    This implicitly activates this [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} and returns the active [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} attached to it.

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[add_frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[position]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[size]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.add_frame){.reference .internal}[¶](#tecplot.layout.Page.add_frame "Link to this definition"){.headerlink}

:   Creates a new [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in this [[`Page`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **position** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} (x,y), optional) -- The position (in inches) of the
          frame relative to the top left corner of the paper. If
          supplied, size must also be supplied.

        - **size** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`floats`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} (width,height), optional) -- The size (in inches)
          of the frame. If supplied, position must also be supplied.

    Returns[:]{.colon}

    :   [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} -- The newly created and activated [[`Frame`{.xref
        .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal}.

    This implicitly activates the [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} and creates and activates a new [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        frame = tp.active_page().add_frame(position=(1, 0.25), size=(8, 9))
    :::
    ::::

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Page.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this page.

    Returns: [[`AuxData`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
    .internal}

    This is the auxiliary data attached to the page. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> aux = tp.active_page().aux_data
        >>> aux['Result'] = '3.14159'
        >>> print(aux['Result'])
        3.14159
    :::
    ::::

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[delete_frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.delete_frame){.reference .internal}[¶](#tecplot.layout.Page.delete_frame "Link to this definition"){.headerlink}

:   Removes the frame from this [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}.

    Raises[:]{.colon}

    :   - [**TecplotRuntimeError**](tecplot.exceptions.html#tecplot.exception.TecplotRuntimeError "tecplot.exception.TecplotRuntimeError"){.reference
          .internal} --

        - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- Could not delete the frame.

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[exists]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Page.exists "Link to this definition"){.headerlink}

:   Checks if the [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} exists in the current layout.

    This will return [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external} after the [[`Page`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} has been deleted:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        page = tp.add_page()
        assert page.exists
        tp.delete_page(page)
        assert not page.exists
    :::
    ::::

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.frame){.reference .internal}[¶](#tecplot.layout.Page.frame "Link to this definition"){.headerlink}

:   Returns the [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} by name.

    Parameters[:]{.colon}

    :   **pattern** ([[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`re.Pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external}) -- Case-insensitive [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} or a compiled [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} used to match the frame by name.

    Returns[:]{.colon}

    :   [[`Frame`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} -- The first [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} identified by *pattern*.

    ::: {.admonition .note}
    Note

    A [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} can contain [[`Frames`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} with identical names and only the first match found is
    returned. This is not guaranteed to be deterministic and care should
    be taken to have only [[`Frames`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} with unique names when this feature is used.
    :::

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot
        page = tecplot.active_page()

        frameA = page.add_frame()
        frameA.name = 'A'

        frameB = page.add_frame()
        frameB.name = 'B'

        assert frameB.active
        assert frameA == page.frame('A')
    :::
    ::::

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[frames]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.frames){.reference .internal}[¶](#tecplot.layout.Page.frames "Link to this definition"){.headerlink}

:   Returns a [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of [[`Frames`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} matching the specified pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`re.Pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external}, optional) -- Case-insensitive [[`glob-style`{.xref
        .any .docutils .literal .notranslate}]{.pre}` `{.xref .any
        .docutils .literal .notranslate}[`pattern`{.xref .any .docutils
        .literal .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} or a compiled [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} used to match frame names.

    Returns[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}: [[`Frames`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} identified by *pattern* or all frames if no *pattern*
        is specified.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        page = tecplot.active_page()
        page.add_frame()  # create a second frame

        # iterate over all frames and print their names
        for frame in page.frames():
            print(frame.name)

        # store a persistent list of frames
        frames = page.frames()

        # prints: ['Frame 001', 'Frame 002']
        print([f.name for f in frames])
    :::
    ::::

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Page.name "Link to this definition"){.headerlink}

:   Name of the page.

    This is the name used when searching for [[`Page`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} objects in [[`tecplot.pages`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.pages "tecplot.pages"){.reference
    .internal} and [[`tecplot.page`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.page "tecplot.page"){.reference
    .internal}. It does not have to be unique.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot

        page = tecplot.active_page()
        page.name = 'My Data'

        # prints: "this page: My Data"
        print('this page:', page.name)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[paper]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Page.paper "Link to this definition"){.headerlink}

:   [[`Paper`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
    .internal}: The [[`Paper`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
    .internal} defined in this [[`Page`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}.

    Every [[`Page`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal} has the concept of a workspace which includes all
    [[`Frames`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} as well as a sub-area of the workspace called the
    [[`Paper`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
    .internal}. The limits of the [[`Paper`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
    .internal} with respect to the placement of [[`Frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} is used when exporting certain image formats.

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Page.position "Link to this definition"){.headerlink}

:   Index of the Page

    The page positions are 0 based positions relative to the current
    page, where the current page has a position value of 0, the next
    page 1, the page after that 2, and so on.

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}

<!-- -->

[[Page.]{.pre}]{.sig-prename .descclassname}[[tile_frames]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mode]{.pre}]{.n}[[=]{.pre}]{.o}[[TileMode.Grid]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Page.tile_frames){.reference .internal}[¶](#tecplot.layout.Page.tile_frames "Link to this definition"){.headerlink}

:   Tile frames based on a certain mode.

    Parameters[:]{.colon}

    :   **mode** ([[`TileMode`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TileMode "tecplot.constant.TileMode"){.reference
        .internal}, optional) -- Direction and layout mode for tiling
        frames. Possible values: [[`TileMode.Grid`{.xref .any .py
        .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TileMode.Grid "tecplot.constant.TileMode.Grid"){.reference
        .internal} (default), [[`TileMode.Columns`{.xref .any .py
        .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TileMode.Columns "tecplot.constant.TileMode.Columns"){.reference
        .internal}, [[`TileMode.Rows`{.xref .any .py .py-attr .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TileMode.Rows "tecplot.constant.TileMode.Rows"){.reference
        .internal}, [[`TileMode.Wrap`{.xref .any .py .py-attr .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TileMode.Wrap "tecplot.constant.TileMode.Wrap"){.reference
        .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TileMode
        >>> page.tile_frame(TileMode.Wrap)
    :::
    ::::
:::

::: {#paper .section}
## [Paper](#id17){.toc-backref role="doc-backlink"}[¶](#paper "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.layout.]{.pre}]{.sig-prename .descclassname}[[Paper]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[page]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/layout/page.html#Paper){.reference .internal}[¶](#tecplot.layout.Paper "Link to this definition"){.headerlink}

:   The [[`Paper`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Paper "tecplot.layout.Paper"){.reference
    .internal} boundary defined on a workspace.

    This is the area used for certain image output formats. It is
    defined for a specific [[`Page`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.layout.Page "tecplot.layout.Page"){.reference
    .internal}. [[`Frames`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} can be laid out in reference to this sub-area of the
    workspace.

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------
      [[`dimensions`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.layout.Paper.dimensions "tecplot.layout.Paper.dimensions"){.reference .internal}   Width and height (read-only).
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------

<!-- -->

[[Paper.]{.pre}]{.sig-prename .descclassname}[[dimensions]{.pre}]{.sig-name .descname}[¶](#tecplot.layout.Paper.dimensions "Link to this definition"){.headerlink}

:   Width and height (read-only).

    the dimensions, *(width, height)* in inches, of the currently
    defined paper in the Tecplot workspace.
:::
:::::::::::::::::::

::: clearer
:::
:::::::::::::::::::::
