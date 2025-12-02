:::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::::::: {#session-and-top-level-functionality .section}
# Session and Top-Level Functionality[¶](#session-and-top-level-functionality "Link to this heading"){.headerlink}

- [tecplot](#module-tecplot){#id4 .reference .internal}

- [Version Information](#version-information){#id5 .reference .internal}

- [Session](#session){#id6 .reference .internal}

- [Configuration](#configuration){#id7 .reference .internal}

- [Miscellaneous](#miscellaneous){#id8 .reference .internal}

::::::::: {#module-tecplot .section}
[]{#tecplot}

## [tecplot](#id4){.toc-backref role="doc-backlink"}[¶](#module-tecplot "Link to this heading"){.headerlink}

[[`tecplot`{.xref .any .py .py-mod .docutils .literal
.notranslate}]{.pre}](#module-tecplot "tecplot"){.reference .internal}
is the top-level module for PyTecplot and it provides access to the
entire public API.

In this example, the tecplot dynamic library is loaded at import time.
The Tecplot Engine is started and the text 'Hello, World!' is added to
the center of the active frame. All logging messages are piped to the
console which may be useful to debug any script:

:::: {.highlight-python .notranslate}
::: highlight
    import sys
    import logging

    import tecplot

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    frame = tecplot.active_frame()
    frame.add_text('Hello, World!', position=(35,50), size=35)
    tecplot.export.save_png('hello_world.png')
:::
::::

::::: {#tecutil-layer .section}
### TecUtil Layer[¶](#tecutil-layer "Link to this heading"){.headerlink}

The interface used to access the Tecplot Engine is called "TecUtil" and
is the same as that used by addons. There are many checks in place for
validating calls into this layer. The vast majority of these are
recoverable and are seen in Python as a raised exception of type
[[`TecplotLogicError`{.xref .any .py .py-exc .docutils .literal
.notranslate}]{.pre}](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
.internal}.

In principle, a user's script should never trigger a
[[`TecplotLogicError`{.xref .any .py .py-exc .docutils .literal
.notranslate}]{.pre}](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
.internal} as it indicates the requested operation is invalid in the
current engine state or that the parameters passed into the TecUtil
layer (indices for example) are not valid. Here is a (contrived) example
of a typical exception one might see:

:::: {.highlight-python .notranslate}
::: highlight
    import tecplot as tp
    from tecplot.tecutil import lock

    '''
    The following will print out something like:

        Assertion trap in function call from an Add-on:
        Assertion Type: Pre-condition
        Assertion: ArgListIsValid(ArgList)
        Tecplot version: 2018.3.0.92441
        Function: TecUtilStateChangedX
        Explanation: Argument list must be valid.
    '''
    try:
        with tp.tecutil.lock():
            tp.tecutil._tecutil.StateChangedX(None)
    except tp.exception.TecplotError as e:
        print(e)
:::
::::

Note that [[`None`{.xref .any .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
.external} is an invalid input value for the
[`StateChangedX()`{.docutils .literal .notranslate}]{.pre} TecUtil
method.
:::::

::: {#tecplot-version-compatibility .section}
### Tecplot Version Compatibility[¶](#tecplot-version-compatibility "Link to this heading"){.headerlink}

It is always recommended to use the most recent version of PyTecplot.
However, doing so may require an update to the underlying [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
installation. Out-of-date installations of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
may be used but features may be missing and care must be taken not to
use such features in the Python scripts. On top of this, there is a
minimum version of the installed [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
required by PyTecplot and the Python library will fail to load if this
is not satisfied.
:::
:::::::::

:::::::::::: {#version-information .section}
## [Version Information](#id5){.toc-backref role="doc-backlink"}[¶](#version-information "Link to this heading"){.headerlink}

::::::::::: {#module-tecplot.version .section}
[]{#tecplot-version}

### tecplot.version[¶](#module-tecplot.version "Link to this heading"){.headerlink}

Version information of the tecplot Python module can be obtained as a
[[`string`{.xref .any .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
.external} of the form "Major.Minor.Patch":

:::: {.highlight-python .notranslate}
::: highlight
    tecplot.__version__
:::
::::

or as a [[`namedtuple`{.xref .any .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
.external} with attributes: "major", "minor", "patch", "build" in that
order:

:::: {.highlight-python .notranslate}
::: highlight
    tecplot.version_info
:::
::::

The underlying [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
installation has its own version which can be obtained as a
[[`str`{.xref .any .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
.external}:

:::: {.highlight-python .notranslate}
::: highlight
    tecplot.sdk_version
:::
::::

or as a [[`namedtuple`{.xref .any .docutils .literal
.notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
.external}:

:::: {.highlight-python .notranslate}
::: highlight
    tecplot.sdk_version_info
:::
::::

PyTecplot adheres to the semantic versioning as outlined in [SemVer
2.0.0](https://semver.org/spec/v2.0.0.html){.reference .external} with
regard to backwards compatibility between releases. For this purpose,
the public interface of PyTecplot is defined as all entities (functions,
properties etc.) presented in the [HTML
documentation](https://www.tecplot.com/docs/pytecplot/){.reference
.external} and does not include methods in the code-base which do not
show up in the HTML documentation, even when a docstring is present. In
short, we will maintain backwards compatibility of the public interface
between all minor releases of the same major version with the exception
of internal changes that fix incorrect behavior or bugs.
:::::::::::
::::::::::::

::::::::::::::::::::: {#session .section}
## [Session](#id6){.toc-backref role="doc-backlink"}[¶](#session "Link to this heading"){.headerlink}

- [tecplot.session](#module-tecplot.session){#id9 .reference .internal}

- [session.suspend()](#session-suspend){#id10 .reference .internal}

- [session.suspend_enter()](#session-suspend-enter){#id11 .reference
  .internal}

- [session.suspend_exit()](#session-suspend-exit){#id12 .reference
  .internal}

- [session.clear_suspend()](#session-clear-suspend){#id13 .reference
  .internal}

- [session.connect()](#session-connect){#id14 .reference .internal}

- [session.connected()](#session-connected){#id15 .reference .internal}

- [session.disconnect()](#session-disconnect){#id16 .reference
  .internal}

- [session.redraw()](#session-redraw){#id17 .reference .internal}

- [session.stop()](#session-stop){#id18 .reference .internal}

- [session.acquire_license()](#session-acquire-license){#id19 .reference
  .internal}

- [session.release_license()](#session-release-license){#id20 .reference
  .internal}

- [session.start_roaming()](#session-start-roaming){#id21 .reference
  .internal}

- [session.stop_roaming()](#session-stop-roaming){#id22 .reference
  .internal}

- [session.license_expiration()](#session-license-expiration){#id23
  .reference .internal}

- [session.tecplot_install_directory()](#session-tecplot-install-directory){#id24
  .reference .internal}

- [session.tecplot_examples_directory()](#session-tecplot-examples-directory){#id25
  .reference .internal}

:::: {#module-tecplot.session .section}
[]{#tecplot-session}

### [tecplot.session](#id9){.toc-backref role="doc-backlink"}[¶](#module-tecplot.session "Link to this heading"){.headerlink}

Tecplot Engine State and [Tecplot 360
License](https://my.tecplot.com){.reference .external} Management

The [[`session`{.xref .any .py .py-mod .docutils .literal
.notranslate}]{.pre}](#module-tecplot.session "tecplot.session"){.reference
.internal} module contains methods used to manipulate the Tecplot Engine
such as notification of a [[State Changes]{.std
.std-ref}](#state-change){.reference .internal} that was done such as
adding or modifying data. It also contains methods for acquiring and
releasing the [Tecplot 360 License](https://my.tecplot.com){.reference
.external}.

::: {#state-changes .section}
[]{#state-change}

#### State Changes[¶](#state-changes "Link to this heading"){.headerlink}

State changes are the method for propagating information when an event
occurs. A state change can be triggered by many events. Examples
include: loading a data file, changing the color of a mesh plot,
creating a new zone, or changing the plot type.

In general, state changes are already handled internally after each call
to the PyTecplot API. This can cause a script that performs many
operations, especially those that alter data, to run slowly since the
Tecplot Engine must update it's internal state every time a state change
is received. To speed up such scripts, it may be necessary to use the
[[`tecplot.session.suspend()`{.xref .any .py .py-func .docutils .literal
.notranslate}]{.pre}](#tecplot.session.suspend "tecplot.session.suspend"){.reference
.internal} context. This will collect state changes for any operation
performed and will emit the required state changes only upon exit of the
context.

Using the [[`tecplot.session.suspend()`{.xref .any .py .py-func
.docutils .literal
.notranslate}]{.pre}](#tecplot.session.suspend "tecplot.session.suspend"){.reference
.internal} context in combination with Python's "-OO" flag which removes
many run-time checks in the PyTecplot API is the recommended way to run
a PyTecplot script which requires faster execution time. The user should
be aware that, when using the "-OO" flag, errors may not be recoverable
by the Tecplot Engine.
:::
::::

::: {#session-suspend .section}
### [session.suspend()](#id10){.toc-backref role="doc-backlink"}[¶](#session-suspend "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[suspend]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#suspend){.reference .internal}[¶](#tecplot.session.suspend "Link to this definition"){.headerlink}

:   Suspend the Tecplot engine and graphical interface.

    This context may speed up several types of operations including the
    creation of zones, filling or alterating the underlying data and the
    setup of complex styles. It will put Tecplot 360 into a "suspended"
    state such that the engine (in batch mode) or the graphical
    interface (in connected mode) will not try to keep up with the
    operations issued from Python. Upon exit of this context, the
    Tecplot 360 will be notified of any data alterations that have
    occured and the interface will be updated accordingly.

    See the [[State Changes]{.std .std-ref}](#state-change){.reference
    .internal} section for more information about how the [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} is updated when style or data is changed from a PyTecplot
    script.

    Example usage where [[`data`{.xref .any .py .py-mod .docutils
    .literal
    .notranslate}]{.pre}](tecplot.data.html#module-tecplot.data "tecplot.data"){.reference
    .internal} is some user-provided data -- see the examples under
    [`pytecplot/examples/working_with_datasets`{.docutils .literal
    .notranslate}]{.pre} folder within the Teplot 360 installation for
    more information.:

    :::: {.highlight-python .notranslate}
    ::: highlight
        fr = tp.active_frame()
        with tp.session.suspend():
            ds = fr.create_dataset('Data', ['x', 'y', 'z'])
            zn = ds.add_ordered_zone('Zone', (10, 10, 10))
            zn.values('x')[:] = data[0]
            zn.values('y')[:] = data[1]
            zn.values('z')[:] = data[2]
        fr.plot_type = tp.constant.PlotType.Cartesian3D
    :::
    ::::

    ::: versionadded
    [New in version 2018.2: ]{.versionmodified .added}The suspend
    context, when used in connected mode, requires Tecplot 360 2018 R2
    or later to realize the full performance benefits though this will
    still provide some performance improvements with older versions of
    Tecplot 360.
    :::
:::

::: {#session-suspend-enter .section}
### [session.suspend_enter()](#id11){.toc-backref role="doc-backlink"}[¶](#session-suspend-enter "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[suspend_enter]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#suspend_enter){.reference .internal}[¶](#tecplot.session.suspend_enter "Link to this definition"){.headerlink}

:   Free-function equivalent to entering the [[`suspend`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.suspend "tecplot.session.suspend"){.reference
    .internal} context.

    This is an example of calling *a previously defined function*
    [`do_work()`{.docutils .literal .notranslate}]{.pre} within a
    suspend context, using [`try/finally`{.docutils .literal
    .notranslate}]{.pre} to ensure the context is properly cleared:

    :::: {.doctest .highlight-default .notranslate}
    ::: highlight
        >>> try:
        >>>     tp.session.suspend_enter()
        >>>     do_work()
        >>> finally:
        >>>     tp.session.suspend_exit()
    :::
    ::::
:::

::: {#session-suspend-exit .section}
### [session.suspend_exit()](#id12){.toc-backref role="doc-backlink"}[¶](#session-suspend-exit "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[suspend_exit]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#suspend_exit){.reference .internal}[¶](#tecplot.session.suspend_exit "Link to this definition"){.headerlink}

:   Free-function equivalent to exiting the [[`suspend`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.suspend "tecplot.session.suspend"){.reference
    .internal} context.

    This must only be used following a call to
    [[`tecplot.session.suspend_enter()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.suspend_enter "tecplot.session.suspend_enter"){.reference
    .internal} and cannot be used within a
    [[`tecplot.session.suspend()`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.session.suspend "tecplot.session.suspend"){.reference
    .internal} context block.
:::

::: {#session-clear-suspend .section}
### [session.clear_suspend()](#id13){.toc-backref role="doc-backlink"}[¶](#session-clear-suspend "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[clear_suspend]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#clear_suspend){.reference .internal}[¶](#tecplot.session.clear_suspend "Link to this definition"){.headerlink}

:   Break out of suspended mode when connected to Tecplot 360.

    Forcibly clears the suspend state of the Tecplot 360 interface. This
    will cause the [[TecUtil Server]{.std
    .std-ref}](../install.html#tecutilserver){.reference .internal} to
    break out of a suspended state which may have been the result of a
    script not properly exiting from a [[`suspend()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.suspend "tecplot.session.suspend"){.reference
    .internal} context, possibly due to a segmentation fault. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        tecplot.session.connect()
        tecplot.session.clear_suspend()
    :::
    ::::
:::

::: {#session-connect .section}
### [session.connect()](#id14){.toc-backref role="doc-backlink"}[¶](#session-connect "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[connect]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[host]{.pre}]{.n}[[=]{.pre}]{.o}[[\'localhost\']{.pre}]{.default_value}*, *[[port]{.pre}]{.n}[[=]{.pre}]{.o}[[7600]{.pre}]{.default_value}*, *[[timeout]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[quiet]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#connect){.reference .internal}[¶](#tecplot.session.connect "Link to this definition"){.headerlink}

:   Connect this PyTecplot to a running instance of Tecplot 360.

    Parameters[:]{.colon}

    :   - **host** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- The host name or IP address of the
          machine running Tecplot 360 with the [[TecUtil Server]{.std
          .std-ref}](../install.html#tecutilserver){.reference
          .internal} addon loaded and listening. (default: localhost)

        - **port** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The port used by the running Tecplot
          360 instance. (default: 7600)

        - **timeout** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Number of seconds to wait before
          giving up. (default: 10)

        - **quiet** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Suppress status messages sent to the
          console. Exception messages will still be presented on errors.
          (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    This will connect the running python script to Tecplot 360, sending
    requests over the network. The [[TecUtil Server]{.std
    .std-ref}](../install.html#tecutilserver){.reference .internal}
    addon must be loaded and the server must be accepting requests. To
    turn on the server in Tecplot 360, go to the main menu, click on
    "Scripting -\> PyTecplot Connections...", and finally check the
    option to "Accept connections." Make sure the same port is used in
    both Tecplot 360 and the python script. For more information, see
    [[Requirements for Connecting to Tecplot 360 GUI]{.std
    .std-ref}](../install.html#connections){.reference .internal}
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.session.connect(port=7600)
        Connecting to Tecplot 360 TecUtil Server on:
            tcp://localhost:7600
        Connection established.
    :::
    ::::

    To activate the [[TecUtil Server]{.std
    .std-ref}](../install.html#tecutilserver){.reference .internal}
    addon in Tecplot 360 on start-up, first create a macro file, named
    something like: *startTecUtilServer.mcr*, with the following
    content:

    :::: {.highlight-none .notranslate}
    ::: highlight
        #!MC 1410
        $!EXTENDEDCOMMAND
            COMMANDPROCESSORID = "TecUtilServer"
            COMMAND = R"(
                AcceptRequests = Yes
                ListenOnAddress = localhost
                ListenOnPort = 7600
            )"
    :::
    ::::

    Then run Tecplot 360 from a command console with this file as one of
    the arguments:

    :::: {.highlight-python .notranslate}
    ::: highlight
        > tec360 startTecUtilServer.mcr
    :::
    ::::

    ::::: {.admonition .warning}
    Warning

    Adding the macro command above may cause a port binding conflict
    when using multiple instances of Tecplot 360. A single port can only
    be bound to one instance of the [[TecUtil Server]{.std
    .std-ref}](../install.html#tecutilserver){.reference .internal}. You
    may still add this to the [`tecplot.add`{.docutils .literal
    .notranslate}]{.pre} file which will be run everytime, but it must
    only be activated when Tecplot 360 is running interactively, i.e.
    not in batch mode. To do this, check the value of
    [`|INBATCHMODE|`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-none .notranslate}
    ::: highlight
        $!IF |INBATCHMODE| == 0
            $!EXTENDEDCOMMAND
                COMMANDPROCESSORID = "TecUtilServer"
                COMMAND = R"(
                    AcceptRequests = Yes
                    ListenOnAddress = localhost
                    ListenOnPort = 7600
                )"
        $!ENDIF
    :::
    ::::
    :::::

    ::: versionadded
    [New in version 2017.3: ]{.versionmodified .added}PyTecplot
    connections requires Tecplot 360 2017 R3 or later.
    :::
:::

::: {#session-connected .section}
### [session.connected()](#id15){.toc-backref role="doc-backlink"}[¶](#session-connected "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[connected]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[timeout]{.pre}]{.n}[[=]{.pre}]{.o}[[5]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#connected){.reference .internal}[¶](#tecplot.session.connected "Link to this definition"){.headerlink}

:   Check if PyTecplot is connected to a running instance of Tecplot
    360.

    This method sends a handshake message to the [[TecUtil Server]{.std
    .std-ref}](../install.html#tecutilserver){.reference .internal} and
    waits for a successful reply, timing out in the number of seconds
    specified.

    Parameters[:]{.colon}

    :   **timeout** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, optional) -- Number of seconds to wait before giving
        up. (default: 5)

    ::: versionadded
    [New in version 2017.3: ]{.versionmodified .added}of Tecplot 360
    PyTecplot connections requires Tecplot 360 2017 R3 or later.
    :::
:::

::: {#session-disconnect .section}
### [session.disconnect()](#id16){.toc-backref role="doc-backlink"}[¶](#session-disconnect "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[disconnect]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[quit]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#disconnect){.reference .internal}[¶](#tecplot.session.disconnect "Link to this definition"){.headerlink}

:   Disconnect from a running instance of Tecplot 360.

    Parameters[:]{.colon}

    :   **quit** ([[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}, optional) -- Attempt to quit and close the instance
        of Tecplot 360 before disconnecting.

    ::: versionadded
    [New in version 2017.3: ]{.versionmodified .added}PyTecplot
    connections requires Tecplot 360 2017 R3 or later.
    :::
:::

::: {#session-redraw .section}
### [session.redraw()](#id17){.toc-backref role="doc-backlink"}[¶](#session-redraw "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[redraw]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#redraw){.reference .internal}[¶](#tecplot.session.redraw "Link to this definition"){.headerlink}

:   Force a refresh of all plots on the screen (connected mode only).

    Forcibly updates all plots and renders everything to the screen.
    This is useful when connected to a live instance of Tecplot 360
    where updates faster than one second (the default) is desired. This
    command is ignored in batch mode.

    Eample usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        for i in range(10):
            zone.values('s')[:] = new_data
            tp.session.redraw() # force redraw on screen before continuing script
    :::
    ::::

    ::: versionadded
    [New in version 1.7: ]{.versionmodified .added}[[`redraw()`{.xref
    .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.redraw "tecplot.session.redraw"){.reference
    .internal} added in PyTecplot 1.7.0.
    :::

    ::: versionadded
    [New in version 2025.1: ]{.versionmodified .added}Forcing a redraw
    is supported in Tecplot 360 2025 R1 and later. For earlier versions
    of Tecplot 360, the redraw is deferred but guaranteed to happen
    within one second after the call.
    :::
:::

::: {#session-stop .section}
### [session.stop()](#id18){.toc-backref role="doc-backlink"}[¶](#session-stop "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[stop]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#stop){.reference .internal}[¶](#tecplot.session.stop "Link to this definition"){.headerlink}

:   Releases the [Tecplot 360
    License](https://my.tecplot.com){.reference .external} and shuts
    down Tecplot Engine.

    This shuts down the Tecplot Engine and releases the [Tecplot 360
    License](https://my.tecplot.com){.reference .external}. Call this
    function when your script is finished using PyTecplot. Calling this
    function is not required. If you do not call this function, it will
    be called automatically when your script exists. However, the
    [Tecplot 360 License](https://my.tecplot.com){.reference .external}
    will not be released until you call this function.

    This method is silently ignored when connected to a running instance
    of [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} (see [[`tecplot.session.connect()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.connect "tecplot.session.connect"){.reference
    .internal}).

    Note that stop() may only be called once during the life of a Python
    session. If it has already been called, subsequent calls do nothing:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # Shutdown tecplot and release license
        >>> tecplot.session.stop()
    :::
    ::::

    See also: [[`tecplot.session.acquire_license()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.acquire_license "tecplot.session.acquire_license"){.reference
    .internal}, [[`tecplot.session.release_license()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.release_license "tecplot.session.release_license"){.reference
    .internal}.
:::

::: {#session-acquire-license .section}
### [session.acquire_license()](#id19){.toc-backref role="doc-backlink"}[¶](#session-acquire-license "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[acquire_license]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#acquire_license){.reference .internal}[¶](#tecplot.session.acquire_license "Link to this definition"){.headerlink}

:   Attempts to acquire the [Tecplot 360
    License](https://my.tecplot.com){.reference .external}

    Call this function to attempt to acquire a [Tecplot 360
    License](https://my.tecplot.com){.reference .external}. If Tecplot
    Engine is not started, this function will start the Tecplot Engine
    before attempting to acquire a license.

    This function can be used to re-acquire a license that was released
    with [[`tecplot.session.release_license`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.release_license "tecplot.session.release_license"){.reference
    .internal}.

    If the Tecplot Engine is currently running, and a [Tecplot 360
    License](https://my.tecplot.com){.reference .external} has already
    been acquired, this function has no effect.

    Licenses may be acquired and released any number of times during the
    same Python session.

    Raises [[`TecplotLicenseError`{.xref .any .py .py-exc .docutils
    .literal
    .notranslate}]{.pre}](tecplot.exceptions.html#tecplot.exception.TecplotLicenseError "tecplot.exception.TecplotLicenseError"){.reference
    .internal} if a valid license could not be acquired.

    ::::::: {.admonition .note}
    Note

    Warning emitted when close to expiration date.

    A warning is emitted using Python's built-in [[`warnings`{.xref .any
    .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/warnings.html#module-warnings "(in Python v3.13)"){.reference
    .external} module if you are within 30 days of your TecPLUS
    subscription expiration date. The message will look like this:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        $ python
        >>> import tecplot
        >>> tecplot.session.acquire_license()
        /path/to/tecutil_connector.py:458: UserWarning:
        Your Tecplot software maintenance subscription
        (TecPLUS) will expire in **13 days**, after which you
        will no longer be able to use PyTecplot. Contact
        sales@tecplot.com to renew your TecPLUS subscription.

          warn(warning_msg)
    :::
    ::::

    These warnings can be suppressed by using the [`-W`{.docutils
    .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`ignore`{.docutils .literal .notranslate}]{.pre}
    option when invoking the python interpreter:

    :::: {.highlight-shell .notranslate}
    ::: highlight
        $ python -W ignore
        >>> import tecplot
        >>> tecplot.session.acquire_license()
    :::
    ::::
    :::::::

    See also: [[`tecplot.session.release_license()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.release_license "tecplot.session.release_license"){.reference
    .internal}

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import tecplot
        >>> # Do useful things
        >>> tecplot.session.release_license()
        >>> # Do time-consuming things not related to |PyTecplot|
        >>> tecplot.session.acquire_license()  # re-acquire the license
        >>> # Do useful |PyTecplot| related things.
    :::
    ::::
:::

::: {#session-release-license .section}
### [session.release_license()](#id20){.toc-backref role="doc-backlink"}[¶](#session-release-license "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[release_license]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#release_license){.reference .internal}[¶](#tecplot.session.release_license "Link to this definition"){.headerlink}

:   Attempts to release the [Tecplot 360
    License](https://my.tecplot.com){.reference .external}

    Call this to release a [Tecplot 360
    License](https://my.tecplot.com){.reference .external}. Normally you
    do not need to call this function since
    [[`tecplot.session.stop()`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.session.stop "tecplot.session.stop"){.reference
    .internal} will call it for you when your script exists and the
    Python interpreter is unloaded.

    This function can be used to release a license so that the license
    is available to other instances of [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external}.

    If the [Tecplot 360 License](https://my.tecplot.com){.reference
    .external} has already been released, this function has no effect.

    Licenses may be acquired and released any number of times during the
    same Python session. This method is silently ignored when connected
    to a running instance of [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} (see [[`tecplot.session.connect()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.connect "tecplot.session.connect"){.reference
    .internal}).

    See also: [[`tecplot.session.acquire_license()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.acquire_license "tecplot.session.acquire_license"){.reference
    .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import tecplot
        >>> # Do useful things
        >>> tecplot.session.release_license()
        >>> # Do time-consuming things not related to |PyTecplot|
        >>> tecplot.session.acquire_license()  # re-acquire the license
        >>> # Do useful |PyTecplot| related things.
    :::
    ::::
:::

::: {#session-start-roaming .section}
### [session.start_roaming()](#id21){.toc-backref role="doc-backlink"}[¶](#session-start-roaming "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[start_roaming]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[days]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#start_roaming){.reference .internal}[¶](#tecplot.session.start_roaming "Link to this definition"){.headerlink}

:   Check out a roaming license.

    Parameters[:]{.colon}

    :   **days** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- Number of days to roam.

    This will acquire a PyTecplot license and then attempt to set it up
    for roaming. The maximum number of days one may roam is
    typically 90. This function can be called in an interactive terminal
    and will affect all subsequent uses of PyTecplot on the local
    machine. Do not forget to [[`release`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.stop_roaming "tecplot.session.stop_roaming"){.reference
    .internal} the roaming license to the server if you are finished
    roaming before the expiration date.

    See also: [[`tecplot.session.stop_roaming()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.stop_roaming "tecplot.session.stop_roaming"){.reference
    .internal}

    Example usage where [`YYYY-MM-DD`{.docutils .literal
    .notranslate}]{.pre} will be the date 10 days from when this code
    was executed:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.session.start_roaming(10)
        You have successfully checked out a roaming license of
        PyTecplot. This will be valid for 10 days until
        midnight of YYY-MM-DD.
        >>> tecplot.session.stop_roaming()
        Your PyTecplot roaming license has been checked in.
    :::
    ::::
:::

::: {#session-stop-roaming .section}
### [session.stop_roaming()](#id22){.toc-backref role="doc-backlink"}[¶](#session-stop-roaming "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[stop_roaming]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[force]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#stop_roaming){.reference .internal}[¶](#tecplot.session.stop_roaming "Link to this definition"){.headerlink}

:   Check in (release) a roaming license.

    This will check in and make available to others on the network a
    license that you previously checked out for roaming.

    See also: [[`tecplot.session.start_roaming()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.session.start_roaming "tecplot.session.start_roaming"){.reference
    .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.session.stop_roaming()
        Your PyTecplot roaming license has been checked in.
    :::
    ::::
:::

::: {#session-license-expiration .section}
### [session.license_expiration()](#id23){.toc-backref role="doc-backlink"}[¶](#session-license-expiration "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[license_expiration]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/session.html#license_expiration){.reference .internal}[¶](#tecplot.session.license_expiration "Link to this definition"){.headerlink}

:   Expiration date of the current license.

    Returns: [[`datetime.date`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.13)"){.reference
    .external}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(tecplot.session.license_expiration())
        1955-11-05
    :::
    ::::
:::

::: {#session-tecplot-install-directory .section}
### [session.tecplot_install_directory()](#id24){.toc-backref role="doc-backlink"}[¶](#session-tecplot-install-directory "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[tecplot_install_directory]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session.html#tecplot_install_directory){.reference .internal}[¶](#tecplot.session.tecplot_install_directory "Link to this definition"){.headerlink}

:   [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} installation directory.

    Top-level installation directory for [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external}. This will typically contain configuration files and the
    examples directory.

    This directory is platform-dependent and will contain configuration
    files and the examples directory:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot

        install_dir = tecplot.session.tecplot_install_directory()
        infile = os.path.join(install_dir, 'examples', 'SimpleData', 'SpaceShip.lpk')

        tecplot.load_layout(infile)
        tecplot.export.save_png('spaceship.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/spaceship.png"
    class="reference internal image-reference"><img
    src="../_images/spaceship.png" style="width: 300px;"
    alt="../_images/spaceship.png" /></a>
    </figure>

    ::: versionchanged
    [Changed in version 1.6: ]{.versionmodified .changed}This function
    now returns a [[`pathlib.Path`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
    .external} object instead of [[`str`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
    .external}.
    :::
:::

::: {#session-tecplot-examples-directory .section}
### [session.tecplot_examples_directory()](#id25){.toc-backref role="doc-backlink"}[¶](#session-tecplot-examples-directory "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[tecplot_examples_directory]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session.html#tecplot_examples_directory){.reference .internal}[¶](#tecplot.session.tecplot_examples_directory "Link to this definition"){.headerlink}

:   [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} examples directory.

    Examples directory that is typically installed with [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external}. This may be overridden with the TECPLOT_EXAMPLES
    environment variable.

    This directory is platform-dependent and by default contains the
    various examples shipped with [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot

        examples_dir = tecplot.session.tecplot_examples_directory()
        infile = os.path.join(examples_dir, 'SimpleData', 'F18.lay')

        tecplot.load_layout(infile)
        tecplot.export.save_png('load_example.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/load_example.png"
    class="reference internal image-reference"><img
    src="../_images/load_example.png" style="width: 300px;"
    alt="../_images/load_example.png" /></a>
    </figure>

    ::: versionchanged
    [Changed in version 1.6: ]{.versionmodified .changed}This function
    now returns a [[`pathlib.Path`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
    .external} object instead of [[`str`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
    .external}.
    :::
:::
:::::::::::::::::::::

:::::: {#configuration .section}
## [Configuration](#id7){.toc-backref role="doc-backlink"}[¶](#configuration "Link to this heading"){.headerlink}

[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[configuration]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.session.tecplot.session.configuration "Link to this definition"){.headerlink}

:   Run-time configuration parameters can be accessed and changed
    through the configuration instance returned by
    [`tecplot.session.configuration()`{.docutils .literal
    .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> conf = tecplot.session.configuration()
        >>> print(conf.latex.command)
        pdflatex -interaction=batchmode -output-directory=@OUTDIR @INFILE
        >>> conf.latex.preamble = '\usepackage{amsmath}'
    :::
    ::::

The default settings have been tested with MiKTeX and TeXLive engines
and should work without the need for any changes to the session
configuration. However, you may wish to change the LaTeX packages which
are loaded by default or use a different LaTeX engine. See the Tecplot
user manual for guidance in changing your LaTeX configuration file so
changes persist across sessions.

Available configuration parameters:

- [[`latex.command`{.docutils .literal
  .notranslate}]{.pre}](#latex-command){#id26 .reference .internal}

- [[`latex.dvipng_command`{.docutils .literal
  .notranslate}]{.pre}](#latex-dvipng-command){#id27 .reference
  .internal}

- [[`latex.preamble`{.docutils .literal
  .notranslate}]{.pre}](#latex-preamble){#id28 .reference .internal}

::: {#latex-command .section}
### [[`latex.command`{.docutils .literal .notranslate}]{.pre}](#id26){.toc-backref role="doc-backlink"}[¶](#latex-command "Link to this heading"){.headerlink}

The system command used to compile LaTeX text objects. Parameters
[`@OUTDIR`{.docutils .literal .notranslate}]{.pre} and
[`@INFILE`{.docutils .literal .notranslate}]{.pre} are replaced with
appropriate strings to coordinate the creation of the final rendered
text.

Type:

:   [[`str`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
    .external}

Default:

:   "latex -interaction=batchmode -output-directory=@OUTDIR \@INFILE"
:::

::: {#latex-dvipng-command .section}
### [[`latex.dvipng_command`{.docutils .literal .notranslate}]{.pre}](#id27){.toc-backref role="doc-backlink"}[¶](#latex-dvipng-command "Link to this heading"){.headerlink}

The system command used to convert the output from the LaTeX command
from DVI to PNG. The parameters [`@DPI`{.docutils .literal
.notranslate}]{.pre}, [`@PAGERANGE`{.docutils .literal
.notranslate}]{.pre}, [`@OUTFILE`{.docutils .literal
.notranslate}]{.pre} and [`@INFILE`{.docutils .literal
.notranslate}]{.pre} are replaced with appropriate strings to coordinate
the creation fo the final rendered text.

Type:

:   [[`str`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
    .external}

Default:

:   "dvipng -bg Transparent -D \@DPI -pp \@PAGERANGE -T tight -o
    \@OUTFILE \@INFILE"
:::

::: {#latex-preamble .section}
### [[`latex.preamble`{.docutils .literal .notranslate}]{.pre}](#id28){.toc-backref role="doc-backlink"}[¶](#latex-preamble "Link to this heading"){.headerlink}

Code that will be placed before the [`\begin{document}`{.docutils
.literal .notranslate}]{.pre} section of the LaTeX source to be
compiled. This primarily used for loading LaTeX packages.

Type:

:   [[`str`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
    .external}

Default:

:   "\\usepackage{amsfonts}\\usepackage{amsmath}\\usepackage{amssymb}\\usepackage{amsthm}"
:::
::::::

::: {#miscellaneous .section}
## [Miscellaneous](#id8){.toc-backref role="doc-backlink"}[¶](#miscellaneous "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.tecutil.]{.pre}]{.sig-prename .descclassname}[[Index]{.pre}]{.sig-name .descname}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/tecutil/util.html#Index){.reference .internal}[¶](#tecplot.tecutil.Index "Link to this definition"){.headerlink}

:   Position identifier type.

    This type is used internally to represent a position in a list. It
    is used to indicate that a change between zero-based indexing and
    one-based indexing must occur at the TecUtil boundary.

    This type can be treated exactly like a Python native [[`int`{.xref
    .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external} and is only meaningful internally to the tecplot Python
    module.

<!-- -->

*[class]{.pre}[ ]{.w}*[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[IndexRange]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[parent]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[svargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/style.html#IndexRange){.reference .internal}[¶](#tecplot.session.IndexRange "Link to this definition"){.headerlink}

:   Index range specification along some axis.

    This is similar to Python's [[`slice`{.xref .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#slice "(in Python v3.13)"){.reference
    .external} object except that [`max`{.docutils .literal
    .notranslate}]{.pre} is included in the evaluated indexes. Here are
    some things to note:

    > <div>
    >
    > - All indices start with 0 and go to some maximum index
    >   [`m`{.docutils .literal .notranslate}]{.pre}.
    >
    > - Negative values represent the indexes starting with the maximum
    >   at -1 and continuing back to the beginning of the range.
    >
    > - A step of [[`None`{.xref .any .docutils .literal
    >   .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    >   .external}, 0 and 1 are all equivalent and mean that no elements
    >   are skipped.
    >
    > - A negative step indicates a skip less than the maximum.
    >
    > </div>

    ::: versionchanged
    [Changed in version 1.1: ]{.versionmodified .changed}**(Bug fix)**
    [`IndexRange`{.docutils .literal .notranslate}]{.pre} max value of
    zero is now interpreted as the first index in the range instead of
    the last index. Prior to version 1.1, the [`max`{.docutils .literal
    .notranslate}]{.pre} parameter interpreted zero to be the end of the
    range instead of the first element. This meant that an
    [`IndexRange`{.docutils .literal .notranslate}]{.pre} of
    [`(0,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`0,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`1)`{.docutils .literal .notranslate}]{.pre} would
    represent the whole range instead of just the first item. The
    standard way to represent the entire index
    :::
:::
::::::::::::::::::::::::::::::::::::::::::::

::: clearer
:::
::::::::::::::::::::::::::::::::::::::::::::::
