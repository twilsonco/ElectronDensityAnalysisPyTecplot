:::::::: {.body role="main"}
::::: {#pytecplot-tecplot-360-python-library .section}
# PyTecplot: [Tecplot 360](https://www.tecplot.com/products/tecplot-360){.reference .external} Python Library[¶](#pytecplot-tecplot-360-python-library "Link to this heading"){.headerlink}

The pytecplot library is a high level API that connects your Python
script to the power of the [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
visualization engine. It offers line plotting, 2D and 3D surface plots
in a variety of formats, and 3D volumetric visualization. Familiarity
with [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
and the [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
macro language is helpful, but not required.

::: {.admonition .note}
Note

PyTecplot requires 64-bit Python and [Tecplot
360](https://www.tecplot.com/products/tecplot-360){.reference .external}
with
[TecPLUS™](https://www.tecplot.com/products/software-maintenance-services){.reference
.external} maintenance service. PyTecplot does not support 32 bit
Python. Please refer to [[Installation]{.std
.std-ref}](install.html#installation){.reference .internal} for
installation instructions, environment setup and system requirements.
For the best experience, developers are encouraged to use the **latest
version of Python**. If you need help converting to Python 3 or wish to
write code compatible with 2 and 3, please refer to the [Python-Future
Cheat
Sheet](https://python-future.org/compatible_idioms.html){.reference
.external}.
:::

::: {.toctree-wrapper .compound}
- [Installation](install.html){.reference .internal}
  - [Python and Tecplot](install.html#python-and-tecplot){.reference
    .internal}
    - [Package Installer](install.html#package-installer){.reference
      .internal}
    - [Connecting PyTecplot to Tecplot 360
      GUI](install.html#connecting-pytecplot-to-tecplot-360-gui){.reference
      .internal}
    - [TecUtil Server](install.html#tecutil-server){.reference
      .internal}
  - [Windows](install.html#windows){.reference .internal}
    - [Installation](install.html#id2){.reference .internal}
    - [Environment Setup](install.html#environment-setup){.reference
      .internal}
    - [Updating](install.html#updating){.reference .internal}
  - [Linux](install.html#linux){.reference .internal}
    - [Installation](install.html#id6){.reference .internal}
    - [Environment Setup (Batch
      Only)](install.html#environment-setup-batch-only){.reference
      .internal}
    - [Updating](install.html#id13){.reference .internal}
  - [macOS](install.html#macos){.reference .internal}
    - [Installation](install.html#id14){.reference .internal}
    - [Environment Setup (Batch Only)](install.html#id22){.reference
      .internal}
    - [Updating](install.html#id23){.reference .internal}
    - [System Integrity Protection
      (SIP)](install.html#system-integrity-protection-sip){.reference
      .internal}
  - [Troubleshooting](install.html#troubleshooting){.reference
    .internal}
  - [Version Information](install.html#version-information){.reference
    .internal}
- [Quick Start](quickstart.html){.reference .internal}
  - [Hello World](quickstart.html#hello-world){.reference .internal}
  - [Zero-based
    Indexing](quickstart.html#zero-based-indexing){.reference .internal}
  - [Macro Integration](quickstart.html#macro-integration){.reference
    .internal}
  - [Getting Help](quickstart.html#getting-help){.reference .internal}
- [Examples](examples.html){.reference .internal}
  - [Hello World](examples.html#hello-world){.reference .internal}
  - [Loading Layouts](examples.html#loading-layouts){.reference
    .internal}
  - [Extracting Slices](examples.html#extracting-slices){.reference
    .internal}
  - [Numpy Integration](examples.html#numpy-integration){.reference
    .internal}
  - [Execute Equation](examples.html#execute-equation){.reference
    .internal}
  - [Line Plots](examples.html#line-plots){.reference .internal}
  - [Creating Slices](examples.html#creating-slices){.reference
    .internal}
  - [Creating
    Iso-surfaces](examples.html#creating-iso-surfaces){.reference
    .internal}
  - [Wing Surface Slices](examples.html#wing-surface-slices){.reference
    .internal}
  - [Mach Iso-surfaces](examples.html#mach-iso-surfaces){.reference
    .internal}
  - [Exception Handling](examples.html#exception-handling){.reference
    .internal}
  - [Streamtraces](examples.html#streamtraces){.reference .internal}
  - [Line Legend](examples.html#line-legend){.reference .internal}
  - [Contour Legend](examples.html#contour-legend){.reference .internal}
  - [3D View](examples.html#d-view){.reference .internal}
  - [Embedding LaTeX](examples.html#embedding-latex){.reference
    .internal}
  - [Multiprocessing](examples.html#multiprocessing){.reference
    .internal}
- [Reference](reference.html){.reference .internal}
  - [Session](api/tecplot.session.html){.reference .internal}
    - [tecplot](api/tecplot.session.html#module-tecplot){.reference
      .internal}
    - [Version
      Information](api/tecplot.session.html#version-information){.reference
      .internal}
    - [Session](api/tecplot.session.html#session){.reference .internal}
    - [Configuration](api/tecplot.session.html#configuration){.reference
      .internal}
    - [Miscellaneous](api/tecplot.session.html#miscellaneous){.reference
      .internal}
  - [Layout](api/tecplot.layout.html){.reference .internal}
    - [tecplot.layout](api/tecplot.layout.html#module-tecplot.layout){.reference
      .internal}
    - [active_frame()](api/tecplot.layout.html#active-frame){.reference
      .internal}
    - [active_page()](api/tecplot.layout.html#active-page){.reference
      .internal}
    - [add_page()](api/tecplot.layout.html#add-page){.reference
      .internal}
    - [delete_page()](api/tecplot.layout.html#delete-page){.reference
      .internal}
    - [next_page()](api/tecplot.layout.html#next-page){.reference
      .internal}
    - [new_layout()](api/tecplot.layout.html#new-layout){.reference
      .internal}
    - [load_layout()](api/tecplot.layout.html#load-layout){.reference
      .internal}
    - [page()](api/tecplot.layout.html#page){.reference .internal}
    - [pages()](api/tecplot.layout.html#pages){.reference .internal}
    - [frames()](api/tecplot.layout.html#frames){.reference .internal}
    - [save_layout()](api/tecplot.layout.html#save-layout){.reference
      .internal}
    - [layout.aux_data()](api/tecplot.layout.html#layout-aux-data){.reference
      .internal}
    - [Frame](api/tecplot.layout.html#frame){.reference .internal}
    - [Page](api/tecplot.layout.html#id1){.reference .internal}
    - [Paper](api/tecplot.layout.html#paper){.reference .internal}
  - [Data](api/tecplot.data.html){.reference .internal}
    - [tecplot.data](api/tecplot.data.html#module-tecplot.data){.reference
      .internal}
    - [Loading Data](api/tecplot.data.html#loading-data){.reference
      .internal}
    - [Saving Data](api/tecplot.data.html#saving-data){.reference
      .internal}
    - [Data Queries](api/tecplot.data.html#data-queries){.reference
      .internal}
    - [Data
      Operations](api/tecplot.data.html#data-operations){.reference
      .internal}
    - [Data
      Extractions](api/tecplot.data.html#data-extractions){.reference
      .internal}
    - [Data Access](api/tecplot.data.html#data-access){.reference
      .internal}
    - [Auxiliary Data](api/tecplot.data.html#auxiliary-data){.reference
      .internal}
  - [Plot](api/tecplot.plot.html){.reference .internal}
    - [Plots](api/tecplot.plot.html#plots){.reference .internal}
    - [Fieldmaps](api/tecplot.plot.html#fieldmaps){.reference .internal}
    - [Linemaps](api/tecplot.plot.html#linemaps){.reference .internal}
  - [Axes](api/tecplot.axes.html){.reference .internal}
    - [Field Axes](api/tecplot.axes.html#field-axes){.reference
      .internal}
    - [Line Axes](api/tecplot.axes.html#line-axes){.reference .internal}
    - [Sketch Axes](api/tecplot.axes.html#sketch-axes){.reference
      .internal}
    - [Axis Elements](api/tecplot.axes.html#axis-elements){.reference
      .internal}
  - [Plot Style](api/tecplot.plot_style.html){.reference .internal}
    - [Scatter
      Plots](api/tecplot.plot_style.html#scatter-plots){.reference
      .internal}
    - [Vector
      Plots](api/tecplot.plot_style.html#vector-plots){.reference
      .internal}
    - [Legends](api/tecplot.plot_style.html#legends){.reference
      .internal}
    - [Contours](api/tecplot.plot_style.html#contours){.reference
      .internal}
    - [Isosurface](api/tecplot.plot_style.html#isosurface){.reference
      .internal}
    - [Slice](api/tecplot.plot_style.html#slice){.reference .internal}
    - [Streamtraces](api/tecplot.plot_style.html#streamtraces){.reference
      .internal}
    - [Text](api/tecplot.plot_style.html#text){.reference .internal}
    - [Data Labels](api/tecplot.plot_style.html#data-labels){.reference
      .internal}
    - [High-Order Element
      Settings](api/tecplot.plot_style.html#high-order-element-settings){.reference
      .internal}
    - [Viewport](api/tecplot.plot_style.html#viewport){.reference
      .internal}
    - [View and
      Lighting](api/tecplot.plot_style.html#view-and-lighting){.reference
      .internal}
    - [Frame
      Linking](api/tecplot.plot_style.html#frame-linking){.reference
      .internal}
  - [Blanking](api/tecplot.blanking.html){.reference .internal}
    - [Value
      Blanking](api/tecplot.blanking.html#value-blanking){.reference
      .internal}
  - [Annotations](api/tecplot.annotations.html){.reference .internal}
    - [Text](api/tecplot.annotations.html#text){.reference .internal}
    - [Geometric
      Shapes](api/tecplot.annotations.html#geometric-shapes){.reference
      .internal}
    - [Images](api/tecplot.annotations.html#images){.reference
      .internal}
  - [Exporting](api/tecplot.exporting.html){.reference .internal}
    - [Exporting
      Images](api/tecplot.exporting.html#exporting-images){.reference
      .internal}
    - [Exporting
      Video](api/tecplot.exporting.html#exporting-video){.reference
      .internal}
  - [Macros](api/tecplot.macros.html){.reference .internal}
    - [tecplot.macro](api/tecplot.macros.html#module-tecplot.macro){.reference
      .internal}
    - [macro.execute_command()](api/tecplot.macros.html#macro-execute-command){.reference
      .internal}
    - [macro.execute_extended_command()](api/tecplot.macros.html#macro-execute-extended-command){.reference
      .internal}
    - [macro.execute_file()](api/tecplot.macros.html#macro-execute-file){.reference
      .internal}
    - [macro.execute_function()](api/tecplot.macros.html#macro-execute-function){.reference
      .internal}
  - [Constants](api/tecplot.constants.html){.reference .internal}
    - [tecplot.constant](api/tecplot.constants.html#module-tecplot.constant){.reference
      .internal}
  - [Exceptions](api/tecplot.exceptions.html){.reference .internal}
    - [tecplot.exception](api/tecplot.exceptions.html#module-tecplot.exception){.reference
      .internal}
:::
:::::

::: {#indices-and-tables .section}
# Indices and tables[¶](#indices-and-tables "Link to this heading"){.headerlink}

- [[Index]{.std .std-ref}](genindex.html){.reference .internal}

- [[Module Index]{.std .std-ref}](py-modindex.html){.reference
  .internal}

- [[Search Page]{.std .std-ref}](search.html){.reference .internal}
:::

::: clearer
:::
::::::::
