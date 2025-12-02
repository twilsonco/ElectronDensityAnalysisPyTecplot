:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#installation .section}
[]{#id1}

# Installation[¶](#installation "Link to this heading"){.headerlink}

- [Python and Tecplot](#python-and-tecplot){#id27 .reference .internal}

  - [Package Installer](#package-installer){#id28 .reference .internal}

  - [Connecting PyTecplot to Tecplot 360
    GUI](#connecting-pytecplot-to-tecplot-360-gui){#id29 .reference
    .internal}

  - [TecUtil Server](#tecutil-server){#id30 .reference .internal}

- [Windows](#windows){#id31 .reference .internal}

  - [Installation](#id2){#id32 .reference .internal}

  - [Environment Setup](#environment-setup){#id33 .reference .internal}

  - [Updating](#updating){#id34 .reference .internal}

- [Linux](#linux){#id35 .reference .internal}

  - [Installation](#id6){#id36 .reference .internal}

  - [Environment Setup (Batch
    Only)](#environment-setup-batch-only){#id37 .reference .internal}

  - [Updating](#id13){#id38 .reference .internal}

- [macOS](#macos){#id39 .reference .internal}

  - [Installation](#id14){#id40 .reference .internal}

  - [Environment Setup (Batch Only)](#id22){#id41 .reference .internal}

  - [Updating](#id23){#id42 .reference .internal}

  - [System Integrity Protection
    (SIP)](#system-integrity-protection-sip){#id43 .reference .internal}

- [Troubleshooting](#troubleshooting){#id44 .reference .internal}

- [Version Information](#version-information){#id45 .reference
  .internal}

::::::: {#python-and-tecplot .section}
## [Python and Tecplot](#id27){.toc-backref role="doc-backlink"}[¶](#python-and-tecplot "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

Software Requirements

- [Tecplot 360](https://www.tecplot.com/products/tecplot-360){.reference
  .external} *2020 R1 or later*

- [Python](https://www.python.org/downloads/){.reference .external} *(64
  bit) 3.9 or later*

*Required Python Modules (normally installed by pip - see below):*

> <div>
>
> - [pyzmq](https://pypi.org/project/pyzmq){.reference .external}
>
> - [protobuf](https://pypi.org/project/protobuf){.reference .external}
>
> </div>

*Optional Python Modules:*

> <div>
>
> - [numpy](https://www.numpy.org){.reference .external} (Recommended
>   for better performance of data operations)
>
> - [ipython](https://ipython.org){.reference .external}
>
> - [pillow](https://python-pillow.org){.reference .external}
>
> </div>
:::

PyTecplot is supported on the three latest releases of Python, 64-bit
only. PyTecplot does not support 32 bit Python. Interacting with the
Tecplot Engine requires a valid [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
installation and [Tecplot 360
License](https://my.tecplot.com){.reference .external} with
[TecPLUS™](https://www.tecplot.com/products/software-maintenance-services){.reference
.external} maintenance service. Visit
[https://www.tecplot.com](https://www.tecplot.com){.reference .external}
for more information about purchasing [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}.

For all platforms, the [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
application must be run once to establish a licensing method. This will
be used when running any script which uses the python *tecplot* module.

::: {#package-installer .section}
### [Package Installer](#id28){.toc-backref role="doc-backlink"}[¶](#package-installer "Link to this heading"){.headerlink}

It is recommended to use [pip](https://pip.pypa.io){.reference
.external} to install PyTecplot, along with all of the dependencies,
from Python's official [PyPI
servers](https://pypi.python.org/pypi/pytecplot){.reference .external}.
The installer, [pip](https://pip.pypa.io){.reference .external}, is a
python module that can be executed directly (from a console) and is part
of the core modules that come with recent version of Python. Please
refer to [pip's documentation](https://pip.pypa.io){.reference
.external} for information if you have issues using
[pip](https://pip.pypa.io){.reference .external}.

Depending on the options you set when installing Python, you may already
have the folder containing [pip](https://pip.pypa.io){.reference
.external} in your [`PATH`{.docutils .literal .notranslate}]{.pre}
environment variable. If this is the case, then you may use
[pip](https://pip.pypa.io){.reference .external} directly instead of
prepending it with [`python`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-m`{.docutils
.literal .notranslate}]{.pre} like we show in the following commands.
:::

::: {#connecting-pytecplot-to-tecplot-360-gui .section}
[]{#connections}

### [Connecting PyTecplot to Tecplot 360 GUI](#id29){.toc-backref role="doc-backlink"}[¶](#connecting-pytecplot-to-tecplot-360-gui "Link to this heading"){.headerlink}

Python scripts that use the PyTecplot package normally run in "batch"
mode. That is, PyTecplot starts it's own Tecplot Engine, thus
interfacing directly with the underlying libraries allows fast execution
of a user's scripts. PyTecplot also has the capability to connect to a
running instance of Tecplot 360 through the TecUtil Server addon.
Connections can be made from the local or a remote host and the GUI will
update as the script progresses, however commands are passed through
sockets and there is a high overhead cost that will cause the script to
be much slower than in batch mode.

In Tecplot 360, the TecUtil Server addon must be loaded and "listening"
on a specific port (click on "Scripting -\> PyTecplot Connections...",
the default port is 7600). Then in the script, the user can call
[[`tecplot.session.connect()`{.xref .any .py .py-func .docutils .literal
.notranslate}]{.pre}](api/tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
.internal} to make the connection and the script will send all following
commands to the running Tecplot 360.
:::

::: {#tecutil-server .section}
[]{#tecutilserver}

### [TecUtil Server](#id30){.toc-backref role="doc-backlink"}[¶](#tecutil-server "Link to this heading"){.headerlink}

Tecplot 360 includes and loads by default the "TecUtil Server" addon,
however it is not active on start-up. As mentioned above, it must be
turned on by going through the "Scripting -\> PyTecplot Connections..."
dialog in Tecplot 360 or via a macro command as described in the
PyTecplot documentation for [[`tecplot.session.connect()`{.xref .any .py
.py-func .docutils .literal
.notranslate}]{.pre}](api/tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
.internal}.

This addon is a remote-procedure-call (RPC) interface to Tecplot 360's
Application Development Kit (ADK), otherwise known as the TecUtil Layer.
For details, please refer to the [ADK User's
Manual](https://tecplot.azureedge.net/products/360/2013r1m1/adkum.pdf){.reference
.external}. Because PyTecplot communicates with this addon over sockets,
it is capable of interacting on a remote machine running a potentially
different operating system. To open up the TecUtil Server to listen for
an incoming message from any remote host, uncheck the "Listen to
localhost only" option in the PyTecplot Connections dialog in Tecplot
360 or specify "\*" as the host in the macro command described in the
documentation for [[`tecplot.session.connect()`{.xref .any .py .py-func
.docutils .literal
.notranslate}]{.pre}](api/tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
.internal}.
:::
:::::::

:::::::::::::::::::::::: {#windows .section}
## [Windows](#id31){.toc-backref role="doc-backlink"}[¶](#windows "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

We recommend using the latest version of Python (64 bit) with Windows
since it comes with [pip](https://pip.pypa.io){.reference .external} and
will require the least amount of post-install configuration. The default
version of Python presented to Windows users is 32 bit which **will not
work** with PyTecplot. You will have to navigate [Python's download
page](https://www.python.org/downloads/windows){.reference .external} to
find the "x86-64" version.
:::

:::::::::::::: {#id2 .section}
### [Installation](#id32){.toc-backref role="doc-backlink"}[¶](#id2 "Link to this heading"){.headerlink}

Once Python is installed along with the
[pip](https://pip.pypa.io){.reference .external} module, you may install
PyTecplot from Python's official [PyPI
servers](https://pypi.python.org/pypi/pytecplot){.reference .external}
by opening a command console and running the following command with
**administrative privileges** if needed:

:::: {.highlight-shell .notranslate}
::: highlight
    python -m pip install pytecplot
:::
::::

::::: {#installing-from-local-source .section}
#### Installing from Local Source[¶](#installing-from-local-source "Link to this heading"){.headerlink}

For those with a restricted internet connection, it is neccessary to
"manually" install all the required dependencies as listed in the
section "Software Requirements" above. This ostensibly involves
downloading these packages from
[https://pypi.org/](https://pypi.org/){.reference .external},
transferring them to the target system and running [`python`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`setup.py`{.docutils .literal .notranslate}]{.pre} in
each. A compiler may be required if there are no pre-compiled binaries
for your specific operating system and Python version.

PyTecplot ships with [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
and can be found under the [`pytecplot`{.docutils .literal
.notranslate}]{.pre} directory. You may run pip from within this
directory to install pytecplot as follows. Note that "\[VERSION\]"
should be replaced with the installed version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
and the use of "." indicates the current working directory:

:::: {.highlight-shell .notranslate}
::: highlight
    cd "C:\Program Files\Tecplot\Tecplot 360 EX [VERSION]\pytecplot"
    python -m pip install .
:::
::::
:::::

::::: {#installing-without-administrative-privileges .section}
#### Installing Without Administrative Privileges[¶](#installing-without-administrative-privileges "Link to this heading"){.headerlink}

If you get a "permission denied" error, this likely means you are
attempting to install PyTecplot into a system-controlled Python package
directory. If this is what you want to do, then you must open the
command console with **administrative privileges**. Alternatively, you
may wish to install PyTecplot into your user-space or home directory.
This can be done by add the option [`--user`{.docutils .literal
.notranslate}]{.pre} to the install step (see the output of the command
[`python`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`-m`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`pip`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`help`{.docutils .literal .notranslate}]{.pre} for
details):

:::: {.highlight-shell .notranslate}
::: highlight
    python -m pip install --user pytecplot
:::
::::
:::::

::::: {#optional-dependencies .section}
#### Optional Dependencies[¶](#optional-dependencies "Link to this heading"){.headerlink}

All **required** dependencies will be installed along with PyTecplot.
There are optional dependencies such as
[Numpy](https://www.numpy.org){.reference .external} and
[IPython](https://ipython.org){.reference .external} which you may want
to install as well. These can be installed by appending
[`[extras]`{.docutils .literal .notranslate}]{.pre} to the installation
command:

:::: {.highlight-shell .notranslate}
::: highlight
    python -m pip install pytecplot[extras]
:::
::::
:::::
::::::::::::::

::::::: {#environment-setup .section}
### [Environment Setup](#id33){.toc-backref role="doc-backlink"}[¶](#environment-setup "Link to this heading"){.headerlink}

PyTecplot scripts can be run in two distinct modes: "batch" in which
PyTecplot manages it's own internal Tecplot 360 "engine," or "connected"
where the PyTecplot script communicates with a running instance of
Tecplot 360 through the "TecUtil Server." When running in "connected"
mode, see [[`tecplot.session.connect()`{.xref .any .py .py-func
.docutils .literal
.notranslate}]{.pre}](api/tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
.internal} for more details, no further environment setup is required.
Conversely, when running in "batch" mode, we need to use environment
variables to point to the installation of Tecplot 360.

Depending on the options you selected when installing [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}, you may need to setup your environment so PyTecplot can find
the dynamic libraries associated with the engine. If [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}'s bin directory is not already in the system's
[`PATH`{.docutils .literal .notranslate}]{.pre} list, you will have to
add it and make sure it is before any other [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
installation. With a standard installation of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}, the path is usually something like the following. Again,
"\[VERSION\]" should be replaced with the installed version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}:

:::: {.highlight-shell .notranslate}
::: highlight
    "C:\Program Files\Tecplot\Tecplot 360 EX [VERSION]\bin"
:::
::::

To view the current path, run the following command in the command
console:

:::: {.highlight-shell .notranslate}
::: highlight
    echo %PATH%
:::
::::

To edit it globally for all consoles you will have to navigate to
"Control Panel" -\> "System" -\> "Advanced System Settings" -\>
"Environment Variables". From there, you should find the
[`PATH`{.docutils .literal .notranslate}]{.pre} environment variable,
edit it, and click "OK"; no reboot is required. After changing the
[`PATH`{.docutils .literal .notranslate}]{.pre}, be sure to close and
re-open your console window.
:::::::

::::: {#updating .section}
### [Updating](#id34){.toc-backref role="doc-backlink"}[¶](#updating "Link to this heading"){.headerlink}

To update PyTecplot after you have already installed it once, you run
the same installation command with the option [`--upgrade`{.docutils
.literal .notranslate}]{.pre}. For example:

:::: {.highlight-shell .notranslate}
::: highlight
    python -m pip install --upgrade pytecplot
:::
::::

When installing a new version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}, you must ensure that the [`PATH`{.docutils .literal
.notranslate}]{.pre} environment variable gets updated accordingly.
:::::
::::::::::::::::::::::::

:::::::::::::::::::::::: {#linux .section}
## [Linux](#id35){.toc-backref role="doc-backlink"}[¶](#linux "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

We recommend using the operating system's package manager to install and
update Python along with [pip](https://pip.pypa.io){.reference
.external}. Once this is done, you can use [`sudo`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pip`{.docutils
.literal .notranslate}]{.pre} to manage the installation of system-wide
python modules.
:::

:::::::::::::: {#id6 .section}
### [Installation](#id36){.toc-backref role="doc-backlink"}[¶](#id6 "Link to this heading"){.headerlink}

Once Python is installed along with the
[pip](https://pip.pypa.io){.reference .external} module, you may install
PyTecplot from Python's official [PyPI
servers](https://pypi.python.org/pypi/pytecplot){.reference .external}
by running the following command with **root privileges (sudo)** if
needed:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install pytecplot
:::
::::

::::: {#id8 .section}
#### Installing from Local Source[¶](#id8 "Link to this heading"){.headerlink}

For those with a restricted internet connection, it is neccessary to
"manually" install all the required dependencies as listed in the
section "Software Requirements" above. This ostensibly involves
downloading these packages from
[https://pypi.org/](https://pypi.org/){.reference .external},
transferring them to the target system and running [`python`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`setup.py`{.docutils .literal .notranslate}]{.pre} in
each. A compiler may be required if there are no pre-compiled binaries
for your specific operating system and Python version.

PyTecplot ships with [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
and can be found under the [`pytecplot`{.docutils .literal
.notranslate}]{.pre} directory. You may run pip from within this
directory to install pytecplot as follows. Note the use of "." indicates
the current working directory:

:::: {.highlight-shell .notranslate}
::: highlight
    cd /path/to/tecplot360/pytecplot
    pip install .
:::
::::
:::::

::::: {#installing-without-root-access .section}
#### Installing Without Root Access[¶](#installing-without-root-access "Link to this heading"){.headerlink}

If you get a "permission denied" error, this likely means you are
attempting to install PyTecplot into a system-controlled Python package
directory. If this is what you want to do, then you must prepend the
above [pip](https://pip.pypa.io){.reference .external} command with
**sudo**. Alternatively, you may wish to install PyTecplot into your
user-space or home directory. This can be done by add the option
[`--user`{.docutils .literal .notranslate}]{.pre} to the install step
(see the output of the command [`pip`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`help`{.docutils .literal .notranslate}]{.pre} for
details):

:::: {.highlight-shell .notranslate}
::: highlight
    pip install --user pytecplot
:::
::::
:::::

::::: {#id10 .section}
#### Optional Dependencies[¶](#id10 "Link to this heading"){.headerlink}

All **required** dependencies will be installed along with PyTecplot.
There are optional dependencies such as
[Numpy](https://www.numpy.org){.reference .external} and
[IPython](https://ipython.org){.reference .external} which you may want
to install as well. These can be installed by appending
[`[extras]`{.docutils .literal .notranslate}]{.pre} to the installation
command:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install pytecplot[extras]
:::
::::
:::::
::::::::::::::

::::::: {#environment-setup-batch-only .section}
### [Environment Setup (Batch Only)](#id37){.toc-backref role="doc-backlink"}[¶](#environment-setup-batch-only "Link to this heading"){.headerlink}

PyTecplot scripts can be run in two distinct modes: "batch" in which
PyTecplot manages it's own internal Tecplot 360 "engine," or "connected"
where the PyTecplot script communicates with a running instance of
Tecplot 360 through the "TecUtil Server." When running in "connected"
mode, see [[`tecplot.session.connect()`{.xref .any .py .py-func
.docutils .literal
.notranslate}]{.pre}](api/tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
.internal} for more details, no further environment setup is required.
Conversely, when running in "batch" mode, PyTecplot needs to configure
and locate the dynamic libraries associated with the [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
engine. This is accomplished through several shell environment
variables.

Since the Tecplot 360 engine can be configured differently based on
rendering needs, such as whether or not an X server connection exists or
whether or not graphics drivers are available, it is best to setup the
environment for each execution of Python. This is the preferred method
so that the environment setup matches the [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
engine configuration. To configure the environment for each execution of
PyTecplot, use the [`tec360-env`{.docutils .literal .notranslate}]{.pre}
script shipped with [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
as follows:

:::: {.highlight-shell .notranslate}
::: highlight
    /path/to/tecplot360/bin/tec360-env [options] -- python [options]
:::
::::

Available options to the [`tec360-env`{.docutils .literal
.notranslate}]{.pre} script can be explored by supplying the
[`--help`{.docutils .literal .notranslate}]{.pre} flag. Notably the
[`--osmesa`{.docutils .literal .notranslate}]{.pre} flag allows for
image export without an X server connection or graphics drivers.

A shell's environment can be permanently configured for repeated
executions of Python so that PyTecplot can find the dynamic libraries
associated with the engine and configure it correctly. Typical usage is
to pass the output to the built-in shell command [`eval`{.docutils
.literal .notranslate}]{.pre}:

:::: {.highlight-shell .notranslate}
::: highlight
    eval `/path/to/tecplot360/bin/tec360-env [options]`
:::
::::

after which multiple executions of Python can be performed within the
configured shell environment.
:::::::

::::: {#id13 .section}
### [Updating](#id38){.toc-backref role="doc-backlink"}[¶](#id13 "Link to this heading"){.headerlink}

To update PyTecplot after you have already installed it once, you run
the same installation command with the option [`--upgrade`{.docutils
.literal .notranslate}]{.pre}. For example:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install --upgrade pytecplot
:::
::::

When installing a new version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}, you must ensure that the [`LD_LIBRARY_PATH`{.docutils
.literal .notranslate}]{.pre} environment variable gets updated
accordingly.
:::::
::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::: {#macos .section}
## [macOS](#id39){.toc-backref role="doc-backlink"}[¶](#macos "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

We highly recommend using a package management tool such as
[Macports](https://www.macports.org){.reference .external},
[Brew](https://brew.sh){.reference .external} or
[Fink](https://finkproject.org){.reference .external} to install and
update Python along with [pip](https://pip.pypa.io){.reference
.external}. Once this is done, you can use [`sudo`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`pip`{.docutils
.literal .notranslate}]{.pre} to manage the installation of system-wide
python modules.
:::

:::::::::::::: {#id14 .section}
### [Installation](#id40){.toc-backref role="doc-backlink"}[¶](#id14 "Link to this heading"){.headerlink}

Once Python is installed along with the
[pip](https://pip.pypa.io){.reference .external} module, you may install
PyTecplot from Python's official [PyPI
servers](https://pypi.python.org/pypi/pytecplot){.reference .external}
by running the following command with **root privileges (sudo)** if
needed:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install pytecplot
:::
::::

::::: {#id16 .section}
#### Installing from Local Source[¶](#id16 "Link to this heading"){.headerlink}

For those with a restricted internet connection, it is neccessary to
"manually" install all the required dependencies as listed in the
section "Software Requirements" above. This ostensibly involves
downloading these packages from
[https://pypi.org/](https://pypi.org/){.reference .external},
transferring them to the target system and running [`python`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`setup.py`{.docutils .literal .notranslate}]{.pre} in
each. A compiler may be required if there are no pre-compiled binaries
for your specific operating system and Python version.

PyTecplot ships with [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
and can be found under the [`pytecplot`{.docutils .literal
.notranslate}]{.pre} directory. You may run pip from within this
directory to install pytecplot as follows. Note that "\[VERSION\]"
should be replaced with the installed version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
and the use of "." indicates the current working directory:

:::: {.highlight-shell .notranslate}
::: highlight
    cd "/Applications/Tecplot 360 EX [VERSION]/pytecplot"
    python -m pip install .
:::
::::
:::::

::::: {#id18 .section}
#### Installing Without Root Access[¶](#id18 "Link to this heading"){.headerlink}

If you get a "permission denied" error, this likely means you are
attempting to install PyTecplot into a system-controlled Python package
directory. If this is what you want to do, then you must prepend the
above [pip](https://pip.pypa.io){.reference .external} command with
**sudo**. Alternatively, you may wish to install PyTecplot into your
user-space or home directory. This can be done by add the option
[`--user`{.docutils .literal .notranslate}]{.pre} to the install step
(see the output of the command [`pip`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`help`{.docutils .literal .notranslate}]{.pre} for
details):

:::: {.highlight-shell .notranslate}
::: highlight
    pip install --user pytecplot
:::
::::
:::::

::::: {#id19 .section}
#### Optional Dependencies[¶](#id19 "Link to this heading"){.headerlink}

All **required** dependencies will be installed along with PyTecplot.
There are optional dependencies such as
[Numpy](https://www.numpy.org){.reference .external} and
[IPython](https://ipython.org){.reference .external} which you may want
to install as well. These can be installed by appending
[`[extras]`{.docutils .literal .notranslate}]{.pre} to the installation
command:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install pytecplot[extras]
:::
::::
:::::
::::::::::::::

:::::::::::::: {#id22 .section}
### [Environment Setup (Batch Only)](#id41){.toc-backref role="doc-backlink"}[¶](#id22 "Link to this heading"){.headerlink}

PyTecplot scripts can be run in two distinct modes: "batch" in which
PyTecplot manages it's own internal Tecplot 360 "engine," or "connected"
where the PyTecplot script communicates with a running instance of
Tecplot 360 through the "TecUtil Server." When running in "connected"
mode, see [[`tecplot.session.connect()`{.xref .any .py .py-func
.docutils .literal
.notranslate}]{.pre}](api/tecplot.session.html#tecplot.session.connect "tecplot.session.connect"){.reference
.internal} for more details, no further environment setup is required.
Conversely, when running in "batch" mode, PyTecplot needs to configure
and locate the dynamic libraries associated with the [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
engine. This is accomplished through several shell environment
variables.

It is best to setup the environment for each execution of Python. This
is the preferred method so that the environment setup matches the
[Tecplot 360](https://www.tecplot.com/products/tecplot-360){.reference
.external} engine configuration. To configure the environment for each
execution of PyTecplot, use the [`tec360-env`{.docutils .literal
.notranslate}]{.pre} script shipped with [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
as follows:

:::: {.highlight-shell .notranslate}
::: highlight
    "/Applications/Tecplot 360 EX [VERSION]/bin/tec360-env" -- python [options]
:::
::::

where [`[VERSION]`{.docutils .literal .notranslate}]{.pre} should be
replaced with the installed version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}.

::::: {.admonition .note}
Note

If you are on an Apple Silicon machine and running a version of 360
older than 2025.1 you must use the Intel-64 Python executable directly:

:::: {.highlight-shell .notranslate}
::: highlight
    "/Applications/Tecplot 360 EX [VERSION]/bin/tec360-env" -- python3-intel64 [options]
:::
::::
:::::

A shell's environment can be permanently configured for repeated
executions of Python so that PyTecplot can find the dynamic libraries
associated with the engine. Typical usage is to pass the output to the
built-in shell command [`eval`{.docutils .literal .notranslate}]{.pre}.
Note the full path is wrapped in quotes to allow for spaces:

:::: {.highlight-shell .notranslate}
::: highlight
    eval `"/Applications/Tecplot 360 EX [VERSION]/bin/tec360-env"`
:::
::::

At this point PyTecplot should be configured for use and you may try
running the "hello world" example. If for some reason the
[`tec360-env`{.docutils .literal .notranslate}]{.pre} script fails to
work, you may add by hand the [`Contents/MacOS`{.docutils .literal
.notranslate}]{.pre} directory to the dynamic library loader search
path. This involves setting the following environment variable (this is
what the [`eval`{.docutils .literal .notranslate}]{.pre} command above
does):

:::: {.highlight-shell .notranslate}
::: highlight
    export DYLD_LIBRARY_PATH="/Applications/Tecplot.../Contents/MacOS"
:::
::::

With a standard installation of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}, the "Tecplot..." above is usually something like the
following. Note that [`[VERSION]`{.docutils .literal
.notranslate}]{.pre} should be replaced with the installed version of
[Tecplot 360](https://www.tecplot.com/products/tecplot-360){.reference
.external}:

:::: {.highlight-shell .notranslate}
::: highlight
    "Tecplot 360 EX [VERSION]/Tecplot 360 EX [VERSION].app"
:::
::::

You can see what this environment variable is set to by running
[`echo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`$DYLD_LIBRARY_PATH`{.docutils .literal
.notranslate}]{.pre} in the terminal.
::::::::::::::

::::: {#id23 .section}
### [Updating](#id42){.toc-backref role="doc-backlink"}[¶](#id23 "Link to this heading"){.headerlink}

To update PyTecplot after you have already installed it once, you run
the same installation command with the option [`--upgrade`{.docutils
.literal .notranslate}]{.pre}. For example:

:::: {.highlight-shell .notranslate}
::: highlight
    pip install --upgrade pytecplot
:::
::::

When installing a new version of [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference
.external}, you must ensure that the [`DYLD_LIBRARY_PATH`{.docutils
.literal .notranslate}]{.pre} environment variable gets updated
accordingly.
:::::

::::::::::::::: {#system-integrity-protection-sip .section}
### [System Integrity Protection (SIP)](#id43){.toc-backref role="doc-backlink"}[¶](#system-integrity-protection-sip "Link to this heading"){.headerlink}

If you installed Python (and the pip module) using
[Macports](https://www.macports.org){.reference .external},
[Brew](https://brew.sh){.reference .external} or
[Fink](https://finkproject.org){.reference .external}, you should have
little trouble using PyTecplot. Please try running the "hello world"
example before continuing here.

Starting with macOS version 10.11, Apple has introduced a highly
restrictive protection agent which unsets the
[`DYLD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre} environment
variable when a sub process is created using a system-installed
executable such as [`/usr/bin/python`{.docutils .literal
.notranslate}]{.pre}. It is easily by-passed but requires some work on
the user's part. We present here two options: 1. Setting up a Python
virtual environment in user-space (the user's home directory) and 2.
disabling Apple's System Integrity Protection (SIP).

::::::::: {#using-a-python-virtual-environment .section}
#### Using a Python Virtual Environment[¶](#using-a-python-virtual-environment "Link to this heading"){.headerlink}

This is the less invasive option and has several advantages as it
isolates the installation of PyTecplot from the system. The user has
total control on which python modules are installed and there is no need
for elevated "root" privileges. However, there is overhead involved on
the user's part. Specifically, the user is now responsible for
installing all the python packages to be used and the environment will
have to "activated" before running any scripts that require it.

Please see the [official
documentation](https://docs.python.org/3/library/venv.html){.reference
.external} concerning Python virtual environments. In short, the
[`venv`{.docutils .literal .notranslate}]{.pre} Python module is used to
create a complete installation of Python in the user's home directory:

:::: {.highlight-shell .notranslate}
::: highlight
    python -m venv myenv
:::
::::

This creates a directory "myenv" and installs Python into it. The
virtual environment can now be activated by sourcing the "activate"
script under the [`myenv`{.docutils .literal .notranslate}]{.pre}
directory:

:::: {.highlight-shell .notranslate}
::: highlight
    source myenv/bin/activate
:::
::::

You should now have [`python`{.docutils .literal .notranslate}]{.pre}
and [pip](https://pip.pypa.io){.reference .external} pointing to this
directory:

:::: {.highlight-shell .notranslate}
::: highlight
    $ which python
    /Users/me/myenv/bin/python
    $ which pip
    /Users/me/myenv/bin/pip
:::
::::

From here, you should be able to install PyTecplot as discussed above
without root (sudo) requirements.
:::::::::

::::::: {#disabling-sip .section}
#### Disabling SIP[¶](#disabling-sip "Link to this heading"){.headerlink}

The system protection enforced by default on the newest versions of
macOS is controlled by the [`csrutil`{.docutils .literal
.notranslate}]{.pre} command which only allows you to change the
settings in recovery mode. To do this, you may follow these steps:

1.  Restart your Mac.

2.  Before macOS starts up, hold down Command-R and keep it held down
    until you see an Apple icon and a progress bar.

3.  From the Utilities menu, select Terminal.

4.  At the prompt, type [`csrutil`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`disable`{.docutils .literal .notranslate}]{.pre} and
    press Return.

5.  Reboot.

The status of SIP can be checked by the user without being in recovery
mode with the command:

:::: {.highlight-shell .notranslate}
::: highlight
    csrutil status
:::
::::

You can test the propagation of the [`DYLD_LIBRARY_PATH`{.docutils
.literal .notranslate}]{.pre} environment variable to the sub process by
running the following command which will print [`True`{.docutils
.literal .notranslate}]{.pre} or [`False`{.docutils .literal
.notranslate}]{.pre}:

:::: {.highlight-shell .notranslate}
::: highlight
    export DYLD_LIBRARY_PATH='test'
    /usr/bin/python -c 'import os;print("DYLD_LIBRARY_PATH" in os.environ)'
:::
::::
:::::::
:::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

::::::: {#troubleshooting .section}
## [Troubleshooting](#id44){.toc-backref role="doc-backlink"}[¶](#troubleshooting "Link to this heading"){.headerlink}

1.  Verify that you have installed and can run [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} version **2020 R1** *or later*.

2.  Verify that you are running 64 bit Python version [`3.8`{.docutils
    .literal .notranslate}]{.pre} or later.

3.  Verify that you have run [`python`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`-m`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`pip`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`install`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`pytecplot`{.docutils .literal .notranslate}]{.pre}
    with the correct python executable.

4.  Installing into the Python's [`site-packages`{.docutils .literal
    .notranslate}]{.pre} typically requires elevated privileges.
    Therefore the [`pip`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`install`{.docutils .literal .notranslate}]{.pre}
    command may need a [`sudo`{.docutils .literal .notranslate}]{.pre}
    or "Run as Administrator" type of environment. Alternatively, you
    may install PyTecplot and all of its dependencies into the user's
    home directory with [`pip`{.docutils .literal .notranslate}]{.pre}'s
    option: [`--user`{.docutils .literal .notranslate}]{.pre}.

5.  Make sure the directory pointed to by [`PATH`{.docutils .literal
    .notranslate}]{.pre}, [`LD_LIBRARY_PATH`{.docutils .literal
    .notranslate}]{.pre} or [`DYLD_LIBRARY_PATH`{.docutils .literal
    .notranslate}]{.pre} for Windows, Linux and macOS respectively
    exists and contains the Tecplot 360 executable and library files. If
    you are running pytecplot on Apple Silicon machines and are using an
    older version of 360 (version 2024.1 or older) make sure to use the
    Intel-64 version of the Python executable (typically
    python3-intel64). See the macOS specific installation notes above.

6.  Though the package is named "pytecplot" the actual python module
    that is imported is just "tecplot" - i.e. you should have "import
    tecplot" and not "import pytecplot" at the top of your scripts.

7.  If your script throws an exception when you attempt to call any
    pytecplot API, the most likely cause is a missing or invalid
    [Tecplot 360 License](https://my.tecplot.com){.reference .external}
    or an expired
    [TecPLUS™](https://www.tecplot.com/products/software-maintenance-services){.reference
    .external} maintenance service subscription. Run [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} and go to *Help* -\> *Tecplot 360 EX Licensing...* to
    verify the license is configured properly.

8.  If an attempt to uninstall PyTecplot using pip fails with a message
    like "No files were found to uninstall.", it may be that Python is
    picking up the tecplot module from either the current working
    directory or from a directory found in the [`PYTHONPATH`{.docutils
    .literal .notranslate}]{.pre} environment variable. Unsetting this
    variable or changing directories to one that does not contain a file
    named [`tecplot.py`{.docutils .literal .notranslate}]{.pre} nor a
    directory named [`tecplot`{.docutils .literal .notranslate}]{.pre}
    should allow you to uninstall PyTecplot.

9.  If PyTecplot was successfully installed but you are still getting a
    message like "ImportError: No module named tecplot", it may be that
    you installed PyTecplot into a different Python installation. Use
    [`python`{.docutils .literal .notranslate}]{.pre}` `{.docutils
    .literal .notranslate}[`-mpip`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`install`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`pytecplot`{.docutils .literal .notranslate}]{.pre} to
    ensure you install PyTecplot into the proper place. Also, be sure
    there are no stray files named "tecplot.py" or directories named
    "tecplot" either in the current working directory or in any of the
    directories listed in the [`PYTHONPATH`{.docutils .literal
    .notranslate}]{.pre} environment variable as Python might attempt to
    pick these up as the PyTecplot module.

::: {.admonition .note}
Note

If the license is missing or invalid, try the following:

1.  On Windows, be sure that the latest version of [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} is first in your PATH environment variable.

2.  Check to see if you can run [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} by double clicking on the desktop icon (Windows), or from
    the command prompt.

3.  On Linux and macOS, be sure that your LD_LIBARARY_PATH (Linux) or
    DYLD_LIBRARY_PATH is set to the latest version of [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external}.

4.  If you are able to run [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} but still cannot run a script that imports the
    [`tecplot`{.docutils .literal .notranslate}]{.pre} module, contact
    [Tecplot Technical Support](mailto:support%40tecplot.com){.reference
    .external}.
:::

::::: {.admonition .note}
Note

On macOS, some Python configurations will fail to export images.

When running a PyTecplot script with Python as installed using MacPorts
or Brew, you may see the message **QGLPixelBuffer: Cannot create a
pbuffer** followed by the exception:

:::: {.highlight-shell .notranslate}
::: highlight
    tecplot.exception.TecplotLogicError: The off-screen image export
    failed.  This may be caused by remote display issues with OpenGL.
    Verify that the remote display settings are set to use 32-bit color
    depth. If this error persists, contact support@tecplot.com.
:::
::::

This has been fixed in **Tecplot 360 2020 R1** and updating Tecplot 360
should allow exporting of images and videos using these versions of
Python. An alternate workaround is to download the official package from
[python.org](https://python.org){.reference .external} and make sure you
are using it instead of the python that was installed via MacPorts or
Brew.
:::::

See the [[Getting Help]{.std
.std-ref}](quickstart.html#getting-help){.reference .internal} section
under [[Quick Start]{.std
.std-ref}](quickstart.html#quick-start){.reference .internal} for
troubleshooting after installation is successful.
:::::::

::::::::::: {#version-information .section}
## [Version Information](#id45){.toc-backref role="doc-backlink"}[¶](#version-information "Link to this heading"){.headerlink}

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
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: clearer
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
