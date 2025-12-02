:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#data .section}
# Data[¶](#data "Link to this heading"){.headerlink}

- [tecplot.data](#module-tecplot.data){#id20 .reference .internal}

- [Loading Data](#loading-data){#id21 .reference .internal}

  - [data.load_tecplot()](#data-load-tecplot){#id22 .reference
    .internal}

  - [data.load_tecplot_szl()](#data-load-tecplot-szl){#id23 .reference
    .internal}

  - [data.load_cfx()](#data-load-cfx){#id24 .reference .internal}

  - [data.load_cgns()](#data-load-cgns){#id25 .reference .internal}

  - [data.load_converge_cgns()](#data-load-converge-cgns){#id26
    .reference .internal}

  - [data.load_converge_hdf5()](#data-load-converge-hdf5){#id27
    .reference .internal}

  - [data.load_converge_output()](#data-load-converge-output){#id28
    .reference .internal}

  - [data.load_ensight()](#data-load-ensight){#id29 .reference
    .internal}

  - [data.load_fluent()](#data-load-fluent){#id30 .reference .internal}

  - [data.load_fluent_cff()](#data-load-fluent-cff){#id31 .reference
    .internal}

  - [data.load_fvcom()](#data-load-fvcom){#id32 .reference .internal}

  - [data.load_openfoam()](#data-load-openfoam){#id33 .reference
    .internal}

  - [data.load_plot3d()](#data-load-plot3d){#id34 .reference .internal}

  - [data.load_telemac()](#data-load-telemac){#id35 .reference
    .internal}

  - [data.load_stl()](#data-load-stl){#id36 .reference .internal}

  - [data.load_vtk()](#data-load-vtk){#id37 .reference .internal}

- [Saving Data](#saving-data){#id38 .reference .internal}

  - [data.save_tecplot_ascii()](#data-save-tecplot-ascii){#id39
    .reference .internal}

  - [data.save_tecplot_plt()](#data-save-tecplot-plt){#id40 .reference
    .internal}

  - [data.save_tecplot_szl()](#data-save-tecplot-szl){#id41 .reference
    .internal}

- [Data Queries](#data-queries){#id42 .reference .internal}

  - [data.query.probe_at_position()](#data-query-probe-at-position){#id43
    .reference .internal}

  - [data.query.probe_on_surface()](#data-query-probe-on-surface){#id44
    .reference .internal}

- [Data Operations](#data-operations){#id45 .reference .internal}

  - [data.operate.execute_equation()](#data-operate-execute-equation){#id46
    .reference .internal}

  - [data.operate.interpolate_inverse_distance()](#data-operate-interpolate-inverse-distance){#id47
    .reference .internal}

  - [data.operate.interpolate_kriging()](#data-operate-interpolate-kriging){#id48
    .reference .internal}

  - [data.operate.interpolate_linear()](#data-operate-interpolate-linear){#id49
    .reference .internal}

  - [data.operate.smooth()](#data-operate-smooth){#id50 .reference
    .internal}

  - [data.operate.transform_polar_to_rectangular()](#data-operate-transform-polar-to-rectangular){#id51
    .reference .internal}

  - [data.operate.transform_rectangular_to_polar()](#data-operate-transform-rectangular-to-polar){#id52
    .reference .internal}

  - [data.operate.transform_rectangular_to_spherical()](#data-operate-transform-rectangular-to-spherical){#id53
    .reference .internal}

  - [data.operate.transform_spherical_to_rectangular()](#data-operate-transform-spherical-to-rectangular){#id54
    .reference .internal}

- [Data Extractions](#data-extractions){#id55 .reference .internal}

  - [data.extract.extract_blanked_zones()](#data-extract-extract-blanked-zones){#id56
    .reference .internal}

  - [data.extract.extract_line()](#data-extract-extract-line){#id57
    .reference .internal}

  - [data.extract.extract_slice()](#data-extract-extract-slice){#id58
    .reference .internal}

  - [data.extract.extract_connected_regions()](#data-extract-extract-connected-regions){#id59
    .reference .internal}

  - [data.extract.triangulate()](#data-extract-triangulate){#id60
    .reference .internal}

- [Data Access](#data-access){#id61 .reference .internal}

  - [Dataset](#dataset){#id62 .reference .internal}

  - [SolutionTimeClustering](#solutiontimeclustering){#id63 .reference
    .internal}

  - [Variable](#variable){#id64 .reference .internal}

  - [Zones](#zones){#id65 .reference .internal}

  - [Array](#array){#id66 .reference .internal}

  - [FECellType](#fecelltype){#id67 .reference .internal}

  - [Nodemap](#nodemap){#id68 .reference .internal}

  - [NodemapSection](#nodemapsection){#id69 .reference .internal}

  - [ClassicNodemap](#classicnodemap){#id70 .reference .internal}

  - [Facemap](#facemap){#id71 .reference .internal}

  - [FaceNeighbors](#faceneighbors){#id72 .reference .internal}

- [Auxiliary Data](#auxiliary-data){#id73 .reference .internal}

  - [AuxData](#auxdata){#id74 .reference .internal}

:::: {#module-tecplot.data .section}
[]{#tecplot-data}

## [tecplot.data](#id20){.toc-backref role="doc-backlink"}[¶](#module-tecplot.data "Link to this heading"){.headerlink}

[[`Dataset`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
.internal} access and manipulation.

A [[`Dataset`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
.internal} consists of a matrix of [[Zones]{.std
.std-ref}](#data-access){.reference .internal} and [[`Variables`{.xref
.any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
.internal}. Each [[Zone]{.std .std-ref}](#data-access){.reference
.internal} - [[`Variable`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
.internal} pair corresponds to a data object which can always be treated
as a 1D array, but which may be interpreted as 2D or 3D in the case of
*ijk*-ordered data. In general, the [[Zone]{.std
.std-ref}](#data-access){.reference .internal} defines the size, shape
and connectivity of the data while the [[`Variable`{.xref .any .py
.py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
.internal} defines the underlying data type and whether the data is
nodal or cell-centered.

::: {.admonition .warning}
Warning

Zero-based Indexing

It is important to know that all indexing in PyTecplot scripts are
zero-based. This is a departure from the macro language which is
one-based. This is to keep with the expectations when working in the
python language. However, PyTecplot does not modify strings that are
passed to the Tecplot Engine. This means that one-based indexing should
be used when running macro commands from python or when using
[[`execute_equation()`{.xref .any .py .py-func .docutils .literal
.notranslate}]{.pre}](#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
.internal}.
:::
::::

::::::::::::::::::: {#loading-data .section}
## [Loading Data](#id21){.toc-backref role="doc-backlink"}[¶](#loading-data "Link to this heading"){.headerlink}

- [data.load_tecplot()](#data-load-tecplot){#id75 .reference .internal}

- [data.load_tecplot_szl()](#data-load-tecplot-szl){#id76 .reference
  .internal}

- [data.load_cfx()](#data-load-cfx){#id77 .reference .internal}

- [data.load_cgns()](#data-load-cgns){#id78 .reference .internal}

- [data.load_converge_cgns()](#data-load-converge-cgns){#id79 .reference
  .internal}

- [data.load_converge_hdf5()](#data-load-converge-hdf5){#id80 .reference
  .internal}

- [data.load_converge_output()](#data-load-converge-output){#id81
  .reference .internal}

- [data.load_ensight()](#data-load-ensight){#id82 .reference .internal}

- [data.load_fluent()](#data-load-fluent){#id83 .reference .internal}

- [data.load_fluent_cff()](#data-load-fluent-cff){#id84 .reference
  .internal}

- [data.load_fvcom()](#data-load-fvcom){#id85 .reference .internal}

- [data.load_openfoam()](#data-load-openfoam){#id86 .reference
  .internal}

- [data.load_plot3d()](#data-load-plot3d){#id87 .reference .internal}

- [data.load_telemac()](#data-load-telemac){#id88 .reference .internal}

- [data.load_stl()](#data-load-stl){#id89 .reference .internal}

- [data.load_vtk()](#data-load-vtk){#id90 .reference .internal}

::: {#data-load-tecplot .section}
### [data.load_tecplot()](#id75){.toc-backref role="doc-backlink"}[¶](#data-load-tecplot "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_tecplot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_first_zone_only]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[collapse]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[skip]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_text]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_geom]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_custom_labels]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_data]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_tecplot){.reference .internal}[¶](#tecplot.data.load_tecplot "Link to this definition"){.headerlink}

:   Read a tecplot data file.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- Files to be read. (See note below concerning
          absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   The [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame is replaced by the
                    new [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}. If other frames were using the same
                    [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} originally in the active frame, they will
                    continue to use it.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame, and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              Default: [[`ReadDataOption.Append`{.xref .any .py .py-attr
              .docutils .literal
              .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
              .internal}

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_first_zone_only** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Informs the Tecplot Engine that after
          the data is loaded it only needs to activate the first enabled
          [[Zone]{.std .std-ref}](#data-access){.reference .internal}
          for the initial plot. This option is particularly useful if
          you have many [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} and want to get
          the data into the Tecplot Engine and the first [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} drawn as fast
          as possible. The inactive [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} can always be
          activated when needed. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`Cartesian3D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}.

        - **zones** ([[`set`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Set of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to load. Use
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} to load all zones. (default: [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **variables** ([[`set`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
          .external} of [[`strings`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Set of [[`Variables`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} to load. If variable names are specified as strings
          and appending then variables will be aligned with existing
          variables. If variable offsets are supplied then the variables
          at those offsets will be loaded and aligned based on the value
          of the collapse parameter. Use [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} to load all variables. (default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **collapse** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- [[`Variables`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} if any are disabled. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **skip** -- (3-[[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) The *ijk*-skip. A value of (1,1,1) loads
          every data point in the *(i,j,k)* directions. A value of
          (2,2,2) loads every other data point and so forth. This only
          applies to ordered data. (default: (1,1,1))

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_text** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load any text, geometries, or custom
          labels (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_geom** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load geometries. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_custom_labels** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- (default: [[`True`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_data** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load data. Set this to
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external} if you only want annotations such as text or
          geometries. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

    Raises[:]{.colon}

    :   - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- Internal error when loading data.

        - [**TecplotTypeError**](tecplot.exceptions.html#tecplot.exception.TecplotTypeError "tecplot.exception.TecplotTypeError"){.reference
          .internal} -- In-valid input.

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
:::

::: {#data-load-tecplot-szl .section}
### [data.load_tecplot_szl()](#id76){.toc-backref role="doc-backlink"}[¶](#data-load-tecplot-szl "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_tecplot_szl]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_first_zone_only]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[server]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[connection_method]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[user]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[authentication_method]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[ssh_private_keyfile]{.pre}]{.n}[[=]{.pre}]{.o}[[PosixPath(\'\~/.ssh/id_rsa\')]{.pre}]{.default_value}*, *[[szlserver_path]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_tecplot_szl){.reference .internal}[¶](#tecplot.data.load_tecplot_szl "Link to this definition"){.headerlink}

:   Read tecplot SZL data file.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- Files to be read. (See note below concerning
          absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}. Note also that when appending, the
                    variables in the incoming dataset will be matched up
                    with the existing variables by name and any new
                    variables will be added to the end of the list.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_first_zone_only** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Informs the Tecplot Engine that after
          the data is loaded it only needs to activate the first enabled
          [[Zone]{.std .std-ref}](#data-access){.reference .internal}
          for the initial plot. This option is particularly useful if
          you have many [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} and want to get
          the data into the Tecplot Engine and the first [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} drawn as fast
          as possible. The inactive [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} can always be
          activated when needed. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`Cartesian3D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}.

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **server** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- Load the data remotely from this
          server address. When provided, file paths will be relative to
          the SZL server's working directory. (default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **connection_method**
          ([[`SZLLoader.RemoteConnectionMethod`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod "tecplot.constant.SZLLoader.RemoteConnectionMethod"){.reference
          .internal}, optional) -- When *server* is given, this
          specifies the type of connection to be made. Possible values
          are: [[`SZLLoader.RemoteConnectionMethod.Tunneled`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled "tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled"){.reference
          .internal} (default),
          [[`SZLLoader.RemoteConnectionMethod.Direct`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct "tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct"){.reference
          .internal}, [[`SZLLoader.RemoteConnectionMethod.Manual`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Manual "tecplot.constant.SZLLoader.RemoteConnectionMethod.Manual"){.reference
          .internal}.

        - **user** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- When *server* is given and
          *connection_method* is
          [[`SZLLoader.RemoteConnectionMethod.Tunneled`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled "tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled"){.reference
          .internal} or
          [[`SZLLoader.RemoteConnectionMethod.Direct`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct "tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct"){.reference
          .internal}, this specifies the username to use when logging
          into the server. This will default to the client host's user
          name.

        - **authentication_method**
          ([[`SZLLoader.RemoteAuthenticationMethod`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteAuthenticationMethod "tecplot.constant.SZLLoader.RemoteAuthenticationMethod"){.reference
          .internal}, optional) -- The authentication method to use when
          connecting to the remote server when *connection_method* is
          [[`SZLLoader.RemoteConnectionMethod.Tunneled`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled "tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled"){.reference
          .internal} or
          [[`SZLLoader.RemoteConnectionMethod.Direct`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct "tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct"){.reference
          .internal}. Possible values are
          [[`SZLLoader.RemoteAuthenticationMethod.SSHAgent`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteAuthenticationMethod.SSHAgent "tecplot.constant.SZLLoader.RemoteAuthenticationMethod.SSHAgent"){.reference
          .internal},
          [[`SZLLoader.RemoteAuthenticationMethod.SSHPrivateKey`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteAuthenticationMethod.SSHPrivateKey "tecplot.constant.SZLLoader.RemoteAuthenticationMethod.SSHPrivateKey"){.reference
          .internal} (default) which uses the file specified by
          *ssh_private_keyfile* or
          [[`SZLLoader.RemoteAuthenticationMethod.Password`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteAuthenticationMethod.Password "tecplot.constant.SZLLoader.RemoteAuthenticationMethod.Password"){.reference
          .internal} which will prompt the user for the remote login
          password in the console.

        - **ssh_private_keyfile** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- When *server* is specified and
          *connection_method* is set to
          [[`SZLLoader.RemoteConnectionMethod.Tunneled`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled "tecplot.constant.SZLLoader.RemoteConnectionMethod.Tunneled"){.reference
          .internal} or
          [[`SZLLoader.RemoteConnectionMethod.Direct`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct "tecplot.constant.SZLLoader.RemoteConnectionMethod.Direct"){.reference
          .internal} and when *authentication_method* is set to
          [[`SZLLoader.RemoteAuthenticationMethod.SSHPrivateKey`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SZLLoader.RemoteAuthenticationMethod.SSHPrivateKey "tecplot.constant.SZLLoader.RemoteAuthenticationMethod.SSHPrivateKey"){.reference
          .internal}, this specifies the full path to the private SSH
          keyfile. This parameter defaults to [`~/.ssh/id_rsa`{.docutils
          .literal .notranslate}]{.pre} where [`~`{.docutils .literal
          .notranslate}]{.pre} expands out to the local user's home
          directory.

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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
:::

::: {#data-load-cfx .section}
### [data.load_cfx()](#id77){.toc-backref role="doc-backlink"}[¶](#data-load-cfx "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_cfx]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[append]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PlotType.Automatic]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_cfx){.reference .internal}[¶](#tecplot.data.load_cfx "Link to this definition"){.headerlink}

:   Read an ANSYS CFX data file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The data file to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **append** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Append the data to the existing
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the existing data attached to the [[`Frame`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is deleted and replaced. (default: [[`True`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Set the initial plot type upon
          loading of the data. Must be one of
          [[`PlotType.Automatic`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`PlotType.Cartesian3D`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal} or [[`PlotType.Cartesian2D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}.

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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

    The CFX loader is not available on macOS.
    :::
:::

::: {#data-load-cgns .section}
### [data.load_cgns()](#id78){.toc-backref role="doc-backlink"}[¶](#data-load-cgns "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_cgns]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_first_zone_only]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[load_convergence_history]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[combine_fe_sections]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[average_to_nodes]{.pre}]{.n}[[=]{.pre}]{.o}[[\'Arithmetic\']{.pre}]{.default_value}*, *[[uniform_grid]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_boundary_conditions]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_cgns){.reference .internal}[¶](#tecplot.data.load_cgns "Link to this definition"){.headerlink}

:   Read CGNS data files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- CGNS data files to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_first_zone_only** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Informs the Tecplot Engine that after
          the data is loaded it only needs to activate the first enabled
          [[Zone]{.std .std-ref}](#data-access){.reference .internal}
          for the initial plot. This option is particularly useful if
          you have many [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} and want to get
          the data into the Tecplot Engine and the first [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} drawn as fast
          as possible. The inactive [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} can always be
          activated when needed. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`Cartesian3D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- List of zone indexes to load starting
          from zero. [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} implies loading all zones. (default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- List of variable indexes, beyond the
          first coordinate variables, to load starting from zero.
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} implies loading all variables. The grid will always
          be loaded and an index of zero indicates the first
          non-coordinate variable. (default: [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **load_convergence_history** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load the global convergence history
          rather than any grid or solution data. (default:
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **combine_fe_sections** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Combine all finite-element sections
          with the zone cell-dimension into one zone. (default:
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **average_to_nodes** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- Average cell-centered data to grid
          nodes using the specified method. (Options: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, "Arithmetic", "Laplacian", default: "Arithmetic")

        - **uniform_grid** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Indicates the grid structure is the
          same for all time steps. (default: [[`True`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_boundary_conditions** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load the boundary conditions along
          with the data. Upon loading, the associated fieldmaps will
          remain inactive. For unstructured data, boundary conditions
          are always loaded and this option is ignored. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

    Raises[:]{.colon}

    :   - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- Internal error when loading data.

        - [**TecplotTypeError**](tecplot.exceptions.html#tecplot.exception.TecplotTypeError "tecplot.exception.TecplotTypeError"){.reference
          .internal} -- Invalid input.

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
:::

::: {#data-load-converge-cgns .section}
### [data.load_converge_cgns()](#id79){.toc-backref role="doc-backlink"}[¶](#data-load-converge-cgns "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_converge_cgns]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_converge_cgns){.reference .internal}[¶](#tecplot.data.load_converge_cgns "Link to this definition"){.headerlink}

:   Read CONVERGE CGNS data files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- CONVERGE CGNS data files to be read. (See note
          below concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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
:::

::: {#data-load-converge-hdf5 .section}
### [data.load_converge_hdf5()](#id80){.toc-backref role="doc-backlink"}[¶](#data-load-converge-hdf5 "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_converge_hdf5]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_converge_hdf5){.reference .internal}[¶](#tecplot.data.load_converge_hdf5 "Link to this definition"){.headerlink}

:   Read CONVERGE HDF5 data files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- CONVERGE HDF5 data files to be read. (See note
          below concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`Cartesian3D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}.

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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

    ::: versionadded
    [New in version 2019.1: ]{.versionmodified .added}Loading CONVERGE
    HDF5 data requires Tecplot 360 2019 R1 or later.
    :::

    ::: versionadded
    [New in version 1.2.]{.versionmodified .added}
    :::
:::

::: {#data-load-converge-output .section}
### [data.load_converge_output()](#id81){.toc-backref role="doc-backlink"}[¶](#data-load-converge-output "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_converge_output]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_converge_output){.reference .internal}[¶](#tecplot.data.load_converge_output "Link to this definition"){.headerlink}

:   Read CONVERGE Output data files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- CONVERGE Output data files to be read. (See
          note below concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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
:::

::: {#data-load-ensight .section}
### [data.load_ensight()](#id82){.toc-backref role="doc-backlink"}[¶](#data-load-ensight "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_ensight]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_first_zone_only]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_ensight){.reference .internal}[¶](#tecplot.data.load_ensight "Link to this definition"){.headerlink}

:   Read Ensight data files and/or boundary file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The case file to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}, [[`Cartesian3D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}. (default: [[`PlotType.Automatic`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal})

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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
:::

::: {#data-load-fluent .section}
### [data.load_fluent()](#id83){.toc-backref role="doc-backlink"}[¶](#data-load-fluent "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_fluent]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[case_filenames]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[data_filenames]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[append]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[all_poly_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[average_to_nodes]{.pre}]{.n}[[=]{.pre}]{.o}[[\'Arithmetic\']{.pre}]{.default_value}*, *[[time_interval]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_particle_data]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_additional_quantities]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[save_uncompressed_files]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_fluent){.reference .internal}[¶](#tecplot.data.load_fluent "Link to this definition"){.headerlink}

:   Read Fluent data files.

    Parameters[:]{.colon}

    :   - **case_filenames** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}, optional) -- Case (*.cas*, *.cas.gz*) files to be
          read. Compressed files with extension *.gz* are supported.
          (See note below concerning absolute and relative paths.)

        - **data_filenames** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}, optional) -- Data (*.dat*, *.xml*, *.dat.gz*,
          *.fdat*, *.fdat.gz*, etc.) files to be read. Compressed files
          with extension *.gz* are supported.

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **append** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Append the data to the existing
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the existing data attached to the [[`Frame`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is deleted and replaced. (default: [[`True`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **zones** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- List of zone indexes (zero-based) to
          load or string specifying the type of zones to load. Possible
          values are: "CellsAndBoundaries", "CellsOnly" and
          "BoundariesOnly". Specifying one of these options is mutually
          exclusive with the [`variables`{.docutils .literal
          .notranslate}]{.pre} option. (default: "CellsAndBoundaries")

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`strings`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- List of variable names to load.
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} implies loading all variables. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **all_poly_zones** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Converts all zones to Tecplot
          polytope (polyhedral or polygonal) zones. (default:
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **average_to_nodes** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- Average cell-centered data to grid
          nodes using the specified method. (Options: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, "Arithmetic", "Laplacian", default: "Arithmetic")

        - **time_interval** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Use a constant time interval between
          each data (*.dat*) file. If [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the flow-data parameter of each solution data
          (*.dat*) file is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) --

          Assign strand ID's to zones that have a strand ID of -1.
          (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

          ::: {.admonition .note}
          Note

          assign_strand_ids only applies if you have also provided a
          time_interval, otherwise it will be ignored.
          :::

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_particle_data** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load particle data from the data
          (*.dat*) files. If loading particle data from an XML file, the
          XML file should be included in the [`data_filenames`{.docutils
          .literal .notranslate}]{.pre} list. (default: [[`False`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_additional_quantities** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Load quantities that were derived
          from the FLUENT's standard quantities. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}) *New in Tecplot 360 2017 R2*.

        - **save_uncompressed_files** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Save the uncompressed files to the
          compressed files' location.

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

    Raises[:]{.colon}

    :   - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- Internal error when loading data.

        - [**TecplotTypeError**](tecplot.exceptions.html#tecplot.exception.TecplotTypeError "tecplot.exception.TecplotTypeError"){.reference
          .internal} -- In-valid input.

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

    Notes

    The [`zones`{.docutils .literal .notranslate}]{.pre} option takes
    either a [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zone indexes to be imported or one of
    "CellsAndBoundaries", "CellsOnly" or "BoundariesOnly" to indicate
    the type of zones the user wants to load, however these options are
    mutually exclusive with the [`variables`{.docutils .literal
    .notranslate}]{.pre} option:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tecplot.data.load_fluent(['one.cas', 'two.cas'],
        ...     data_filenames=['one.dat', 'two.dat'],
        ...     variables = ['Pressure','Velocity'],
        ...     zones = [0,1,3])
    :::
    ::::
:::

::: {#data-load-fluent-cff .section}
### [data.load_fluent_cff()](#id84){.toc-backref role="doc-backlink"}[¶](#data-load-fluent-cff "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_fluent_cff]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[solution_time_source]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_interior_face_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_particle_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_fluent_cff){.reference .internal}[¶](#tecplot.data.load_fluent_cff "Link to this definition"){.headerlink}

:   Read Fluent Common Fluids Format files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- One or more Fluent CFF case (*.cas.h5*) files
          followed by zero or more Fluent CFF data (*.dat.h5*) files
          (See note below concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}, [[`Cartesian3D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}. (default: [[`PlotType.Automatic`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal})

        - **solution_time_source**
          ([[`FluentCFFLoader.SolutionTimeSource`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FluentCFFLoader.SolutionTimeSource "tecplot.constant.FluentCFFLoader.SolutionTimeSource"){.reference
          .internal}, optional) --

          Assign the solution times of the zones based on the specified
          criteria. (default:
          [[`FluentCFFLoader.SolutionTimeSource.Auto`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FluentCFFLoader.SolutionTimeSource.Auto "tecplot.constant.FluentCFFLoader.SolutionTimeSource.Auto"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`FluentCFFLoader.SolutionTimeSource.Auto`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FluentCFFLoader.SolutionTimeSource.Auto "tecplot.constant.FluentCFFLoader.SolutionTimeSource.Auto"){.reference .internal}

                :   First looks for and uses solution time specified in
                    the simulation settings of the Fluent CFF data
                    files. If that information isn't present in all
                    supplied files, next looks for solution time
                    embedded in [`filenames`{.docutils .literal
                    .notranslate}]{.pre}. If solution time cannot be
                    determined, the loader assigns a constant time
                    interval, starting at zero and incrementing by one,
                    if there is a single file, or if there are case and
                    data file combinations, otherwise assigns static
                    solution times of zero.

              - 

                [[`FluentCFFLoader.SolutionTimeSource.SteadyState`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FluentCFFLoader.SolutionTimeSource.SteadyState "tecplot.constant.FluentCFFLoader.SolutionTimeSource.SteadyState"){.reference .internal}

                :   Assigns a static solution time of zero to all zones.

              - 

                [[`FluentCFFLoader.SolutionTimeSource.ConstantTimeInterval`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FluentCFFLoader.SolutionTimeSource.ConstantTimeInterval "tecplot.constant.FluentCFFLoader.SolutionTimeSource.ConstantTimeInterval"){.reference .internal}

                :   Assigns a constant time interval, starting at zero
                    and incrementing by one

        - **include_interior_face_zones** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Interior face zones, which are used
          to build cell zones, are loaded as independent face zones.
          (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_particle_zones** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Loads particle data as I-ordered
          zones and nodal variables if it exists in the data (*dat.h5*)
          file(s). (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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

    The Fluent CFF loader is not available on macOS.
    :::

    The Fluent CFF loader takes one or more case files, followed by zero
    or more data files in a single list:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tecplot.data.load_fluent_cff(
        ...     ['one.cas.h5', 'one.dat.h5', 'two.dat.h5', 'three.cas.h5'],
        ...     read_data_option = ReadDataOption.Replace,
        ...     include_interior_face_zones = True)
    :::
    ::::

    ::: versionadded
    [New in version 2021.1: ]{.versionmodified .added}Loading Fluent CFF
    files requires Tecplot 360 2021 R1 or later.
    :::

    ::: versionadded
    [New in version 1.4.]{.versionmodified .added}
    :::
:::

::: {#data-load-fvcom .section}
### [data.load_fvcom()](#id85){.toc-backref role="doc-backlink"}[¶](#data-load-fvcom "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_fvcom]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_fvcom){.reference .internal}[¶](#tecplot.data.load_fvcom "Link to this definition"){.headerlink}

:   Read FVCOM netCDF data files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- FVCOM data files to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`Cartesian3D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}.

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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

    ::: versionadded
    [New in version 2018.2: ]{.versionmodified .added}Loading FVCOM data
    requires Tecplot 360 2018 R2 or later.
    :::
:::

::: {#data-load-openfoam .section}
### [data.load_openfoam()](#id86){.toc-backref role="doc-backlink"}[¶](#data-load-openfoam "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_openfoam]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[append]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[boundary_zone_construction]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PlotType.Automatic]{.pre}]{.default_value}*, *[[initial_plot_first_zone_only]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_openfoam){.reference .internal}[¶](#tecplot.data.load_openfoam "Link to this definition"){.headerlink}

:   Read an OpenFOAM data file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The data file to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **append** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Append the data to the existing
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the existing data attached to the [[`Frame`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is deleted and replaced. (default: [[`True`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **boundary_zone_construction**
          ([[`OpenFOAMLoader.BoundaryZoneConstruction`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.OpenFOAMLoader.BoundaryZoneConstruction "tecplot.constant.OpenFOAMLoader.BoundaryZoneConstruction"){.reference
          .internal}, optional) -- Set how the boundary zones are
          constructed. This may be either
          [[`OpenFOAMLoader.BoundaryZoneConstruction.Reconstructed`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.OpenFOAMLoader.BoundaryZoneConstruction.Reconstructed "tecplot.constant.OpenFOAMLoader.BoundaryZoneConstruction.Reconstructed"){.reference
          .internal} (default) or
          [[`OpenFOAMLoader.BoundaryZoneConstruction.Decomposed`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.OpenFOAMLoader.BoundaryZoneConstruction.Decomposed "tecplot.constant.OpenFOAMLoader.BoundaryZoneConstruction.Decomposed"){.reference
          .internal}. This option requires Tecplot 360 2019 R1 or later.

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Set the initial plot type upon
          loading of the data. Must be one of
          [[`PlotType.Automatic`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`PlotType.Cartesian3D`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal} or [[`PlotType.Cartesian2D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}.

        - **initial_plot_first_zone_only** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Informs the Tecplot Engine that after
          the data is loaded it only needs to activate the first enabled
          [[Zone]{.std .std-ref}](#data-access){.reference .internal}
          for the initial plot. This option is particularly useful if
          you have many [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} and want to get
          the data into the Tecplot Engine and the first [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} drawn as fast
          as possible. The inactive [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} can always be
          activated when needed. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::
:::

::: {#data-load-plot3d .section}
### [data.load_plot3d()](#id87){.toc-backref role="doc-backlink"}[¶](#data-load-plot3d "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_plot3d]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[grid_filenames]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[solution_filenames]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[function_filenames]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[name_filename]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[append]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[data_structure]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[is_multi_grid]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[ascii_is_double]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[ascii_has_blanking]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[uniform_grid]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[append_function_variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_boundaries]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_plot3d){.reference .internal}[¶](#tecplot.data.load_plot3d "Link to this definition"){.headerlink}

:   Read Plot3D data files.

    Parameters[:]{.colon}

    :   - **grid_filenames** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}, optional) -- One or more grid file names to be
          read. (See note below concerning absolute and relative paths.)

        - **solution_filenames** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}, optional) -- One or more solution data file names
          to be read.

        - **function_filenames** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}, optional) -- One or more function file names.

        - **name_filename** ([[`pathlib.Path`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- Path to the name file.

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **append** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Append the data to the existing
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the existing data attached to the [[`Frame`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is deleted and replaced. (default: [[`True`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **data_structure** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- Specifies the data structure and
          overrides the automatic detection. Options are:
          [`1D`{.docutils .literal .notranslate}]{.pre}, [`2D`{.docutils
          .literal .notranslate}]{.pre}, [`3DP`{.docutils .literal
          .notranslate}]{.pre}, [`3DW`{.docutils .literal
          .notranslate}]{.pre}, [`UNSTRUCTURED`{.docutils .literal
          .notranslate}]{.pre}. Setting this requires
          [`is_multi_grid`{.docutils .literal .notranslate}]{.pre} and
          [`style`{.docutils .literal .notranslate}]{.pre} to be set as
          well.

        - **is_multi_grid** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Sets data as multi-grid and overrides
          the automatic data structure detection. Setting this requires
          [`data_structure`{.docutils .literal .notranslate}]{.pre} and
          [`style`{.docutils .literal .notranslate}]{.pre} to be set as
          well.

        - **style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Specifies the data style and
          overrides the automatic data structure detection. Options are:
          [`PLOT3DCLASSIC`{.docutils .literal .notranslate}]{.pre},
          [`PLOT3DFUNCTION`{.docutils .literal .notranslate}]{.pre},
          [`OVERFLOW`{.docutils .literal .notranslate}]{.pre}. Setting
          this requires [`data_structure`{.docutils .literal
          .notranslate}]{.pre} and [`is_multi_grid`{.docutils .literal
          .notranslate}]{.pre} to be set as well.

        - **ascii_is_double** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Indicates that floating-point numbers
          found in the text data files should be store with 64-bit
          precision. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **ascii_has_blanking** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Indicates that the text data files
          contain blanking. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **uniform_grid** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Indicates the grid structure is the
          same for all time steps. (default: [[`True`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **append_function_variables** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Append variables in function files to
          those found in solution files. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_boundaries** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Loads boundary zones found in the
          ".g.fvbnd" file located in the same directory as the grid
          file, if available. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

    Raises[:]{.colon}

    :   - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} -- Internal error when loading data.

        - [**TecplotValueError**](tecplot.exceptions.html#tecplot.exception.TecplotValueError "tecplot.exception.TecplotValueError"){.reference
          .internal} -- In-valid input.

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

    Data structure is automatically detected by default.

    The options [`data_structure`{.docutils .literal
    .notranslate}]{.pre}, [`is_multi_grid`{.docutils .literal
    .notranslate}]{.pre} and [`style`{.docutils .literal
    .notranslate}]{.pre} must be supplied together or not at all. When
    all of these are [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}, the data structure is automatically detected.
    :::

    The variables from the function files can be appended to the dataset
    upon loading:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tecplot.data.load_plot3d(
        ...     grid_filenames = 'data.g',
        ...     solution_filenames = ['t0.q', 't1.q'],
        ...     function_filenames = ['t0.f', 't1.f'],
        ...     append_function_variables = True)
    :::
    ::::
:::

::: {#data-load-telemac .section}
### [data.load_telemac()](#id88){.toc-backref role="doc-backlink"}[¶](#data-load-telemac "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_telemac]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[boundary_filename]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_telemac){.reference .internal}[¶](#tecplot.data.load_telemac "Link to this definition"){.headerlink}

:   Read Telemac data files and/or boundary file.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}, optional) -- Telemac data file(s) to be read. (See
          note below concerning absolute and relative paths.) Not
          required if a boundary file is being appended to an existing
          data set.

        - **boundary_filename** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- Boundary file. If loaded with
          multiple Telemac files, will be applied to the first Telemac
          file. If loaded with no Telemac files, must be appended to an
          existing data set (read_data_option must be
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal}, the default).

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   Remove the dataset from the active frame prior to
                    reading in the new dataset. If other frames use the
                    same [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame, they will continue
                    to use the old one.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}, [[`Cartesian3D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}. (default: [[`PlotType.Automatic`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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

    ::: versionadded
    [New in version 2019.1: ]{.versionmodified .added}Loading Telemac
    data requires Tecplot 360 2019 R1 or later.
    :::
:::

::: {#data-load-stl .section}
### [data.load_stl()](#id89){.toc-backref role="doc-backlink"}[¶](#data-load-stl "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_stl]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[append]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[subdivide_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[SubdivideZones.DoNotSubdivide]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PlotType.Automatic]{.pre}]{.default_value}*, *[[initial_plot_first_zone_only]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_stl){.reference .internal}[¶](#tecplot.data.load_stl "Link to this definition"){.headerlink}

:   Read a 3D Systems STL data file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The data file to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **append** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Append the data to the existing
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the existing data attached to the [[`Frame`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is deleted and replaced. (default: [[`True`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **subdivide_zones** ([[`STLLoader.SubdivideZones`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.STLLoader.SubdivideZones "tecplot.constant.STLLoader.SubdivideZones"){.reference
          .internal}, optional) -- Specify method of zone division.
          Possible values are:
          [[`STLLoader.SubdivideZones.DoNotSubdivide`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.STLLoader.SubdivideZones.DoNotSubdivide "tecplot.constant.STLLoader.SubdivideZones.DoNotSubdivide"){.reference
          .internal} (default),
          [[`STLLoader.SubdivideZones.ByComponent`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.STLLoader.SubdivideZones.ByComponent "tecplot.constant.STLLoader.SubdivideZones.ByComponent"){.reference
          .internal} and
          [[`STLLoader.SubdivideZones.ByElementType`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.STLLoader.SubdivideZones.ByElementType "tecplot.constant.STLLoader.SubdivideZones.ByElementType"){.reference
          .internal}.

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Set the initial plot type upon
          loading of the data. Must be one of
          [[`PlotType.Automatic`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`PlotType.Cartesian3D`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal} or [[`PlotType.Cartesian2D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}.

        - **initial_plot_first_zone_only** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Informs the Tecplot Engine that after
          the data is loaded it only needs to activate the first enabled
          [[Zone]{.std .std-ref}](#data-access){.reference .internal}
          for the initial plot. This option is particularly useful if
          you have many [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} and want to get
          the data into the Tecplot Engine and the first [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} drawn as fast
          as possible. The inactive [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} can always be
          activated when needed. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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
:::

::: {#data-load-vtk .section}
### [data.load_vtk()](#id90){.toc-backref role="doc-backlink"}[¶](#data-load-vtk "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[load_vtk]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filenames]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[read_data_option]{.pre}]{.n}[[=]{.pre}]{.o}[[ReadDataOption.Append]{.pre}]{.default_value}*, *[[reset_style]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[initial_plot_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PlotType.Automatic]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[add_zones_to_existing_strands]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[solution_time_source]{.pre}]{.n}[[=]{.pre}]{.o}[[SolutionTimeSource.Auto]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/load.html#load_vtk){.reference .internal}[¶](#tecplot.data.load_vtk "Link to this definition"){.headerlink}

:   Read VTK data files.

    Parameters[:]{.colon}

    :   - **filenames** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external}, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external}) -- The data file(s) to be read. (See note below
          concerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} to attach the resulting [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used and the zones are appended by default.

        - **read_data_option** ([[`ReadDataOption`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption "tecplot.constant.ReadDataOption"){.reference
          .internal}, optional) --

          Specify how the data is loaded into Tecplot. (default:
          [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
          .internal})

          Possible values are:

          :   - 

                [[`ReadDataOption.ReplaceInActiveFrame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.ReplaceInActiveFrame "tecplot.constant.ReadDataOption.ReplaceInActiveFrame"){.reference .internal}

                :   The [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} in the active frame is replaced by the
                    new [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}. If other frames were using the same
                    [[`Dataset`{.xref .any .py .py-class .docutils
                    .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} originally in the active frame, they will
                    continue to use it.

              - 

                [[`ReadDataOption.Append`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference .internal}

                :   Append to the existing [[`Dataset`{.xref .any .py
                    .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              - 

                [[`ReadDataOption.Replace`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Replace "tecplot.constant.ReadDataOption.Replace"){.reference .internal}

                :   Replace the [[`Dataset`{.xref .any .py .py-class
                    .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal} attached to the active frame, and to all
                    other frames that use the same [[`Dataset`{.xref
                    .any .py .py-class .docutils .literal
                    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
                    .internal}.

              Default: [[`ReadDataOption.Append`{.xref .any .py .py-attr
              .docutils .literal
              .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ReadDataOption.Append "tecplot.constant.ReadDataOption.Append"){.reference
              .internal}

        - **reset_style** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Reset the style for destination
          [[`Frame`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}'s current style is preserved. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **initial_plot_type** ([[`PlotType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType "tecplot.constant.PlotType"){.reference
          .internal}, optional) -- Forces a specific type of plot upon
          loading of the data. Only used if *resetstyle* is
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}. To have [Tecplot
          360](https://www.tecplot.com/products/tecplot-360){.reference
          .external} determine the most appropriate plot type for the
          data, use [[`PlotType.Automatic`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal}. Possible values are: [[`PlotType.Automatic`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Automatic "tecplot.constant.PlotType.Automatic"){.reference
          .internal} (default), [[`Cartesian3D`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
          .internal}, [[`Cartesian2D`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
          .internal}, [[`XYLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.XYLine "tecplot.constant.PlotType.XYLine"){.reference
          .internal}, [[`PlotType.Sketch`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
          .internal}, [[`PolarLine`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.PolarLine "tecplot.constant.PlotType.PolarLine"){.reference
          .internal}.

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Assign strand ID's to zones that have
          a strand ID of -1. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **add_zones_to_existing_strands** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Add the [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to matching
          strands, if they exist. Otherwise, if the new data specifies
          strands, new ones will be created beginning after the last
          strand in the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **solution_time_source**
          ([[`VTKLoader.SolutionTimeSource`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VTKLoader.SolutionTimeSource "tecplot.constant.VTKLoader.SolutionTimeSource"){.reference
          .internal}, optional) -- Assign the solution times of the
          zones based on the specified criteria. Possible values are:
          [[`VTKLoader.SolutionTimeSource.Auto`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VTKLoader.SolutionTimeSource.Auto "tecplot.constant.VTKLoader.SolutionTimeSource.Auto"){.reference
          .internal} (default) which favors the "time" scalar over the
          numbers embedded in the file names,
          [[`VTKLoader.SolutionTimeSource.None_`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VTKLoader.SolutionTimeSource.None_ "tecplot.constant.VTKLoader.SolutionTimeSource.None_"){.reference
          .internal} which does not assign solutions times or strands,
          [[`VTKLoader.SolutionTimeSource.FromFieldData`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VTKLoader.SolutionTimeSource.FromFieldData "tecplot.constant.VTKLoader.SolutionTimeSource.FromFieldData"){.reference
          .internal} which uses the "time" scalar and
          [[`VTKLoader.SolutionTimeSource.FromFilename`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VTKLoader.SolutionTimeSource.FromFilename "tecplot.constant.VTKLoader.SolutionTimeSource.FromFilename"){.reference
          .internal} which uses the solution time embedded in the file
          names.

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} holding the loaded data.

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
:::
:::::::::::::::::::

:::::: {#saving-data .section}
## [Saving Data](#id38){.toc-backref role="doc-backlink"}[¶](#saving-data "Link to this heading"){.headerlink}

- [data.save_tecplot_ascii()](#data-save-tecplot-ascii){#id91 .reference
  .internal}

- [data.save_tecplot_plt()](#data-save-tecplot-plt){#id92 .reference
  .internal}

- [data.save_tecplot_szl()](#data-save-tecplot-szl){#id93 .reference
  .internal}

::: {#data-save-tecplot-ascii .section}
### [data.save_tecplot_ascii()](#id91){.toc-backref role="doc-backlink"}[¶](#data-save-tecplot-ascii "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[save_tecplot_ascii]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_text]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[precision]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_geom]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_data]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_data_share_linkage]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_autogen_face_neighbors]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[use_point_format]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/save.html#save_tecplot_ascii){.reference .internal}[¶](#tecplot.data.save_tecplot_ascii "Link to this definition"){.headerlink}

:   Write Tecplot ASCII data file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Name of the data file to write. (See note below
          conerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} which holds the [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to be written. If this option and *dataset* are
          both [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to write out. If this and *frame* are both
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} of the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **include_text** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out all text, geometries and
          custom labels. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_geom** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out all geometries. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_data** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out the data. Set this to
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external} if you only want to write out annotations.
          (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_data_share_linkage** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Conserve space and write the variable
          and connectivity linkage wherever possible. If [[`False`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, this will write out all data, losing the
          connectivity sharing linkage for future dataset reads of the
          file. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_autogen_face_neighbors** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Save the face neighbor connectivity.
          This may produce very large data files. (default:
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **use_point_format** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out point format, otherwise use
          block format. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          [[Zones]{.std .std-ref}](#data-access){.reference .internal}
          to write out. Use [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} to write out all [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}, optional) -- [[`Variables`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} to write out. Use [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} to write out all [[`Variables`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}. (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **precision** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- ASCII decimal precision to use.
          (default: 12)

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} read from when saving.

    Raises[:]{.colon}

    :   - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} --

        - [**TecplotLogicError**](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
          .internal} --

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

    Example

    In this example, we load sample data and save the data in Tecplot
    ASCII format:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot
        examples_directory = tecplot.session.tecplot_examples_directory()
        infile = path.join(examples_directory,
                           'OneraM6wing', 'OneraM6_SU2_RANS.plt')
        dataset = tecplot.data.load_tecplot(infile)
        variables_to_save = [dataset.variable(V)
                             for V in ('x','y','z','Pressure_Coefficient')]

        zone_to_save = dataset.zone('WingSurface')
        # write data out to an ascii file
        tecplot.data.save_tecplot_ascii('wing.dat', dataset=dataset,
                                        variables=variables_to_save,
                                        zones=[zone_to_save])
    :::
    ::::
:::

::: {#data-save-tecplot-plt .section}
### [data.save_tecplot_plt()](#id92){.toc-backref role="doc-backlink"}[¶](#data-save-tecplot-plt "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[save_tecplot_plt]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[version]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_text]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_geom]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_data]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_data_share_linkage]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[include_autogen_face_neighbors]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[associate_with_layout]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/save.html#save_tecplot_plt){.reference .internal}[¶](#tecplot.data.save_tecplot_plt "Link to this definition"){.headerlink}

:   Write Tecplot binary PLT data file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Name of the data file to write. (See note below
          conerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} which holds the [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to be written. If this option and *dataset* are
          both [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to write out. If this and *frame* are both
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} of the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          [[Zones]{.std .std-ref}](#data-access){.reference .internal}
          to write out. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, all [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} will be saved.

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}, optional) -- [[`Variables`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} to write out. If [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, all [[`Variables`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} will be saved.

        - **include_text** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out all text, geometries and
          custom labels. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_geom** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out all geometries. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_data** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Write out the data. Set this to
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external} if you only want to write out annotations.
          (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **include_data_share_linkage** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Conserve space and write the variable
          and connectivity linkage wherever possible. If [[`False`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, this will write out all data, losing the
          connectivity sharing linkage for future dataset reads of the
          file. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **include_autogen_face_neighbors** ([[`bool`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Save the face neighbor connectivity.
          This may produce very large data files. (default:
          [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **associate_with_layout** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Associate this data file with the
          current layout. Set to [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external} to write the datafile without modifying Tecplot's
          current data file to layout association. If *version* is set
          to anything other than [[`BinaryFileVersion.Current`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion.Current "tecplot.constant.BinaryFileVersion.Current"){.reference
          .internal}, this association is not possible, and this
          parameter will be ignored. (default: [[`True`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **version** ([[`BinaryFileVersion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion "tecplot.constant.BinaryFileVersion"){.reference
          .internal}, optional) -- Specifies the file version to write.
          Note that some data may be excluded from the file if it cannot
          be supported in the specified version. Possible values are:
          [[`Tecplot2006`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion.Tecplot2006 "tecplot.constant.BinaryFileVersion.Tecplot2006"){.reference
          .internal}, [[`Tecplot2008`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion.Tecplot2008 "tecplot.constant.BinaryFileVersion.Tecplot2008"){.reference
          .internal}, [[`Tecplot2009`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion.Tecplot2009 "tecplot.constant.BinaryFileVersion.Tecplot2009"){.reference
          .internal} and [[`BinaryFileVersion.Current`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion.Current "tecplot.constant.BinaryFileVersion.Current"){.reference
          .internal}. (default: [[`BinaryFileVersion.Current`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BinaryFileVersion.Current "tecplot.constant.BinaryFileVersion.Current"){.reference
          .internal})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} read from when saving.

    Raises[:]{.colon}

    :   - [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
          .internal} --

        - [**TecplotLogicError**](tecplot.exceptions.html#tecplot.exception.TecplotLogicError "tecplot.exception.TecplotLogicError"){.reference
          .internal} --

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

    Example

    In this example, we load sample data and save the data in Tecplot
    binary PLT format:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot
        examples_directory = tecplot.session.tecplot_examples_directory()
        infile = path.join(examples_directory,
                           'OneraM6wing', 'OneraM6_SU2_RANS.plt')
        dataset = tecplot.data.load_tecplot(infile)
        variables_to_save = [dataset.variable(V)
                             for V in ('x', 'y', 'z',
                                       'Pressure_Coefficient')]

        zone_to_save = dataset.zone('WingSurface')
        # write data out to a binary file
        tecplot.data.save_tecplot_plt('wing.plt', dataset=dataset,
                                        variables=variables_to_save,
                                        zones=[zone_to_save])
    :::
    ::::
:::

::: {#data-save-tecplot-szl .section}
### [data.save_tecplot_szl()](#id93){.toc-backref role="doc-backlink"}[¶](#data-save-tecplot-szl "Link to this heading"){.headerlink}

[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[save_tecplot_szl]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/save.html#save_tecplot_szl){.reference .internal}[¶](#tecplot.data.save_tecplot_szl "Link to this definition"){.headerlink}

:   Write Tecplot SZL data file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Name of the data file to write. (See note below
          conerning absolute and relative paths.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} which holds the [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to be written. If this option and *dataset* are
          both [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to write out. If this and *frame* are both
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the [[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} of the currently active [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} is used. (default: [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Dataset`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} -- The [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} read from when saving.

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

    Example

    In this example, we load sample data and save it in Tecplot SZL
    format:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot
        examples_directory = tecplot.session.tecplot_examples_directory()
        infile = path.join(examples_directory,
                           'OneraM6wing', 'OneraM6_SU2_RANS.plt')
        dataset = tecplot.data.load_tecplot(infile)
        tecplot.data.save_tecplot_szl('wing.szplt')
    :::
    ::::
:::
::::::

::::: {#data-queries .section}
## [Data Queries](#id42){.toc-backref role="doc-backlink"}[¶](#data-queries "Link to this heading"){.headerlink}

::: {#data-query-probe-at-position .section}
### [data.query.probe_at_position()](#id43){.toc-backref role="doc-backlink"}[¶](#data-query-probe-at-position "Link to this heading"){.headerlink}

[[tecplot.data.query.]{.pre}]{.sig-prename .descclassname}[[probe_at_position]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[x]{.pre}]{.n}*, *[[y]{.pre}]{.n}*, *[[z]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[nearest]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[starting_cell]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[starting_zone]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/query.html#probe_at_position){.reference .internal}[¶](#tecplot.data.query.probe_at_position "Link to this definition"){.headerlink}

:   Returns field values at a point in space.

    ::: {.admonition .note}
    Note

    The position is taken according to the axis assignments of the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} which may be any of the associated variables in the
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} and not necessarily [`(X,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Y,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Z)`{.docutils .literal .notranslate}]{.pre}. See:
    [[`Cartesian3DFieldAxis.variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.Cartesian3DFieldAxis.variable "tecplot.plot.Cartesian3DFieldAxis.variable"){.reference
    .internal}.
    :::

    Parameters[:]{.colon}

    :   - **x** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, *z* is optional) -- position to probe for field
          values.

        - **y** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, *z* is optional) -- position to probe for field
          values.

        - **z** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, *z* is optional) -- position to probe for field
          values.

        - **nearest** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}) -- Returns the values at the nearest node to the
          given position. Probe position must be inside the volume of
          the data being queried, otherwise this will return
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **starting_cell** (3-[[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The [`(i,j,k)`{.docutils .literal
          .notranslate}]{.pre}-index of the cell to start looking for
          the given position. This must be used with
          [`starting_zone`{.docutils .literal .notranslate}]{.pre}.

        - **starting_zone** ([[Zone]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          The first zone to start searching. This is required only when
          [`starting_cell`{.docutils .literal .notranslate}]{.pre} is
          specified.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          Limits the search to the given zones. [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} implies searching all zones. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to probe. (defaults to the active [[`Dataset`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} which determines the spatial variable assignment
          [`(X,Y,Z)`{.docutils .literal .notranslate}]{.pre}. (defaults
          to the active [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}.)

    Returns[:]{.colon}

    :   [[`namedtuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
        .external} --

        [`(data,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
        .literal .notranslate}[`cell,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`zone)`{.docutils .literal .notranslate}]{.pre}:

        > <div>
        >
        > [`data`{.docutils .literal .notranslate}]{.pre} ([[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of [[`floats`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference .external})
        >
        > :   The values of each variable in the dataset at the given
        >     position.
        >
        > [`cell`{.docutils .literal .notranslate}]{.pre} (3-[[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external} of [[`integers`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external})
        >
        > :   [`(i,j,k)`{.docutils .literal .notranslate}]{.pre} of the
        >     cell containing the given position.
        >
        > [`zone`{.docutils .literal .notranslate}]{.pre} ([[Zone]{.std .std-ref}](#data-access){.reference .internal})
        >
        > :   Zone containing the given position
        >
        > </div>

    ::::: {.admonition .note}
    Note

    Returns [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external} if the position can't be probed.

    This method will return [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external} if the position is outside the volume of the data being
    queried. This means one should capture the results in a single
    variable and test it against [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external} before proceeding:

    :::: {.highlight-python .notranslate}
    ::: highlight
        result = tp.data.query.probe_at_position(1.0, 2.0, 3.0)
        if result is None:
            print('probe failed.')
        else:
            data, cell, zone = result
    :::
    ::::

    Additionally, with Tecplot 360 versions 2018 R1 and later, this
    function will raise an exception if Tecplot 360 was interrupted via
    the GUI during the probe operation.
    :::::
:::

::: {#data-query-probe-on-surface .section}
### [data.query.probe_on_surface()](#id44){.toc-backref role="doc-backlink"}[¶](#data-query-probe-on-surface "Link to this heading"){.headerlink}

[[tecplot.data.query.]{.pre}]{.sig-prename .descclassname}[[probe_on_surface]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[positions]{.pre}]{.n}[[=]{.pre}]{.o}[[((0,),]{.pre} [(0,),]{.pre} [(0,))]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[probe_nearest]{.pre}]{.n}[[=]{.pre}]{.o}[[ProbeNearest.Position]{.pre}]{.default_value}*, *[[obey_blanking]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*, *[[num_nearest_nodes]{.pre}]{.n}[[=]{.pre}]{.o}[[20]{.pre}]{.default_value}*, *[[tolerance]{.pre}]{.n}[[=]{.pre}]{.o}[[1e-05]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/query.html#probe_on_surface){.reference .internal}[¶](#tecplot.data.query.probe_on_surface "Link to this definition"){.headerlink}

:   Returns field values at points on a surface closest the points
    given.

    ::: {.admonition .note}
    Note

    The positions are processed according to the axis assignments of the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} which may be any of the associated variables in the
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} and not necessarily (but usually) [`(X,`{.docutils
    .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Y,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Z)`{.docutils .literal .notranslate}]{.pre}. See:
    [[`Cartesian3DFieldAxis.variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.Cartesian3DFieldAxis.variable "tecplot.plot.Cartesian3DFieldAxis.variable"){.reference
    .internal}.
    :::

    Parameters[:]{.colon}

    :   - **positions** (2D [[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} array) -- Array of points to probe dimensioned by
          [`(3,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
          .literal .notranslate}[`N)`{.docutils .literal
          .notranslate}]{.pre} where the first dimension corresponds to
          [`(x,`{.docutils .literal .notranslate}]{.pre}` `{.docutils
          .literal .notranslate}[`y,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`z)`{.docutils .literal .notranslate}]{.pre}. A
          1D [[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} array is accepted for single point probes, however
          this should be avoided when probing several positions as the
          internal algorithm is optimized for probing many positions at
          once.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          Limits the search to the given zones. [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} implies searching all active relevant surface zones
          including surfaces of ordered volume zones. To search FE or
          polygonal volume boundaries, include the volume zones in this
          list. (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The variables within the dataset to
          probe. [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} implies all variables. (default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **probe_nearest** ([[`ProbeNearest`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ProbeNearest "tecplot.constant.ProbeNearest"){.reference
          .internal}, optional) -- Probe at the nodal location
          ([[`ProbeNearest.Node`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ProbeNearest.Node "tecplot.constant.ProbeNearest.Node"){.reference
          .internal}) or interpolate to nearest location on the surface
          ([[`ProbeNearest.Position`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ProbeNearest.Position "tecplot.constant.ProbeNearest.Position"){.reference
          .internal}, default). The return parameter **cells_or_nodes**
          will be cells if set to [[`ProbeNearest.Position`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ProbeNearest.Position "tecplot.constant.ProbeNearest.Position"){.reference
          .internal} (default), or nodes if set to
          [[`ProbeNearest.Node`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ProbeNearest.Node "tecplot.constant.ProbeNearest.Node"){.reference
          .internal}.

        - **obey_blanking** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Do not search blanked cells according
          the frame's style settings. (default: [[`True`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **num_nearest_nodes** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Only consider surface cells that
          contain one of the closest [`N`{.docutils .literal
          .notranslate}]{.pre} nodes to the probed position. For highly
          varying surfaces, the nearest cell may or may not contain the
          nearest nodes to the probe position and so this value should
          be increased accordingly, however doing so increases the
          search-space linearly. (default: 20)

        - **tolerance** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The percentage of the longest
          cartesian [`(x,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`y,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`z)`{.docutils .literal .notranslate}]{.pre}
          dimension subtended by the polygons of the surface. This is
          used in several parts of the algorithm to find the nearest
          position on the surface zones and should be increased when
          probing imprecise nodal position data. (default: 1e-5)

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to probe. (defaults to the active [[`Dataset`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}.)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} which determines the spatial variable assignment
          [`(X,Y,Z)`{.docutils .literal .notranslate}]{.pre}. (defaults
          to the active [[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}.)

    Returns[:]{.colon}

    :   [[`namedtuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
        .external} -- [`(data,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`cells_or_nodes,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`planes,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`zone)`{.docutils .literal .notranslate}]{.pre}:

        > <div>
        >
        > [`data`{.docutils .literal .notranslate}]{.pre} ([[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of [[`floats`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference .external})
        >
        > :   Flattened [[`float`{.xref .any .docutils .literal
        >     .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        >     .external} array which can be reshaped to [`(V,`{.docutils
        >     .literal .notranslate}]{.pre}` `{.docutils .literal
        >     .notranslate}[`N)`{.docutils .literal .notranslate}]{.pre}
        >     where [`V`{.docutils .literal .notranslate}]{.pre} is the
        >     number of variables returned (either the number of
        >     variables in the dataset or the length of **variables**
        >     input parameter) and [`N`{.docutils .literal
        >     .notranslate}]{.pre} is the number of points probed.
        >
        > [`cells_or_nodes`{.docutils .literal .notranslate}]{.pre} ([[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of [[`integers`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external})
        >
        > :   The index to the cells (or nodes if
        >     [[`ProbeNearest.Node`{.xref .any .py .py-attr .docutils
        >     .literal
        >     .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ProbeNearest.Node "tecplot.constant.ProbeNearest.Node"){.reference
        >     .internal} was passed in to **probe_nearest**) containing
        >     the returned positions.
        >
        > [`planes`{.docutils .literal .notranslate}]{.pre} ([[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of [[`IJKPlanes`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AnimationType.IJKPlanes "tecplot.constant.AnimationType.IJKPlanes"){.reference .internal})
        >
        > :   For ordered zones, these are the plane-orientations of the
        >     cells for each probed position.
        >
        > [`zones`{.docutils .literal .notranslate}]{.pre} ([[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of [[Zones]{.std .std-ref}](#data-access){.reference .internal})
        >
        > :   Zones containing the given positions.
        >
        > </div>

    ::: versionadded
    [New in version 2018.1: ]{.versionmodified .added}Probe on surface
    requires Tecplot 360 2018 R1 or later.
    :::

    ::::: {.admonition .note}
    Note

    The frame's plot type must be set to [[`PlotType.Cartesian3D`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal}

    Probe on surface requires the spatial variables to be set according
    to the frame's style. This can be done by setting the plot type to
    [[`PlotType.Cartesian3D`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal}. Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        tp.active_frame().plot_type = tp.constant.PlotType.Cartesian3D
    :::
    ::::

    For probing on 2D data, use [[`probe_at_position()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.query.probe_at_position "tecplot.data.query.probe_at_position"){.reference
    .internal}.
    :::::

    ::: {.admonition .note}
    Note

    Linear zones will always return nearest nodal values.

    If linear zones, which are ignored by default, are included in the
    **zones** parameter, the resulting values on that zone will always
    be nodal and no interpolation on the position will be done.
    :::

    ::: {.admonition .note}
    Note

    Irregular or jaggged surfaces may behave poorly.

    For performance reasons, this algorithm has the potential to miss
    the closest position on highly varying surfaces. This can be
    addressed by first increasing **num_nearest_nodes** to search more
    of the zones and then by increasing the **tolerance** to allow for
    imprecise position data - skewed polygons for example.

    All nodes of each cell considered are checked for co-planarity. This
    check can be relaxed slightly by increasing the **tolerance**
    parameter. The nearest position calculation will then be made
    assuming the cells are planar and the resulting positions may be
    imprecise.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import numpy as np

        import tecplot as tp
        from tecplot.constant import PlotType

        examples = tp.session.tecplot_examples_directory()
        datafile = path.join(examples, 'SimpleData', 'F18.plt')
        ds = tp.data.load_tecplot(datafile)
        fr = tp.active_frame()
        fr.plot_type = PlotType.Cartesian3D

        # probe a single point
        res = tp.data.query.probe_on_surface((13.5, 4.0, 0.6 ))

        '''
        The following line will print:
            (13.499723788684996, 3.9922783797612795, 0.49241572276992346,
            0.0018958827755862578, 0.07313805429221854, 0.997276718375976,
            0.06335166319722907)
        '''
        print(res.data)

        # probe multiple points
        points = np.array([[13.5,  4.0, 0.6],  # just above starboard wing
                           [13.5, -4.0, 0.6]]) # just above port wing

        res = tp.data.query.probe_on_surface(points.transpose())
        values = np.array(res.data).reshape((-1, len(points))).transpose()

        '''
        The following will print the probed position and the result of the probe
            [ 13.5   4.    0.6] [  1.34997238e+01   3.99227838e+00   4.92415723e-01
               1.89588278e-03   7.31380543e-02   9.97276718e-01   6.33516632e-02]
            [ 13.5  -4.    0.6] [  1.34997238e+01  -3.99227838e+00   4.92415723e-01
               1.89588278e-03   7.31380543e-02   9.97276718e-01   6.33516632e-02]
        '''
        for pt, v in zip(points, values):
            print(pt, v)
    :::
    ::::
:::
:::::

:::::::::::: {#data-operations .section}
## [Data Operations](#id45){.toc-backref role="doc-backlink"}[¶](#data-operations "Link to this heading"){.headerlink}

- [data.operate.execute_equation()](#data-operate-execute-equation){#id94
  .reference .internal}

- [data.operate.interpolate_inverse_distance()](#data-operate-interpolate-inverse-distance){#id95
  .reference .internal}

- [data.operate.interpolate_kriging()](#data-operate-interpolate-kriging){#id96
  .reference .internal}

- [data.operate.interpolate_linear()](#data-operate-interpolate-linear){#id97
  .reference .internal}

- [data.operate.smooth()](#data-operate-smooth){#id98 .reference
  .internal}

- [data.operate.transform_polar_to_rectangular()](#data-operate-transform-polar-to-rectangular){#id99
  .reference .internal}

- [data.operate.transform_rectangular_to_polar()](#data-operate-transform-rectangular-to-polar){#id100
  .reference .internal}

- [data.operate.transform_rectangular_to_spherical()](#data-operate-transform-rectangular-to-spherical){#id101
  .reference .internal}

- [data.operate.transform_spherical_to_rectangular()](#data-operate-transform-spherical-to-rectangular){#id102
  .reference .internal}

::: {#data-operate-execute-equation .section}
### [data.operate.execute_equation()](#id94){.toc-backref role="doc-backlink"}[¶](#data-operate-execute-equation "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[execute_equation]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[equation]{.pre}]{.n}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[i_range]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[j_range]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[k_range]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[value_location]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variable_data_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[ignore_divide_by_zero]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#execute_equation){.reference .internal}[¶](#tecplot.data.operate.execute_equation "Link to this definition"){.headerlink}

:   The execute_equation function operates on a data set within the
    Tecplot Engine using FORTRAN-like equations.

    Parameters[:]{.colon}

    :   - **equation** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) --

          String containing the equation. Multiple equations can be
          processed by separating each equation with a newline. See
          Section 20 - 1 "Data Alteration through Equations" in the
          [Tecplot User's
          Manual](https://tecplot.azureedge.net/products/360/current/help/users_manual/title-page.html){.reference
          .external} for more information on using equations. Iterable
          container of [[Zone]{.std .std-ref}](#data-access){.reference
          .internal} objects to operate on. May be a list, set, tuple,
          or any iterable container. If [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the equation will be applied to all zones.

          ::: {.admonition .note}
          Note

          In the equation string, variable names should be enclosed in
          curly braces. For example, '{X} = {X} + 1'
          :::

        - **zones** -- (Iterable container of [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} objects,
          optional): Iterable container of [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} objects to
          operate on. May be a list, set, tuple, or any iterable
          container. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the equation will be applied to all zones.

        - **i_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Tuple of integers for I: (min, max,
          step). If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then the equation will operate on the entire
          range. Not used for finite element nodal data.

        - **j_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Tuple of integers for J: (min, max,
          step). If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then the equation will operate on the entire
          range. Not used for finite element nodal data.

        - **k_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Tuple of integers for K: (min, max,
          step). If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then the equation will operate on the entire
          range. Not used for finite element nodal data.

        - **value_location** ([[`ValueLocation`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
          .internal}, optional) -- Variable [[`ValueLocation`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
          .internal} for the variable on the left hand side. This is
          used only if this variable is being created for the first
          time. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, Tecplot Engine will choose the location for you.

        - **variable_data_type** ([[`FieldDataType`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType "tecplot.constant.FieldDataType"){.reference
          .internal}, optional) -- Data type for the variable on the
          left hand side. This is used only if this variable is being
          created for the first time. If [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, Tecplot Engine will choose the type for you.

        - **ignore_divide_by_zero** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- [[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external} value which instructs Tecplot Engine to ignore
          divide by zero errors. The result is clamped such that 0/0 is
          clamped to zero and (+/-N)/0 where N != 0 clamps to +/-maximum
          value for the given type.

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
    .notranslate}]{.pre}](#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal}.
    :::

    Add one to variable 'X' for zones 'Rectangular' and 'Circular' for
    every data point:

    :::: {.doctest .highlight-default .notranslate}
    ::: highlight
        >>> dataset = tecplot.active_frame().dataset
        >>> execute_equation('{X} = {X} + 1', zones=[dataset.zone('Rectangular'),
        >>>                  dataset.zone('Circular')])
    :::
    ::::

    Create a new, double precision variable called DIST:

    :::: {.doctest .highlight-default .notranslate}
    ::: highlight
        >>> execute_equation('{DIST} = SQRT({X}**2 + {Y}**2)',
        ...                  variable_data_type=FieldDataType.Double)
    :::
    ::::

    Set a variable called **P** to zero along the boundary of an
    IJ-ordered zone:

    :::: {.doctest .highlight-default .notranslate}
    ::: highlight
        >>> execute_equation('{P} = 0', i_range=(0, -1, 0), j_range=(0, -1, 0))
    :::
    ::::

    Using 1-based indexing in equations and 0-based indexing in
    parameters. Zone 4 is subtracted from zone 3 and the result is
    placed in zone 2:

    :::: {.doctest .highlight-default .notranslate}
    ::: highlight
        >>> execute_equation('{T} = {T}[3]-{T}[4]', zones=[ds.zone(1)])
    :::
    ::::
:::

::: {#data-operate-interpolate-inverse-distance .section}
### [data.operate.interpolate_inverse_distance()](#id95){.toc-backref role="doc-backlink"}[¶](#data-operate-interpolate-inverse-distance "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[interpolate_inverse_distance]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[destination_zone]{.pre}]{.n}*, *[[source_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[exponent]{.pre}]{.n}[[=]{.pre}]{.o}[[3.5]{.pre}]{.default_value}*, *[[min_radius]{.pre}]{.n}[[=]{.pre}]{.o}[[0.0]{.pre}]{.default_value}*, *[[point_selection]{.pre}]{.n}[[=]{.pre}]{.o}[[PtSelection.OctantN]{.pre}]{.default_value}*, *[[num_points]{.pre}]{.n}[[=]{.pre}]{.o}[[8]{.pre}]{.default_value}*, *[[plot]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#interpolate_inverse_distance){.reference .internal}[¶](#tecplot.data.operate.interpolate_inverse_distance "Link to this definition"){.headerlink}

:   Inverse-Distance interpolation onto a destination zone.

    Parameters[:]{.colon}

    :   - **destination_zone** ([[zone]{.std
          .std-ref}](#data-access){.reference .internal} or
          [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The destination zone (or zone index) for
          interpolation.

        - **source_zones** ([[zones]{.std
          .std-ref}](#data-access){.reference .internal} or
          [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zones (or zone indices) used to
          obtain the field values for interpolation. By default, all
          zones except the *destination_zone* will be used. All source
          zones must be FE-Tetra, FE-Brick or be IJK-ordered when doing
          linear interpolation in 3D.

        - **variables** ([[`variables`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal} or [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Variables (or variable indices) to
          interpolate. By default, all variables except those assigned
          to the axes will be used and is in general dependent on the
          active plot type of the frame.

        - **exponent** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Exponent for the inverse-distance
          weighting. (default: 3.5)

        - **min_radius** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Minimum distance used for the
          inverse-distance weighting. (default: 0.0)

        - **point_selection** ([[`PtSelection`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection "tecplot.constant.PtSelection"){.reference
          .internal}, optional) -- Method for determining which source
          points to consider for each destination data point. Possible
          values: [[`PtSelection.OctantN`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.OctantN "tecplot.constant.PtSelection.OctantN"){.reference
          .internal} (default) closest *num_points* selected by
          coordinate-system octants, [[`PtSelection.NearestN`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.NearestN "tecplot.constant.PtSelection.NearestN"){.reference
          .internal} closest *num_points* to the destination point,
          [[`PtSelection.All`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.All "tecplot.constant.PtSelection.All"){.reference
          .internal} all points in the source zone.

        - **num_points** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Number of source points to consider
          for each destination data point if *point_selection* is
          [[`PtSelection.OctantN`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.OctantN "tecplot.constant.PtSelection.OctantN"){.reference
          .internal} or [[`PtSelection.NearestN`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.NearestN "tecplot.constant.PtSelection.NearestN"){.reference
          .internal}. (default: 8)

        - **plot** ([[Plot]{.std
          .std-ref}](tecplot.plot.html#plot){.reference .internal},
          optional) -- The plot to use when interpolating which
          determines the dimensionality and spatial variables. By
          default, the active plot on the active frame will be used.

    ::: {.admonition .note}
    Note

    Cartesian 2D and 3D plots only.

    This interpolation method relies on the coordinates, [\\((x,
    y)\\)]{.math .notranslate .nohighlight} for 2D or [\\((x, y,
    z)\\)]{.math .notranslate .nohighlight} for 3D, set for the active
    (or given) plot which must be either Cartesian2D or Cartesian3D.
    :::

    The following example loads a 2D dataset and interpolates the first
    zone to a new one with a larger grid spacing:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import numpy as np
        import tecplot as tp
        from tecplot.constant import *

        # Use interpolation to merge information from two independent zones
        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'RainierElevation.plt')
        dataset = tp.data.load_tecplot(datafile)
        # Get list of source zones to use later
        srczones = list(dataset.zones())

        fr = tp.active_frame()
        plot = fr.plot(PlotType.Cartesian2D)
        plot.activate()
        plot.show_contour = True
        plot.show_edge = True

        # Show two section of the plot independently
        plot.contour(0).legend.show = False
        plot.contour(1).legend.show = False
        plot.contour(1).colormap_name = 'Diverging - Blue/Red'
        for scrzone in srczones:
            plot.fieldmap(scrzone).edge.line_thickness = 0.4
        plot.fieldmap(0).contour.flood_contour_group = plot.contour(1)

        # export image of original data
        tp.export.save_png('interpolate_2d_source.png', 600, supersample=3)

        # use the first zone as the source, and get the range of (x, y)
        xvar = plot.axes.x_axis.variable
        yvar = plot.axes.y_axis.variable
        ymin, xmin = 99999,99999
        ymax, xmax = -99999,-99999
        for scrzone in srczones:
            curxmin, curxmax = scrzone.values(xvar.index).minmax()
            curymin, curymax = scrzone.values(yvar.index).minmax()
            ymin = min(curymin,ymin)
            ymax = max(curymax,ymax)
            xmin = min(curxmin,xmin)
            xmax = max(curxmax,xmax)

        # create new zone with a coarse grid
        # onto which we will interpolate from the source zone
        xpoints = 40
        ypoints = 40
        newzone = dataset.add_ordered_zone('Interpolated', (xpoints, ypoints))

        # setup the (x, y) positions of the new grid
        xx = np.linspace(xmin, xmax, xpoints)
        yy = np.linspace(ymin, ymax, ypoints)
        YY, XX = np.meshgrid(yy, xx, indexing='ij')
        newzone.values(xvar.index)[:] = XX.ravel()
        newzone.values(yvar.index)[:] = YY.ravel()

        # perform linear interpolation from the source to the new zone
        tp.data.operate.interpolate_inverse_distance(newzone, source_zones=srczones)

        # show the new zone's data, hide the source
        plot.fieldmap(newzone).show = True
        plot.fieldmap(newzone).contour.show = True
        plot.fieldmap(newzone).contour.flood_contour_group = plot.contour(0)
        plot.fieldmap(newzone).edge.show = True
        plot.fieldmap(newzone).edge.line_thickness = .4
        plot.fieldmap(newzone).edge.color = Color.Orange

        for scrzone in srczones:
            plot.fieldmap(scrzone).show = False

        # export image of interpolated data
        tp.export.save_png('interpolate_invdst_2d_dest.png', 600, supersample=3)
    :::
    ::::

    <figure id="id12" class="align-default" style="width: 300px">
    <a href="../_images/interpolate_2d_source.png"
    class="reference internal image-reference"><img
    src="../_images/interpolate_2d_source.png" style="width: 300px;"
    alt="../_images/interpolate_2d_source.png" /></a>
    <figcaption><p><span class="caption-text">Source data.</span><a
    href="#id12" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>

    <figure id="id13" class="align-default" style="width: 300px">
    <a href="../_images/interpolate_invdst_2d_dest.png"
    class="reference internal image-reference"><img
    src="../_images/interpolate_invdst_2d_dest.png" style="width: 300px;"
    alt="../_images/interpolate_invdst_2d_dest.png" /></a>
    <figcaption><p><span class="caption-text">Interpolated data.</span><a
    href="#id13" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>
:::

::: {#data-operate-interpolate-kriging .section}
### [data.operate.interpolate_kriging()](#id96){.toc-backref role="doc-backlink"}[¶](#data-operate-interpolate-kriging "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[interpolate_kriging]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[destination_zone]{.pre}]{.n}*, *[[source_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[krig_range]{.pre}]{.n}[[=]{.pre}]{.o}[[0.3]{.pre}]{.default_value}*, *[[zero_value]{.pre}]{.n}[[=]{.pre}]{.o}[[0.0]{.pre}]{.default_value}*, *[[drift]{.pre}]{.n}[[=]{.pre}]{.o}[[Drift.Linear]{.pre}]{.default_value}*, *[[point_selection]{.pre}]{.n}[[=]{.pre}]{.o}[[PtSelection.OctantN]{.pre}]{.default_value}*, *[[num_points]{.pre}]{.n}[[=]{.pre}]{.o}[[8]{.pre}]{.default_value}*, *[[plot]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#interpolate_kriging){.reference .internal}[¶](#tecplot.data.operate.interpolate_kriging "Link to this definition"){.headerlink}

:   Kriging interpolation onto a destination zone.

    Parameters[:]{.colon}

    :   - **destination_zone** ([[zone]{.std
          .std-ref}](#data-access){.reference .internal} or
          [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The destination zone (or zone index) for
          interpolation.

        - **source_zones** ([[zones]{.std
          .std-ref}](#data-access){.reference .internal} or
          [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zones (or zone indices) used to
          obtain the field values for interpolation. By default, all
          zones except the *destination_zone* will be used. All source
          zones must be FE-Tetra, FE-Brick or IJK-ordered when doing
          kriging interpolation in 3D.

        - **variables** ([[`variables`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal} or [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Variables (or variable indices) to
          interpolate. By default, all variables except those assigned
          to the axes will be used and is in general dependent on the
          active plot type of the frame.

        - **krig_range** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Distance beyond which source points
          become insignificant. Must be between zero and one, inclusive.
          (default: 0.3)

        - **zero_value** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Semi-variance at each source data
          point on a normalized scale from zero to one. (default: 0.0)

        - **drift** ([[`Drift`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Drift "tecplot.constant.Drift"){.reference
          .internal}, optional) -- Overall trend for the data. Possible
          values: [[`Drift.None_`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Drift.None_ "tecplot.constant.Drift.None_"){.reference
          .internal} no trend, [[`Drift.Linear`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Drift.Linear "tecplot.constant.Drift.Linear"){.reference
          .internal} (default) linear trend, [[`Drift.Quad`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Drift.Quad "tecplot.constant.Drift.Quad"){.reference
          .internal} quadratic trend.

        - **point_selection** ([[`PtSelection`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection "tecplot.constant.PtSelection"){.reference
          .internal}, optional) -- Method for determining which source
          points to consider for each destination data point. Possible
          values: [[`PtSelection.OctantN`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.OctantN "tecplot.constant.PtSelection.OctantN"){.reference
          .internal} (default) closest *num_points* selected by
          coordinate-system octants, [[`PtSelection.NearestN`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.NearestN "tecplot.constant.PtSelection.NearestN"){.reference
          .internal} closest *num_points* to the destination point,
          [[`PtSelection.All`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.All "tecplot.constant.PtSelection.All"){.reference
          .internal} all points in the source zone.

        - **num_points** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Number of source points to consider
          for each destination data point if *point_selection* is
          [[`PtSelection.OctantN`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.OctantN "tecplot.constant.PtSelection.OctantN"){.reference
          .internal} or [[`PtSelection.NearestN`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PtSelection.NearestN "tecplot.constant.PtSelection.NearestN"){.reference
          .internal}. (default: 8)

        - **plot** ([[Plot]{.std
          .std-ref}](tecplot.plot.html#plot){.reference .internal},
          optional) -- The plot to use when interpolating which
          determines the dimensionality and spatial variables. By
          default, the active plot on the active frame will be used.

    ::: {.admonition .note}
    Note

    Cartesian 2D and 3D plots only.

    This interpolation method relies on the coordinates, [\\((x,
    y)\\)]{.math .notranslate .nohighlight} for 2D or [\\((x, y,
    z)\\)]{.math .notranslate .nohighlight} for 3D, set for the active
    (or given) plot which must be either Cartesian2D or Cartesian3D.
    :::

    The following example loads a 2D dataset and interpolates the first
    zone to a new one with a larger grid spacing:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import numpy as np
        import tecplot as tp
        from tecplot.constant import *

        # Use interpolation to merge information from two independent zones
        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData',
                                'RainierElevation.plt')
        dataset = tp.data.load_tecplot(datafile)
        # Get list of source zones to use later
        srczones = list(dataset.zones())

        fr = tp.active_frame()
        plot = fr.plot(PlotType.Cartesian2D)
        plot.activate()
        plot.show_contour = True
        plot.show_edge = True

        # Show two section of the plot independently
        plot.contour(0).legend.show = False
        plot.contour(1).legend.show = False
        plot.contour(1).colormap_name = 'Diverging - Blue/Red'
        for scrzone in srczones:
            plot.fieldmap(scrzone).edge.line_thickness = 0.4
        plot.fieldmap(0).contour.flood_contour_group = plot.contour(1)

        # export image of original data
        tp.export.save_png('interpolate_2d_source.png', 600, supersample=3)

        # use the first zone as the source, and get the range of (x, y)
        xvar = plot.axes.x_axis.variable
        yvar = plot.axes.y_axis.variable
        ymin, xmin = 99999,99999
        ymax, xmax = -99999,-99999
        for scrzone in srczones:
            curxmin, curxmax = scrzone.values(xvar.index).minmax()
            curymin, curymax = scrzone.values(yvar.index).minmax()
            ymin = min(curymin,ymin)
            ymax = max(curymax,ymax)
            xmin = min(curxmin,xmin)
            xmax = max(curxmax,xmax)

        # create new zone with a coarse grid
        # onto which we will interpolate from the source zone
        xpoints = 20
        ypoints = 20
        newzone = dataset.add_ordered_zone('Interpolated', (xpoints, ypoints))

        # setup the (x, y) positions of the new grid
        xx = np.linspace(xmin, xmax, xpoints)
        yy = np.linspace(ymin, ymax, ypoints)
        YY, XX = np.meshgrid(yy, xx, indexing='ij')
        newzone.values(xvar.index)[:] = XX.ravel()
        newzone.values(yvar.index)[:] = YY.ravel()

        # perform linear interpolation from the source to the new zone
        tp.data.operate.interpolate_kriging(newzone, source_zones=srczones,
                                            drift=Drift.None_, num_points=1)

        # show the new zone's data, hide the source
        plot.fieldmap(newzone).show = True
        plot.fieldmap(newzone).contour.show = True
        plot.fieldmap(newzone).contour.flood_contour_group = plot.contour(0)
        plot.fieldmap(newzone).edge.show = True
        plot.fieldmap(newzone).edge.line_thickness = .4
        plot.fieldmap(newzone).edge.color = Color.Orange

        for scrzone in srczones:
            plot.fieldmap(scrzone).show = False

        # export image of interpolated data
        tp.export.save_png('interpolate_krig_2d_dest.png', 600, supersample=3)
    :::
    ::::

    <figure id="id14" class="align-default" style="width: 300px">
    <a href="../_images/interpolate_2d_source.png"
    class="reference internal image-reference"><img
    src="../_images/interpolate_2d_source.png" style="width: 300px;"
    alt="../_images/interpolate_2d_source.png" /></a>
    <figcaption><p><span class="caption-text">Source data.</span><a
    href="#id14" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>

    <figure id="id15" class="align-default" style="width: 300px">
    <a href="../_images/interpolate_krig_2d_dest.png"
    class="reference internal image-reference"><img
    src="../_images/interpolate_krig_2d_dest.png" style="width: 300px;"
    alt="../_images/interpolate_krig_2d_dest.png" /></a>
    <figcaption><p><span class="caption-text">Interpolated data.</span><a
    href="#id15" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>
:::

::: {#data-operate-interpolate-linear .section}
### [data.operate.interpolate_linear()](#id97){.toc-backref role="doc-backlink"}[¶](#data-operate-interpolate-linear "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[interpolate_linear]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[destination_zone]{.pre}]{.n}*, *[[source_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[variables]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[fill_value]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[plot]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#interpolate_linear){.reference .internal}[¶](#tecplot.data.operate.interpolate_linear "Link to this definition"){.headerlink}

:   Linear interpolation onto a destination zone.

    Parameters[:]{.colon}

    :   - **destination_zone** ([[zone]{.std
          .std-ref}](#data-access){.reference .internal} or
          [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The destination zone (or zone index) for
          interpolation.

        - **source_zones** ([[zones]{.std
          .std-ref}](#data-access){.reference .internal} or
          [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zones (or zone indices) used to
          obtain the field values for interpolation. By default, all
          zones except the *destination_zone* will be used. All source
          zones must be FE-Tetra, FE-Brick or be IJK-ordered when doing
          linear interpolation in 3D.

        - **variables** ([[`variables`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal} or [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Variables (or variable indices) to
          interpolate. By default, all variables except those assigned
          to the axes will be used and is in general dependent on the
          active plot type of the frame.

        - **fill_value** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Constant value to which all points
          outside the data field are set. By default, the values outside
          the field are preserved.

        - **plot** ([[Plot]{.std
          .std-ref}](tecplot.plot.html#plot){.reference .internal},
          optional) -- The plot to use when interpolating which
          determines the dimensionality and spatial variables. By
          default, the active plot on the active frame will be used.

    ::: {.admonition .note}
    Note

    Cartesian 2D and 3D plots only.

    This interpolation method relies on the coordinates, [\\((x,
    y)\\)]{.math .notranslate .nohighlight} for 2D or [\\((x, y,
    z)\\)]{.math .notranslate .nohighlight} for 3D, set for the active
    (or given) plot which must be either Cartesian2D or Cartesian3D.
    :::

    The following example loads a 2D dataset and uses interpolation to
    merge information from two independent zones:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import numpy as np
        import tecplot as tp
        from tecplot.constant import *

        # Use interpolation to merge information from two independent zones
        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'RainierElevation.plt')
        dataset = tp.data.load_tecplot(datafile)
        # Get list of source zones to use later
        srczones = list(dataset.zones())

        fr = tp.active_frame()
        plot = fr.plot(PlotType.Cartesian2D)
        plot.activate()
        plot.show_contour = True
        plot.show_edge = True

        # Show two section of the plot independently
        plot.contour(0).legend.show = False
        plot.contour(1).legend.show = False
        plot.contour(1).colormap_name = 'Diverging - Blue/Red'
        for scrzone in srczones:
            plot.fieldmap(scrzone).edge.line_thickness = 0.4
        plot.fieldmap(0).contour.flood_contour_group = plot.contour(1)

        # export image of original data
        tp.export.save_png('interpolate_2d_source.png', 600, supersample=3)

        # use the first zone as the source, and get the range of (x, y)
        xvar = plot.axes.x_axis.variable
        yvar = plot.axes.y_axis.variable
        ymin, xmin = 99999,99999
        ymax, xmax = -99999,-99999
        for scrzone in srczones:
            curxmin, curxmax = scrzone.values(xvar.index).minmax()
            curymin, curymax = scrzone.values(yvar.index).minmax()
            ymin = min(curymin,ymin)
            ymax = max(curymax,ymax)
            xmin = min(curxmin,xmin)
            xmax = max(curxmax,xmax)

        # create new zone with a coarse grid
        # onto which we will interpolate from the source zone
        xpoints = 40
        ypoints = 40
        newzone = dataset.add_ordered_zone('Interpolated', (xpoints, ypoints))

        # setup the (x, y) positions of the new grid
        xx = np.linspace(xmin, xmax, xpoints)
        yy = np.linspace(ymin, ymax, ypoints)
        YY, XX = np.meshgrid(yy, xx, indexing='ij')
        newzone.values(xvar.index)[:] = XX.ravel()
        newzone.values(yvar.index)[:] = YY.ravel()

        # perform linear interpolation from the source to the new zone
        tp.data.operate.interpolate_linear(newzone, source_zones=srczones)

        # show the new zone's data, hide the source
        plot.fieldmap(newzone).show = True
        plot.fieldmap(newzone).contour.show = True
        plot.fieldmap(newzone).contour.flood_contour_group = plot.contour(0)
        plot.fieldmap(newzone).edge.show = True
        plot.fieldmap(newzone).edge.line_thickness = .4
        plot.fieldmap(newzone).edge.color = Color.Orange

        for scrzone in srczones:
            plot.fieldmap(scrzone).show = False

        # export image of interpolated data
        tp.export.save_png('interpolate_linear_2d_dest.png', 600, supersample=3)
    :::
    ::::

    <figure id="id16" class="align-default" style="width: 300px">
    <a href="../_images/interpolate_2d_source.png"
    class="reference internal image-reference"><img
    src="../_images/interpolate_2d_source.png" style="width: 300px;"
    alt="../_images/interpolate_2d_source.png" /></a>
    <figcaption><p><span class="caption-text">Source data.</span><a
    href="#id16" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>

    <figure id="id17" class="align-default" style="width: 300px">
    <a href="../_images/interpolate_linear_2d_dest.png"
    class="reference internal image-reference"><img
    src="../_images/interpolate_linear_2d_dest.png" style="width: 300px;"
    alt="../_images/interpolate_linear_2d_dest.png" /></a>
    <figcaption><p><span class="caption-text">Interpolated data.</span><a
    href="#id17" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>
:::

::: {#data-operate-smooth .section}
### [data.operate.smooth()](#id98){.toc-backref role="doc-backlink"}[¶](#data-operate-smooth "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[smooth]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[array]{.pre}]{.n}*, *[[num_passes]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[weight]{.pre}]{.n}[[=]{.pre}]{.o}[[0.8]{.pre}]{.default_value}*, *[[boundary_condition]{.pre}]{.n}[[=]{.pre}]{.o}[[BoundaryCondition.Fixed]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#smooth){.reference .internal}[¶](#tecplot.data.operate.smooth "Link to this definition"){.headerlink}

:   Smooth a field data [[`Array`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArgListArgType.Array "tecplot.constant.ArgListArgType.Array"){.reference
    .internal} in the dataset.

    Parameters[:]{.colon}

    :   - **array** ([[`Array`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArgListArgType.Array "tecplot.constant.ArgListArgType.Array"){.reference
          .internal}) -- The field data to smooth.

        - **num_passes** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of smoothing passes to
          perform. (default: 1)

        - **weight** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The relaxation factor for each pass
          of smoothing. Must be a number between zero and one
          exclusively. Higher numbers indicate a greater smoothing
          effect. (default: 0.8)

        - **boundary_condition** ([[`BoundaryCondition`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BoundaryCondition "tecplot.constant.BoundaryCondition"){.reference
          .internal}, optional) -- The boundary condition by which to
          smooth. Possible values are [[`BoundaryCondition.Fixed`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BoundaryCondition.Fixed "tecplot.constant.BoundaryCondition.Fixed"){.reference
          .internal} (default), [[`BoundaryCondition.ZeroGradient`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BoundaryCondition.ZeroGradient "tecplot.constant.BoundaryCondition.ZeroGradient"){.reference
          .internal} and [[`BoundaryCondition.Zero2nd`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BoundaryCondition.Zero2nd "tecplot.constant.BoundaryCondition.Zero2nd"){.reference
          .internal}.

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- The [[`Frame`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} that specifies the spatial variables to smooth over
          via the active plot. By default, the frame associated with the
          input [[`Array`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArgListArgType.Array "tecplot.constant.ArgListArgType.Array"){.reference
          .internal} object will be used.

    The data will be smoothed over the spatial variables set by the plot
    and is dependent on the active plot type of the associated
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} ([[`Cartesian2D`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
    .internal} or [[`Cartesian3D`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal}). Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.data.operate.smooth(dataset.zone('Zone').values('Pressure'))
    :::
    ::::
:::

::: {#data-operate-transform-polar-to-rectangular .section}
### [data.operate.transform_polar_to_rectangular()](#id99){.toc-backref role="doc-backlink"}[¶](#data-operate-transform-polar-to-rectangular "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[transform_polar_to_rectangular]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[r]{.pre}]{.n}*, *[[theta]{.pre}]{.n}*, *[[x]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[y]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[angle_units]{.pre}]{.n}[[=]{.pre}]{.o}[[AngleUnits.Radians]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#transform_polar_to_rectangular){.reference .internal}[¶](#tecplot.data.operate.transform_polar_to_rectangular "Link to this definition"){.headerlink}

:   Transform all points from polar to rectangular coordinates.

    Parameters[:]{.colon}

    :   - **r** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The radial input variable.

        - **theta** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The angular input variable in **angle_units**
          from the [\\(x\\)]{.math .notranslate .nohighlight}-axis.

        - **x** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The rectangular output
          [\\(x\\)]{.math .notranslate .nohighlight} variable. By
          default, a new variable will be created. Both **x** and **y**
          must be specified together as either existing variables or as
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **y** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The rectangular output
          [\\(y\\)]{.math .notranslate .nohighlight} variable. By
          default, a new variable will be created. Both **x** and **y**
          must be specified together as either existing variables or as
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **angle_units** ([[`AngleUnits`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits "tecplot.constant.AngleUnits"){.reference
          .internal}, optional) -- The units of the angular variables.
          This may be either [[`AngleUnits.Radians`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Radians "tecplot.constant.AngleUnits.Radians"){.reference
          .internal} (default) or [[`AngleUnits.Degrees`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Degrees "tecplot.constant.AngleUnits.Degrees"){.reference
          .internal}.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          Specific zones to transform. By default, all zones are
          transformed.

    This example will create two new variables in the dataset
    corresponding to the [\\(x\\)]{.math .notranslate .nohighlight} and
    [\\(y\\)]{.math .notranslate .nohighlight} equivalents of the
    [\\(r\\)]{.math .notranslate .nohighlight} and [\\(theta\\)]{.math
    .notranslate .nohighlight} variables:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tp.active_frame().dataset
        >>> r = dataset.variable('R (m)')
        >>> theta = dataset.variable('Theta (rad)')
        >>> tp.data.operate.transform_polar_to_rectangular(r, theta)
        >>> x, y = dataset.variable(-2), dataset.variable(-1)
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Source variables must have the same location as the destination
    variables.**

    The variables involved with this transformation must all be either
    nodal or cell-centered.
    :::
:::

::: {#data-operate-transform-rectangular-to-polar .section}
### [data.operate.transform_rectangular_to_polar()](#id100){.toc-backref role="doc-backlink"}[¶](#data-operate-transform-rectangular-to-polar "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[transform_rectangular_to_polar]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[x]{.pre}]{.n}*, *[[y]{.pre}]{.n}*, *[[r]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[theta]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[angle_units]{.pre}]{.n}[[=]{.pre}]{.o}[[AngleUnits.Radians]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#transform_rectangular_to_polar){.reference .internal}[¶](#tecplot.data.operate.transform_rectangular_to_polar "Link to this definition"){.headerlink}

:   Transform all points from rectangular to polar coordinates.

    Parameters[:]{.colon}

    :   - **x** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The rectangular input [\\(x\\)]{.math
          .notranslate .nohighlight} variable.

        - **y** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The rectangular input [\\(y\\)]{.math
          .notranslate .nohighlight} variable.

        - **r** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The radial output [\\(r\\)]{.math
          .notranslate .nohighlight} variable. By default, a new
          variable will be created. Both **r** and **theta** must be
          specified together as either existing variables or as
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **theta** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The angular output
          [\\(theta\\)]{.math .notranslate .nohighlight} variable. By
          default, a new variable will be created. Both **r** and
          **theta** must be specified together as either existing
          variables or as [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **angle_units** ([[`AngleUnits`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits "tecplot.constant.AngleUnits"){.reference
          .internal}, optional) -- The units of the angular variables.
          This may be either [[`AngleUnits.Radians`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Radians "tecplot.constant.AngleUnits.Radians"){.reference
          .internal} (default) or [[`AngleUnits.Degrees`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Degrees "tecplot.constant.AngleUnits.Degrees"){.reference
          .internal}.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          Specific zones to transform. By default, all zones are
          transformed.

    This example will create two new variables in the dataset
    corresponding to the [\\(r\\)]{.math .notranslate .nohighlight} and
    [\\(theta\\)]{.math .notranslate .nohighlight} equivalents of the
    [\\(x\\)]{.math .notranslate .nohighlight} and [\\(y\\)]{.math
    .notranslate .nohighlight} variables:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tp.active_frame().dataset
        >>> x = dataset.variable('X (m)')
        >>> y = dataset.variable('Y (m)')
        >>> tp.data.operate.transform_rectangular_to_polar(x, y)
        >>> theta, r = dataset.variable(-2), dataset.variable(-1)
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Source variables must have the same location as the destination
    variables.**

    The variables involved with this transformation must all be either
    nodal or cell-centered.
    :::
:::

::: {#data-operate-transform-rectangular-to-spherical .section}
### [data.operate.transform_rectangular_to_spherical()](#id101){.toc-backref role="doc-backlink"}[¶](#data-operate-transform-rectangular-to-spherical "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[transform_rectangular_to_spherical]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[x]{.pre}]{.n}*, *[[y]{.pre}]{.n}*, *[[z]{.pre}]{.n}*, *[[r]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[theta]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[psi]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[angle_units]{.pre}]{.n}[[=]{.pre}]{.o}[[AngleUnits.Radians]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#transform_rectangular_to_spherical){.reference .internal}[¶](#tecplot.data.operate.transform_rectangular_to_spherical "Link to this definition"){.headerlink}

:   Transform all points from rectangular to spherical coordinates.

    Parameters[:]{.colon}

    :   - **x** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The rectangular input [\\(x\\)]{.math
          .notranslate .nohighlight} variable.

        - **y** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The rectangular input [\\(y\\)]{.math
          .notranslate .nohighlight} variable.

        - **z** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The rectangular input [\\(z\\)]{.math
          .notranslate .nohighlight} variable.

        - **r** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The radial output [\\(r\\)]{.math
          .notranslate .nohighlight} variable. By default, a new
          variable will be created. All of **r**, **theta** and **psi**
          must be specified together as either existing variables or as
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **theta** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The angular output
          [\\(theta\\)]{.math .notranslate .nohighlight} variable from
          the [\\(x\\)]{.math .notranslate .nohighlight}-axis. By
          default, a new variable will be created. All of **r**,
          **theta** and **psi** must be specified together as either
          existing variables or as [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **psi** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The angular output [\\(psi\\)]{.math
          .notranslate .nohighlight} variable from the [\\(z\\)]{.math
          .notranslate .nohighlight}-axis. By default, a new variable
          will be created. All of **r**, **theta** and **psi** must be
          specified together as either existing variables or as
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **angle_units** ([[`AngleUnits`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits "tecplot.constant.AngleUnits"){.reference
          .internal}, optional) -- The units of the angular variables.
          This may be either [[`AngleUnits.Radians`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Radians "tecplot.constant.AngleUnits.Radians"){.reference
          .internal} (default) or [[`AngleUnits.Degrees`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Degrees "tecplot.constant.AngleUnits.Degrees"){.reference
          .internal}.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          Specific zones to transform. By default, all zones are
          transformed.

    This example will create three new variables in the dataset
    corresponding to the [\\((r, theta, psi)\\)]{.math .notranslate
    .nohighlight} equivalents of the [\\((x, y, z)\\)]{.math
    .notranslate .nohighlight} variables:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tp.active_frame().dataset
        >>> x = dataset.variable('X (m)')
        >>> y = dataset.variable('Y (m)')
        >>> z = dataset.variable('Z (m)')
        >>> tp.data.operate.transform_rectangular_to_spherical(x, y, z)
        >>> theta = dataset.variable(-3)
        >>> r = dataset.variable(-2)
        >>> psi = dataset.variable(-1)
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Source variables must have the same location as the destination
    variables.**

    The variables involved with this transformation must all be either
    nodal or cell-centered.
    :::
:::

::: {#data-operate-transform-spherical-to-rectangular .section}
### [data.operate.transform_spherical_to_rectangular()](#id102){.toc-backref role="doc-backlink"}[¶](#data-operate-transform-spherical-to-rectangular "Link to this heading"){.headerlink}

[[tecplot.data.operate.]{.pre}]{.sig-prename .descclassname}[[transform_spherical_to_rectangular]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[r]{.pre}]{.n}*, *[[theta]{.pre}]{.n}*, *[[psi]{.pre}]{.n}*, *[[x]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[y]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[z]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[angle_units]{.pre}]{.n}[[=]{.pre}]{.o}[[AngleUnits.Radians]{.pre}]{.default_value}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/operate.html#transform_spherical_to_rectangular){.reference .internal}[¶](#tecplot.data.operate.transform_spherical_to_rectangular "Link to this definition"){.headerlink}

:   Transform all points from spherical to rectangular coordinates.

    Parameters[:]{.colon}

    :   - **r** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The radial input variable.

        - **theta** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The angular input variable in **angle_units**
          from the [\\(x\\)]{.math .notranslate .nohighlight}-axis.

        - **psi** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The angular input variable in **angle_units**
          from the [\\(z\\)]{.math .notranslate .nohighlight}-axis.

        - **x** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The rectangular output
          [\\(x\\)]{.math .notranslate .nohighlight} variable. By
          default, a new variable will be created. All of **x**, **y**
          and **z** must be specified together as either existing
          variables or as [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **y** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The rectangular output
          [\\(y\\)]{.math .notranslate .nohighlight} variable. By
          default, a new variable will be created. All of **x**, **y**
          and **z** must be specified together as either existing
          variables or as [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **z** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}, optional) -- The rectangular output
          [\\(z\\)]{.math .notranslate .nohighlight} variable. By
          default, a new variable will be created. All of **x**, **y**
          and **z** must be specified together as either existing
          variables or as [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **angle_units** ([[`AngleUnits`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits "tecplot.constant.AngleUnits"){.reference
          .internal}, optional) -- The units of the angular variables.
          This may be either [[`AngleUnits.Radians`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Radians "tecplot.constant.AngleUnits.Radians"){.reference
          .internal} (default) or [[`AngleUnits.Degrees`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AngleUnits.Degrees "tecplot.constant.AngleUnits.Degrees"){.reference
          .internal}.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          Specific zones to transform. By default, all zones are
          transformed.

    This example will create three new variables in the dataset
    corresponding to the [\\((x, y, z)\\)]{.math .notranslate
    .nohighlight} equivalents of the [\\((r, theta, psi)\\)]{.math
    .notranslate .nohighlight} variables:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tp.active_frame().dataset
        >>> r = dataset.variable('R (m)')
        >>> theta = dataset.variable('Theta (rad)')
        >>> psi = dataset.variable('Psi (rad)')
        >>> tp.data.operate.transform_spherical_to_rectangular(r, theta, psi)
        >>> x = dataset.variable(-3)
        >>> y = dataset.variable(-2)
        >>> z = dataset.variable(-1)
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Source variables must have the same location as the destination
    variables.**

    The variables involved with this transformation must all be either
    nodal or cell-centered.
    :::
:::
::::::::::::

:::::::: {#data-extractions .section}
## [Data Extractions](#id55){.toc-backref role="doc-backlink"}[¶](#data-extractions "Link to this heading"){.headerlink}

::: {#data-extract-extract-blanked-zones .section}
### [data.extract.extract_blanked_zones()](#id56){.toc-backref role="doc-backlink"}[¶](#data-extract-extract-blanked-zones "Link to this heading"){.headerlink}

[[tecplot.data.extract.]{.pre}]{.sig-prename .descclassname}[[extract_blanked_zones]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/extract.html#extract_blanked_zones){.reference .internal}[¶](#tecplot.data.extract.extract_blanked_zones "Link to this definition"){.headerlink}

:   Extract subsets of [Zones](#id7){.reference .internal} based on
    blanking conditions of the plot.

    Parameters[:]{.colon}

    :   **\*zones** ([Zones](#id7){.reference .internal}, required) --
        Set of source zones to extract.

    Keyword Arguments[:]{.colon}

    :   **plot** ([[`Cartesian3DFieldPlot`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot "tecplot.plot.Cartesian3DFieldPlot"){.reference
        .internal} or other data-backed plot type, optional) -- The plot
        that defines the blanking conditions. By default, the active
        plot will be used.

    Returns[:]{.colon}

    :   [Zones](#id7){.reference .internal} -- A [[`list`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of the extracted zones.

    A new zone will be created for each zone specified unless blanking
    dictates that all cells and points in the entire zone are blanked.
    The following example extracts all zones in the dataset:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os

        import tecplot as tp
        from tecplot.constant import *

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'VortexShedding.plt')

        dataset = tp.data.load_tecplot(datafile)

        plot = tp.active_frame().plot()
        plot.show_contour = True

        xax = plot.axes.x_axis
        xax.min = -0.005
        xax.max = 0.015
        yax = plot.axes.y_axis
        yax.min = -0.01
        yax.max = 0.002

        # Setup value blanking
        vblank = plot.value_blanking
        constraint = vblank.constraint(0)
        constraint.variable_index = 1
        constraint.comparison_operator = RelOp.GreaterThan
        constraint.active = True
        vblank.active = True

        # Use list comprehension to get all zones assocaitated with
        # a specific strand, in this case strand 1
        in_zns = [zn for zn in dataset.zones() if zn.strand == 1]

        # Extract all zones assocaitated with strand 1
        ext_zns = tp.data.extract.extract_blanked_zones(in_zns)

        # Place all extracted zones into the same strand
        for zn in ext_zns:
            zn.strand = 2

        # Turn off plotting for the original zone and turn on plotting
        # of the extracted zones.
        plot.fieldmap(0).show = False
        plot.fieldmap(1).show = True

        tp.export.save_time_animation_mpeg4('extract_blanked_zones.mp4',
                                            width=400, end_time=0.0004,
                                            supersample=3)
    :::
    ::::

    I\'m sorry; your browser doesn\'t support HTML5 MPEG4/H.264 video.

    ::: versionadded
    [New in version 2020.1: ]{.versionmodified .added}Extracting blanked
    zones requires Tecplot 360 2020 R1 or later.
    :::
:::

::: {#data-extract-extract-line .section}
### [data.extract.extract_line()](#id57){.toc-backref role="doc-backlink"}[¶](#data-extract-extract-line "Link to this heading"){.headerlink}

[[tecplot.data.extract.]{.pre}]{.sig-prename .descclassname}[[extract_line]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[points]{.pre}]{.n}*, *[[num_points]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/extract.html#extract_line){.reference .internal}[¶](#tecplot.data.extract.extract_line "Link to this definition"){.headerlink}

:   Create new zone from a line in the dataset.

    Parameters[:]{.colon}

    :   - **points** ([`2D`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`numeric`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`array`{.docutils .literal .notranslate}]{.pre})
          -- The points defining the line in two or three dimensions.
          This array must be of the shape *(N, D)* where *N* is the
          number points and *D* is the number of dimensions. That is, it
          must take the form [`[(x0,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`y0,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`z0),`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`(x1,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`y1,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`z1)`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`...]`{.docutils .literal .notranslate}]{.pre}.
          Points that do not lie within the dataset volume will be
          removed from the resulting zone.

        - **num_points** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of points to evenly
          distribute along the polyline. (default: length of *points* or
          *N*)

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- A [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} that holds the [[`Dataset`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to operate on which must match *dataset* if given.
          (default: currently active [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to operate on which must be attached to *frame* if
          given. (default: currently active [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal})

    Returns[:]{.colon}

    :   A 1D [[`OrderedZone`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.OrderedZone "tecplot.data.OrderedZone"){.reference
        .internal} representing a line through the data. Points outside
        of the dataset will be removed from the extracted zone resulting
        in fewer points than input.

    ::::: {.admonition .warning}
    Warning

    Line extraction is only available when the plot type is set to
    [[`Cartesian2D`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian2D "tecplot.constant.PlotType.Cartesian2D"){.reference
    .internal} or [[`Cartesian3D`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame.plot_type = PlotType.Cartesian3D
    :::
    ::::
    :::::

    This example shows how to extract a zone along a line, overlaying
    the result in a new frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        from os import path

        import tecplot as tp
        from tecplot.constant import *

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'VortexShedding.plt')
        dataset = tp.data.load_tecplot(datafile)

        frame = tp.active_frame()
        frame.activate()
        plot = frame.plot()
        plot.contour(0).variable = dataset.variable("P(N/M2)")
        plot.show_contour = True
        plot.contour(0).levels.reset(num_levels=11)
        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'

        plot.axes.y_axis.min = -0.01
        plot.axes.y_axis.max = 0.01
        plot.axes.x_axis.min = -0.005
        plot.axes.x_axis.max = 0.015

        xx = np.linspace(0, 0.01, 100)
        yy = np.zeros(100)
        line = tp.data.extract.extract_line(zip(xx, yy))

        plot.show_mesh = True
        plot.fieldmap(0).mesh.show = False

        frame = tp.active_page().add_frame()
        frame.position = (3.0, 0.5)
        frame.height = 2
        frame.width = 4
        plot = tp.active_frame().plot(PlotType.XYLine)
        plot.activate()

        plot.delete_linemaps()
        lmap = plot.add_linemap('data', line, x=dataset.variable('P(N/M2)'),
                                y=dataset.variable('T(K)'))
        lmap.line.line_thickness = 2.0
        plot.axes.x_axis(0).title.font.size = 10
        plot.axes.y_axis(0).title.font.size = 10
        plot.axes.viewport.left = 20
        plot.axes.viewport.bottom = 20
        plot.view.fit()

        tp.export.save_png("extract_line.png", region=ExportRegion.AllFrames,
                           width=600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/extract_line.png"
    class="reference internal image-reference"><img
    src="../_images/extract_line.png" style="width: 300px;"
    alt="../_images/extract_line.png" /></a>
    </figure>
:::

::: {#data-extract-extract-slice .section}
### [data.extract.extract_slice()](#id58){.toc-backref role="doc-backlink"}[¶](#data-extract-extract-slice "Link to this heading"){.headerlink}

[[tecplot.data.extract.]{.pre}]{.sig-prename .descclassname}[[extract_slice]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[origin]{.pre}]{.n}[[=]{.pre}]{.o}[[(0,]{.pre} [0,]{.pre} [0)]{.pre}]{.default_value}*, *[[normal]{.pre}]{.n}[[=]{.pre}]{.o}[[(0,]{.pre} [0,]{.pre} [1)]{.pre}]{.default_value}*, *[[source]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[mode]{.pre}]{.n}[[=]{.pre}]{.o}[[ExtractMode.SingleZone]{.pre}]{.default_value}*, *[[copy_cell_centers]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[assign_strand_ids]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[transient_mode]{.pre}]{.n}[[=]{.pre}]{.o}[[TransientOperationMode.SingleSolutionTime]{.pre}]{.default_value}*, *[[frame]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[dataset]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[resulting_1d_zone_type]{.pre}]{.n}[[=]{.pre}]{.o}[[Resulting1DZoneType.FELineSegment]{.pre}]{.default_value}*, *[[\*\*]{.pre}]{.o}[[kw]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/extract.html#extract_slice){.reference .internal}[¶](#tecplot.data.extract.extract_slice "Link to this definition"){.headerlink}

:   Create new zone from a plane in the dataset.

    Parameters[:]{.colon}

    :   - **origin** (array of three [[`floats`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Point in space, [\\((x, y, z)\\)]{.math
          .notranslate .nohighlight}, that lies on the slice plane.

        - **normal** (array of three [[`floats`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}) -- Vector direction, [\\((x, y, z)\\)]{.math
          .notranslate .nohighlight}, indicating the normal of the slice
          plane.

        - **source** ([[`SliceSource`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SliceSource "tecplot.constant.SliceSource"){.reference
          .internal}) -- Source zone types to consider when extracting
          the slice. Possible values: [[`SliceSource.LinearZones`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SliceSource.LinearZones "tecplot.constant.SliceSource.LinearZones"){.reference
          .internal}, [[`SliceSource.SurfaceZones`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SliceSource.SurfaceZones "tecplot.constant.SliceSource.SurfaceZones"){.reference
          .internal}, [[`SliceSource.SurfacesOfVolumeZones`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SliceSource.SurfacesOfVolumeZones "tecplot.constant.SliceSource.SurfacesOfVolumeZones"){.reference
          .internal}, [[`SliceSource.VolumeZones`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SliceSource.VolumeZones "tecplot.constant.SliceSource.VolumeZones"){.reference
          .internal} (default).

        - **mode** ([[`ExtractMode`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExtractMode "tecplot.constant.ExtractMode"){.reference
          .internal}) -- Controls how many zones are created. Possible
          values are: [[`ExtractMode.SingleZone`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExtractMode.SingleZone "tecplot.constant.ExtractMode.SingleZone"){.reference
          .internal} (default),
          [[`ExtractMode.OneZonePerConnectedRegion`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExtractMode.OneZonePerConnectedRegion "tecplot.constant.ExtractMode.OneZonePerConnectedRegion"){.reference
          .internal} and [[`ExtractMode.OneZonePerSourceZone`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExtractMode.OneZonePerSourceZone "tecplot.constant.ExtractMode.OneZonePerSourceZone"){.reference
          .internal}.

        - **copy_cell_centers** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}) -- If [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}, cell-center values will be copied when possible to
          the extracted slice plane. Cell-centers are copied when a
          variable is cell-centered for all the source zones through
          which the slice passes. Otherwise, extracted planes use
          node-centered data, which is calculated by interpolation.
          (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}) -- Automatically assign strand IDs to the data
          extracted from transient sources. This is only available if
          *multiple_zones* is [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **transient_mode** ([[`TransientOperationMode`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientOperationMode "tecplot.constant.TransientOperationMode"){.reference
          .internal}) -- Determines which solution times are used to
          extract slices when transient data is available in the
          dataset. Possible values are
          [[`TransientOperationMode.SingleSolutionTime`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientOperationMode.SingleSolutionTime "tecplot.constant.TransientOperationMode.SingleSolutionTime"){.reference
          .internal} (default) or
          [[`TransientOperationMode.AllSolutionTimes`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientOperationMode.AllSolutionTimes "tecplot.constant.TransientOperationMode.AllSolutionTimes"){.reference
          .internal}.

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- A [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} that holds the [[`Dataset`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to operate on which must match *dataset* if given.
          (default: currently active [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to operate on which must be attached to *frame* if
          given. (default: currently active [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal})

        - **resulting_1d_zone_type** ([[`Resulting1DZoneType`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Resulting1DZoneType "tecplot.constant.Resulting1DZoneType"){.reference
          .internal}, optional) -- The type of zone to create when the
          result is one-dimensional. Possible values are:
          [[`Resulting1DZoneType.FELineSegment`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Resulting1DZoneType.FELineSegment "tecplot.constant.Resulting1DZoneType.FELineSegment"){.reference
          .internal} (default) and
          [[`Resulting1DZoneType.IOrderedIfPossible`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Resulting1DZoneType.IOrderedIfPossible "tecplot.constant.Resulting1DZoneType.IOrderedIfPossible"){.reference
          .internal}.

    Returns[:]{.colon}

    :   One or a [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std .std-ref}](#data-access){.reference
        .internal} representing a planar slice.

    ::::: {.admonition .warning}
    Warning

    Slicing is only available when the plot type is set to 3D:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame.plot_type = PlotType.Cartesian3D
    :::
    ::::
    :::::

    ::: {.admonition .note}
    Note

    The extracted zone is returned if **mode** is
    [[`ExtractMode.SingleZone`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExtractMode.SingleZone "tecplot.constant.ExtractMode.SingleZone"){.reference
    .internal} and **transient_mode** is
    [[`TransientOperationMode.SingleSolutionTime`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientOperationMode.SingleSolutionTime "tecplot.constant.TransientOperationMode.SingleSolutionTime"){.reference
    .internal}, otherwise a
    [generator](https://docs.python.org/3/reference/expressions.html#generator-expressions){.reference
    .external} of the extracted zones.
    :::

    ::: {.admonition .seealso}
    See also

    [[`tecplot.plot.SliceGroup.extract()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroup.extract "tecplot.plot.SliceGroup.extract"){.reference
    .internal}
    :::

    This example shows extracting a slice zone from the surface a wing:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import tecplot as tp
        from tecplot.constant import PlotType, SliceSource

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'OneraM6wing',
                                'OneraM6_SU2_RANS.plt')
        dataset = tp.data.load_tecplot(datafile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian3D

        # set active plot to 3D and extract
        # an arbitrary slice from the surface
        # data on the wing
        extracted_slice = tp.data.extract.extract_slice(
            origin=(0, 0.25, 0),
            normal=(0, 1, 0),
            source=SliceSource.SurfaceZones,
            dataset=dataset)

        # switch plot type in current frame, clear plot
        plot = frame.plot(PlotType.XYLine)
        plot.activate()
        plot.delete_linemaps()

        # create line plot from extracted zone data
        cp_linemap = plot.add_linemap(
            name='Quarter-chord C_p',
            zone=extracted_slice,
            x=dataset.variable('x'),
            y=dataset.variable('Pressure_Coefficient'))

        # set style of linemap plot and
        # update axes limits to show data
        cp_linemap.line.color = tp.constant.Color.Blue
        cp_linemap.line.line_thickness = 0.8
        cp_linemap.y_axis.reverse = True
        plot.view.fit()

        # export image of pressure coefficient as a function of x
        tp.export.save_png('wing_slice_pressure_coeff.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/wing_slice_pressure_coeff.png"
    class="reference internal image-reference"><img
    src="../_images/wing_slice_pressure_coeff.png" style="width: 300px;"
    alt="../_images/wing_slice_pressure_coeff.png" /></a>
    </figure>
:::

::: {#data-extract-extract-connected-regions .section}
### [data.extract.extract_connected_regions()](#id59){.toc-backref role="doc-backlink"}[¶](#data-extract-extract-connected-regions "Link to this heading"){.headerlink}

[[tecplot.data.extract.]{.pre}]{.sig-prename .descclassname}[[extract_connected_regions]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/extract.html#extract_connected_regions){.reference .internal}[¶](#tecplot.data.extract.extract_connected_regions "Link to this definition"){.headerlink}

:   Create new zones from regions of connected cells.

    Parameters[:]{.colon}

    :   **\*zones** ([Zones](#id7){.reference .internal}, required) --
        Source zones from which to extract connected regions. All source
        zones must be finite-element zones, either classic FE or
        polygonal/polyhedral.

    Keyword Arguments[:]{.colon}

    :   - **assign_strand_ids** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Automatically assign strand IDs to
          the zones extracted from transient sources. If True the
          resulting zones will be all be assigned to the same newly
          created strand id. (default: [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

        - **frame** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, optional) -- A [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} that holds the [[`Dataset`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to operate on which must match *dataset* if given.
          (default: currently active [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal})

        - **dataset** ([[`Dataset`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}, optional) -- The [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} to operate on which must be attached to *frame* if
          given. (default: currently active [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal})

    Returns[:]{.colon}

    :   A [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of the extracted [[Zones]{.std
        .std-ref}](#data-access){.reference .internal}.

    ::: versionadded
    [New in version 2020.2: ]{.versionmodified .added}Extracting
    connected regions requires Tecplot 360 2020 R2 or later.
    :::
:::

::: {#data-extract-triangulate .section}
### [data.extract.triangulate()](#id60){.toc-backref role="doc-backlink"}[¶](#data-extract-triangulate "Link to this heading"){.headerlink}

[[tecplot.data.extract.]{.pre}]{.sig-prename .descclassname}[[triangulate]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/extract.html#triangulate){.reference .internal}[¶](#tecplot.data.extract.triangulate "Link to this definition"){.headerlink}

:   Create a new zone by forming triangles from points in 2D zones.

    Parameters[:]{.colon}

    :   **\*zones** ([Zones](#id7){.reference .internal}) -- Set of
        2-dimensional source zones to triangulate.

    Keyword Arguments[:]{.colon}

    :   - **boundary_zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [\\(I\\)]{.math .notranslate
          .nohighlight}-Ordered [Zones](#id7){.reference .internal},
          optional) -- Set of [\\(I\\)]{.math .notranslate
          .nohighlight}-ordered zones that define the boundaries across
          which no triangles can be created. (default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **include_boundary_points** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- If [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}, boundary points will be used to create triangles.
          (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **keep_factor** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external} in the range \[0.0, 0.5\], optional) -- The smaller
          the number, the more likely it will be that highly obtuse
          triangles will be created opening toward the outside of the
          triangulated zone.

        - **plot** ([[`Cartesian2DFieldPlot`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian2DFieldPlot "tecplot.plot.Cartesian2DFieldPlot"){.reference
          .internal}, optional) -- The plot defining the [\\((x,
          y)\\)]{.math .notranslate .nohighlight} variables in the
          dataset. If not set, the active plot will be used which must
          be of type [[`Cartesian2DFieldPlot`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian2DFieldPlot "tecplot.plot.Cartesian2DFieldPlot"){.reference
          .internal}.

    Returns[:]{.colon}

    :   [[`ClassicFEZone`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.ClassicFEZone "tecplot.data.ClassicFEZone"){.reference
        .internal} -- The resulting triangulated zone.

    The active plot or the plot specified must be of type
    [[`Cartesian2DFieldPlot`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian2DFieldPlot "tecplot.plot.Cartesian2DFieldPlot"){.reference
    .internal} and the boundary zones, if supplied, may only be
    [\\(I\\)]{.math .notranslate .nohighlight}-ordered zones. This
    example creates a new zone by triangulating data points from two
    other [Zones](#id7){.reference .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone0 = dataset.zone('Zone 0')
        >>> zone1 = dataset.zone('Zone 1')
        >>> new_zone = tp.data.extract.triangulate(zone0, zone1)
    :::
    ::::
:::
::::::::

::::::::::::::::::: {#data-access .section}
[]{#id4}

## [Data Access](#id61){.toc-backref role="doc-backlink"}[¶](#data-access "Link to this heading"){.headerlink}

- [Dataset](#dataset){#id103 .reference .internal}

- [SolutionTimeClustering](#solutiontimeclustering){#id104 .reference
  .internal}

- [Variable](#variable){#id105 .reference .internal}

- [Zones](#zones){#id106 .reference .internal}

  - [tecplot.data.zone](#module-tecplot.data.zone){#id107 .reference
    .internal}

  - [OrderedZone](#orderedzone){#id108 .reference .internal}

  - [ClassicFEZone](#classicfezone){#id109 .reference .internal}

  - [MixedFEZone](#mixedfezone){#id110 .reference .internal}

  - [PolyFEZone](#polyfezone){#id111 .reference .internal}

- [Array](#array){#id112 .reference .internal}

- [FECellType](#fecelltype){#id113 .reference .internal}

- [Nodemap](#nodemap){#id114 .reference .internal}

- [NodemapSection](#nodemapsection){#id115 .reference .internal}

- [ClassicNodemap](#classicnodemap){#id116 .reference .internal}

- [Facemap](#facemap){#id117 .reference .internal}

- [FaceNeighbors](#faceneighbors){#id118 .reference .internal}

::: {#dataset .section}
### [Dataset](#id103){.toc-backref role="doc-backlink"}[¶](#dataset "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[Dataset]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset){.reference .internal}[¶](#tecplot.data.Dataset "Link to this definition"){.headerlink}

:   Table of [[`Arrays`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} identified by [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} and
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.

    This is the primary data container within the Tecplot Engine. A
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} can be shared among several [[`Frames`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}, though any particular [[`Dataset`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} object will have a handle to at least one of them. Any
    modification of a shared [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} will be reflected in all [[`Frames`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it.

    Though a [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} is usually attached to a [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} and the plot style associated with that, it can be
    thought of as independent from any style or plotting representation.
    Each [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} consists of a list of [[`Variables`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} which are used by one or more of a list of [[Zones]{.std
    .std-ref}](#data-access){.reference .internal}. The
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} determines the data type, while the [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} determines the layout
    such as shape and ordered vs unordered.

    The actual data are found at the intersection of a [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} and
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} and the resulting object is an [[`Array`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal}. The data array can be obtained using either path:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # These two lines obtain the same object "x"
        >>> x = dataset.zone('My Zone').values('X')
        >>> x = dataset.variable('X').values('My Zone')
    :::
    ::::

    A [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} is the object returned by most data-loading operations in
    PyTecplot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset = tecplot.data.load_tecplot('my_data.plt')
    :::
    ::::

    Under [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}, there are a number methods to create and delete
    [[Zones]{.std .std-ref}](#data-access){.reference .internal} and
    [[`variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`VariablesNamedTuple`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.VariablesNamedTuple "tecplot.data.Dataset.VariablesNamedTuple"){.reference .internal}                  A [[`collections.namedtuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference .external} object using variable names.
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.aux_data "tecplot.data.Dataset.aux_data"){.reference .internal}                                                   Auxiliary data for this dataset.
      [[`num_solution_times`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.num_solution_times "tecplot.data.Dataset.num_solution_times"){.reference .internal}                     Number of solution times in the dataset.
      [[`num_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.num_variables "tecplot.data.Dataset.num_variables"){.reference .internal}                                    [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} in this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`num_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.num_zones "tecplot.data.Dataset.num_zones"){.reference .internal}                                                [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[Zones]{.std .std-ref}](#data-access){.reference .internal} in this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`solution_time_clustering`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.solution_time_clustering "tecplot.data.Dataset.solution_time_clustering"){.reference .internal}   Solution time clustering options.
      [[`solution_times`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.solution_times "tecplot.data.Dataset.solution_times"){.reference .internal}                                 Solution times in the dataset.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.title "tecplot.data.Dataset.title"){.reference .internal}                                                            [[`str`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference .external}: Title of this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`variable_names`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.variable_names "tecplot.data.Dataset.variable_names"){.reference .internal}                                 A [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of names for all variables in the dataset.
      [[`zone_names`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.zone_names "tecplot.data.Dataset.zone_names"){.reference .internal}                                             A [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of names for all zones in the dataset.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`add_fe_mixed_zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.add_fe_mixed_zone "tecplot.data.Dataset.add_fe_mixed_zone"){.reference .internal}(name, num_points, \...)         Add a finite-element [[Zone]{.std .std-ref}](#data-access){.reference .internal} consisting of one or more blocks of uniform cell-type (sections).
      [[`add_fe_zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.add_fe_zone "tecplot.data.Dataset.add_fe_zone"){.reference .internal}(zone_type, name, num_points, \...)                Add a single finite-element [[Zone]{.std .std-ref}](#data-access){.reference .internal} to this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`add_ordered_zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.add_ordered_zone "tecplot.data.Dataset.add_ordered_zone"){.reference .internal}(name, shape, \*\*kwargs)           Add a single ordered [[Zone]{.std .std-ref}](#data-access){.reference .internal} to this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`add_poly_zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.add_poly_zone "tecplot.data.Dataset.add_poly_zone"){.reference .internal}(zone_type, name, num_points, \...)          Add a single polygonal [[Zone]{.std .std-ref}](#data-access){.reference .internal} to this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`add_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.add_variable "tecplot.data.Dataset.add_variable"){.reference .internal}(name\[, dtypes, locations\])                   Add a single [[`Variable`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} to the active [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`add_zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference .internal}(zone_type, name, shape\[, dtypes, \...\])                  Add a single [[Zone]{.std .std-ref}](#data-access){.reference .internal} to this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`branch_connectivity`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.branch_connectivity "tecplot.data.Dataset.branch_connectivity"){.reference .internal}(zones)                    Breaks connectivity sharing between zones.
      [[`branch_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference .internal}(zones, variables\[, copy_data\])   Breaks data sharing between zones.
      [[`copy_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.copy_zones "tecplot.data.Dataset.copy_zones"){.reference .internal}(\*zones, \*\*kwargs)                                 Copies [[Zones]{.std .std-ref}](#data-access){.reference .internal} within this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`delete_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.delete_variables "tecplot.data.Dataset.delete_variables"){.reference .internal}(\*variables)                       Remove [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} from this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`delete_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.delete_zones "tecplot.data.Dataset.delete_zones"){.reference .internal}(\*zones)                                       Remove [[Zones]{.std .std-ref}](#data-access){.reference .internal} from this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`mirror_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.mirror_zones "tecplot.data.Dataset.mirror_zones"){.reference .internal}(mirror_variables, \*zones)                     Mirrors [[Zones]{.std .std-ref}](#data-access){.reference .internal} within this [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`share_connectivity`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.share_connectivity "tecplot.data.Dataset.share_connectivity"){.reference .internal}(source_zone, \...)           Share connectivity between zones.
      [[`share_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.share_variables "tecplot.data.Dataset.share_variables"){.reference .internal}(source_zone, \...)                    Share field data between zones.
      [[`variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.variable "tecplot.data.Dataset.variable"){.reference .internal}(pattern)                                                   Returns the [[`Variable`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} by index or string pattern.
      [[`variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.variables "tecplot.data.Dataset.variables"){.reference .internal}(\[pattern\])                                            Yields all [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} matching a *pattern*.
      [[`zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.zone "tecplot.data.Dataset.zone"){.reference .internal}(pattern)                                                               Returns [[Zone]{.std .std-ref}](#data-access){.reference .internal} by index or string pattern.
      [[`zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset.zones "tecplot.data.Dataset.zones"){.reference .internal}(\[pattern\])                                                        Yields all [[Zones]{.std .std-ref}](#data-access){.reference .internal} matching a *pattern*.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[VariablesNamedTuple]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.VariablesNamedTuple "Link to this definition"){.headerlink}

:   A [[`collections.namedtuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
    .external} object using variable names.

    The variable names are transformed to be unique, valid identifiers
    suitable for use as the key-list for a
    [[`collections.namedtuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
    .external}. This means that all invalid characters such as spaces
    and dashes are converted to underscores, Python keywords are
    appended by an underscore, leading numbers or empty names are
    prepended with a "v" and duplicate variable names are indexed
    starting with zero, padded left with zeros variable names duplicated
    more than nine times. The following table gives some specific
    examples:

    > <div>
    >
    >   Variable names                                                                                                                                                                                                                                                                                         Resulting namedtuple fields
    >   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    >   [`'x',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'y'`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                      [`'x',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'y'`{.docutils .literal .notranslate}]{.pre}
    >   [`'x',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'x'`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                      [`'x0',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'x1'`{.docutils .literal .notranslate}]{.pre}
    >   [`'X',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'Y=f(X)'`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                 [`'X',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'Y_f_X_'`{.docutils .literal .notranslate}]{.pre}
    >   [`'x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`2',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'_',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'_'`{.docutils .literal .notranslate}]{.pre}   [`'x_2',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'v0',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'v1'`{.docutils .literal .notranslate}]{.pre}
    >   [`'def',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'if'`{.docutils .literal .notranslate}]{.pre}                                                                                                                                                                   [`'def_',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'if_'`{.docutils .literal .notranslate}]{.pre}
    >   [`'1',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'2',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'3'`{.docutils .literal .notranslate}]{.pre}                                                                                   [`'v1',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'v2',`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`'v3'`{.docutils .literal .notranslate}]{.pre}
    >
    > </div>

    This example shows how one can use this n-tuple type with the result
    from a call to [[`tecplot.data.query.probe_at_position`{.xref .any
    .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.query.probe_at_position "tecplot.data.query.probe_at_position"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir,'SimpleData','DownDraft.plt')
        dataset = tp.data.load_tecplot(datafile)
        result = tp.data.query.probe_at_position(0,0.1,0.3)
        data = dataset.VariablesNamedTuple(*result.data)

        # prints: (RHO, E) = (1.17, 252930.37)
        msg = '(RHO, E) = ({:.2f}, {:.2f})'
        print(msg.format(data.RHO, data.E))
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[add_fe_mixed_zone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[num_points]{.pre}]{.n}*, *[[sections]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.add_fe_mixed_zone){.reference .internal}[¶](#tecplot.data.Dataset.add_fe_mixed_zone "Link to this definition"){.headerlink}

:   Add a finite-element [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} consisting of one or
    more blocks of uniform cell-type (sections).

    Parameters[:]{.colon}

    :   - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- have to be unique.

        - **num_points** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Number of points (nodes) in this zone.

        - **sections** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} or [[`tuples`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external}) -- A list of the properties of the sections in the
          form: [`(num_elements,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`cell_shape,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`grid_order,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`basis_function)`{.docutils .literal
          .notranslate}]{.pre}. The **grid_order** and **basis_func**
          items may be omitted and will default to **1** (linear) and
          [[`FECellBasisFunction.Lagrangian`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellBasisFunction.Lagrangian "tecplot.constant.FECellBasisFunction.Lagrangian"){.reference
          .internal} respectively.

        - **\*\*kwargs** -- These arguments are passed to
          [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
          .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}

    Keyword arguments are passed to the parent zone creation method
    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}.
    :::

    :::: {.admonition .warning}
    Warning

    **Setting connectivity in connected mode.**

    When connected to a running instance of Tecplot 360 using the
    TecUtil Server, care must be taken to ensure that the GUI does not
    try to render the data between the creation of the zone and the
    setting of the connectivity, through the [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal} or [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} objects. This can be achieved by setting the plot type of
    the frame(s) holding on to the dataset to [[`PlotType.Sketch`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
    .internal} before creating the zone and only going to
    [[`PlotType.Cartesian3D`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal} after the connectivity is set. Tecplot 360 may get into a
    bad state, corrupting loaded data, if it attempts to render
    (especially polytope) data without connectivity.

    ::: {.admonition .warning}
    Warning

    **Variable Sharing.**
    :::

    If a new zone has the same type and shape as an existing zone,
    variables may be shared by Tecplot to conserve memory. This variable
    sharing can be broken with the [[`branch_variables()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
    .internal} method. More information on when variable sharing occurs
    can be found in the [Tecplot User's
    Manual](https://tecplot.azureedge.net/products/360/current/help/users_manual/title-page.html){.reference
    .external}.
    ::::

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

    For more details, see the "working with datasets" examples shipped
    with PyTecplot in the Tecplot 360 distribution.

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[add_fe_zone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone_type]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[num_points]{.pre}]{.n}*, *[[num_elements]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.add_fe_zone){.reference .internal}[¶](#tecplot.data.Dataset.add_fe_zone "Link to this definition"){.headerlink}

:   Add a single finite-element [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} to this
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **zone_type** ([[`ZoneType`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
          .internal}) -- created. Possible values are:
          [[`FETriangle`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FETriangle "tecplot.constant.ZoneType.FETriangle"){.reference
          .internal}, [[`FEQuad`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEQuad "tecplot.constant.ZoneType.FEQuad"){.reference
          .internal}, [[`FETetra`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FETetra "tecplot.constant.ZoneType.FETetra"){.reference
          .internal}, [[`FEBrick`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEBrick "tecplot.constant.ZoneType.FEBrick"){.reference
          .internal} and [[`FELineSeg`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FELineSeg "tecplot.constant.ZoneType.FELineSeg"){.reference
          .internal}.

        - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- does not have to be unique.

        - **num_points** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Number of points (nodes) in this zone.

        - **num_elements** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Number of elements in this zone. The nodemap
          will have the shape (num_points, num_elements).

        - **\*\*kwargs** -- These arguments are passed to
          [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
          .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}

    Keyword arguments are passed to the parent zone creation method
    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}.
    :::

    :::: {.admonition .warning}
    Warning

    **Setting connectivity in connected mode.**

    When connected to a running instance of Tecplot 360 using the
    TecUtil Server, care must be taken to ensure that the GUI does not
    try to render the data between the creation of the zone and the
    setting of the connectivity, through the [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal} or [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} objects. This can be achieved by setting the plot type of
    the frame(s) holding on to the dataset to [[`PlotType.Sketch`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
    .internal} before creating the zone and only going to
    [[`PlotType.Cartesian3D`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal} after the connectivity is set. Tecplot 360 may get into a
    bad state, corrupting loaded data, if it attempts to render
    (especially polytope) data without connectivity.

    ::: {.admonition .warning}
    Warning

    **Variable Sharing.**
    :::

    If a new zone has the same type and shape as an existing zone,
    variables may be shared by Tecplot to conserve memory. This variable
    sharing can be broken with the [[`branch_variables()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
    .internal} method. More information on when variable sharing occurs
    can be found in the [Tecplot User's
    Manual](https://tecplot.azureedge.net/products/360/current/help/users_manual/title-page.html){.reference
    .external}.
    ::::

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

    The number of points (also known as nodes) per finite-element is
    determined from the [`zone_type`{.docutils .literal
    .notranslate}]{.pre} parameter. The follow table shows the number of
    points per element for the available zone types along with the
    resulting shape of the nodemap based on the number of points
    specified ([\\(N\\)]{.math .notranslate .nohighlight}):

    > <div>
    >
    >   Zone Type                                               Points/Element   Nodemap Shape
    >   ------------------------------------------------------- ---------------- --------------------------------------------------------------------------------------------
    >   [`FELineSeg`{.docutils .literal .notranslate}]{.pre}    2                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(2 N\\)]{.math .notranslate .nohighlight})
    >   [`FETriangle`{.docutils .literal .notranslate}]{.pre}   3                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(3 N\\)]{.math .notranslate .nohighlight})
    >   [`FEQuad`{.docutils .literal .notranslate}]{.pre}       4                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(4 N\\)]{.math .notranslate .nohighlight})
    >   [`FETetra`{.docutils .literal .notranslate}]{.pre}      4                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(4 N\\)]{.math .notranslate .nohighlight})
    >   [`FEBrick`{.docutils .literal .notranslate}]{.pre}      8                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(8 N\\)]{.math .notranslate .nohighlight})
    >
    > </div>

    For more details, see the "working with datasets" examples shipped
    with PyTecplot in the Tecplot 360 distribution.

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[add_ordered_zone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[shape]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.add_ordered_zone){.reference .internal}[¶](#tecplot.data.Dataset.add_ordered_zone "Link to this definition"){.headerlink}

:   Add a single ordered [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} to this
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- does not have to be unique.

        - **shape** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Specifies the length and dimension **(i, j,
          k)** of the new [[Zone]{.std
          .std-ref}](#data-access){.reference .internal}. A 1D
          [[Zone]{.std .std-ref}](#data-access){.reference .internal} is
          assumed if a single [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} is given.

        - **\*\*kwargs** -- These arguments are passed to
          [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
          .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}

    Keyword arguments are passed to the parent zone creation method
    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}.
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

    This example creates a 10x10x10 ordered zone of double-precision
    floating-point numbers:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import FieldDataType
        >>> my_zone = dataset.add_zone('My Zone', (10, 10, 10),
        ...                            dtypes=FieldDataType.Double)
    :::
    ::::

    Here is a full example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        # Generate data
        x = np.linspace(-4, 4, 100)

        # Setup Tecplot dataset
        dataset = tp.active_frame().create_dataset('Data', ['x', 'y'])

        # Create a zone
        zone = dataset.add_ordered_zone('sin(x)', len(x))
        zone.values('x')[:] = x
        zone.values('y')[:] = np.sin(x)

        # Create another zone
        zone = dataset.add_ordered_zone('cos(x)', len(x))
        zone.values('x')[:] = x
        zone.values('y')[:] = np.cos(x)

        # And one more zone
        zone = dataset.add_ordered_zone('tan(x)', len(x))
        zone.values('x')[:] = x
        zone.values('y')[:] = np.tan(x)

        # Set plot type to XYLine
        plot = tp.active_frame().plot(PlotType.XYLine)
        plot.activate()

        # Show all linemaps and make the lines a bit thicker
        for lmap in plot.linemaps():
            lmap.show = True
            lmap.line.line_thickness = 0.6

        plot.legend.show = True

        tp.export.save_png('add_ordered_zones.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/add_ordered_zones.png"
    class="reference internal image-reference"><img
    src="../_images/add_ordered_zones.png" style="width: 300px;"
    alt="../_images/add_ordered_zones.png" /></a>
    </figure>

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[add_poly_zone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone_type]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[num_points]{.pre}]{.n}*, *[[num_elements]{.pre}]{.n}*, *[[num_faces]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.add_poly_zone){.reference .internal}[¶](#tecplot.data.Dataset.add_poly_zone "Link to this definition"){.headerlink}

:   Add a single polygonal [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} to this
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **zone_type** ([[`ZoneType`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
          .internal}) -- created. Possible values are:
          [[`FEPolyhedron`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEPolyhedron "tecplot.constant.ZoneType.FEPolyhedron"){.reference
          .internal} and [[`FEPolygon`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEPolygon "tecplot.constant.ZoneType.FEPolygon"){.reference
          .internal}.

        - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- does not have to be unique.

        - **num_points** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Number of points in this zone.

        - **num_elements** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Number of elements in this zone.

        - **num_faces** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Number of faces in this zone.

        - **\*\*kwargs** -- These arguments are passed to
          [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
          .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}

    Keyword arguments are passed to the parent zone creation method
    [[`Dataset.add_zone`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}.
    :::

    :::: {.admonition .warning}
    Warning

    **Setting connectivity in connected mode.**

    When connected to a running instance of Tecplot 360 using the
    TecUtil Server, care must be taken to ensure that the GUI does not
    try to render the data between the creation of the zone and the
    setting of the connectivity, through the [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal} or [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} objects. This can be achieved by setting the plot type of
    the frame(s) holding on to the dataset to [[`PlotType.Sketch`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
    .internal} before creating the zone and only going to
    [[`PlotType.Cartesian3D`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal} after the connectivity is set. Tecplot 360 may get into a
    bad state, corrupting loaded data, if it attempts to render
    (especially polytope) data without connectivity.

    ::: {.admonition .warning}
    Warning

    **Variable Sharing.**
    :::

    If a new zone has the same type and shape as an existing zone,
    variables may be shared by Tecplot to conserve memory. This variable
    sharing can be broken with the [[`branch_variables()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
    .internal} method. More information on when variable sharing occurs
    can be found in the [Tecplot User's
    Manual](https://tecplot.azureedge.net/products/360/current/help/users_manual/title-page.html){.reference
    .external}.
    ::::

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

    ::::::: {.admonition .note}
    Note

    The **num_faces** is the number of *unique faces*.

    The number of unique faces, given an element map can be obtained
    using the following function for polygon data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        def num_unique_faces(elementmap):
            return len(set( tuple(sorted([e[i], e[(i+1)%len(e)]]))
                        for e in elementmap for i in range(len(e)) ))
    :::
    ::::

    This function creates a unique set of node pairs (edges around the
    polygons) and counts them. For polyhedron data, the following can be
    used:

    :::: {.highlight-python .notranslate}
    ::: highlight
        def num_unique_faces(elementmap):
            return len(set( tuple(sorted(f)) for e in elementmap
                                             for f in e ))
    :::
    ::::

    which merely counts the number of unique faces defined in the
    element map.
    :::::::

    For more details, see the "working with datasets" examples shipped
    with PyTecplot in the Tecplot 360 distribution.

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[add_variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}*, *[[dtypes]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[locations]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.add_variable){.reference .internal}[¶](#tecplot.data.Dataset.add_variable "Link to this definition"){.headerlink}

:   Add a single [[`Variable`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} to the active [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The name of the new [[`Variable`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}. This does not have to be unique.

        - **dtypes** ([[`FieldDataType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType "tecplot.constant.FieldDataType"){.reference
          .internal} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`FieldDataType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType "tecplot.constant.FieldDataType"){.reference
          .internal}, optional) -- Data types of this [[`Variable`{.xref
          .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} for each [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} in the
          currently active [[`Dataset`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. Options are: [[`FieldDataType.Float`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Float "tecplot.constant.FieldDataType.Float"){.reference
          .internal}, [[`Double`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Double "tecplot.constant.FieldDataType.Double"){.reference
          .internal}, [[`Int32`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Int32 "tecplot.constant.FieldDataType.Int32"){.reference
          .internal}, [[`Int16`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Int16 "tecplot.constant.FieldDataType.Int16"){.reference
          .internal}, [[`Byte`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Byte "tecplot.constant.FieldDataType.Byte"){.reference
          .internal} and [[`Bit`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Bit "tecplot.constant.FieldDataType.Bit"){.reference
          .internal}. If a single value, this will be duplicated for all
          [[Zones]{.std .std-ref}](#data-access){.reference .internal}.
          (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **locations** ([[`ValueLocation`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
          .internal} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`ValueLocation`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
          .internal}, optional) -- Point locations of this
          [[`Variable`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} for each [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} in the
          currently active [[`Dataset`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. Options are: [[`Nodal`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.Nodal "tecplot.constant.ValueLocation.Nodal"){.reference
          .internal} and [[`CellCentered`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.CellCentered "tecplot.constant.ValueLocation.CellCentered"){.reference
          .internal}. If a single value, this will be duplicated for all
          [[Zones]{.std .std-ref}](#data-access){.reference .internal}.
          (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}

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

    The added [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} will be available for use in each [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} of the dataset. This
    method should be used in conjunction with other data creation
    methods such as [[`Dataset.add_zone`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_zone "tecplot.data.Dataset.add_zone"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import math
        import tecplot as tp
        from tecplot.constant import PlotType

        # Setup Tecplot dataset
        dataset = tp.active_frame().create_dataset('Data')
        dataset.add_variable('x')
        dataset.add_variable('s')
        zone = dataset.add_ordered_zone('Zone', 100)

        # Fill the dataset
        x = [0.1 * i for i in range(100)]
        zone.values('x')[:] = x
        zone.values('s')[:] = [math.sin(i) for i in x]

        # Set plot type to XYLine
        tp.active_frame().plot(PlotType.XYLine).activate()

        tp.export.save_png('add_variables.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/add_variables.png"
    class="reference internal image-reference"><img
    src="../_images/add_variables.png" style="width: 300px;"
    alt="../_images/add_variables.png" /></a>
    </figure>

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[add_zone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone_type]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[shape]{.pre}]{.n}*, *[[dtypes]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[locations]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[face_neighbor_mode]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[parent_zone]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[solution_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[strand_id]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[index]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[sections]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.add_zone){.reference .internal}[¶](#tecplot.data.Dataset.add_zone "Link to this definition"){.headerlink}

:   Add a single [[Zone]{.std .std-ref}](#data-access){.reference
    .internal} to this [[`Dataset`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **zone_type** ([[`ZoneType`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
          .internal}) -- created. Possible values are: [[`Ordered`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.Ordered "tecplot.constant.ZoneType.Ordered"){.reference
          .internal}, [[`FETriangle`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FETriangle "tecplot.constant.ZoneType.FETriangle"){.reference
          .internal}, [[`FEQuad`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEQuad "tecplot.constant.ZoneType.FEQuad"){.reference
          .internal}, [[`FETetra`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FETetra "tecplot.constant.ZoneType.FETetra"){.reference
          .internal}, [[`FEBrick`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEBrick "tecplot.constant.ZoneType.FEBrick"){.reference
          .internal}, [[`FELineSeg`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FELineSeg "tecplot.constant.ZoneType.FELineSeg"){.reference
          .internal}, [[`FEPolyhedron`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEPolyhedron "tecplot.constant.ZoneType.FEPolyhedron"){.reference
          .internal}, [[`FEPolygon`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEPolygon "tecplot.constant.ZoneType.FEPolygon"){.reference
          .internal} and [[`FEMixed`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEMixed "tecplot.constant.ZoneType.FEMixed"){.reference
          .internal}.

        - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- does not have to be unique.

        - **shape** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Specifies the length and dimension (up to
          three) of the new [[Zone]{.std
          .std-ref}](#data-access){.reference .internal}. A 1D
          [[Zone]{.std .std-ref}](#data-access){.reference .internal} is
          assumed if a single [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} is given. This is **(i, j, k)** for ordered
          [[Zones]{.std .std-ref}](#data-access){.reference .internal},
          **(num_points, num_elements)** for finite-element
          [[Zones]{.std .std-ref}](#data-access){.reference .internal}
          and **(num_points, num_elements, num_faces)** for polytope
          [[Zones]{.std .std-ref}](#data-access){.reference .internal}
          where the number of faces is known.

        - **dtypes** ([[`FieldDataType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType "tecplot.constant.FieldDataType"){.reference
          .internal}, [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`FieldDataType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType "tecplot.constant.FieldDataType"){.reference
          .internal}, optional) -- Data types of this [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} for each
          [[`Variable`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} in the currently active [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. Options are: [[`Float`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Float "tecplot.constant.FieldDataType.Float"){.reference
          .internal}, [[`Double`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Double "tecplot.constant.FieldDataType.Double"){.reference
          .internal}, [[`Int32`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Int32 "tecplot.constant.FieldDataType.Int32"){.reference
          .internal}, [[`Int16`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Int16 "tecplot.constant.FieldDataType.Int16"){.reference
          .internal}, [[`Byte`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Byte "tecplot.constant.FieldDataType.Byte"){.reference
          .internal} and [[`Bit`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Bit "tecplot.constant.FieldDataType.Bit"){.reference
          .internal}. If a single value, this will be duplicated for all
          [[`Variables`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} then the type of the first [[`Variable`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}, defaulting to [[`FieldDataType.Float`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType.Float "tecplot.constant.FieldDataType.Float"){.reference
          .internal}, is used for all. (default: [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **locations** ([[`ValueLocation`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
          .internal}, [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`ValueLocation`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
          .internal}, optional) -- Point locations of this [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} for each
          [[`Variable`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} in the currently active [[`Dataset`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal}. Options are: [[`Nodal`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.Nodal "tecplot.constant.ValueLocation.Nodal"){.reference
          .internal} and [[`CellCentered`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.CellCentered "tecplot.constant.ValueLocation.CellCentered"){.reference
          .internal}. If a single value, this will be duplicated for all
          [[`Variables`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} then the type of the first [[`Variable`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}, defaulting to [[`Nodal`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.Nodal "tecplot.constant.ValueLocation.Nodal"){.reference
          .internal}, is used for all. (default: [[`None`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **face_neighbor_mode** ([[`FaceNeighborMode`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode "tecplot.constant.FaceNeighborMode"){.reference
          .internal}, optional) -- Specifies the face-neighbor mode for
          this zone. Options are:
          [[`FaceNeighborMode.LocalOneToOne`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.LocalOneToOne "tecplot.constant.FaceNeighborMode.LocalOneToOne"){.reference
          .internal} (default),
          [[`FaceNeighborMode.LocalOneToMany`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.LocalOneToMany "tecplot.constant.FaceNeighborMode.LocalOneToMany"){.reference
          .internal}, [[`FaceNeighborMode.GlobalOneToOne`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.GlobalOneToOne "tecplot.constant.FaceNeighborMode.GlobalOneToOne"){.reference
          .internal} or [[`FaceNeighborMode.GlobalOneToMany`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.GlobalOneToMany "tecplot.constant.FaceNeighborMode.GlobalOneToMany"){.reference
          .internal}.

        - **parent_zone** ([[Zone]{.std
          .std-ref}](#data-access){.reference .internal}, optional) -- A
          parent [[Zone]{.std .std-ref}](#data-access){.reference
          .internal} to be used when generating surface-restricted
          streamtraces.

        - **solution_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- Solution time for this zone.
          (default: 0)

        - **strand_id** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Associate this new [[Zone]{.std
          .std-ref}](#data-access){.reference .internal} with a
          particular strand.

        - **index** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Number of the zone to add or replace.
          If omitted or set to [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the new zone will be appended to the dataset. This
          value can be set to the number of a zone that already exists
          thereby replacing the existing zone. (default: [[`None`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **sections** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} or [[`tuples`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external}) -- A list of the properties of the sections in the
          form: [`(num_element,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`cell_shape,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`grid_order,`{.docutils .literal
          .notranslate}]{.pre}` `{.docutils .literal
          .notranslate}[`basis_function)`{.docutils .literal
          .notranslate}]{.pre}. The **grid_order** and **basis_func**
          items may be omitted and will default to **1** (linear) and
          [[`FECellBasisFunction.Lagrangian`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellBasisFunction.Lagrangian "tecplot.constant.FECellBasisFunction.Lagrangian"){.reference
          .internal} respectively. This parameter is only used when
          **zone_type** is set to [[`FEMixed`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEMixed "tecplot.constant.ZoneType.FEMixed"){.reference
          .internal}.

    Returns[:]{.colon}

    :   [[Zone]{.std .std-ref}](#data-access){.reference .internal}

    :::: {.admonition .warning}
    Warning

    **Setting connectivity in connected mode.**

    When connected to a running instance of Tecplot 360 using the
    TecUtil Server, care must be taken to ensure that the GUI does not
    try to render the data between the creation of the zone and the
    setting of the connectivity, through the [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal} or [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} objects. This can be achieved by setting the plot type of
    the frame(s) holding on to the dataset to [[`PlotType.Sketch`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Sketch "tecplot.constant.PlotType.Sketch"){.reference
    .internal} before creating the zone and only going to
    [[`PlotType.Cartesian3D`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PlotType.Cartesian3D "tecplot.constant.PlotType.Cartesian3D"){.reference
    .internal} after the connectivity is set. Tecplot 360 may get into a
    bad state, corrupting loaded data, if it attempts to render
    (especially polytope) data without connectivity.

    ::: {.admonition .warning}
    Warning

    **Variable Sharing.**
    :::

    If a new zone has the same type and shape as an existing zone,
    variables may be shared by Tecplot to conserve memory. This variable
    sharing can be broken with the [[`branch_variables()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
    .internal} method. More information on when variable sharing occurs
    can be found in the [Tecplot User's
    Manual](https://tecplot.azureedge.net/products/360/current/help/users_manual/title-page.html){.reference
    .external}.
    ::::

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

    The added [[Zone]{.std .std-ref}](#data-access){.reference
    .internal} will be able to use all [[`Variables`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} defined in the dataset. This method should be used in
    conjunction with other data creation methods such as
    [[`Frame.create_dataset`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.create_dataset "tecplot.layout.Frame.create_dataset"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ZoneType
        >>> zone = dataset.add_zone(ZoneType.Ordered, 'Zone', (10, 10, 10))
    :::
    ::::

    ::: {.admonition .note}
    Note

    The relationship and meaning of this method's parameters change
    depending on the type of zone being created. Therefore, it is
    recommended to use the more specific zone creation methods:

    > <div>
    >
    > - [[`Dataset.add_ordered_zone`{.xref .any .py .py-meth .docutils
    >   .literal
    >   .notranslate}]{.pre}](#tecplot.data.Dataset.add_ordered_zone "tecplot.data.Dataset.add_ordered_zone"){.reference
    >   .internal}
    >
    > - [[`Dataset.add_fe_zone`{.xref .any .py .py-meth .docutils
    >   .literal
    >   .notranslate}]{.pre}](#tecplot.data.Dataset.add_fe_zone "tecplot.data.Dataset.add_fe_zone"){.reference
    >   .internal}
    >
    > - [[`Dataset.add_poly_zone`{.xref .any .py .py-meth .docutils
    >   .literal
    >   .notranslate}]{.pre}](#tecplot.data.Dataset.add_poly_zone "tecplot.data.Dataset.add_poly_zone"){.reference
    >   .internal}
    >
    > </div>
    :::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this dataset.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the dataset. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> aux = frame.dataset.aux_data
        >>> aux['Result'] = '3.14159'
        >>> print(aux['Result'])
        3.14159
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[branch_connectivity]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zones]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.branch_connectivity){.reference .internal}[¶](#tecplot.data.Dataset.branch_connectivity "Link to this definition"){.headerlink}

:   Breaks connectivity sharing between zones.

    Parameters[:]{.colon}

    :   **zones** ([[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std .std-ref}](#data-access){.reference
        .internal}) -- Zones to be branched.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.share_connectivity()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.share_connectivity "tecplot.data.Dataset.share_connectivity"){.reference
    .internal}
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> z = dataset.zone('My Zone')
        >>> zcopy = z.copy()
        >>> print([zn.index for zn in z.shared_connectivity])
        [0,1]
        >>> dataset.branch_connectivity(zcopy)
        >>> print([zn.index for zn in z.shared_connectivity])
        []
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[branch_variables]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zones]{.pre}]{.n}*, *[[variables]{.pre}]{.n}*, *[[copy_data]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.branch_variables){.reference .internal}[¶](#tecplot.data.Dataset.branch_variables "Link to this definition"){.headerlink}

:   Breaks data sharing between zones.

    Parameters[:]{.colon}

    :   - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}) -- Zones to be
          branched.

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}) -- Variables to be branched.

        - **copy_data** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Allocate space for the branched
          values and copy the data. If [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, the new variables will be passive. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    ::: {.admonition .seealso}
    See also

    [[`Dataset.share_variables()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.share_variables "tecplot.data.Dataset.share_variables"){.reference
    .internal}
    :::

    Variable sharing allows you to lower the use of physical memory
    (RAM). When sharing a variable the memory used by the source zone is
    shared with the copied zone. Alterations to the variable in one zone
    will affect the other. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> z = dataset.zone('My Zone')
        >>> zcopy = z.copy(share_variables=True)
        >>> print([zn.index for zn in z.values(0).shared_zones])
        [0,1]
        >>> dataset.branch_variables(zcopy,dataset.variable(0))
        >>> print([zn.index for zn in z.values(0).shared_zones])
        []
        >>> print([zn.index for zn in z.values(1).shared_zones])
        [0,1]
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[copy_zones]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.copy_zones){.reference .internal}[¶](#tecplot.data.Dataset.copy_zones "Link to this definition"){.headerlink}

:   Copies [[Zones]{.std .std-ref}](#data-access){.reference .internal}
    within this [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **\*zones** ([[Zone]{.std .std-ref}](#data-access){.reference
          .internal}, optional) -- Specific [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to copy. All
          zones will be copied if none are supplied.

        - **share_variables** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}) -- Share all variables between the original and
          generated zones if [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} or the list of Variables to be shared. Variable
          sharing allows you to lower the use of physical memory (RAM).
          When sharing a variable the memory used by the source zone is
          shared with the copied zone. Alterations to the variable in
          one zone will affect the other. See also
          [[`Dataset.branch_variables()`{.xref .any .py .py-meth
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
          .internal}. Default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}.

        - **i_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Range (min, max, step) along the
          [`i`{.docutils .literal .notranslate}]{.pre} dimension for
          ordered data. Min and max are zero-based indicies where max is
          inclusive. If step causes max to be skipped, max will be
          included. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default), the entire range will be copied.

        - **j_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Range (min, max, step) along the
          [`j`{.docutils .literal .notranslate}]{.pre} dimension for
          ordered data. Min and max are zero-based indicies where max is
          inclusive. If step causes max to be skipped, max will be
          included. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default), the entire range will be copied.

        - **k_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Range (min, max, step) along the
          [`k`{.docutils .literal .notranslate}]{.pre} dimension for
          ordered data. Min and max are zero-based indicies where max is
          inclusive. If step causes max to be skipped, max will be
          included. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default), the entire range will be copied.

    Returns[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of the newly created [[Zones]{.std
        .std-ref}](#data-access){.reference .internal}.

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

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        ds = tp.active_page().add_frame().create_dataset('D', ['x','y','z'])
        z = ds.add_ordered_zone('Z1', (3,3,3))
        ds.copy_zones(z, i_range=(1, -1, 2), share_variables=True)
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[delete_variables]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[variables]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.delete_variables){.reference .internal}[¶](#tecplot.data.Dataset.delete_variables "Link to this definition"){.headerlink}

:   Remove [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} from this [[`Dataset`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **\*variables** ([[`Variable`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} or index [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- Variables to remove from this dataset.

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.variable_names)
        ['X','Y','Z']
        >>> dataset.delete_variables(dataset.variable('Z'))
        >>> print(dataset.variable_names)
        ['X','Y']
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    Deleting [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} invalidates iterators referencing them in the containing
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} such as those obtained from [[`Dataset.variables()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.variables "tecplot.data.Dataset.variables"){.reference
    .internal}. It is recommended to create a list of the
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} you want to delete and to pass that into a single call to
    [[`Dataset.delete_variables()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.delete_variables "tecplot.data.Dataset.delete_variables"){.reference
    .internal}
    :::

    Notes

    Multiple [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} can be deleted at once, though the last
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} can not be deleted. The following example deletes all but
    the first [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} in the [[`Dataset`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} (usually [`X`{.docutils .literal .notranslate}]{.pre}):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # Try to delete all variables:
        >>> dataset.delete_variables(dataset.variables())
        >>> # Dataset requires at least one variable to
        >>> # exist, so it leaves the first one:
        >>> print(dataset.variable_names)
        ['X']
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[delete_zones]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.delete_zones){.reference .internal}[¶](#tecplot.data.Dataset.delete_zones "Link to this definition"){.headerlink}

:   Remove [[Zones]{.std .std-ref}](#data-access){.reference .internal}
    from this [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **\*zones** ([[Zones]{.std .std-ref}](#data-access){.reference
        .internal} or index [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- Zones to remove from this dataset.

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone_names)
        ['Zone 1', 'Zone 2']
        >>> dataset.delete_zones(dataset.zone('Zone 2'))
        >>> print(dataset.zone_names)
        ['Zone 1']
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    Deleting [[Zones]{.std .std-ref}](#data-access){.reference
    .internal} invalidates iterators referencing them in the containing
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} such as those obtained from [[`Dataset.zones()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.zones "tecplot.data.Dataset.zones"){.reference
    .internal}. It is recommended to create a list of the [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} you want to delete
    and to pass that into a single call to
    [[`Dataset.delete_zones()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.delete_zones "tecplot.data.Dataset.delete_zones"){.reference
    .internal}
    :::

    Notes

    Multiple [[Zones]{.std .std-ref}](#data-access){.reference
    .internal} can be deleted at once, though the last [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} can not be deleted.
    The following example deletes all but the first [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} in the
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.delete_zones(dataset.zones())
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[mirror_zones]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mirror_variables]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[zones]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.mirror_zones){.reference .internal}[¶](#tecplot.data.Dataset.mirror_zones "Link to this definition"){.headerlink}

:   Mirrors [[Zones]{.std .std-ref}](#data-access){.reference .internal}
    within this [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Each mirror zone has a name of the form "Mirror of zone
    *sourcezone*", where *sourcezone* is the number of the zone from
    which the mirrored zone was created. The variables in the newly
    created zones are shared with their corresponding source zones,
    except for variables to be mirrored as specified.

    Parameters[:]{.colon}

    :   - **mirror_variables** ([[`Variable`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}) -- Variables in the new zone to be multiplied by
          [\\(-1\\)]{.math .notranslate .nohighlight} after the zone is
          copied. the variables may be [[`Variable`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal} objects, [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} names or [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} indices.

        - **\*zones** ([[Zones]{.std .std-ref}](#data-access){.reference
          .internal}, optional) -- Specific [[Zones]{.std
          .std-ref}](#data-access){.reference .internal} to mirror. All
          zones will be mirrored if none are supplied. The values may
          also be [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external} names or [[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} indices.

    Returns[:]{.colon}

    :   Generator of mirrored zones.

    This example show how to mirror all zones across the xy-plane in 3D:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> mirrored_zones = dataset.mirror_zones('Z')
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[num_solution_times]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.num_solution_times "Link to this definition"){.headerlink}

:   Number of solution times in the dataset.

    This property is read-only. Solution times are grouped according to
    the current solution time clustering settings (see
    [[`Dataset.solution_time_clustering`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.solution_time_clustering "tecplot.data.Dataset.solution_time_clustering"){.reference
    .internal}). Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.num_solution_times)
        10
    :::
    ::::

    ::: versionadded
    [New in version 2017.3: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R3 or later.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (read-only)

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[num_variables]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.num_variables "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[`Variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} in this [[`Dataset`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This count includes disabled variables which were skipped when the
    data was loaded. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for i in range(dataset.num_variables):
        ...     variable = dataset.variable(i)
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[num_zones]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.num_zones "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} in this
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This count includes disabled zones which were skipped when loading
    the data. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for i in range(dataset.num_zones):
        ...     zone = dataset.zone(i)
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[share_connectivity]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[source_zone]{.pre}]{.n}*, *[[destination_zones]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.share_connectivity){.reference .internal}[¶](#tecplot.data.Dataset.share_connectivity "Link to this definition"){.headerlink}

:   Share connectivity between zones.

    This method links the connectivity ([[`nodemap`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.nodemap "tecplot.data.ClassicFEZone.nodemap"){.reference
    .internal} or [[`facemap`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.PolyFEZone.facemap "tecplot.data.PolyFEZone.facemap"){.reference
    .internal}) of the destination [[zones]{.std
    .std-ref}](#data-access){.reference .internal} to the connectivity
    of the source zone. Modifying the connectivity of one zone will
    affect all others in this group.

    Parameters[:]{.colon}

    :   - **source_zone** ([[Zone]{.std
          .std-ref}](#data-access){.reference .internal}) -- Zone which
          provides data to be shared.

        - **destination_zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}) -- Zones where
          connectivity list will be overwritten.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.branch_connectivity()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.branch_connectivity "tecplot.data.Dataset.branch_connectivity"){.reference
    .internal}
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> z = dataset.zone('My Zone')
        >>> zcopy = z.copy()
        >>> print([zn.index for zn in z.shared_connectivity])
        [0,1]
        >>> dataset.branch_connectivity(zcopy)
        >>> print([zn.index for zn in z.shared_connectivity])
        []
        >>> dataset.share_connectivity(z,zcopy)
        >>> print([zn.index for zn in z.shared_connectivity])
        [0,1]
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[share_variables]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[source_zone]{.pre}]{.n}*, *[[destination_zones]{.pre}]{.n}*, *[[variables]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.share_variables){.reference .internal}[¶](#tecplot.data.Dataset.share_variables "Link to this definition"){.headerlink}

:   Share field data between zones.

    This method links the underlying data [[`arrays`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} of the destination [[zones]{.std
    .std-ref}](#data-access){.reference .internal} to the data of the
    source [[zone]{.std .std-ref}](#data-access){.reference .internal}.
    Modifying the array data of one zone will affect all others in this
    group.

    Parameters[:]{.colon}

    :   - **source_zone** ([[Zone]{.std
          .std-ref}](#data-access){.reference .internal}) -- Zone which
          provides data to be shared.

        - **destination_zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}) -- Zones where
          data will be overwritten.

        - **variables** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}) -- Variables to be shared.

    ::: {.admonition .seealso}
    See also

    [[`Dataset.branch_variables()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
    .internal}
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> z = dataset.zone('My Zone')
        >>> zcopy = z.copy(share_variables=False)
        >>> print([zn.index for zn in z.values(0).shared_zones])
        []
        >>> dataset.share_variables(zcopy,[z],[dataset.variable(0)])
        >>> print([zn.index for zn in z.values(0).shared_zones])
        [0,1]
        >>> print([zn.index for zn in z.values(1).shared_zones])
        []
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[solution_time_clustering]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.solution_time_clustering "Link to this definition"){.headerlink}

:   Solution time clustering options.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TimeScaling
        >>> dataset.solution_time_clustering.time_scaling = \
        ...     TimeScaling.Logarithmic
    :::
    ::::

    ::: versionadded
    [New in version 2021.2: ]{.versionmodified .added}Solution time
    clustering requires Tecplot 360 2021 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`SolutionTimeClustering`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.SolutionTimeClustering "tecplot.data.SolutionTimeClustering"){.reference
        .internal}

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[solution_times]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.solution_times "Link to this definition"){.headerlink}

:   Solution times in the dataset.

    This property is read-only. Solution times are grouped according to
    the current solution time clustering settings (see
    [[`Dataset.solution_time_clustering`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.solution_time_clustering "tecplot.data.Dataset.solution_time_clustering"){.reference
    .internal}). Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.solution_times)
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    :::
    ::::

    ::: versionadded
    [New in version 2017.3: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R3 or later.
    :::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`floats`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.title "Link to this definition"){.headerlink}

:   [[`str`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
    .external}: Title of this [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.title = 'My Data'
    :::
    ::::

    ::: versionchanged
    [Changed in version 2017.3: ]{.versionmodified .changed}of Tecplot
    360 The dataset title property requires Tecplot 360 2017 R3 or
    later.
    :::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.variable){.reference .internal}[¶](#tecplot.data.Dataset.variable "Link to this definition"){.headerlink}

:   Returns the [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`re.Pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external}) -- Zero-based index, case-insensitive
        [[`glob-style`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} or a compiled [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} used to match the variable by name. A negative index
        is interpreted as counting from the end of the available
        variable.

    Returns[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external} if no matching [[`Variable`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} name was found.

    Raises[:]{.colon}

    :   [**TecplotIndexError**](tecplot.exceptions.html#tecplot.exception.TecplotIndexError "tecplot.exception.TecplotIndexError"){.reference
        .internal} --

    ::: {.admonition .note}
    Note

    A [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} can contain [[`variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} with identical names and only the first match found is
    returned. This is not guaranteed to be deterministic and care should
    be taken to have only [[`variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} with unique names when this feature is used.
    :::

    The [[`Variable.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable.name "tecplot.data.Variable.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} though this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: ['Rectangular zone']
          Variables: ['x', 'y', 'z']
        >>> x = ds.variable('x')
        >>> x == ds.variable(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[variable_names]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.variable_names "Link to this definition"){.headerlink}

:   A [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of names for all variables in the dataset.

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.variable_names)
        ['x', 'y', 'z', 's']
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[variables]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.variables){.reference .internal}[¶](#tecplot.data.Dataset.variables "Link to this definition"){.headerlink}

:   Yields all [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} matching a *pattern*.

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
        .external} used to match variable names.

    Returns[:]{.colon}

    :   Generator of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}. All [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} if *pattern* is not specified.

    Example using case-insensitive glob-style matching:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for variable in dataset.variables('A*'):
        ...     array = variable.values('My Zone')
    :::
    ::::

    Example using (case-sensitive) regex:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import re
        >>> for variable in dataset.variables(re.compile(r'A.*')):
        ...     array = variable.values('My Zone')
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[zone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.zone){.reference .internal}[¶](#tecplot.data.Dataset.zone "Link to this definition"){.headerlink}

:   Returns [[Zone]{.std .std-ref}](#data-access){.reference .internal}
    by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`re.Pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external}) -- Zero-based index, case-insensitive
        [[`glob-style`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} or a compiled [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} used to match the zones by name. A negative index is
        interpreted as counting from the end of the available zones.

    Returns[:]{.colon}

    :   [[`OrderedZone`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.OrderedZone "tecplot.data.OrderedZone"){.reference
        .internal}, [[`ClassicFEZone`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.ClassicFEZone "tecplot.data.ClassicFEZone"){.reference
        .internal} or [[`PolyFEZone`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.PolyFEZone "tecplot.data.PolyFEZone"){.reference
        .internal} depending on the zone type, [[`None`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external} no matching [[zone]{.std
        .std-ref}](#data-access){.reference .internal} name was found.

    Raises[:]{.colon}

    :   [**TecplotIndexError**](tecplot.exceptions.html#tecplot.exception.TecplotIndexError "tecplot.exception.TecplotIndexError"){.reference
        .internal} --

    ::: {.admonition .note}
    Note

    A [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} can contain [[zones]{.std
    .std-ref}](#data-access){.reference .internal} with identical names
    and only the first match found is returned. This is not guaranteed
    to be deterministic and care should be taken to have only
    [[zones]{.std .std-ref}](#data-access){.reference .internal} with
    unique names when this feature is used.
    :::

    The [[`Zone.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.OrderedZone.name "tecplot.data.OrderedZone.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[Zone]{.std .std-ref}](#data-access){.reference .internal} though
    this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: ['Rectangular zone']
          Variables: ['x', 'y', 'z']
        >>> rectzone = ds.zone('Rectangular zone')
        >>> rectzone == ds.zone(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[zone_names]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Dataset.zone_names "Link to this definition"){.headerlink}

:   A [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of names for all zones in the dataset.

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone_names)
        ['Zone A', 'Zone B', 'Zone C']
    :::
    ::::

<!-- -->

[[Dataset.]{.pre}]{.sig-prename .descclassname}[[zones]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#Dataset.zones){.reference .internal}[¶](#tecplot.data.Dataset.zones "Link to this definition"){.headerlink}

:   Yields all [[Zones]{.std .std-ref}](#data-access){.reference
    .internal} matching a *pattern*.

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
        .external} used to match zone names.

    Returns[:]{.colon}

    :   Generator of [[`OrderedZones`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.OrderedZone "tecplot.data.OrderedZone"){.reference
        .internal}, [[`ClassicFEZones`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.ClassicFEZone "tecplot.data.ClassicFEZone"){.reference
        .internal} or [[`PolyFEZones`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.PolyFEZone "tecplot.data.PolyFEZone"){.reference
        .internal} depending on the zone types. All [[zones]{.std
        .std-ref}](#data-access){.reference .internal} if *pattern* is
        not specified.

    If **pattern** is a string, this will be interpreted as a
    case-insensitive [[`glob-style`{.xref .any .docutils .literal
    .notranslate}]{.pre}` `{.xref .any .docutils .literal
    .notranslate}[`pattern`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
    .external}. Example using glob which will match all zones starting
    with "A" or "a":

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for zone in dataset.zones('A*'):
        ...     x_array = zone.variable('X')
    :::
    ::::

    Alternatively, a regular-expression may be compiled using
    [[`re.compile`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
    .external} which will be used directly. This example shows a
    case-sensitive regex search:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import re
        >>> pattern = re.compile('[A-Z]*')
        >>> for zone in dataset.zones(pattern):
        ...     x_array = zone.variable('X')
    :::
    ::::

    Use list comprehension to construct a list of all zones with 'Wing'
    in the zone name. In contrast to the [[`Dataset.zones()`{.xref .any
    .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.zones "tecplot.data.Dataset.zones"){.reference
    .internal} method, this is case-sensitive:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> wing_zones = [Z for Z in dataset.zones() if 'Wing' in Z.name]
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::
:::

::: {#solutiontimeclustering .section}
### [SolutionTimeClustering](#id104){.toc-backref role="doc-backlink"}[¶](#solutiontimeclustering "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[SolutionTimeClustering]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[dataset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/dataset.html#SolutionTimeClustering){.reference .internal}[¶](#tecplot.data.SolutionTimeClustering "Link to this definition"){.headerlink}

:   Settings for controlling solution time clustering of solution times.

    By default, a dataset's zones solution times are organized into time
    steps with the assumption that they are distributed linearly, and
    are grouped together if they are within the following solution time
    tolerance:

    :::: {.highlight-python .notranslate}
    ::: highlight
        (tolerance_factor)*(max_time - min_time) + absolute_tolerance
    :::
    ::::

    Where by default the tolerance_factor is 1.0e-6 and the
    absolute_tolerance is 0.0.

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------
      [[`absolute_tolerance`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.SolutionTimeClustering.absolute_tolerance "tecplot.data.SolutionTimeClustering.absolute_tolerance"){.reference .internal}   Absolute tolerance used to cluster zones by their solution times.
      [[`time_scaling`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.SolutionTimeClustering.time_scaling "tecplot.data.SolutionTimeClustering.time_scaling"){.reference .internal}                     Scaling used to cluster zones by their solution times.
      [[`tolerance_factor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.SolutionTimeClustering.tolerance_factor "tecplot.data.SolutionTimeClustering.tolerance_factor"){.reference .internal}         Tolerance factor used to cluster zones by solution times.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------

<!-- -->

[[SolutionTimeClustering.]{.pre}]{.sig-prename .descclassname}[[absolute_tolerance]{.pre}]{.sig-name .descname}[¶](#tecplot.data.SolutionTimeClustering.absolute_tolerance "Link to this definition"){.headerlink}

:   Absolute tolerance used to cluster zones by their solution times.

    Absolute tolerance applied to each solution time when clustering
    with nearby times. (Default: 0.0)

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.solution_time_clustering.absolute_tolerance = 0.0025
    :::
    ::::

    ::: versionadded
    [New in version 2021.2: ]{.versionmodified .added}Solution time
    clustering requires Tecplot 360 2021 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SolutionTimeClustering.]{.pre}]{.sig-prename .descclassname}[[time_scaling]{.pre}]{.sig-name .descname}[¶](#tecplot.data.SolutionTimeClustering.time_scaling "Link to this definition"){.headerlink}

:   Scaling used to cluster zones by their solution times.

    Identifies if the dataset's zone solution times are distributed
    linearly or logarithmically. (Default: [[`TimeScaling.Linear`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TimeScaling.Linear "tecplot.constant.TimeScaling.Linear"){.reference
    .internal})

    Possible values: [[`TimeScaling.Linear`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TimeScaling.Linear "tecplot.constant.TimeScaling.Linear"){.reference
    .internal}, [[`TimeScaling.Logarithmic`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TimeScaling.Logarithmic "tecplot.constant.TimeScaling.Logarithmic"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TimeScaling
        >>> dataset.solution_time_clustering.time_scaling = \
        ...     TimeScaling.Logarithmic
    :::
    ::::

    ::: versionadded
    [New in version 2021.2: ]{.versionmodified .added}Solution time
    clustering requires Tecplot 360 2021 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`TimeScaling`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TimeScaling "tecplot.constant.TimeScaling"){.reference
        .internal}

<!-- -->

[[SolutionTimeClustering.]{.pre}]{.sig-prename .descclassname}[[tolerance_factor]{.pre}]{.sig-name .descname}[¶](#tecplot.data.SolutionTimeClustering.tolerance_factor "Link to this definition"){.headerlink}

:   Tolerance factor used to cluster zones by solution times.

    Tolerance factor, which is multiplied by the overall solution time
    delta and applied to each solution time when clustering nearby
    times. (Default: 1.0e-6)

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.solution_time_clustering.tolerance_factor = 1.0e-4
    :::
    ::::

    ::: versionadded
    [New in version 2021.2: ]{.versionmodified .added}Solution time
    clustering requires Tecplot 360 2021 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::

::: {#variable .section}
### [Variable](#id105){.toc-backref role="doc-backlink"}[¶](#variable "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[Variable]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[dataset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/variable.html#Variable){.reference .internal}[¶](#tecplot.data.Variable "Link to this definition"){.headerlink}

:   Key value for a data array within a [[`Dataset`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} can be identified (uniquely) by the index within their
    parent [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} or (non-uniquely) by name. In general, a [[Zone]{.std
    .std-ref}](#data-access){.reference .internal} must also be selected
    to access the underlying data array. This object is used by several
    style controlling classes such as contours and vectors. The
    following example sets the contour variable for the first contour
    group to the first variable named 'S':

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.contour(0).variable = dataset.variable('S')
    :::
    ::::

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.aux_data "tecplot.data.Variable.aux_data"){.reference .internal}      Auxiliary data for this variable.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.index "tecplot.data.Variable.index"){.reference .internal}               [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal}: Zero-based position within the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`lock_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.lock_mode "tecplot.data.Variable.lock_mode"){.reference .internal}   Type of lock or [[`None`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference .external} (read-only).
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.name "tecplot.data.Variable.name"){.reference .internal}                  Returns or sets the name.
      [[`num_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.num_zones "tecplot.data.Variable.num_zones"){.reference .internal}   [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[Zones]{.std .std-ref}](#data-access){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.max "tecplot.data.Variable.max"){.reference .internal}()                   Upper bound of the values stored in this variable across all zones.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.min "tecplot.data.Variable.min"){.reference .internal}()                   Lower bound of the values stored in this variable across all zones.
      [[`minmax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.minmax "tecplot.data.Variable.minmax"){.reference .internal}()          Limits of the values stored in this variable across all zones.
      [[`values`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable.values "tecplot.data.Variable.values"){.reference .internal}(pattern)   Returns [[`Array`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference .internal} by index or string pattern.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Variable.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this variable.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the variable. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> aux = frame.dataset.variable('X').aux_data
        >>> aux['X_weighted_avg'] = '3.14159'
        >>> print(aux['X_weighted_avg'])
        3.14159
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Variable.index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}: Zero-based position within the parent [[`Dataset`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.contour(0).variable_index = dataset.variable('S').index
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[lock_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Variable.lock_mode "Link to this definition"){.headerlink}

:   Type of lock or [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external} (read-only).

    Variables may be locked as a result of other operations, typically
    through the use of the CFD Analyzer. This read-only property returns
    [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external} if the variable is not locked,
    [[`VarLockMode.ValueChange`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VarLockMode.ValueChange "tecplot.constant.VarLockMode.ValueChange"){.reference
    .internal} if the variable may not be modified or
    [[`VarLockMode.Delete`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VarLockMode.Delete "tecplot.constant.VarLockMode.Delete"){.reference
    .internal} if the variable may not be deleted.

    This example modifies variable [`s`{.docutils .literal
    .notranslate}]{.pre} only if it is not locked:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> variable_s = dataset.variable('s')
        >>> if variable_s.lock_mode is None:
        ...     tp.data.operate.execute_equation('{s} = {p}**2')
    :::
    ::::

    ::: versionadded
    [New in version 2019.1: ]{.versionmodified .added}Variable lock mode
    property requires Tecplot 360 2019 R1 or later.
    :::

    Type[:]{.colon}

    :   [[`VarLockMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VarLockMode "tecplot.constant.VarLockMode"){.reference
        .internal}

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/variable.html#Variable.max){.reference .internal}[¶](#tecplot.data.Variable.max "Link to this definition"){.headerlink}

:   Upper bound of the values stored in this variable across all zones.

    Return type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

    This always returns a [[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external} regardless of the underlying data type:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.variable('x').max())
        10
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/variable.html#Variable.min){.reference .internal}[¶](#tecplot.data.Variable.min "Link to this definition"){.headerlink}

:   Lower bound of the values stored in this variable across all zones.

    Return type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

    This always returns a [[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external} regardless of the underlying data type:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.variable('x').min())
        0
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[minmax]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/variable.html#Variable.minmax){.reference .internal}[¶](#tecplot.data.Variable.minmax "Link to this definition"){.headerlink}

:   Limits of the values stored in this variable across all zones.

    Return type[:]{.colon}

    :   2-tuple of [[`floats`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

    This always returns [[`floats`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external} regardless of the underlying data type:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.variable('x').minmax())
        (0, 10)
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Variable.name "Link to this definition"){.headerlink}

:   Returns or sets the name.

    Return type[:]{.colon}

    :   [[`string`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.variable(0).name)
        X
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[num_zones]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Variable.num_zones "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} in the parent
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage, looping over all zones by index:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for zindex in range(dataset.num_zones):
        ...     zone = dataset.zone(zindex)
    :::
    ::::

<!-- -->

[[Variable.]{.pre}]{.sig-prename .descclassname}[[values]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/variable.html#Variable.values){.reference .internal}[¶](#tecplot.data.Variable.values "Link to this definition"){.headerlink}

:   Returns [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[Zone]{.std .std-ref}](#data-access){.reference
        .internal}) -- Zero-based index or [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} in which case, the first match is returned, or a
        [[Zone]{.std .std-ref}](#data-access){.reference .internal}
        object.

    ::: {.admonition .note}
    Note

    **Data operations can make use of Numpy when installed.**

    When doing large data transfers into and out of Tecplot using
    PyTecplot, it is recommended to install the Python array-processing
    module [Numpy](https://scipy.org){.reference .external}. PyTecplot
    will automatically use this to optimize data transfers which may
    result in significant performance gains.
    :::

    The [[`Zone.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.OrderedZone.name "tecplot.data.OrderedZone.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} though this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: 'Rectangular zone'
          Variables: 'x', 'y', 'z'
        >>> x = ds.variable('x')
        >>> rectzone = x.values('Rectangular zone')
        >>> rectzone == x.values(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::
:::

:::::::: {#zones .section}
### [Zones](#id106){.toc-backref role="doc-backlink"}[¶](#zones "Link to this heading"){.headerlink}

- [tecplot.data.zone](#module-tecplot.data.zone){#id119 .reference
  .internal}

- [OrderedZone](#orderedzone){#id120 .reference .internal}

- [ClassicFEZone](#classicfezone){#id121 .reference .internal}

- [MixedFEZone](#mixedfezone){#id122 .reference .internal}

- [PolyFEZone](#polyfezone){#id123 .reference .internal}

::: {#module-tecplot.data.zone .section}
[]{#tecplot-data-zone}

#### [tecplot.data.zone](#id119){.toc-backref role="doc-backlink"}[¶](#module-tecplot.data.zone "Link to this heading"){.headerlink}

Zones describe the size, shape, element (cell) geometry, connectivity
and solution time of arrays in a dataset. Zones created as "ordered,"
"classic finite-element," or "polytopal finite-element" along with the
number of nodes and elements which can not be changed (without creating
a new zone). Ordered zones are always considered to be
logically-rectangular grids of one, two or three dimensions depending on
the shape. Classic finite-element zones must use a fixed-type element
throughout. This means that each element has the same number of faces
and nodes. Polytopal zones can have a varying number of faces and nodes
for each element. The connectivity is implied in ordered zones and
explicitly provided by the user for finite-element zones.

In PyTecplot, there are three zone class objects: [[`OrderedZone`{.xref
.any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.OrderedZone "tecplot.data.zone.OrderedZone"){.reference
.internal}, [[`ClassicFEZone`{.xref .any .py .py-class .docutils
.literal
.notranslate}]{.pre}](#tecplot.data.ClassicFEZone "tecplot.data.zone.ClassicFEZone"){.reference
.internal} and [[`PolyFEZone`{.xref .any .py .py-class .docutils
.literal
.notranslate}]{.pre}](#tecplot.data.PolyFEZone "tecplot.data.zone.PolyFEZone"){.reference
.internal}. The [[`OrderedZone`{.xref .any .py .py-class .docutils
.literal
.notranslate}]{.pre}](#tecplot.data.OrderedZone "tecplot.data.zone.OrderedZone"){.reference
.internal} and [[`ClassicFEZone`{.xref .any .py .py-class .docutils
.literal
.notranslate}]{.pre}](#tecplot.data.ClassicFEZone "tecplot.data.zone.ClassicFEZone"){.reference
.internal} classes use the [[`FaceNeighbors`{.xref .any .py .py-class
.docutils .literal
.notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
.internal} class to handle "global" face-neighbor connections from one
zone to another. The connectivity for the [[`ClassicFEZone`{.xref .any
.py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.ClassicFEZone "tecplot.data.zone.ClassicFEZone"){.reference
.internal} objects are accessed through the [[`Nodemap`{.xref .any .py
.py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
.internal} class. The [[`PolyFEZone`{.xref .any .py .py-class .docutils
.literal
.notranslate}]{.pre}](#tecplot.data.PolyFEZone "tecplot.data.zone.PolyFEZone"){.reference
.internal} objects provide element definition and connectivity access
through the [[`Facemap`{.xref .any .py .py-class .docutils .literal
.notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
.internal} class.
:::

::: {#orderedzone .section}
#### [OrderedZone](#id120){.toc-backref role="doc-backlink"}[¶](#orderedzone "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[OrderedZone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[dataset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/zone.html#OrderedZone){.reference .internal}[¶](#tecplot.data.OrderedZone "Link to this definition"){.headerlink}

:   An ordered [`(i,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`j,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`k)`{.docutils .literal .notranslate}]{.pre} zone
    within a [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Ordered zones contain nodal or cell-centered arrays where the
    connectivity is implied by the dimensions and ordering of the data.

    [[Zones]{.std .std-ref}](#data-access){.reference .internal} can be
    identified (uniquely) by the index with their parent
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} or (non-uniquely) by name. In general, a
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} must be selected to access the underlying data array.
    This object is used by fieldmaps and linemaps to apply style to
    specific zones. Here we obtain the fieldmap associated with the zone
    named 'My Zone':

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap = plot.fieldmap(dataset.zone('My Zone'))
    :::
    ::::

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.aux_data "tecplot.data.OrderedZone.aux_data"){.reference .internal}                                             Auxiliary data for this zone.
      [[`dimensions`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.dimensions "tecplot.data.OrderedZone.dimensions"){.reference .internal}                                       Nodal dimensions along [`(i,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`j,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`k)`{.docutils .literal .notranslate}]{.pre}.
      [[`face_neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.face_neighbors "tecplot.data.OrderedZone.face_neighbors"){.reference .internal}                           The face neighbor list for this ordered zone.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.index "tecplot.data.OrderedZone.index"){.reference .internal}                                                      [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal}: Zero-based position within the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.name "tecplot.data.OrderedZone.name"){.reference .internal}                                                         The name of the zone.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.num_elements "tecplot.data.OrderedZone.num_elements"){.reference .internal}                                 Number of cells in this zone.
      [[`num_faces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.num_faces "tecplot.data.OrderedZone.num_faces"){.reference .internal}                                          Number of faces in this zone.
      [[`num_faces_per_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.num_faces_per_element "tecplot.data.OrderedZone.num_faces_per_element"){.reference .internal}      Number of faces per element in this ordered zone.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.num_points "tecplot.data.OrderedZone.num_points"){.reference .internal}                                       Total number of nodes within this zone.
      [[`num_points_per_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.num_points_per_element "tecplot.data.OrderedZone.num_points_per_element"){.reference .internal}   Points per cell for ordered zones.
      [[`num_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.num_variables "tecplot.data.OrderedZone.num_variables"){.reference .internal}                              [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`rank`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.rank "tecplot.data.OrderedZone.rank"){.reference .internal}                                                         Number of dimensions of the data array.
      [[`solution_time`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.solution_time "tecplot.data.OrderedZone.solution_time"){.reference .internal}                              The solution time for this zone.
      [[`strand`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.strand "tecplot.data.OrderedZone.strand"){.reference .internal}                                                   The strand ID number.
      [[`zone_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.zone_type "tecplot.data.OrderedZone.zone_type"){.reference .internal}                                          The [[`ZoneType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference .internal} indicating structure of the data contained.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`copy`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.copy "tecplot.data.OrderedZone.copy"){.reference .internal}(\[share_variables, i_range, j_range, \...\])   Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`mirror`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.mirror "tecplot.data.OrderedZone.mirror"){.reference .internal}(mirror_variables)                        Mirror this [[Zone]{.std .std-ref}](#data-access){.reference .internal}.
      [[`values`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.OrderedZone.values "tecplot.data.OrderedZone.values"){.reference .internal}(pattern)                                 Returns an [[`Array`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference .internal} by index or string pattern.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this zone.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the zone. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> aux = frame.dataset.zone('My Zone').aux_data
        >>> aux['X_weighted_avg'] = '3.14159'
        >>> print(aux['X_weighted_avg'])
        3.14159
    :::
    ::::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[copy]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[share_variables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[i_range]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[j_range]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[k_range]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/zone.html#OrderedZone.copy){.reference .internal}[¶](#tecplot.data.OrderedZone.copy "Link to this definition"){.headerlink}

:   Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    The name is also copied but can be changed after duplication.

    Parameters[:]{.colon}

    :   - **share_variables** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external} or [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`Variables`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
          .internal}) -- Share all variables between the original and
          generated zones if [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} or the list of Variables to be shared. Variable
          sharing allows you to lower the use of physical memory (RAM).
          When sharing a variable the memory used by the source zone is
          shared with the copied zone. Alterations to the variable in
          one zone will affect the other. See also
          [[`Dataset.branch_variables()`{.xref .any .py .py-meth
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
          .internal}. Default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}.

        - **i_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Range (min, max, step) along the
          [`i`{.docutils .literal .notranslate}]{.pre} dimension for
          ordered data. Min and max are zero-based indicies where max is
          inclusive. If step causes max to be skipped, max will be
          included. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default), the entire range will be copied.

        - **j_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Range (min, max, step) along the
          [`j`{.docutils .literal .notranslate}]{.pre} dimension for
          ordered data. Min and max are zero-based indicies where max is
          inclusive. If step causes max to be skipped, max will be
          included. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default), the entire range will be copied.

        - **k_range** ([[`tuple`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Range (min, max, step) along the
          [`k`{.docutils .literal .notranslate}]{.pre} dimension for
          ordered data. Min and max are zero-based indicies where max is
          inclusive. If step causes max to be skipped, max will be
          included. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} (default), the entire range will be copied.

    Returns[:]{.colon}

    :   [[Zone]{.std .std-ref}](#data-access){.reference .internal} --
        The newly created zone.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        ds = tp.active_page().add_frame().create_dataset('D', ['x','y','z'])
        z = ds.add_ordered_zone('Z1', (3,3,3))
        zcopy = z.copy(i_range=(1, -1, 2))
    :::
    ::::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[dimensions]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.dimensions "Link to this definition"){.headerlink}

:   Nodal dimensions along [`(i,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`j,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`k)`{.docutils .literal .notranslate}]{.pre}.

    Returns[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} -- [`(i,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`j,`{.docutils .literal
        .notranslate}]{.pre}` `{.docutils .literal
        .notranslate}[`k)`{.docutils .literal .notranslate}]{.pre} for
        ordered data.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.dimensions)
        (128, 128, 128)
    :::
    ::::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[face_neighbors]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.face_neighbors "Link to this definition"){.headerlink}

:   The face neighbor list for this ordered zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone(0)
        >>> print(zone.face_neighbors.mode)
        FaceNeighborMode.LocalOneToOne
    :::
    ::::

    Type[:]{.colon}

    :   [[`FaceNeighbors`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
        .internal}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}: Zero-based position within the parent [[`Dataset`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This is the value used to obtain a specific zone if you have
    duplicately named zones in the dataset:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.new_layout()
        >>> frame = tp.active_frame()
        >>> dataset = frame.create_dataset('Dataset', ['x', 'y'])
        >>> dataset.add_ordered_zone('Zone', (10,10,10))
        >>> dataset.add_ordered_zone('Zone', (3,3,3))
        >>> # getting zone by name always returns first match
        >>> print(dataset.zone('Zone').index)
        0
        >>> # use index to get specific zone
        >>> print(dataset.zone(1).dimensions)
        (3, 3, 3)
    :::
    ::::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[mirror]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mirror_variables]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.OrderedZone.mirror "Link to this definition"){.headerlink}

:   Mirror this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal}.

    The name of the resulting zone will be "Mirror of zone
    *sourcezone*", where *sourcezone* is the number of the zone from
    which the mirrored zone was created. The variables in the newly
    created zones are shared with their corresponding source zones,
    except for variables to be mirrored as specified.

    Parameters[:]{.colon}

    :   **mirror_variables** ([[`Variable`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Variables in the new zone to be multiplied by
        [\\(-1\\)]{.math .notranslate .nohighlight} after the zone is
        copied. the variables may be [[`Variable`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} objects, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} names or [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} indices.

    Returns[:]{.colon}

    :   A zone of the same type as the source.

    This example show how to mirror the first zone across the xy-plane
    in 3D:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> mirrored_zone = dataset.zone(0).mirror('Z')
    :::
    ::::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.name "Link to this definition"){.headerlink}

:   The name of the zone.

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone(0).name = 'Zone 0'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.num_elements "Link to this definition"){.headerlink}

:   Number of cells in this zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.dimensions)
        (128, 128, 128)
        >>> print(zone.num_elements)
        2048383
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[num_faces]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.num_faces "Link to this definition"){.headerlink}

:   Number of faces in this zone.

    This is the same as the number of elements times the number of faces
    per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_faces)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[num_faces_per_element]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.num_faces_per_element "Link to this definition"){.headerlink}

:   Number of faces per element in this ordered zone.

    This is determined by the rank of the zone:

    > <div>
    >
    >   Rank   Faces Per Element
    >   ------ -------------------
    >   0      0
    >   1      1
    >   2      4
    >   3      6
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.dimensions)
        (1, 10, 10)
        >>> print(zone.rank)
        2
        >>> print(zone.num_faces_per_element)
        4
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.num_points "Link to this definition"){.headerlink}

:   Total number of nodes within this zone.

    This is number of nodes within the zone and is equivalent to the
    product of the values in [[`OrderedZone.dimensions`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.OrderedZone.dimensions "tecplot.data.OrderedZone.dimensions"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.dimensions)
        (128, 128, 128)
        >>> print(zone.num_points)
        2097152
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[num_points_per_element]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.num_points_per_element "Link to this definition"){.headerlink}

:   Points per cell for ordered zones.

    For ordered zones, this is [\\(2\^{d}\\)]{.math .notranslate
    .nohighlight} where [\\(d\\)]{.math .notranslate .nohighlight} is
    the number of dimensions greater than one:

    > <div>
    >
    >   Rank   Faces Per Element
    >   ------ -------------------
    >   0      0
    >   1      2
    >   2      4
    >   3      8
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.dimensions)
        (10, 10, 1)
        >>> print(zone.rank)
        2
        >>> print(zone.num_points_per_element)
        4
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[num_variables]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.num_variables "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[`Variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage, iterating over all variables by index:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for i in range(dataset.num_variables):
        ...     variable = dataset.variable(i)
    :::
    ::::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[rank]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.rank "Link to this definition"){.headerlink}

:   Number of dimensions of the data array.

    This will return the number of dimensions which contain more than
    one value:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.dimensions)
        (10, 10, 1)
        >>> print(zone.rank)
        2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[solution_time]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.solution_time "Link to this definition"){.headerlink}

:   The solution time for this zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').solution_time = 3.14
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[strand]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.strand "Link to this definition"){.headerlink}

:   The strand ID number.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').strand = 2
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[values]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.OrderedZone.values "Link to this definition"){.headerlink}

:   Returns an [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`Variable`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Zero-based index, [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} in which case, the first match is returned, or a
        [[`Variable`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} object.

    ::: {.admonition .note}
    Note

    **Data operations can make use of Numpy when installed.**

    When doing large data transfers into and out of Tecplot using
    PyTecplot, it is recommended to install the Python array-processing
    module [Numpy](https://scipy.org){.reference .external}. PyTecplot
    will automatically use this to optimize data transfers which may
    result in significant performance gains.
    :::

    The [[`Variable.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable.name "tecplot.data.Variable.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} though this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: ['Rectangular zone']
          Variables: ['x', 'y', 'z']
        >>> zone = ds.zone('Rectangular zone')
        >>> x = zone.values('x')
        >>> x == zone.values(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[OrderedZone.]{.pre}]{.sig-prename .descclassname}[[zone_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.OrderedZone.zone_type "Link to this definition"){.headerlink}

:   The [[`ZoneType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
    .internal} indicating structure of the data contained.

    The specific type of zone this object represents:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).zone_type)
        ZoneType.Ordered
    :::
    ::::

    Type[:]{.colon}

    :   [[`ZoneType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
        .internal}
:::

::: {#classicfezone .section}
#### [ClassicFEZone](#id121){.toc-backref role="doc-backlink"}[¶](#classicfezone "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[ClassicFEZone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[dataset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/zone.html#ClassicFEZone){.reference .internal}[¶](#tecplot.data.ClassicFEZone "Link to this definition"){.headerlink}

:   A classic finite-element zone within a [[`Dataset`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Classic finite-element zones are arrays of nodes that are connected
    explicitly into pre-defined geometric shapes called "elements." The
    geometry is consistent across the whole zone so that the number of
    nodes per element is constant.

    [[Zones]{.std .std-ref}](#data-access){.reference .internal} can be
    identified (uniquely) by the index with their parent
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} or (non-uniquely) by name. In general, a
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} must be selected to access the underlying data array.
    This object is used by fieldmaps and linemaps to apply style to
    specific zones. Here we obtain the fieldmap associated with the zone
    named 'My Zone':

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap = plot.fieldmap(dataset.zone('My Zone'))
    :::
    ::::

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.aux_data "tecplot.data.ClassicFEZone.aux_data"){.reference .internal}                                             Auxiliary data for this zone.
      [[`face_neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.face_neighbors "tecplot.data.ClassicFEZone.face_neighbors"){.reference .internal}                           The face neighbor list for this finite-element zone.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.index "tecplot.data.ClassicFEZone.index"){.reference .internal}                                                      [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal}: Zero-based position within the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.name "tecplot.data.ClassicFEZone.name"){.reference .internal}                                                         The name of the zone.
      [[`nodemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.nodemap "tecplot.data.ClassicFEZone.nodemap"){.reference .internal}                                                The connectivity for this finite-element zone.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.num_elements "tecplot.data.ClassicFEZone.num_elements"){.reference .internal}                                 Number of cells in this finite-element zone.
      [[`num_faces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.num_faces "tecplot.data.ClassicFEZone.num_faces"){.reference .internal}                                          Number of faces in this zone.
      [[`num_faces_per_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.num_faces_per_element "tecplot.data.ClassicFEZone.num_faces_per_element"){.reference .internal}      Number of faces per element.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.num_points "tecplot.data.ClassicFEZone.num_points"){.reference .internal}                                       Total number of nodes within this zone.
      [[`num_points_per_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.num_points_per_element "tecplot.data.ClassicFEZone.num_points_per_element"){.reference .internal}   Points per element for classic finite-element zones.
      [[`num_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.num_variables "tecplot.data.ClassicFEZone.num_variables"){.reference .internal}                              [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`rank`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.rank "tecplot.data.ClassicFEZone.rank"){.reference .internal}                                                         Number of dimensions of the data array.
      [[`shared_connectivity`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.shared_connectivity "tecplot.data.ClassicFEZone.shared_connectivity"){.reference .internal}            [[Zones]{.std .std-ref}](#data-access){.reference .internal} sharing connectivity.
      [[`solution_time`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.solution_time "tecplot.data.ClassicFEZone.solution_time"){.reference .internal}                              The solution time for this zone.
      [[`strand`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.strand "tecplot.data.ClassicFEZone.strand"){.reference .internal}                                                   The strand ID number.
      [[`zone_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.zone_type "tecplot.data.ClassicFEZone.zone_type"){.reference .internal}                                          The [[`ZoneType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference .internal} indicating structure of the data contained.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`copy`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.copy "tecplot.data.ClassicFEZone.copy"){.reference .internal}(\[share_variables\])      Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`mirror`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.mirror "tecplot.data.ClassicFEZone.mirror"){.reference .internal}(mirror_variables)   Mirror this [[Zone]{.std .std-ref}](#data-access){.reference .internal}.
      [[`values`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicFEZone.values "tecplot.data.ClassicFEZone.values"){.reference .internal}(pattern)            Returns an [[`Array`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference .internal} by index or string pattern.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this zone.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the zone. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> aux = frame.dataset.zone('My Zone').aux_data
        >>> aux['X_weighted_avg'] = '3.14159'
        >>> print(aux['X_weighted_avg'])
        3.14159
    :::
    ::::

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[copy]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[share_variables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.data.ClassicFEZone.copy "Link to this definition"){.headerlink}

:   Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    The name is also copied but can be changed after duplication.

    Parameters[:]{.colon}

    :   **share_variables** ([[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Share all variables between the original and
        generated zones if [[`True`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} or the list of Variables to be shared. Variable
        sharing allows you to lower the use of physical memory (RAM).
        When sharing a variable the memory used by the source zone is
        shared with the copied zone. Alterations to the variable in one
        zone will affect the other. See also
        [[`Dataset.branch_variables()`{.xref .any .py .py-meth .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
        .internal}. Default: [[`False`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}.

    Returns[:]{.colon}

    :   [[Zone]{.std .std-ref}](#data-access){.reference .internal} --
        The newly created zone.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> new_zone = dataset.zone('My Zone').copy()
        >>> print(new_zone.name)
        My Zone
        >>> new_zone.name = 'My Zone Copy'
        >>> print(new_zone.name)
        My Zone Copy
    :::
    ::::

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[face_neighbors]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.face_neighbors "Link to this definition"){.headerlink}

:   The face neighbor list for this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone(0)
        >>> print(zone.face_neighbors.mode)
        FaceNeighborMode.LocalOneToMany
    :::
    ::::

    Type[:]{.colon}

    :   [[`FaceNeighbors`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
        .internal}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}: Zero-based position within the parent [[`Dataset`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This is the value used to obtain a specific zone if you have
    duplicately named zones in the dataset:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.new_layout()
        >>> frame = tp.active_frame()
        >>> dataset = frame.create_dataset('Dataset', ['x', 'y'])
        >>> dataset.add_ordered_zone('Zone', (10,10,10))
        >>> dataset.add_ordered_zone('Zone', (3,3,3))
        >>> # getting zone by name always returns first match
        >>> print(dataset.zone('Zone').index)
        0
        >>> # use index to get specific zone
        >>> print(dataset.zone(1).dimensions)
        (3, 3, 3)
    :::
    ::::

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[mirror]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mirror_variables]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.ClassicFEZone.mirror "Link to this definition"){.headerlink}

:   Mirror this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal}.

    The name of the resulting zone will be "Mirror of zone
    *sourcezone*", where *sourcezone* is the number of the zone from
    which the mirrored zone was created. The variables in the newly
    created zones are shared with their corresponding source zones,
    except for variables to be mirrored as specified.

    Parameters[:]{.colon}

    :   **mirror_variables** ([[`Variable`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Variables in the new zone to be multiplied by
        [\\(-1\\)]{.math .notranslate .nohighlight} after the zone is
        copied. the variables may be [[`Variable`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} objects, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} names or [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} indices.

    Returns[:]{.colon}

    :   A zone of the same type as the source.

    This example show how to mirror the first zone across the xy-plane
    in 3D:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> mirrored_zone = dataset.zone(0).mirror('Z')
    :::
    ::::

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.name "Link to this definition"){.headerlink}

:   The name of the zone.

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone(0).name = 'Zone 0'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[nodemap]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.nodemap "Link to this definition"){.headerlink}

:   The connectivity for this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone(0)
        >>> print(zone.nodemap.num_points_per_element)
        4
    :::
    ::::

    Type[:]{.colon}

    :   [[`ClassicNodemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.ClassicNodemap "tecplot.data.ClassicNodemap"){.reference
        .internal}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.num_elements "Link to this definition"){.headerlink}

:   Number of cells in this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_elements)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[num_faces]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.num_faces "Link to this definition"){.headerlink}

:   Number of faces in this zone.

    This is the same as the number of elements times the number of faces
    per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_faces)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[num_faces_per_element]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.num_faces_per_element "Link to this definition"){.headerlink}

:   Number of faces per element.

    This is dependent on the type of element this zone contains:

    > <div>
    >
    >   Zone Type                                               Faces Per Element
    >   ------------------------------------------------------- -------------------
    >   [`FELineSeg`{.docutils .literal .notranslate}]{.pre}    1
    >   [`FETriangle`{.docutils .literal .notranslate}]{.pre}   3
    >   [`FEQuad`{.docutils .literal .notranslate}]{.pre}       4
    >   [`FETetra`{.docutils .literal .notranslate}]{.pre}      4
    >   [`FEBrick`{.docutils .literal .notranslate}]{.pre}      6
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_faces_per_element)
        4
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.num_points "Link to this definition"){.headerlink}

:   Total number of nodes within this zone.

    This is the total number of nodes in the zone. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_points)
        2048
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[num_points_per_element]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.num_points_per_element "Link to this definition"){.headerlink}

:   Points per element for classic finite-element zones.

    The number of points (also known as nodes) per finite-element is
    determined from the [`zone_type`{.docutils .literal
    .notranslate}]{.pre} parameter. The following table shows the number
    of points per element for the available zone types along with the
    resulting shape of the nodemap based on the number of elements
    specified ([\\(N\\)]{.math .notranslate .nohighlight}):

    > <div>
    >
    >   Zone Type                                               Points/Element   Nodemap Shape
    >   ------------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------
    >   [`FELineSeg`{.docutils .literal .notranslate}]{.pre}    2                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(2\\)]{.math .notranslate .nohighlight})
    >   [`FETriangle`{.docutils .literal .notranslate}]{.pre}   3                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(3\\)]{.math .notranslate .nohighlight})
    >   [`FEQuad`{.docutils .literal .notranslate}]{.pre}       4                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(4\\)]{.math .notranslate .nohighlight})
    >   [`FETetra`{.docutils .literal .notranslate}]{.pre}      4                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(4\\)]{.math .notranslate .nohighlight})
    >   [`FEBrick`{.docutils .literal .notranslate}]{.pre}      8                ([\\(N\\)]{.math .notranslate .nohighlight}, [\\(8\\)]{.math .notranslate .nohighlight})
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.zone_type)
        ZoneType.FETriangle
        >>> print(zone.num_points_per_element)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[num_variables]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.num_variables "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[`Variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage, iterating over all variables by index:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for i in range(dataset.num_variables):
        ...     variable = dataset.variable(i)
    :::
    ::::

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[rank]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.rank "Link to this definition"){.headerlink}

:   Number of dimensions of the data array.

    This indicates the dimensionality of the data and is dependent on
    the type of element this zone contains.

    > <div>
    >
    >   Zone Type                                               Rank
    >   ------------------------------------------------------- ------
    >   [`FELineSeg`{.docutils .literal .notranslate}]{.pre}    1
    >   [`FETriangle`{.docutils .literal .notranslate}]{.pre}   2
    >   [`FEQuad`{.docutils .literal .notranslate}]{.pre}       2
    >   [`FETetra`{.docutils .literal .notranslate}]{.pre}      3
    >   [`FEBrick`{.docutils .literal .notranslate}]{.pre}      3
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.zone_type)
        ZoneType.FEBrick
        >>> print(zone.rank)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[shared_connectivity]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.shared_connectivity "Link to this definition"){.headerlink}

:   [[Zones]{.std .std-ref}](#data-access){.reference .internal} sharing
    connectivity.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').copy()
        >>> for zone in dataset.zone('My Zone').shared_connectivity:
        ...     print(zone.index)
        0
        1
    :::
    ::::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std .std-ref}](#data-access){.reference
        .internal}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[solution_time]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.solution_time "Link to this definition"){.headerlink}

:   The solution time for this zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').solution_time = 3.14
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[strand]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.strand "Link to this definition"){.headerlink}

:   The strand ID number.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').strand = 2
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[values]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.ClassicFEZone.values "Link to this definition"){.headerlink}

:   Returns an [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`Variable`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Zero-based index, [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} in which case, the first match is returned, or a
        [[`Variable`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} object.

    ::: {.admonition .note}
    Note

    **Data operations can make use of Numpy when installed.**

    When doing large data transfers into and out of Tecplot using
    PyTecplot, it is recommended to install the Python array-processing
    module [Numpy](https://scipy.org){.reference .external}. PyTecplot
    will automatically use this to optimize data transfers which may
    result in significant performance gains.
    :::

    The [[`Variable.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable.name "tecplot.data.Variable.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} though this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: ['Rectangular zone']
          Variables: ['x', 'y', 'z']
        >>> zone = ds.zone('Rectangular zone')
        >>> x = zone.values('x')
        >>> x == zone.values(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[ClassicFEZone.]{.pre}]{.sig-prename .descclassname}[[zone_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicFEZone.zone_type "Link to this definition"){.headerlink}

:   The [[`ZoneType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
    .internal} indicating structure of the data contained.

    The specific type of zone this object represents:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).zone_type)
        ZoneType.FEBrick
    :::
    ::::

    Type[:]{.colon}

    :   [[`ZoneType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
        .internal}
:::

::: {#mixedfezone .section}
#### [MixedFEZone](#id122){.toc-backref role="doc-backlink"}[¶](#mixedfezone "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[MixedFEZone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[dataset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/zone.html#MixedFEZone){.reference .internal}[¶](#tecplot.data.MixedFEZone "Link to this definition"){.headerlink}

:   A finite-element zone capable of storing high-order elements.

    The nodemap for mixed finite-element zones consists of sections of
    uniform cell types:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Dataset.add_fe_mixed_zone()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset.add_fe_mixed_zone "tecplot.data.Dataset.add_fe_mixed_zone"){.reference
    .internal}
    :::

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.aux_data "tecplot.data.MixedFEZone.aux_data"){.reference .internal}                                    Auxiliary data for this zone.
      [[`face_neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.face_neighbors "tecplot.data.MixedFEZone.face_neighbors"){.reference .internal}                  The face neighbor list for this finite-element zone.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.index "tecplot.data.MixedFEZone.index"){.reference .internal}                                             [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal}: Zero-based position within the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.name "tecplot.data.MixedFEZone.name"){.reference .internal}                                                The name of the zone.
      [[`nodemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.nodemap "tecplot.data.MixedFEZone.nodemap"){.reference .internal}                                       The connectivity [[`Nodemap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference .internal} for this finite-element zone.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.num_elements "tecplot.data.MixedFEZone.num_elements"){.reference .internal}                        Number of cells in this finite-element zone.
      [[`num_faces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.num_faces "tecplot.data.MixedFEZone.num_faces"){.reference .internal}                                 Number of faces in this zone.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.num_points "tecplot.data.MixedFEZone.num_points"){.reference .internal}                              Total number of nodes within this zone.
      [[`num_sections`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.num_sections "tecplot.data.MixedFEZone.num_sections"){.reference .internal}                        The number of sections of uniform cell type.
      [[`num_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.num_variables "tecplot.data.MixedFEZone.num_variables"){.reference .internal}                     [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`rank`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.rank "tecplot.data.MixedFEZone.rank"){.reference .internal}                                                Number of dimensions of the data array.
      [[`shared_connectivity`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.shared_connectivity "tecplot.data.MixedFEZone.shared_connectivity"){.reference .internal}   [[Zones]{.std .std-ref}](#data-access){.reference .internal} sharing connectivity.
      [[`solution_time`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.solution_time "tecplot.data.MixedFEZone.solution_time"){.reference .internal}                     The solution time for this zone.
      [[`strand`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.strand "tecplot.data.MixedFEZone.strand"){.reference .internal}                                          The strand ID number.
      [[`zone_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.zone_type "tecplot.data.MixedFEZone.zone_type"){.reference .internal}                                 The [[`ZoneType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference .internal} indicating structure of the data contained.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`copy`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.copy "tecplot.data.MixedFEZone.copy"){.reference .internal}(\[share_variables\])                              Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`mirror`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.mirror "tecplot.data.MixedFEZone.mirror"){.reference .internal}(mirror_variables)                           Mirror this [[Zone]{.std .std-ref}](#data-access){.reference .internal}.
      [[`section_metrics`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.section_metrics "tecplot.data.MixedFEZone.section_metrics"){.reference .internal}(section_index)   Returns the type and number of cells within a specific section.
      [[`values`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.MixedFEZone.values "tecplot.data.MixedFEZone.values"){.reference .internal}(pattern)                                    Returns an [[`Array`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference .internal} by index or string pattern.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this zone.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the zone. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> aux = frame.dataset.zone('My Zone').aux_data
        >>> aux['X_weighted_avg'] = '3.14159'
        >>> print(aux['X_weighted_avg'])
        3.14159
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[copy]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[share_variables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.data.MixedFEZone.copy "Link to this definition"){.headerlink}

:   Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    The name is also copied but can be changed after duplication.

    Parameters[:]{.colon}

    :   **share_variables** ([[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Share all variables between the original and
        generated zones if [[`True`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} or the list of Variables to be shared. Variable
        sharing allows you to lower the use of physical memory (RAM).
        When sharing a variable the memory used by the source zone is
        shared with the copied zone. Alterations to the variable in one
        zone will affect the other. See also
        [[`Dataset.branch_variables()`{.xref .any .py .py-meth .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
        .internal}. Default: [[`False`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}.

    Returns[:]{.colon}

    :   [[Zone]{.std .std-ref}](#data-access){.reference .internal} --
        The newly created zone.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> new_zone = dataset.zone('My Zone').copy()
        >>> print(new_zone.name)
        My Zone
        >>> new_zone.name = 'My Zone Copy'
        >>> print(new_zone.name)
        My Zone Copy
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[face_neighbors]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.face_neighbors "Link to this definition"){.headerlink}

:   The face neighbor list for this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone(0)
        >>> print(zone.face_neighbors.mode)
        FaceNeighborMode.LocalOneToMany
    :::
    ::::

    Type[:]{.colon}

    :   [[`FaceNeighbors`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
        .internal}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}: Zero-based position within the parent [[`Dataset`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This is the value used to obtain a specific zone if you have
    duplicately named zones in the dataset:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.new_layout()
        >>> frame = tp.active_frame()
        >>> dataset = frame.create_dataset('Dataset', ['x', 'y'])
        >>> dataset.add_ordered_zone('Zone', (10,10,10))
        >>> dataset.add_ordered_zone('Zone', (3,3,3))
        >>> # getting zone by name always returns first match
        >>> print(dataset.zone('Zone').index)
        0
        >>> # use index to get specific zone
        >>> print(dataset.zone(1).dimensions)
        (3, 3, 3)
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[mirror]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mirror_variables]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.MixedFEZone.mirror "Link to this definition"){.headerlink}

:   Mirror this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal}.

    The name of the resulting zone will be "Mirror of zone
    *sourcezone*", where *sourcezone* is the number of the zone from
    which the mirrored zone was created. The variables in the newly
    created zones are shared with their corresponding source zones,
    except for variables to be mirrored as specified.

    Parameters[:]{.colon}

    :   **mirror_variables** ([[`Variable`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Variables in the new zone to be multiplied by
        [\\(-1\\)]{.math .notranslate .nohighlight} after the zone is
        copied. the variables may be [[`Variable`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} objects, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} names or [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} indices.

    Returns[:]{.colon}

    :   A zone of the same type as the source.

    This example show how to mirror the first zone across the xy-plane
    in 3D:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> mirrored_zone = dataset.zone(0).mirror('Z')
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.name "Link to this definition"){.headerlink}

:   The name of the zone.

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone(0).name = 'Zone 0'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[nodemap]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.nodemap "Link to this definition"){.headerlink}

:   The connectivity [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} for this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone(0)
        >>> print(zone.nodemap.num_points_per_element)
        4
    :::
    ::::

    Type[:]{.colon}

    :   [[`Nodemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
        .internal}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.num_elements "Link to this definition"){.headerlink}

:   Number of cells in this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_elements)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[num_faces]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.num_faces "Link to this definition"){.headerlink}

:   Number of faces in this zone.

    This is the same as the number of elements times the number of faces
    per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_faces)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.num_points "Link to this definition"){.headerlink}

:   Total number of nodes within this zone.

    This is the total number of nodes in the zone. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_points)
        2048
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[num_sections]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.num_sections "Link to this definition"){.headerlink}

:   The number of sections of uniform cell type.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.num_sections)
        1
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[num_variables]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.num_variables "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[`Variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage, iterating over all variables by index:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for i in range(dataset.num_variables):
        ...     variable = dataset.variable(i)
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[rank]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.rank "Link to this definition"){.headerlink}

:   Number of dimensions of the data array.

    This indicates the dimensionality of the data and is dependent on
    the type of element this zone contains. All sections within an
    "FE-mixed zone" (a zone of type [[`ZoneType.FEMixed`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEMixed "tecplot.constant.ZoneType.FEMixed"){.reference
    .internal}), must consist of sections with the same dimension.

    ::: {.admonition .note}
    Note

    All sections within a zone are required to have the same
    dimensionality and therefore only the first section is queried when
    fetching the rank of the zone.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.zone_type)
        ZoneType.FEMixed
        >>> print(zone.section_metrics(0).cell_shape)
        FECellShape.Tetrahedron
        >>> print(zone.rank)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[section_metrics]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[section_index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/zone.html#MixedFEZone.section_metrics){.reference .internal}[¶](#tecplot.data.MixedFEZone.section_metrics "Link to this definition"){.headerlink}

:   Returns the type and number of cells within a specific section.

    Returns[:]{.colon}

    :   

        [[`collections.namedtuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference .external}

        :   

            cell_shape: [[`FECellShape`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellShape "tecplot.constant.FECellShape"){.reference .internal}

            :   The shape of all cells within this section.

            grid_order: [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}

            :   The grid-order for all cell in this section. A value of
                one indicates a "linear" cell with corners only and no
                high-order nodes.

            basis_func: [[`FECellBasisFunction`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellBasisFunction "tecplot.constant.FECellBasisFunction"){.reference .internal}

            :   This determines the number of high-order nodes for a
                given shape and grid order as well as the winding
                (ordering) of the nodes. Currently, only
                [[`FECellBasisFunction.Lagrangian`{.xref .any .py
                .py-attr .docutils .literal
                .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellBasisFunction.Lagrangian "tecplot.constant.FECellBasisFunction.Lagrangian"){.reference
                .internal} is supported.

            num_elements: [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}

            :   The total number of elements or cells within this
                section.

            num_corners_per_elem: [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}

            :   The number of linear nodes (those nodes at the corners)
                for all cells within this section.

            num_nodes_per_elem: [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}

            :   The total number of nodes for each cell within this
                section. This will be the same as
                **num_corners_per_elem** for grid-order one cells.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> metrics = zone.section_metrics(0)  # first section
        >>> print(metrics.cell_shape)
        FECellShape.Tetrahedron
        >>> print(metrics.grid_order)
        2
        >>> print(metrics.basis_func)
        FECellBasisFunction.Lagrangian
        >>> print(metrics.num_elements)
        1024
    :::
    ::::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[shared_connectivity]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.shared_connectivity "Link to this definition"){.headerlink}

:   [[Zones]{.std .std-ref}](#data-access){.reference .internal} sharing
    connectivity.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').copy()
        >>> for zone in dataset.zone('My Zone').shared_connectivity:
        ...     print(zone.index)
        0
        1
    :::
    ::::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std .std-ref}](#data-access){.reference
        .internal}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[solution_time]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.solution_time "Link to this definition"){.headerlink}

:   The solution time for this zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').solution_time = 3.14
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[strand]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.strand "Link to this definition"){.headerlink}

:   The strand ID number.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').strand = 2
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[values]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.MixedFEZone.values "Link to this definition"){.headerlink}

:   Returns an [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`Variable`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Zero-based index, [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} in which case, the first match is returned, or a
        [[`Variable`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} object.

    ::: {.admonition .note}
    Note

    **Data operations can make use of Numpy when installed.**

    When doing large data transfers into and out of Tecplot using
    PyTecplot, it is recommended to install the Python array-processing
    module [Numpy](https://scipy.org){.reference .external}. PyTecplot
    will automatically use this to optimize data transfers which may
    result in significant performance gains.
    :::

    The [[`Variable.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable.name "tecplot.data.Variable.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} though this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: ['Rectangular zone']
          Variables: ['x', 'y', 'z']
        >>> zone = ds.zone('Rectangular zone')
        >>> x = zone.values('x')
        >>> x == zone.values(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[MixedFEZone.]{.pre}]{.sig-prename .descclassname}[[zone_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.MixedFEZone.zone_type "Link to this definition"){.headerlink}

:   The [[`ZoneType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
    .internal} indicating structure of the data contained.

    This will always return [[`ZoneType.FEMixed`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType.FEMixed "tecplot.constant.ZoneType.FEMixed"){.reference
    .internal} for [[`MixedFEZone`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.MixedFEZone "tecplot.data.MixedFEZone"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).zone_type)
        ZoneType.FEMixed
    :::
    ::::

    Type[:]{.colon}

    :   [[`ZoneType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
        .internal}
:::

::: {#polyfezone .section}
#### [PolyFEZone](#id123){.toc-backref role="doc-backlink"}[¶](#polyfezone "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[PolyFEZone]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[dataset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/zone.html#PolyFEZone){.reference .internal}[¶](#tecplot.data.PolyFEZone "Link to this definition"){.headerlink}

:   A polygonal finite-element zone within a [[`Dataset`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    A polygonal zone consists of arrays of nodes which are connected
    explicitly into arbitrary and varying geometric elements. These
    elements are 2D or 3D in nature and have a number of faces
    (connections between nodes) which hold the concept of a left and
    right neighbor.

    [[Zones]{.std .std-ref}](#data-access){.reference .internal} can be
    identified (uniquely) by the index with their parent
    [[`Dataset`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal} or (non-uniquely) by name. In general, a
    [[`Variable`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} must be selected to access the underlying data array.
    This object is used by fieldmaps and linemaps to apply style to
    specific zones. Here we obtain the fieldmap associated with the zone
    named 'My Zone':

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap = plot.fieldmap(dataset.zone('My Zone'))
    :::
    ::::

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.aux_data "tecplot.data.PolyFEZone.aux_data"){.reference .internal}                                    Auxiliary data for this zone.
      [[`facemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.facemap "tecplot.data.PolyFEZone.facemap"){.reference .internal}                                       The connectivity [[`Facemap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference .internal} for this polygonal finite-element zone.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.index "tecplot.data.PolyFEZone.index"){.reference .internal}                                             [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal}: Zero-based position within the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.name "tecplot.data.PolyFEZone.name"){.reference .internal}                                                The name of the zone.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.num_elements "tecplot.data.PolyFEZone.num_elements"){.reference .internal}                        Number of cells in this finite-element zone.
      [[`num_faces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.num_faces "tecplot.data.PolyFEZone.num_faces"){.reference .internal}                                 Number of faces in this finite-element zone.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.num_points "tecplot.data.PolyFEZone.num_points"){.reference .internal}                              Total number of nodes within this zone.
      [[`num_variables`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.num_variables "tecplot.data.PolyFEZone.num_variables"){.reference .internal}                     [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Number of [[`Variables`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`rank`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.rank "tecplot.data.PolyFEZone.rank"){.reference .internal}                                                Number of dimensions of the data array.
      [[`shared_connectivity`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.shared_connectivity "tecplot.data.PolyFEZone.shared_connectivity"){.reference .internal}   [[Zones]{.std .std-ref}](#data-access){.reference .internal} sharing connectivity.
      [[`solution_time`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.solution_time "tecplot.data.PolyFEZone.solution_time"){.reference .internal}                     The solution time for this zone.
      [[`strand`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.strand "tecplot.data.PolyFEZone.strand"){.reference .internal}                                          The strand ID number.
      [[`zone_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.zone_type "tecplot.data.PolyFEZone.zone_type"){.reference .internal}                                 The [[`ZoneType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference .internal} indicating structure of the data contained.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`copy`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.copy "tecplot.data.PolyFEZone.copy"){.reference .internal}(\[share_variables\])      Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference .internal} in the parent [[`Dataset`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference .internal}.
      [[`mirror`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.mirror "tecplot.data.PolyFEZone.mirror"){.reference .internal}(mirror_variables)   Mirror this [[Zone]{.std .std-ref}](#data-access){.reference .internal}.
      [[`values`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.PolyFEZone.values "tecplot.data.PolyFEZone.values"){.reference .internal}(pattern)            Returns an [[`Array`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference .internal} by index or string pattern.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this zone.

    Returns[:]{.colon}

    :   [[`AuxData`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
        .internal}

    This is the auxiliary data attached to the zone. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> aux = frame.dataset.zone('My Zone').aux_data
        >>> aux['X_weighted_avg'] = '3.14159'
        >>> print(aux['X_weighted_avg'])
        3.14159
    :::
    ::::

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[copy]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[share_variables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.data.PolyFEZone.copy "Link to this definition"){.headerlink}

:   Duplicate this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    The name is also copied but can be changed after duplication.

    Parameters[:]{.colon}

    :   **share_variables** ([[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Share all variables between the original and
        generated zones if [[`True`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} or the list of Variables to be shared. Variable
        sharing allows you to lower the use of physical memory (RAM).
        When sharing a variable the memory used by the source zone is
        shared with the copied zone. Alterations to the variable in one
        zone will affect the other. See also
        [[`Dataset.branch_variables()`{.xref .any .py .py-meth .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Dataset.branch_variables "tecplot.data.Dataset.branch_variables"){.reference
        .internal}. Default: [[`False`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}.

    Returns[:]{.colon}

    :   [[Zone]{.std .std-ref}](#data-access){.reference .internal} --
        The newly created zone.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> new_zone = dataset.zone('My Zone').copy()
        >>> print(new_zone.name)
        My Zone
        >>> new_zone.name = 'My Zone Copy'
        >>> print(new_zone.name)
        My Zone Copy
    :::
    ::::

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[facemap]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.facemap "Link to this definition"){.headerlink}

:   The connectivity [[`Facemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal} for this polygonal finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone(0)
        >>> print(zone.facemap.num_faces)
        4500
    :::
    ::::

    Type[:]{.colon}

    :   [[`Facemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
        .internal}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}: Zero-based position within the parent [[`Dataset`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This is the value used to obtain a specific zone if you have
    duplicately named zones in the dataset:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.new_layout()
        >>> frame = tp.active_frame()
        >>> dataset = frame.create_dataset('Dataset', ['x', 'y'])
        >>> dataset.add_ordered_zone('Zone', (10,10,10))
        >>> dataset.add_ordered_zone('Zone', (3,3,3))
        >>> # getting zone by name always returns first match
        >>> print(dataset.zone('Zone').index)
        0
        >>> # use index to get specific zone
        >>> print(dataset.zone(1).dimensions)
        (3, 3, 3)
    :::
    ::::

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[mirror]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[mirror_variables]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.PolyFEZone.mirror "Link to this definition"){.headerlink}

:   Mirror this [[Zone]{.std .std-ref}](#data-access){.reference
    .internal}.

    The name of the resulting zone will be "Mirror of zone
    *sourcezone*", where *sourcezone* is the number of the zone from
    which the mirrored zone was created. The variables in the newly
    created zones are shared with their corresponding source zones,
    except for variables to be mirrored as specified.

    Parameters[:]{.colon}

    :   **mirror_variables** ([[`Variable`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} or [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`Variables`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Variables in the new zone to be multiplied by
        [\\(-1\\)]{.math .notranslate .nohighlight} after the zone is
        copied. the variables may be [[`Variable`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} objects, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} names or [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} indices.

    Returns[:]{.colon}

    :   A zone of the same type as the source.

    This example show how to mirror the first zone across the xy-plane
    in 3D:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> mirrored_zone = dataset.zone(0).mirror('Z')
    :::
    ::::

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.name "Link to this definition"){.headerlink}

:   The name of the zone.

    ::: {.admonition .warning}
    Warning

    **Newlines in string identifiers may affect performance.**

    When iterating over many items by name, such as must be done when
    fetching an item via pattern matching, PyTecplot will optimize the
    search only if there are no newline characters in the searched
    items. Iterating over strings that contain newlines will be slower
    and therefore, it is best to avoid using newlines in string
    identifiers or names of objects such as [[Zones]{.std
    .std-ref}](#data-access){.reference .internal} or
    [[`Variables`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal}.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone(0).name = 'Zone 0'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.num_elements "Link to this definition"){.headerlink}

:   Number of cells in this finite-element zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_elements)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[num_faces]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.num_faces "Link to this definition"){.headerlink}

:   Number of faces in this finite-element zone.

    The number of faces may be [`0`{.docutils .literal
    .notranslate}]{.pre} if unknown or facemap creation is deferred.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_faces)
        1048576
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.num_points "Link to this definition"){.headerlink}

:   Total number of nodes within this zone.

    This is the total number of nodes in the zone. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('My Zone').num_points)
        2048
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[num_variables]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.num_variables "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Number of [[`Variables`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
    .internal} in the parent [[`Dataset`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    Example usage, iterating over all variables by index:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for i in range(dataset.num_variables):
        ...     variable = dataset.variable(i)
    :::
    ::::

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[rank]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.rank "Link to this definition"){.headerlink}

:   Number of dimensions of the data array.

    This indicates the dimensionality of the data and is dependent on
    the type of element this zone contains:

    > <div>
    >
    >   Zone Type                                                 Rank
    >   --------------------------------------------------------- ------
    >   [`FEPolygon`{.docutils .literal .notranslate}]{.pre}      2
    >   [`FEPolyhedron`{.docutils .literal .notranslate}]{.pre}   3
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.zone_type)
        ZoneType.FEPolygon
        >>> print(zone.rank)
        2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[shared_connectivity]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.shared_connectivity "Link to this definition"){.headerlink}

:   [[Zones]{.std .std-ref}](#data-access){.reference .internal} sharing
    connectivity.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').copy()
        >>> for zone in dataset.zone('My Zone').shared_connectivity:
        ...     print(zone.index)
        0
        1
    :::
    ::::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std .std-ref}](#data-access){.reference
        .internal}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[solution_time]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.solution_time "Link to this definition"){.headerlink}

:   The solution time for this zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').solution_time = 3.14
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[strand]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.strand "Link to this definition"){.headerlink}

:   The strand ID number.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').strand = 2
    :::
    ::::

    ::: {.admonition .note}
    Note

    **Possible side-effect when connected to Tecplot 360.**

    Changing the solution times in the dataset or modifying the active
    fieldmaps in a frame may trigger a change in the active plot's
    solution time by the Tecplot 360 interface. This is done to keep the
    GUI controls consistent. In batch mode, no such side-effect will
    take place and the user must take care to set the plot's solution
    time with the [[`plot.solution_time`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[values]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.PolyFEZone.values "Link to this definition"){.headerlink}

:   Returns an [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} by index or string pattern.

    Parameters[:]{.colon}

    :   **pattern** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`Variable`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal}) -- Zero-based index, [[`glob-style`{.xref .any
        .docutils .literal .notranslate}]{.pre}` `{.xref .any .docutils
        .literal .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "(in Python v3.13)"){.reference
        .external} in which case, the first match is returned, or a
        [[`Variable`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Variable "tecplot.data.Variable"){.reference
        .internal} object.

    ::: {.admonition .note}
    Note

    **Data operations can make use of Numpy when installed.**

    When doing large data transfers into and out of Tecplot using
    PyTecplot, it is recommended to install the Python array-processing
    module [Numpy](https://scipy.org){.reference .external}. PyTecplot
    will automatically use this to optimize data transfers which may
    result in significant performance gains.
    :::

    The [[`Variable.name`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Variable.name "tecplot.data.Variable.name"){.reference
    .internal} attribute is used to match the *pattern* to the desired
    [[`Array`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} though this is not necessarily unique:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.dataset
        >>> print(ds)
        Dataset:
          Zones: ['Rectangular zone']
          Variables: ['x', 'y', 'z']
        >>> zone = ds.zone('Rectangular zone')
        >>> x = zone.values('x')
        >>> x == zone.values(0)
        True
    :::
    ::::

    ::: {.admonition .warning}
    Warning

    **Zone and variable ordering may change between releases**

    Due to possible changes in data loaders or data formats over time,
    the ordering of zones and variables may be different between
    versions of Tecplot 360. Therefore it is recommended to always
    reference zones and variables **by name** instead of by index.
    :::

<!-- -->

[[PolyFEZone.]{.pre}]{.sig-prename .descclassname}[[zone_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.PolyFEZone.zone_type "Link to this definition"){.headerlink}

:   The [[`ZoneType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
    .internal} indicating structure of the data contained.

    The specific type of zone this object represents:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).zone_type)
        ZoneType.FEPolygon
    :::
    ::::

    Type[:]{.colon}

    :   [[`ZoneType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ZoneType "tecplot.constant.ZoneType"){.reference
        .internal}
:::
::::::::

::: {#array .section}
### [Array](#id112){.toc-backref role="doc-backlink"}[¶](#array "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[Array]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*, *[[variable]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/array.html#Array){.reference .internal}[¶](#tecplot.data.Array "Link to this definition"){.headerlink}

:   Low-level accessor for underlying data within a [[`Dataset`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
    .internal}.

    This object exposes a list-like interface to the underlying data
    array. Using it, values can be directly queried and modified. After
    any modification to the data, the Tecplot Engine will have to be
    notified of the change. This notification will happen automatically
    in most cases, but can be turned off using the [[`suspend`{.xref
    .any .py .py-func .docutils .literal .notranslate}]{.pre}` `{.xref
    .any .py .py-func .docutils .literal .notranslate}[`context`{.xref
    .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.suspend "tecplot.session.suspend"){.reference
    .internal} for a significant performance increase on large data
    sets.

    Accessing values within an [[`Array`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array "tecplot.data.Array"){.reference
    .internal} is done through the standard [`[]`{.docutils .literal
    .notranslate}]{.pre} syntax:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(array[3])
        3.1415
    :::
    ::::

    The numbers passed are interpreted just like Python's built-in
    [[`slice`{.xref .py .py-class .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#slice "(in Python v3.13)"){.reference
    .external} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # print the values at indices: 5, 7, 9
        >>> print(array[5:10:2])
        [1.0, 1.0, 1.0]
    :::
    ::::

    Elements within an array can be manipulated in-place with the
    assignment operator:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> array[3] = 5.0
        >>> print(array[3])
        5.0
    :::
    ::::

    Element-by-element access is *not* guaranteed to be performant and
    users should avoid writing loops over indices in Python. Instead,
    whole arrays should be used. This will effectively push the loop
    down to the underlying native library and will be much faster in
    virtually all cases.

    Consider this array of 10k elements:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ds = frame.create_dataset('Dataset', ['x'])
        >>> zn = ds.add_ordered_zone('Zone', 10000)
        >>> array = zn.values('x')
    :::
    ::::

    The following loop, which takes the sine of all values in the array
    will require several Python function calls per element which is a
    tremendous overhead:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import math
        >>> for i in range(len(ar)):
        ...     ar[i] = math.sin(ar[i])
    :::
    ::::

    An immediate improvement on this can be made by looping over the
    elements in Python only when reading the values, but assigning them
    using the whole array. This will be several times faster for even
    modest arrays:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ar[:] = [math.sin(x) for x in ar]
    :::
    ::::

    But there is still a large performance penalty for looping over
    elements directly in Python and PyTecplot supports two solutions for
    large arrays: [[`tecplot.data.operate.execute_equation`{.xref .any
    .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal} and [[`Array.as_numpy_array()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array.as_numpy_array "tecplot.data.Array.as_numpy_array"){.reference
    .internal}. Please refer to these for details. Continuing with the
    example above, we could accomplish the same thing with either of the
    following using [[`execute_equation()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal} (assuming the array is identified by the first zone,
    first variable):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.data.operate import execute_equation
        >>> execute_equation('V1 = SIN(V1)', zones=[dataset.zone(0)])
    :::
    ::::

    or by using the [[`numpy`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://numpy.org/doc/stable/reference/index.html#module-numpy "(in NumPy v2.3)"){.reference
    .external} library:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import numpy as np
        >>> ar[:] = np.sin(ar[:])
    :::
    ::::

    In both of these cases, the calculation of the sine and loop over
    elements is pushed to the low level library and is much faster. Note
    that only the [[`execute_equation()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.operate.execute_equation "tecplot.data.operate.execute_equation"){.reference
    .internal} solution does the calculation within Tecplot and does not
    require the data to copied out to Python so it will typically be the
    fastest option.

    ::: {.admonition .note}
    Note

    When modifying data using this class, it may be necessary to update
    the range of any associated contouring with a call to
    [[`ContourLevels.reset()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourLevels.reset "tecplot.plot.ContourLevels.reset"){.reference
    .internal} or similar. This will ensure that the total range of the
    new values is presented in the plot.
    :::

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`c_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.c_type "tecplot.data.Array.c_type"){.reference .internal}                     [[`ctypes`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.13)"){.reference .external} compatible data type of this array.
      [[`data_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.data_type "tecplot.data.Array.data_type"){.reference .internal}            Indicating the underlying value type of this array.
      [[`location`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.location "tecplot.data.Array.location"){.reference .internal}               Data points location with respect to the elements.
      [[`passive`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.passive "tecplot.data.Array.passive"){.reference .internal}                  An unallocated zone-variable combination.
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.shape "tecplot.data.Array.shape"){.reference .internal}                        [`(i,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`j,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`k)`{.docutils .literal .notranslate}]{.pre} shape for this array.
      [[`shared_zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.shared_zones "tecplot.data.Array.shared_zones"){.reference .internal}   All zones sharing this array.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`as_numpy_array`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.as_numpy_array "tecplot.data.Array.as_numpy_array"){.reference .internal}(\[offset, size, copy\])   Present the underlying data array as a [[`numpy.ndarray`{.xref .any .docutils .literal .notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)"){.reference .external}.
      [[`copy`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.copy "tecplot.data.Array.copy"){.reference .internal}(\[offset, size\])                                       Copy the whole or part of the array into a ctypes array.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.max "tecplot.data.Array.max"){.reference .internal}()                                                          Upper bound of the values stored in this array.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.min "tecplot.data.Array.min"){.reference .internal}()                                                          Lower bound of the values stored in this array.
      [[`minmax`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Array.minmax "tecplot.data.Array.minmax"){.reference .internal}()                                                 Limits of the values stored in this array.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[as_numpy_array]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[offset]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[size]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[copy]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/array.html#Array.as_numpy_array){.reference .internal}[¶](#tecplot.data.Array.as_numpy_array "Link to this definition"){.headerlink}

:   Present the underlying data array as a [[`numpy.ndarray`{.xref .any
    .docutils .literal
    .notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)"){.reference
    .external}.

    If the **copy** parameter is [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, this method will attempt to return an array pointing to
    the actual data stored in the Tecplot Engine. This will fail in
    connected mode or if the loader does not support immediate loading
    of the entire array into memory. Care should be taken to ensure the
    validity of the pointers to the data.

    Parameters[:]{.colon}

    :   - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based offset into the array.
          This will be the starting point of the resulting data.
          (default: 0)

        - **size** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Number of elements in the resulting
          array. The default (a value of [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}) is to go to the end of the data.

        - **copy** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Copy the data out from the Tecplot
          Engine. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external}, an attempt is made to point to the underlying raw
          data and an exception is thrown on error. (default:
          [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`numpy.ndarray`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.3)"){.reference
        .external}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> x = dataset.zone('Zone').values('X').as_numpy_array()
    :::
    ::::

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[c_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Array.c_type "Link to this definition"){.headerlink}

:   [[`ctypes`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.13)"){.reference
    .external} compatible data type of this array.

    This is the [[`ctypes`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.13)"){.reference
    .external} equivalent of [[`Array.data_type`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Array.data_type "tecplot.data.Array.data_type"){.reference
    .internal} and will return one of the following:

    > <div>
    >
    > - [[`ctypes.c_float`{.xref .any .docutils .literal
    >   .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_float "(in Python v3.13)"){.reference
    >   .external}
    >
    > - [[`ctypes.c_double`{.xref .any .docutils .literal
    >   .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "(in Python v3.13)"){.reference
    >   .external}
    >
    > - [[`ctypes.c_int`{.xref .any .docutils .literal
    >   .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "(in Python v3.13)"){.reference
    >   .external}
    >
    > - [[`ctypes.c_int16`{.xref .any .docutils .literal
    >   .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int16 "(in Python v3.13)"){.reference
    >   .external}
    >
    > - [[`ctypes.c_int8`{.xref .any .docutils .literal
    >   .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int8 "(in Python v3.13)"){.reference
    >   .external}
    >
    > </div>

    and can be used to create a [[`ctypes`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.13)"){.reference
    .external} array to store a copy of the data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        frame = tp.active_frame()
        dataset = frame.create_dataset('Dataset', ['x'])
        dataset.add_ordered_zone('Zone', (3,3,3))
        x = dataset.zone('Zone').values('x')
        # allocate array using Python's ctypes
        x_array = (x.c_type * len(x))()
        # copy values from Dataset into ctypes array
        x_array[:] = x[:]
    :::
    ::::

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[copy]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[offset]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[size]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/array.html#Array.copy){.reference .internal}[¶](#tecplot.data.Array.copy "Link to this definition"){.headerlink}

:   Copy the whole or part of the array into a ctypes array.

    Parameters[:]{.colon}

    :   - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based offset for starting index
          to copy. (default: 0)

        - **size** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Number of values to copy into the
          resulting array. A value of [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} will copy to the end of the array. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

    Here we will copy out chunks of the data, do some operation and set
    the values back into the dataset:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        tp.new_layout()
        frame = tp.active_frame()
        dataset = frame.create_dataset('Dataset', ['x'])
        dataset.add_ordered_zone('Zone', (2, 2, 2))
        x = dataset.zone('Zone').values('x')

        # loop over array copying out 4 values at a time
        for i, offset in enumerate(range(0, len(x), 4)):
            x_array = x.copy(offset, 4)
            x_array[:] = [i] * 4
            x[offset:offset + 4] = x_array

        # will print: [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0]
        print(x[:])
    :::
    ::::

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[data_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Array.data_type "Link to this definition"){.headerlink}

:   Indicating the underlying value type of this array.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('Zone').values('X').data_type)
        FieldDataType.Float
    :::
    ::::

    Type[:]{.colon}

    :   [[`FieldDataType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FieldDataType "tecplot.constant.FieldDataType"){.reference
        .internal}

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[location]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Array.location "Link to this definition"){.headerlink}

:   Data points location with respect to the elements.

    Possible values are [[`ValueLocation.CellCentered`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.CellCentered "tecplot.constant.ValueLocation.CellCentered"){.reference
    .internal} and [[`ValueLocation.Nodal`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation.Nodal "tecplot.constant.ValueLocation.Nodal"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).values('X').location)
        ValueLocation.Nodal
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueLocation`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueLocation "tecplot.constant.ValueLocation"){.reference
        .internal}

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/array.html#Array.max){.reference .internal}[¶](#tecplot.data.Array.max "Link to this definition"){.headerlink}

:   Upper bound of the values stored in this array.

    Return type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

    This always returns a [[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external} regardless of the underlying data type:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('Zone').values('x').max())
        10
    :::
    ::::

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/array.html#Array.min){.reference .internal}[¶](#tecplot.data.Array.min "Link to this definition"){.headerlink}

:   Lower bound of the values stored in this array.

    Return type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

    This always returns a [[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external} regardless of the underlying data type:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('Zone').values('x').min())
        0
    :::
    ::::

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[minmax]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/array.html#Array.minmax){.reference .internal}[¶](#tecplot.data.Array.minmax "Link to this definition"){.headerlink}

:   Limits of the values stored in this array.

    Return type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`floats`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

    This always returns [[`floats`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external} regardless of the underlying data type:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone('Zone').values('x').minmax())
        (0, 10)
    :::
    ::::

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[passive]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Array.passive "Link to this definition"){.headerlink}

:   An unallocated zone-variable combination.

    Passive variables are placeholders where no data is defined for a
    zone variable combination. Passive variables will always return zero
    when queried:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        ds = tp.active_page().add_frame().create_dataset('D', ['x','y'])
        z = ds.add_ordered_zone('Z1', (3,))
        assert not z.values(0).passive
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[shape]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Array.shape "Link to this definition"){.headerlink}

:   [`(i,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`j,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`k)`{.docutils .literal .notranslate}]{.pre} shape for
    this array.

    This is defined by the parent zone and can be used to reshape
    arrays. The following example assumes 32-bit floating point array
    and copies the Tecplot-owned [`data`{.docutils .literal
    .notranslate}]{.pre} into the [[`numpy`{.xref .any .docutils
    .literal
    .notranslate}]{.pre}](https://numpy.org/doc/stable/reference/index.html#module-numpy "(in NumPy v2.3)"){.reference
    .external}-owned [`array`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> import numpy as np
        >>> data = dataset.zone('Zone').values('X')
        >>> array = np.empty(data.shape, dtype=np.float32)
        >>> arr_ptr = array.ctypes.data_as(POINTER(data.c_type))
        >>> memmove(arr_ptr, data.copy(), sizeof(data.c_type) * len(data))
    :::
    ::::

    The data array presented is normally one-dimensional. For ordered
    data, you may wish to reshape the array indexing according to the
    dimensionality given by the [`shape`{.docutils .literal
    .notranslate}]{.pre} attribute:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp

        frame = tp.active_frame()
        dataset = frame.create_dataset('Dataset', ['X'])
        zone = dataset.add_ordered_zone('Zone', shape=(3,3,3))

        '''
        the following will print:
        [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.
          0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
        '''
        x = np.array(zone.values('X')[:])
        print(x)

        '''
        the following will print:
        [[[ 0.  0.  0.]
          [ 0.  0.  0.]
          [ 0.  0.  0.]]

         [[ 0.  0.  0.]
          [ 0.  0.  0.]
          [ 0.  0.  0.]]

         [[ 0.  0.  0.]
          [ 0.  0.  0.]
          [ 0.  0.  0.]]]
        '''
        x.shape = zone.values('X').shape
        print(x)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`floats`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Array.]{.pre}]{.sig-prename .descclassname}[[shared_zones]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Array.shared_zones "Link to this definition"){.headerlink}

:   All zones sharing this array.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> dataset.zone('My Zone').copy(share_variables=True)
        >>> for z in dataset.zone('My Zone').values(0).shared_zones:
        ...     print(z.index)
        0
        1
    :::
    ::::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std .std-ref}](#data-access){.reference
        .internal}
:::

::: {#fecelltype .section}
### [FECellType](#id113){.toc-backref role="doc-backlink"}[¶](#fecelltype "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[FECellType]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[cell_shape]{.pre}]{.n}*, *[[grid_order]{.pre}]{.n}*, *[[basis_func]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/fe_cell_type.html#FECellType){.reference .internal}[¶](#tecplot.data.FECellType "Link to this definition"){.headerlink}

:   **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------
      [[`basis_func`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FECellType.basis_func "tecplot.data.FECellType.basis_func"){.reference .internal}                                 The basis function used for this cell.
      [[`grid_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FECellType.grid_order "tecplot.data.FECellType.grid_order"){.reference .internal}                                 Grid order of the nodes in the cell (order 1 is the linear case).
      [[`num_corners`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FECellType.num_corners "tecplot.data.FECellType.num_corners"){.reference .internal}                              Number of nodes at the corners of the cell.
      [[`num_high_order_nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FECellType.num_high_order_nodes "tecplot.data.FECellType.num_high_order_nodes"){.reference .internal}   Number of high-order nodes for the cell (not the corners).
      [[`num_nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FECellType.num_nodes "tecplot.data.FECellType.num_nodes"){.reference .internal}                                    Total number of nodes for the cell including corners and high-order nodes.
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FECellType.shape "tecplot.data.FECellType.shape"){.reference .internal}                                                Geometric shape of the cell.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------

<!-- -->

[[FECellType.]{.pre}]{.sig-prename .descclassname}[[basis_func]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FECellType.basis_func "Link to this definition"){.headerlink}

:   The basis function used for this cell.

    Type[:]{.colon}

    :   [[`FECellBasisFunction`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellBasisFunction "tecplot.constant.FECellBasisFunction"){.reference
        .internal}

<!-- -->

[[FECellType.]{.pre}]{.sig-prename .descclassname}[[grid_order]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FECellType.grid_order "Link to this definition"){.headerlink}

:   Grid order of the nodes in the cell (order 1 is the linear case).

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FECellType.]{.pre}]{.sig-prename .descclassname}[[num_corners]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FECellType.num_corners "Link to this definition"){.headerlink}

:   Number of nodes at the corners of the cell.

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FECellType.]{.pre}]{.sig-prename .descclassname}[[num_high_order_nodes]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FECellType.num_high_order_nodes "Link to this definition"){.headerlink}

:   Number of high-order nodes for the cell (not the corners).

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FECellType.]{.pre}]{.sig-prename .descclassname}[[num_nodes]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FECellType.num_nodes "Link to this definition"){.headerlink}

:   Total number of nodes for the cell including corners and high-order
    nodes.

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FECellType.]{.pre}]{.sig-prename .descclassname}[[shape]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FECellType.shape "Link to this definition"){.headerlink}

:   Geometric shape of the cell.

    Type[:]{.colon}

    :   [[`FECellShape`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellShape "tecplot.constant.FECellShape"){.reference
        .internal}
:::

::: {#nodemap .section}
### [Nodemap](#id114){.toc-backref role="doc-backlink"}[¶](#nodemap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[Nodemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#Nodemap){.reference .internal}[¶](#tecplot.data.Nodemap "Link to this definition"){.headerlink}

:   Element to node map for a mixed-FE zone.

    This object maps elements (cells) to specific nodes (points) in the
    dataset. The elements are grouped by cell type into sections and
    each section stores the corners (linear part of the cell) separate
    from the high-order nodes of the cells into two different arrays.

    For more details, see the "working with datasets" examples shipped
    with PyTecplot in the Tecplot 360 distribution.

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------
      [[`c_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.c_type "tecplot.data.Nodemap.c_type"){.reference .internal}   The underlying data type for this nodemap.
      --------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------

    **Methods**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`assignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.assignment "tecplot.data.Nodemap.assignment"){.reference .internal}()                         Context manager for assigning to the nodemap.
      [[`element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.element "tecplot.data.Nodemap.element"){.reference .internal}(node, offset)                      The element containing a given node.
      [[`nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.nodes "tecplot.data.Nodemap.nodes"){.reference .internal}(element\[, section\])                    Returns node values for a specific element.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.num_elements "tecplot.data.Nodemap.num_elements"){.reference .internal}(node)               The number of elements that use a given node.
      [[`section`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.section "tecplot.data.Nodemap.section"){.reference .internal}(index)                             Returns a [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal} of the nodemap.
      [[`section_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Nodemap.section_element "tecplot.data.Nodemap.section_element"){.reference .internal}(element)   Returns the section and element within that section for a globally-indexed element.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[assignment]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.data.Nodemap.assignment "Link to this definition"){.headerlink}

:   Context manager for assigning to the nodemap.

    When setting values to the nodemap, a [[State Changes]{.std
    .std-ref}](tecplot.session.html#state-change){.reference .internal}
    is emitted to the engine after every statement. This can degrade
    performance if in the script the nodemap is being set many times.
    This context provides a way to suspend the state change notification
    until all assignments have been completed. In the following example,
    the state change is emitted only after the
    [`nodemap.assignment()`{.docutils .literal .notranslate}]{.pre}
    context exits:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> with nodemap.assignment():
        ...     nodemap[:] = node_data
    :::
    ::::

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[c_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Nodemap.c_type "Link to this definition"){.headerlink}

:   The underlying data type for this nodemap.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    This is the [[`ctypes`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.13)"){.reference
    .external} integer type used by the Tecplot Engine to store the
    nodemap data. This is used internally and is not normally needed for
    simple nodemap access.

    Type[:]{.colon}

    :   [[`ctypes.c_int32`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "(in Python v3.13)"){.reference
        .external} or [[`ctypes.c_int64`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[element]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[node]{.pre}]{.n}*, *[[offset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#Nodemap.element){.reference .internal}[¶](#tecplot.data.Nodemap.element "Link to this definition"){.headerlink}

:   The element containing a given node.

    Parameters[:]{.colon}

    :   - **node** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based index of a node.

        - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based index of the element that uses the
          given node.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} - Zero-based index of the element.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> print(nodemap.element(3, 7))
        324
    :::
    ::::

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[nodes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*, *[[section]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#Nodemap.nodes){.reference .internal}[¶](#tecplot.data.Nodemap.nodes "Link to this definition"){.headerlink}

:   Returns node values for a specific element.

    Parameters[:]{.colon}

    :   - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Element index with in the section if specified,
          otherwise this is the element index across all sections.

        - **section** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Section index. If no section is
          speficied, the element index will span across all sections.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.nodemap.nodes(1))
        (0, 1, 3, 4)
    :::
    ::::

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[node]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#Nodemap.num_elements){.reference .internal}[¶](#tecplot.data.Nodemap.num_elements "Link to this definition"){.headerlink}

:   The number of elements that use a given node.

    Parameters[:]{.colon}

    :   **node** -- ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}): Zero-based index of a node.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} - The number of elements that use this node.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> nodemap.num_elements(3)
        8
    :::
    ::::

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[section]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#Nodemap.section){.reference .internal}[¶](#tecplot.data.Nodemap.section "Link to this definition"){.headerlink}

:   Returns a [[`NodemapSection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal} of the nodemap.

    Each section of a [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} consists of a mapping for a specific cell type. The data
    may be linear or higher-order.

    Parameters[:]{.colon}

    :   **index** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The zero-based section index.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> nmap_section = zone.nodemap.section(0)
        >>> print(nmap_section.cell_shape)
        FECellShape.Tetrahedron
    :::
    ::::

<!-- -->

[[Nodemap.]{.pre}]{.sig-prename .descclassname}[[section_element]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#Nodemap.section_element){.reference .internal}[¶](#tecplot.data.Nodemap.section_element "Link to this definition"){.headerlink}

:   Returns the section and element within that section for a
    globally-indexed element.

    Parameters[:]{.colon}

    :   **element** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The zero-based element index spanning all
        sections in the nodemap.

    Returns: [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external} of [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external} (zero-based) indices: [`(section,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`element)`{.docutils .literal .notranslate}]{.pre}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.nodemap.section_element(1))
        (0, 1)
    :::
    ::::
:::

::: {#nodemapsection .section}
### [NodemapSection](#id115){.toc-backref role="doc-backlink"}[¶](#nodemapsection "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[NodemapSection]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[nodemap]{.pre}]{.n}*, *[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#NodemapSection){.reference .internal}[¶](#tecplot.data.NodemapSection "Link to this definition"){.headerlink}

:   A section of uniform cell-type in a [[`Nodemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal}.

    A [[`MixedFEZone`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.MixedFEZone "tecplot.data.MixedFEZone"){.reference
    .internal} contains a [[`Nodemap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap "tecplot.data.Nodemap"){.reference
    .internal} that is made of one or more sections of uniform cell type
    ([[`NodemapSection`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}). Within these sections, the nodemap data is stored in an
    array consisting of the node indices.

    For more details, see the "working with datasets" examples shipped
    with PyTecplot in the Tecplot 360 distribution.

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`array`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.array "tecplot.data.NodemapSection.array"){.reference .internal}                                                      Flattened array accessor for node data.
      [[`basis_func`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.basis_func "tecplot.data.NodemapSection.basis_func"){.reference .internal}                                       The basis function used to determine the node winding for elements in this [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal}.
      [[`cell_shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.cell_shape "tecplot.data.NodemapSection.cell_shape"){.reference .internal}                                       The geometric shape of elements in this [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal}.
      [[`cell_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.cell_type "tecplot.data.NodemapSection.cell_type"){.reference .internal}                                          The cell type of this [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal}.
      [[`grid_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.grid_order "tecplot.data.NodemapSection.grid_order"){.reference .internal}                                       The grid order of the cell type in this [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal}.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.num_elements "tecplot.data.NodemapSection.num_elements"){.reference .internal}                                 The total number of elements in this [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal}.
      [[`num_points_per_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.num_points_per_element "tecplot.data.NodemapSection.num_points_per_element"){.reference .internal}   Points per element for this [[`NodemapSection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference .internal}.
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.shape "tecplot.data.NodemapSection.shape"){.reference .internal}                                                      Shape of the nodemap array.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.size "tecplot.data.NodemapSection.size"){.reference .internal}                                                         Total number of nodes stored in the nodemap array.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------
      [[`nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.NodemapSection.nodes "tecplot.data.NodemapSection.nodes"){.reference .internal}(element)   Returns node values for a specific element in this section.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[array]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.array "Link to this definition"){.headerlink}

:   Flattened array accessor for node data.

    A section of the nodemap is normally dimensioned by [\\((N_e,
    N\_{npe})\\)]{.math .notranslate .nohighlight} where
    [\\(N_e\\)]{.math .notranslate .nohighlight} is the number of
    elements and [\\(N\_{npe}\\)]{.math .notranslate .nohighlight} is
    the number of nodes per element. This property represents a
    flattened view into the array containing the nodes of each element.

    Standard Python list slicing works for both fetching values and
    assignments. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nmap_section = dataset.zone('My Zone').nodemap.section(0)
        >>> nmap_section.array[:] = mydata
        >>> print(nmap_section.array[:10])
        [1, 10, 8, 0, 5, 18, 6, 12, 18, 11]
    :::
    ::::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}-like array

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[basis_func]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.basis_func "Link to this definition"){.headerlink}

:   The basis function used to determine the node winding for elements
    in this [[`NodemapSection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    Currently, Tecplot only supports the Lagrangian basis function.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> nmap_section = zone.nodemap.section(0)
        >>> print(nmap_section.basis_func)
        FECellBasisFunction.Lagrangian
    :::
    ::::

    Type[:]{.colon}

    :   [[`FECellBasisFunction`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellBasisFunction "tecplot.constant.FECellBasisFunction"){.reference
        .internal}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[cell_shape]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.cell_shape "Link to this definition"){.headerlink}

:   The geometric shape of elements in this [[`NodemapSection`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> nmap_section = zone.nodemap.section(0)
        >>> print(nmap_section.cell_shape)
        FECellShape.Tetrahedron
    :::
    ::::

    Type[:]{.colon}

    :   [[`FECellShape`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FECellShape "tecplot.constant.FECellShape"){.reference
        .internal}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[cell_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.cell_type "Link to this definition"){.headerlink}

:   The cell type of this [[`NodemapSection`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    The cell type encapsulates the shape, grid order and basis function
    for the elemens in the section of the zone.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> cell_type = zone.nodemap.section(0).cell_type
        >>> print(cell_type.shape)
        FECellShape.Tetrahedron
        >>> print(cell_type.grid_order)
        2
    :::
    ::::

    Type[:]{.colon}

    :   [[`FECellType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.FECellType "tecplot.data.FECellType"){.reference
        .internal}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[grid_order]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.grid_order "Link to this definition"){.headerlink}

:   The grid order of the cell type in this [[`NodemapSection`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    A grid order of 1 is the classic case with linear cells where the
    nodes are exclusively on the corners of the elements. Note that the
    **high_order_array** and high-order node data is only available for
    grid orders 2 or greater.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> nmap_section = zone.nodemap.section(0)
        >>> print(nmap_section.grid_order)
        2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[nodes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#NodemapSection.nodes){.reference .internal}[¶](#tecplot.data.NodemapSection.nodes "Link to this definition"){.headerlink}

:   Returns node values for a specific element in this section.

    Parameters[:]{.colon}

    :   **element** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The element index.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.nodemap.section(0).nodes(1))
        (0, 1, 3, 4)
    :::
    ::::

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.num_elements "Link to this definition"){.headerlink}

:   The total number of elements in this [[`NodemapSection`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> nmap_section = zone.nodemap.section(0)
        >>> print(nmap_section.num_elements)
        1024
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[num_points_per_element]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.num_points_per_element "Link to this definition"){.headerlink}

:   Points per element for this [[`NodemapSection`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.NodemapSection "tecplot.data.NodemapSection"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    The number of points (also known as nodes) per finite-element is
    determined from the cell shape, grid order and the basis function
    used.

    This example shows the output for a high-order Tet-10 section:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> nmap_section = zone.nodemap.section(0)
        >>> print(nmap_section.cell_shape)
        FECellShape.Tetrahedron
        >>> print(nmap_section.grid_order)
        2
        >>> print(nmap_section.num_points_per_element)
        10
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[shape]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.shape "Link to this definition"){.headerlink}

:   Shape of the nodemap array.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    This is defined by the zone type and is equal to [\\((N_e,
    N\_{npe})\\)]{.math .notranslate .nohighlight} where
    [\\(N_e\\)]{.math .notranslate .nohighlight} is the number of
    elements and [\\(N\_{npe}\\)]{.math .notranslate .nohighlight} is
    the number of nodes per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).nodemap.section(0).shape)
        (1024, 4)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[NodemapSection.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.data.NodemapSection.size "Link to this definition"){.headerlink}

:   Total number of nodes stored in the nodemap array.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    This is defined by the cell type and is equal to [\\(N_e \\times
    N\_{npe}\\)]{.math .notranslate .nohighlight} where
    [\\(N_e\\)]{.math .notranslate .nohighlight} is the number of
    elements and [\\(N\_{npe}\\)]{.math .notranslate .nohighlight} is
    the number of nodes per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).nodemap.section(0).shape)
        (1024, 4)
        >>> print(dataset.zone(0).nodemap.section(0).size)
        4096
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}
:::

::: {#classicnodemap .section}
### [ClassicNodemap](#id116){.toc-backref role="doc-backlink"}[¶](#classicnodemap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[ClassicNodemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#ClassicNodemap){.reference .internal}[¶](#tecplot.data.ClassicNodemap "Link to this definition"){.headerlink}

:   Connectivity list definition and control for classic FE zones.

    A nodemap holds the connectivity between nodes and elements for
    classic finite-element zones. It is nominally a two-dimensionaly
    array of shape [\\((N_e, N\_{npe})\\)]{.math .notranslate
    .nohighlight} where [\\(N_e\\)]{.math .notranslate .nohighlight} is
    the number of elements and [\\(N\_{npe}\\)]{.math .notranslate
    .nohighlight} is the number of nodes per element. The nodemap
    interface has flat-array access through the
    [[`ClassicNodemap.array`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.array "tecplot.data.ClassicNodemap.array"){.reference
    .internal} property as well as reverse look-up with
    [[`Nodemap.num_elements()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap.num_elements "tecplot.data.Nodemap.num_elements"){.reference
    .internal} and [[`Nodemap.element()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Nodemap.element "tecplot.data.Nodemap.element"){.reference
    .internal}.

    The nodemap behaves mostly like a two-dimensional array and can be
    treated as such:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> print('nodes in the first element:', nodemap[0])
        nodes in the first element: [0, 1, 2, 3]
        >>> print(nodemap[:3])
        [[0, 1, 2, 3], [2, 3, 4, 5], [4, 5, 6, 7]]
        >>> nodemap[0] = [6, 7, 8, 9]
        >>> print(nodemap[0])
        [6, 7, 8, 9]
    :::
    ::::

    Just for clarity, the nodemap indexing is by element first, then
    offset within that element:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> element = 6
        >>> offset = 2
        >>> node = nodemap[element][offset]
        >>> print(node)
        21
    :::
    ::::

    Setting node indices must be done for an entire element because
    getting values out of the nodemap and into Python always creates a
    copy. For example, **this will not work**:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> # Trying to set the 3rd node of the element 10
        >>> nodemap[10][2] = 5  # Error: nodemap[10] returns a copy
    :::
    ::::

    To modify a single node in a nodemap, it is neccessary to do a round
    trip like so:

    :::: {.highlight-python .notranslate}
    ::: highlight
        nodemap = dataset.zone('My Zone').nodemap
        >>> nodes = nodemap[10]
        >>> nodes[2] = 5
        >>> nodemap[10] = nodes  # OK: setting whole element at a time
        >>> print(nodemap[10])
        [20, 21, 5, 22]
    :::
    ::::

    The following script creates a quad of two triangles from scratch
    using the PyTecplot low-level data creation interface. The general
    steps are:

    1.  Setup the data

    2.  Create the tecplot dataset and variables

    3.  Create the zone

    4.  Set the node locations and connectivity lists

    5.  Set the (scalar) data

    6.  Write out data file

    7.  Adjust plot style and export image

    The data created looks like this:

    :::: {.highlight-none .notranslate}
    ::: highlight
        Node positions (x,y,z):

                       (1,1,1)
                      3
                     / \
                    /   \
         (0,1,.5)  2-----1  (1,0,.5)
                    \   /
                     \ /
                      0
                       (0,0,0)
    :::
    ::::

    Breaking up the two triangular elements, the faces look like this.
    Notice the first element (index: 0) is on the bottom:

    :::: {.highlight-none .notranslate}
    ::: highlight
        Element 1 Faces:
                           *
           (nodes 3-2)  1 / \ 0  (nodes 1-3)
                         /   \
                        *-----*
                           2
                            (nodes 2-1)

        Element 0 Faces:
                            (nodes 1-2)
                           1
                        *-----*
                         \   /
           (nodes 2-0)  2 \ / 0  (nodes 0-1)
                           *
    :::
    ::::

    The nodes are created as a list of [\\((x, y, z)\\)]{.math
    .notranslate .nohighlight} positions:

    :::: {.highlight-python .notranslate}
    ::: highlight
        [(x0, y0, z0), (x1, y1, z1)...]
    :::
    ::::

    which are transposed to lists of [\\(x\\)]{.math .notranslate
    .nohighlight}, [\\(y\\)]{.math .notranslate .nohighlight} and
    [\\(z\\)]{.math .notranslate .nohighlight}-positions:

    :::: {.highlight-python .notranslate}
    ::: highlight
        [(x0, x1, x2...), (y0, y1, y2...)...]
    :::
    ::::

    and passed to the [\\((x, y, z)\\)]{.math .notranslate .nohighlight}
    arrays. The nodemap, or connectivity list, is given as an array of
    dimensions [\\((N, D)\\)]{.math .notranslate .nohighlight} where
    [\\(N\\)]{.math .notranslate .nohighlight} is the number of elements
    and [\\(D\\)]{.math .notranslate .nohighlight} is the number of
    nodes per element. The order of the node locations determines the
    indices used when specifying the connectivity list. The Nodemap can
    be set individually and separately or all at once as shown here:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        # Triangle 0
        nodes0 = (
            (0, 0, 0  ),
            (1, 0, 0.5),
            (0, 1, 0.5))
        scalar_data0 = (0, 1, 2)
        conn0 = ((0, 1, 2),)
        neighbors0 = ((None, 0, None),)
        neighbor_zones0 = ((None, 1, None),)

        # Triangle 1
        nodes1 = (
            (1, 0, 0.5),
            (0, 1, 0.5),
            (1, 1, 1  ))
        scalar_data1 = (1, 2, 3)
        conn1 = ((0, 1, 2),)
        neighbors1 = ((0, None, None),)
        neighbor_zones1 = ((0, None, None),)

        # Create the dataset and zones
        ds = tp.active_frame().create_dataset('Data', ['x','y','z','s'])
        z0 = ds.add_fe_zone(ZoneType.FETriangle,
                            name='FE Triangle Float (3,1) Nodal 0',
                            num_points=len(nodes0), num_elements=len(conn0),
                            face_neighbor_mode=FaceNeighborMode.GlobalOneToOne)
        z1 = ds.add_fe_zone(ZoneType.FETriangle,
                            name='FE Triangle Float (3,1) Nodal 1',
                            num_points=len(nodes1), num_elements=len(conn1),
                            face_neighbor_mode=FaceNeighborMode.GlobalOneToOne)

        # Fill in and connect first triangle
        z0.values('x')[:] = [n[0] for n in nodes0]
        z0.values('y')[:] = [n[1] for n in nodes0]
        z0.values('z')[:] = [n[2] for n in nodes0]
        z0.nodemap[:] = conn0
        z0.values('s')[:] = scalar_data0

        # Fill in and connect second triangle
        z1.values('x')[:] = [n[0] for n in nodes1]
        z1.values('y')[:] = [n[1] for n in nodes1]
        z1.values('z')[:] = [n[2] for n in nodes1]
        z1.nodemap[:] = conn1
        z1.values('s')[:] = scalar_data1

        # Set face neighbors
        z0.face_neighbors.set_neighbors(neighbors0, neighbor_zones0, obscures=True)
        z1.face_neighbors.set_neighbors(neighbors1, neighbor_zones1, obscures=True)


        ### Setup a view of the data
        plot = tp.active_frame().plot(PlotType.Cartesian3D)
        plot.activate()

        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'
        plot.contour(0).colormap_filter.distribution = ColorMapDistribution.Continuous

        for ax in plot.axes:
            ax.show = True

        plot.show_mesh = False
        plot.show_contour = True
        plot.show_edge = True
        plot.use_translucency = True

        # View parameters obtained interactively from Tecplot 360
        plot.view.distance = 10
        plot.view.width = 2
        plot.view.psi = 80
        plot.view.theta = 30
        plot.view.alpha = 0
        plot.view.position = (-4.2, -8.0, 2.3)

        fmaps = plot.fieldmaps()
        fmaps.surfaces.surfaces_to_plot = SurfacesToPlot.All
        fmaps.effects.surface_translucency = 40

        # Turning on mesh, we can see all the individual triangles
        plot.show_mesh = True
        fmaps.mesh.line_pattern = LinePattern.Dashed

        plot.contour(0).levels.reset_to_nice()
        tp.export.save_png('fe_triangles1.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fe_triangles1.png"
    class="reference internal image-reference"><img
    src="../_images/fe_triangles1.png" style="width: 300px;"
    alt="../_images/fe_triangles1.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------
      [[`array`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.array "tecplot.data.ClassicNodemap.array"){.reference .internal}                                                      Flattened array accessor for this nodemap.
      [[`c_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.c_type "tecplot.data.ClassicNodemap.c_type"){.reference .internal}                                                   The underlying data type for this nodemap.
      [[`num_points_per_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.num_points_per_element "tecplot.data.ClassicNodemap.num_points_per_element"){.reference .internal}   Points per element for classic finite-element zones.
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.shape "tecplot.data.ClassicNodemap.shape"){.reference .internal}                                                      Shape of the nodemap array.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.size "tecplot.data.ClassicNodemap.size"){.reference .internal}                                                         Total number of nodes stored in the nodemap array.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------
      [[`assignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.assignment "tecplot.data.ClassicNodemap.assignment"){.reference .internal}()             Context manager for assigning to the nodemap.
      [[`element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.element "tecplot.data.ClassicNodemap.element"){.reference .internal}(node, offset)          The element containing a given node.
      [[`nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.nodes "tecplot.data.ClassicNodemap.nodes"){.reference .internal}(element)                     Returns node values for a specific element.
      [[`num_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.ClassicNodemap.num_elements "tecplot.data.ClassicNodemap.num_elements"){.reference .internal}(node)   The number of elements that use a given node.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[array]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicNodemap.array "Link to this definition"){.headerlink}

:   Flattened array accessor for this nodemap.

    The nodemap is normally dimensioned by [\\((N_e, N\_{npe})\\)]{.math
    .notranslate .nohighlight} where [\\(N_e\\)]{.math .notranslate
    .nohighlight} is the number of elements and [\\(N\_{npe}\\)]{.math
    .notranslate .nohighlight} is the number of nodes per element. This
    property represents a flattened view into the array which is of
    length [\\(N_e \\times N\_{npe}\\)]{.math .notranslate
    .nohighlight}. This may be more convenient than flattening the array
    in your script using a looping construct.

    Standard Python list slicing works for both fetching values and
    assignments. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nmap = dataset.zone('My Zone').nodemap
        >>> nmap.array[:] = mydata
        >>> print(nmap.array[:10])
        [1, 10, 8, 0, 5, 18, 6, 12, 18, 11]
    :::
    ::::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}-like array

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[assignment]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.data.ClassicNodemap.assignment "Link to this definition"){.headerlink}

:   Context manager for assigning to the nodemap.

    When setting values to the nodemap, a [[State Changes]{.std
    .std-ref}](tecplot.session.html#state-change){.reference .internal}
    is emitted to the engine after every statement. This can degrade
    performance if in the script the nodemap is being set many times.
    This context provides a way to suspend the state change notification
    until all assignments have been completed. In the following example,
    the state change is emitted only after the
    [`nodemap.assignment()`{.docutils .literal .notranslate}]{.pre}
    context exits:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> with nodemap.assignment():
        ...     nodemap[:] = node_data
    :::
    ::::

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[c_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicNodemap.c_type "Link to this definition"){.headerlink}

:   The underlying data type for this nodemap.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    This is the [[`ctypes`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.13)"){.reference
    .external} integer type used by the Tecplot Engine to store the
    nodemap data. This is used internally and is not normally needed for
    simple nodemap access.

    Type[:]{.colon}

    :   [[`ctypes.c_int32`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "(in Python v3.13)"){.reference
        .external} or [[`ctypes.c_int64`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[element]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[node]{.pre}]{.n}*, *[[offset]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.ClassicNodemap.element "Link to this definition"){.headerlink}

:   The element containing a given node.

    Parameters[:]{.colon}

    :   - **node** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based index of a node.

        - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based index of the element that uses the
          given node.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} - Zero-based index of the element.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> print(nodemap.element(3, 7))
        324
    :::
    ::::

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[nodes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/nodemap.html#ClassicNodemap.nodes){.reference .internal}[¶](#tecplot.data.ClassicNodemap.nodes "Link to this definition"){.headerlink}

:   Returns node values for a specific element.

    Parameters[:]{.colon}

    :   **element** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The element index.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.nodemap.nodes(1))
        (0, 1, 3, 4)
    :::
    ::::

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[num_elements]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[node]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.data.ClassicNodemap.num_elements "Link to this definition"){.headerlink}

:   The number of elements that use a given node.

    Parameters[:]{.colon}

    :   **node** -- ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}): Zero-based index of a node.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} - The number of elements that use this node.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> nodemap = dataset.zone('My Zone').nodemap
        >>> nodemap.num_elements(3)
        8
    :::
    ::::

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[num_points_per_element]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicNodemap.num_points_per_element "Link to this definition"){.headerlink}

:   Points per element for classic finite-element zones.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    The number of points (also known as nodes) per finite-element is
    determined from the [`zone_type`{.docutils .literal
    .notranslate}]{.pre} parameter. The following table shows the number
    of points per element for the available zone types along with the
    resulting shape of the nodemap based on the number of points
    specified ([\\(N\\)]{.math .notranslate .nohighlight}):

    > <div>
    >
    >   Zone Type                                               Points/Element   Nodemap Shape
    >   ------------------------------------------------------- ---------------- ---------------------------------------------------
    >   [`FELineSeg`{.docutils .literal .notranslate}]{.pre}    2                [\\((N, 2 N)\\)]{.math .notranslate .nohighlight}
    >   [`FETriangle`{.docutils .literal .notranslate}]{.pre}   3                [\\((N, 3 N)\\)]{.math .notranslate .nohighlight}
    >   [`FEQuad`{.docutils .literal .notranslate}]{.pre}       4                [\\((N, 4 N)\\)]{.math .notranslate .nohighlight}
    >   [`FETetra`{.docutils .literal .notranslate}]{.pre}      4                [\\((N, 4 N)\\)]{.math .notranslate .nohighlight}
    >   [`FEBrick`{.docutils .literal .notranslate}]{.pre}      8                [\\((N, 8 N)\\)]{.math .notranslate .nohighlight}
    >
    > </div>

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.zone('My Zone')
        >>> print(zone.zone_type)
        ZoneType.FETriangle
        >>> print(zone.nodemap.num_points_per_element)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[shape]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicNodemap.shape "Link to this definition"){.headerlink}

:   Shape of the nodemap array.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    This is defined by the zone type and is equal to [\\((N_e,
    N\_{npe})\\)]{.math .notranslate .nohighlight} where
    [\\(N_e\\)]{.math .notranslate .nohighlight} is the number of
    elements and [\\(N\_{npe}\\)]{.math .notranslate .nohighlight} is
    the number of nodes per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).nodemap.shape)
        (1024, 4)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ClassicNodemap.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.data.ClassicNodemap.size "Link to this definition"){.headerlink}

:   Total number of nodes stored in the nodemap array.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    This is defined by the zone type and is equal to [\\(N_e \\times
    N\_{npe}\\)]{.math .notranslate .nohighlight} where
    [\\(N_e\\)]{.math .notranslate .nohighlight} is the number of
    elements and [\\(N\_{npe}\\)]{.math .notranslate .nohighlight} is
    the number of nodes per element. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(dataset.zone(0).nodemap.shape)
        (1024, 4)
        >>> print(dataset.zone(0).nodemap.size)
        4096
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}
:::

::: {#facemap .section}
### [Facemap](#id117){.toc-backref role="doc-backlink"}[¶](#facemap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[Facemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap){.reference .internal}[¶](#tecplot.data.Facemap "Link to this definition"){.headerlink}

:   Connectivity list definition and control.

    A facemap holds the connectivity for a polytopal finite-element
    zone. This includes node-to-element and element-to-element
    connections. The following script creates a quad of two triangles
    from scratch using the PyTecplot low-level data creation interface.
    The data created looks like this:

    :::: {.highlight-none .notranslate}
    ::: highlight
        Node positions (x,y,z):

                       (1,1,1)
                      3
                     / \
                    /   \
         (0,1,.5)  2-----1  (1,0,.5)
                    \   /
                     \ /
                      0
                       (0,0,0)
    :::
    ::::

    Element indices are used when identifying the left and right of each
    face, where [\\(-1\\)]{.math .notranslate .nohighlight} is used to
    indicate no element:

    :::: {.highlight-none .notranslate}
    ::: highlight
            *
        -1 / \ -1
          / 1 \
         *-----*
          \ 0 /
        -1 \ / -1
            *
    :::
    ::::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        nodes = ((0, 0, 0  ),
                 (1, 0, 0.5),
                 (0, 1, 0.5),
                 (1, 1, 1  ))
        faces = ((0, 1),
                 (1, 2),
                 (2, 0),
                 (1, 3),
                 (3, 2))
        elements = (( 0, 0,  0,  1,  1),  # elements to the left of each face
                    (-1, 1, -1, -1, -1))  # elements to the right of each face
        num_elements = 2
        scalar_data = (0, 1, 2, 3)

        ds = tp.active_frame().create_dataset('Data', ['x','y','z','s'])
        z = ds.add_poly_zone(ZoneType.FEPolygon,
                             name='FE Polygon Float (4,2,5) Nodal',
                             num_points=len(nodes),
                             num_elements=num_elements,
                             num_faces=len(faces))

        z.values('x')[:] = [n[0] for n in nodes]
        z.values('y')[:] = [n[1] for n in nodes]
        z.values('z')[:] = [n[2] for n in nodes]
        z.facemap.set_mapping(faces, elements)
        z.values('s')[:] = scalar_data

        ### setup a view of the data
        plot = tp.active_frame().plot(PlotType.Cartesian3D)
        plot.activate()

        cont = plot.contour(0)
        cont.colormap_name = 'Sequential - Yellow/Green/Blue'
        cont.colormap_filter.distribution = ColorMapDistribution.Continuous

        for ax in plot.axes:
            ax.show = True

        plot.show_mesh = False
        plot.show_contour = True
        plot.show_edge = True
        plot.use_translucency = True

        fmap = plot.fieldmap(z)
        fmap.surfaces.surfaces_to_plot = SurfacesToPlot.All
        fmap.effects.surface_translucency = 40

        # View parameters obtained interactively from Tecplot 360
        plot.view.distance = 10
        plot.view.width = 2
        plot.view.psi = 80
        plot.view.theta = 30
        plot.view.alpha = 0
        plot.view.position = (-4.2, -8.0, 2.3)

        # Turning on mesh, we can see all the individual triangles
        plot.show_mesh = True
        plot.fieldmap(z).mesh.line_pattern = LinePattern.Dashed

        cont.levels.reset_to_nice()
        tp.export.save_png('polygons1.png', 600, supersample=3)
    :::
    ::::

    <figure id="id18" class="align-default" style="width: 300px">
    <a href="../_images/polygons1.png"
    class="reference internal image-reference"><img
    src="../_images/polygons1.png" style="width: 300px;"
    alt="../_images/polygons1.png" /></a>
    <figcaption><p><span class="caption-text">Two triangle polygons showing
    edge and mesh lines.</span><a href="#id18" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`element_c_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.element_c_type "tecplot.data.Facemap.element_c_type"){.reference .internal}         The data type of the element indices.
      [[`node_c_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.node_c_type "tecplot.data.Facemap.node_c_type"){.reference .internal}                  The data type of the node indices.
      [[`num_unique_nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.num_unique_nodes "tecplot.data.Facemap.num_unique_nodes"){.reference .internal}   The number of unique nodes in this [[`Facemap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference .internal}.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`alloc`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.alloc "tecplot.data.Facemap.alloc"){.reference .internal}(face_nodes\[, boundary_faces, \...\])                                         Allocate space for the facemap.
      [[`assignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.assignment "tecplot.data.Facemap.assignment"){.reference .internal}()                                                              Context manager for assigning facemap connections.
      [[`boundary_connection`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.boundary_connection "tecplot.data.Facemap.boundary_connection"){.reference .internal}(face, offset\[, element\])          The connected element and zone along a boundary face.
      [[`face`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.face "tecplot.data.Facemap.face"){.reference .internal}(element, offset)                                                                 Face index on a specific element.
      [[`left_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.left_element "tecplot.data.Facemap.left_element"){.reference .internal}(face\[, element\])                                       The element to the left of a specific face.
      [[`node`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.node "tecplot.data.Facemap.node"){.reference .internal}(face, offset\[, element\])                                                       The node index along a specific face.
      [[`num_boundary_connections`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.num_boundary_connections "tecplot.data.Facemap.num_boundary_connections"){.reference .internal}(\[face, element\])   The number of boundary connections for a given face.
      [[`num_faces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.num_faces "tecplot.data.Facemap.num_faces"){.reference .internal}(\[element\])                                                      The number of faces of an element in this [[`Facemap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference .internal}.
      [[`num_nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.num_nodes "tecplot.data.Facemap.num_nodes"){.reference .internal}(\[face, element\])                                                The number nodes for a given face in this [[`Facemap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference .internal}.
      [[`right_element`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.right_element "tecplot.data.Facemap.right_element"){.reference .internal}(face\[, element\])                                    The element to the right of a specific face.
      [[`set_boundary_connections`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.set_boundary_connections "tecplot.data.Facemap.set_boundary_connections"){.reference .internal}(elements, zones)     Set the boundary connections.
      [[`set_elementmap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.set_elementmap "tecplot.data.Facemap.set_elementmap"){.reference .internal}(elementmap)                                        Define connectivity per element.
      [[`set_elements`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.set_elements "tecplot.data.Facemap.set_elements"){.reference .internal}(left_elements, right_elements)                           Sets the polytope connectivity.
      [[`set_mapping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference .internal}(facemap, elements\[, \...\])                                Set the node and element connectivity for this polytope zone.
      [[`set_nodes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.Facemap.set_nodes "tecplot.data.Facemap.set_nodes"){.reference .internal}(facemap)                                                          Sets the polytope connectivity.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[alloc]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face_nodes]{.pre}]{.n}*, *[[boundary_faces]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[boundary_connections]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.alloc){.reference .internal}[¶](#tecplot.data.Facemap.alloc "Link to this definition"){.headerlink}

:   Allocate space for the facemap.

    Parameters[:]{.colon}

    :   - **face_nodes** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Total number of nodes for all faces. This is
          not the number of unique nodes but the total number. For
          example if a facemap defines two triangle polygons that share
          a common face, [`faces`{.docutils .literal
          .notranslate}]{.pre} would be 5 and [`face_nodes`{.docutils
          .literal .notranslate}]{.pre} would be 6, not 4.

        - **boundary_faces** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Total number of boundary faces.
          (default: 0)

        - **boundary_connections** ([[`int`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Total number of boundary face
          elements or boundary face element/zone pairs. (default: 0)

    Returns[:]{.colon}

    :   [[`Facemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
        .internal}

    This is called when using the [[`Facemap.set_mapping()`{.xref .any
    .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference
    .internal} method which is the preferred method for filling the
    connectivity of polytope zones. If the zone does not already have
    space allocated for a facemap and if you wish to use the
    [[`Facemap.set_nodes()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_nodes "tecplot.data.Facemap.set_nodes"){.reference
    .internal} and [[`Facemap.set_elements()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_elements "tecplot.data.Facemap.set_elements"){.reference
    .internal} methods to fill in the connectivity, then this must be
    called first:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> facemap = zone.facemap.alloc(400, 25, 50)
    :::
    ::::

    ::: {.admonition .note}
    Note

    Tecplot version 2017.2 or later.

    Setting the boundary faces and boundary connections using PyTecplot
    requires Tecplot version 2017.2 or later.
    :::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[assignment]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.assignment){.reference .internal}[¶](#tecplot.data.Facemap.assignment "Link to this definition"){.headerlink}

:   Context manager for assigning facemap connections.

    This context ensures the proper book keeping is done when setting
    the connectivity list and must be used with
    [[`Facemap.set_nodes()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_nodes "tecplot.data.Facemap.set_nodes"){.reference
    .internal}, [[`Facemap.set_elements()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_elements "tecplot.data.Facemap.set_elements"){.reference
    .internal} and [[`Facemap.set_boundary_connections()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_boundary_connections "tecplot.data.Facemap.set_boundary_connections"){.reference
    .internal}, which are used to define the connectivity of the zone.

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[boundary_connection]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face]{.pre}]{.n}*, *[[offset]{.pre}]{.n}*, *[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.boundary_connection){.reference .internal}[¶](#tecplot.data.Facemap.boundary_connection "Link to this definition"){.headerlink}

:   The connected element and zone along a boundary face.

    Parameters[:]{.colon}

    :   - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face.

        - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the node being
          requested.

        - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based index of an element. If
          given, *face* will be locally indexed within this element,
          otherwise *face* is globally indexed over the whole zone.

    Returns[:]{.colon}

    :   [[`namedtuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
        .external} --

        [`(element,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`zone)`{.docutils .literal .notranslate}]{.pre}:

        :   

            [`element`{.docutils .literal .notranslate}]{.pre}

            :   The zero-based index of the neighboring element.

            [`zone`{.docutils .literal .notranslate}]{.pre}

            :   The zone holding the neighboring element.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> bconn = zone.facemap.boundary_connection(0, 2)
        >>> print(bconn.element)
        128
        >>> print(bconn.zone.index)
        2
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[element_c_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Facemap.element_c_type "Link to this definition"){.headerlink}

:   The data type of the element indices.

    Possible values: [[`ctypes.c_int32`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "(in Python v3.13)"){.reference
    .external}, [[`ctypes.c_int64`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "(in Python v3.13)"){.reference
    .external}

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[face]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*, *[[offset]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.face){.reference .internal}[¶](#tecplot.data.Facemap.face "Link to this definition"){.headerlink}

:   Face index on a specific element.

    Parameters[:]{.colon}

    :   - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the element.

        - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face being
          requested.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} Zero-based index of the face at the specified
        location.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.face(0, 2))
        128
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[left_element]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face]{.pre}]{.n}*, *[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.left_element){.reference .internal}[¶](#tecplot.data.Facemap.left_element "Link to this definition"){.headerlink}

:   The element to the left of a specific face.

    Parameters[:]{.colon}

    :   - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face.

        - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based index of an element. If
          given, *face* will be locally indexed within this element,
          otherwise *face* is globally indexed over the whole zone.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

    A negative number indicates there is no element to the left of this
    face. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.left_element(0))
        128
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[node]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face]{.pre}]{.n}*, *[[offset]{.pre}]{.n}*, *[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.node){.reference .internal}[¶](#tecplot.data.Facemap.node "Link to this definition"){.headerlink}

:   The node index along a specific face.

    Parameters[:]{.colon}

    :   - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face.

        - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the node being
          requested.

        - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based index of an element. If
          given, *face* will be locally indexed within this element,
          otherwise *face* is globally indexed over the whole zone.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} The node at the specified location.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.face_node(0, 2))
        128
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[node_c_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Facemap.node_c_type "Link to this definition"){.headerlink}

:   The data type of the node indices.

    Possible values: [[`ctypes.c_int32`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "(in Python v3.13)"){.reference
    .external}, [[`ctypes.c_int64`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "(in Python v3.13)"){.reference
    .external}

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[num_boundary_connections]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.num_boundary_connections){.reference .internal}[¶](#tecplot.data.Facemap.num_boundary_connections "Link to this definition"){.headerlink}

:   The number of boundary connections for a given face.

    Parameters[:]{.colon}

    :   - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, required if no element is given) -- The zero-based
          index of the face.

        - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based index of an element. If
          given, *face* will be locally indexed within this element,
          otherwise *face* is globally indexed over the whole zone.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} The number of boundary connections.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.num_boundary_connections(1))
        1
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[num_faces]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.num_faces){.reference .internal}[¶](#tecplot.data.Facemap.num_faces "Link to this definition"){.headerlink}

:   The number of faces of an element in this [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   **element** ([[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}, optional) -- Zero-based index of an element. If no
        element is given, the total number of faces in the map are
        returned.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.num_faces())
        1048576
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[num_nodes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.num_nodes){.reference .internal}[¶](#tecplot.data.Facemap.num_nodes "Link to this definition"){.headerlink}

:   The number nodes for a given face in this [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal}.

    Parameters[:]{.colon}

    :   - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, required if no *element* is given) -- The
          zero-based index of the face either within the given *element*
          or globally. If no face is given, the number of nodes on the
          given *element* are returned.

        - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, required if no face is given) -- The zero-based
          index of an element. If no element is given, then *face* is
          globally indexed from zero over the whole zone.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} The number of nodes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.num_nodes(face=1))
        4
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[num_unique_nodes]{.pre}]{.sig-name .descname}[¶](#tecplot.data.Facemap.num_unique_nodes "Link to this definition"){.headerlink}

:   The number of unique nodes in this [[`Facemap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.num_unique_nodes)
        4194304
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[right_element]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[face]{.pre}]{.n}*, *[[element]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.right_element){.reference .internal}[¶](#tecplot.data.Facemap.right_element "Link to this definition"){.headerlink}

:   The element to the right of a specific face.

    Parameters[:]{.colon}

    :   - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face.

        - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based index of an element. If
          given, *face* will be locally indexed within this element,
          otherwise *face* is globally indexed over the whole zone.

    Returns[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

    A negative number indicates there is no element to the right of this
    face. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(zone.facemap.right_element(0))
        -1
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[set_boundary_connections]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[elements]{.pre}]{.n}*, *[[zones]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.set_boundary_connections){.reference .internal}[¶](#tecplot.data.Facemap.set_boundary_connections "Link to this definition"){.headerlink}

:   Set the boundary connections.

    Parameters[:]{.colon}

    :   - **elements** (2D array of [[`integers`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based indices of the connected elements.
          This is a "ragged" array of dimension [\\((N,E_i)\\)]{.math
          .notranslate .nohighlight} where [\\(N\\)]{.math .notranslate
          .nohighlight} is the number of boundary faces and
          [\\(E_i\\)]{.math .notranslate .nohighlight} is the number of
          boundary connected elements for the [\\(i\^{th}\\)]{.math
          .notranslate .nohighlight} face.

        - **zones** (2D array of [[`integers`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based indices of the zones for each entry
          given in *elements*. This must be the same shape as
          *elements*.

    The facemap must first be allocated with [[`Facemap.alloc()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.alloc "tecplot.data.Facemap.alloc"){.reference
    .internal} and must be called from within a
    [[`Facemap.assignment()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.assignment "tecplot.data.Facemap.assignment"){.reference
    .internal} context, and should follow calls to
    [[`Facemap.set_nodes()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_nodes "tecplot.data.Facemap.set_nodes"){.reference
    .internal} and [[`Facemap.set_elements()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_elements "tecplot.data.Facemap.set_elements"){.reference
    .internal} to complete the connectivity map information needed for
    rendering. Using [[`Facemap.set_mapping()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference
    .internal} is recommended, which does all the required book keeping.

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[set_elementmap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[elementmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.set_elementmap){.reference .internal}[¶](#tecplot.data.Facemap.set_elementmap "Link to this definition"){.headerlink}

:   Define connectivity per element.

    Parameters[:]{.colon}

    :   **elementmap** ([[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- Zero-based indices of the nodes that make up each
        face of each element. For polygons, the map is a list of
        elements, each made of up a list of nodes. For polyhedrons, this
        is a list of elements, made up a list of faces, each made up of
        a list of nodes.

    ::: {.admonition .warning}
    Warning

    This method is mutually exclusive with the
    [[`Facemap.set_mapping()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference
    .internal} and [[`Facemap.assignment()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.assignment "tecplot.data.Facemap.assignment"){.reference
    .internal}, [[`Facemap.set_nodes()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_nodes "tecplot.data.Facemap.set_nodes"){.reference
    .internal}, [[`Facemap.set_elements()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_elements "tecplot.data.Facemap.set_elements"){.reference
    .internal} and [[`Facemap.set_boundary_connections()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_boundary_connections "tecplot.data.Facemap.set_boundary_connections"){.reference
    .internal} family of methods. The size of the underlying arrays are
    calculated based on the elementmap given and a call to
    [[`Facemap.alloc()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.alloc "tecplot.data.Facemap.alloc"){.reference
    .internal} is made which will override any previous allocation.
    :::

    This may be a more convenient way to describe the connectivity of a
    polytope zone, however it does not support boundary face connections
    to other zones (see [[`Facemap.set_mapping()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference
    .internal}).

    Here is an example of an elementmap for two triangles (polygons):

    :::: {.highlight-python .notranslate}
    ::: highlight
        nodes = ((0, 0, 0  ),
                 (1, 0, 0.5),
                 (0, 1, 0.5),
                 (1, 1, 1  ))
        elementmap = ((0, 1, 2),  # polygon 0, 3 faces
                      (1, 3, 2))  # polygon 1, 3 faces
    :::
    ::::

    This is an example of an elementmap for two tetrahedrons
    (polyhedrons):

    :::: {.highlight-python .notranslate}
    ::: highlight
        nodes = ((0, 0, 0),
                 (1, 1, 0),
                 (1, 0, 1),
                 (0, 1, 1),
                 (0, 0, 1))
        elementmap = (((0, 1, 2),  # polyhedron 0, 4 faces
                       (0, 1, 3),
                       (1, 3, 2),
                       (0, 2, 3)),
                      ((0, 2, 3),  # polyhedron 1, 4 faces
                       (2, 3, 4),
                       (0, 2, 4),
                       (0, 4, 3)))
    :::
    ::::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[set_elements]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[left_elements]{.pre}]{.n}*, *[[right_elements]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.set_elements){.reference .internal}[¶](#tecplot.data.Facemap.set_elements "Link to this definition"){.headerlink}

:   Sets the polytope connectivity.

    Parameters[:]{.colon}

    :   - **left_elements** (array of zero-based [[`integers`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- This is an array of the elements to the left of
          each face in the facemap and must be the same length as the
          number of faces.

        - **right_elements** (array of zero-based [[`integers`{.xref
          .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Same as *left_elements* for the right side of
          each face.

    The facemap must first be allocated with [[`Facemap.alloc()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.alloc "tecplot.data.Facemap.alloc"){.reference
    .internal} and must be called from within a
    [[`Facemap.assignment()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.assignment "tecplot.data.Facemap.assignment"){.reference
    .internal} context and should follow a call to
    [[`Facemap.set_nodes()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_nodes "tecplot.data.Facemap.set_nodes"){.reference
    .internal} to complete the connectivity map information needed for
    rendering. Using [[`Facemap.set_mapping()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference
    .internal} is recommended, which does all the required book keeping.

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[set_mapping]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[facemap]{.pre}]{.n}*, *[[elements]{.pre}]{.n}*, *[[boundary_elements]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[boundary_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.set_mapping){.reference .internal}[¶](#tecplot.data.Facemap.set_mapping "Link to this definition"){.headerlink}

:   Set the node and element connectivity for this polytope zone.

    Parameters[:]{.colon}

    :   - **facemap** (2D array of zero-based [[`integers`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The [[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`lists`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} which need not all be the same length, defining the
          individual elements by their nodes.

        - **elements** (2D array of zero-based [[`integers`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- This is a [\\((2,N)\\)]{.math .notranslate
          .nohighlight} array where [\\(N\\)]{.math .notranslate
          .nohighlight} is the number of faces and the items are a list
          of the elements to the left and right of the face
          respectively.

        - **boundary_elements** (2D array of [[`integers`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based indices of the connected
          elements. This is a "ragged" array of dimension [\\((N,
          E_i)\\)]{.math .notranslate .nohighlight} where
          [\\(N\\)]{.math .notranslate .nohighlight} is the number of
          boundary faces and [\\(E_i\\)]{.math .notranslate
          .nohighlight} is the number of boundary connected elements for
          the [\\(i\^{th}\\)]{.math .notranslate .nohighlight} face.

        - **boundary_zones** (2D array of [[`integers`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Zero-based indices of the zones for
          each entry given in *elements*. This must be the same shape as
          *elements*.

    See the code example for the [[`Facemap`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap "tecplot.data.Facemap"){.reference
    .internal} class object for details.

    ::: {.admonition .note}
    Note

    **boundary_elements** and **boundary_zones**

    The two parameters, **boundary_elements** and **boundary_zones**,
    must be supplied together or not at all.
    :::

<!-- -->

[[Facemap.]{.pre}]{.sig-prename .descclassname}[[set_nodes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[facemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/facemap.html#Facemap.set_nodes){.reference .internal}[¶](#tecplot.data.Facemap.set_nodes "Link to this definition"){.headerlink}

:   Sets the polytope connectivity.

    Parameters[:]{.colon}

    :   **facemap** (2D array of zero-based [[`integers`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`lists`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} which need not all be the same length, defining the
        individual elements by their nodes.

    The facemap must first be allocated with [[`Facemap.alloc()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.alloc "tecplot.data.Facemap.alloc"){.reference
    .internal} and must be called from within a
    [[`Facemap.assignment()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.assignment "tecplot.data.Facemap.assignment"){.reference
    .internal} context and should be followed by a call to
    [[`Facemap.set_elements()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_elements "tecplot.data.Facemap.set_elements"){.reference
    .internal} to complete the connectivity map information needed for
    rendering. It is recomended to use the
    [[`Facemap.set_mapping()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.Facemap.set_mapping "tecplot.data.Facemap.set_mapping"){.reference
    .internal} which does all the required book keeping.
:::

::: {#faceneighbors .section}
### [FaceNeighbors](#id118){.toc-backref role="doc-backlink"}[¶](#faceneighbors "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.data.]{.pre}]{.sig-prename .descclassname}[[FaceNeighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors){.reference .internal}[¶](#tecplot.data.FaceNeighbors "Link to this definition"){.headerlink}

:   Face neighbor definition and control.

    Face neighbors are used when the face of an element overlaps with
    another face from another element. Specifying these two (or more)
    overlapping faces as "face neighbors" indicates element connections
    outside the implicit faces of the nodemap. By specifying face
    neighbors it ensures that plot elements like shading, creases and
    edges are treated continously even if there is a zone or cell
    boundry.

    The neighbors can be completely "local", within a single zone, or
    "global" conntecting two or more zones together. Furthermore, the
    connections made can be one-to-one meaning there any given face can
    only neighbor one other face, or one-to-many where a single face can
    neighbor several other faces.

    This example creates two triangles in two different zones. Global
    one-to-one face neighbors are then used to stitch the two triangles
    into a quad. The data created looks like this:

    :::: {.highlight-none .notranslate}
    ::: highlight
        Node positions (x,y,z):

                       (1,1,1)
                      *
                     / \
                    /   \
         (0,1,.5)  *-----*  (1,0,.5)
                    \   /
                     \ /
                      *
                       (0,0,0)
    :::
    ::::

    The two triangles will have separate nodes at the shared locations:

    :::: {.highlight-none .notranslate}
    ::: highlight
        Nodes:
                           2
            Zone 1:       / \
                         /   \
                        1-----0
                        2-----1
                         \   /
            Zone 0:       \ /
                           0
    :::
    ::::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        # Triangle 0
        nodes0 = (
            (0, 0, 0  ),
            (1, 0, 0.5),
            (0, 1, 0.5))
        scalar_data0 = (0, 1, 2)
        conn0 = ((0, 1, 2),)
        neighbors0 = ((None, 0, None),)
        neighbor_zones0 = ((None, 1, None),)

        # Triangle 1
        nodes1 = (
            (1, 0, 0.5),
            (0, 1, 0.5),
            (1, 1, 1  ))
        scalar_data1 = (1, 2, 3)
        conn1 = ((0, 1, 2),)
        neighbors1 = ((0, None, None),)
        neighbor_zones1 = ((0, None, None),)

        # Create the dataset and zones
        ds = tp.active_frame().create_dataset('Data', ['x','y','z','s'])
        z0 = ds.add_fe_zone(ZoneType.FETriangle,
                            name='FE Triangle Float (3,1) Nodal 0',
                            num_points=len(nodes0), num_elements=len(conn0),
                            face_neighbor_mode=FaceNeighborMode.GlobalOneToOne)
        z1 = ds.add_fe_zone(ZoneType.FETriangle,
                            name='FE Triangle Float (3,1) Nodal 1',
                            num_points=len(nodes1), num_elements=len(conn1),
                            face_neighbor_mode=FaceNeighborMode.GlobalOneToOne)

        # Fill in and connect first triangle
        z0.values('x')[:] = [n[0] for n in nodes0]
        z0.values('y')[:] = [n[1] for n in nodes0]
        z0.values('z')[:] = [n[2] for n in nodes0]
        z0.nodemap[:] = conn0
        z0.values('s')[:] = scalar_data0

        # Fill in and connect second triangle
        z1.values('x')[:] = [n[0] for n in nodes1]
        z1.values('y')[:] = [n[1] for n in nodes1]
        z1.values('z')[:] = [n[2] for n in nodes1]
        z1.nodemap[:] = conn1
        z1.values('s')[:] = scalar_data1

        # Set face neighbors
        z0.face_neighbors.set_neighbors(neighbors0, neighbor_zones0, obscures=True)
        z1.face_neighbors.set_neighbors(neighbors1, neighbor_zones1, obscures=True)


        ### Setup a view of the data
        plot = tp.active_frame().plot(PlotType.Cartesian3D)
        plot.activate()

        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'
        plot.contour(0).colormap_filter.distribution = ColorMapDistribution.Continuous

        for ax in plot.axes:
            ax.show = True

        plot.show_mesh = False
        plot.show_contour = True
        plot.show_edge = True
        plot.use_translucency = True

        # View parameters obtained interactively from Tecplot 360
        plot.view.distance = 10
        plot.view.width = 2
        plot.view.psi = 80
        plot.view.theta = 30
        plot.view.alpha = 0
        plot.view.position = (-4.2, -8.0, 2.3)

        fmaps = plot.fieldmaps()
        fmaps.surfaces.surfaces_to_plot = SurfacesToPlot.All
        fmaps.effects.surface_translucency = 40

        # Turning on mesh, we can see all the individual triangles
        plot.show_mesh = True
        fmaps.mesh.line_pattern = LinePattern.Dashed

        plot.contour(0).levels.reset_to_nice()
        tp.export.save_png('fe_triangles1.png', 600, supersample=3)
    :::
    ::::

    <figure id="id19" class="align-default" style="width: 300px">
    <a href="../_images/fe_triangles1.png"
    class="reference internal image-reference"><img
    src="../_images/fe_triangles1.png" style="width: 300px;"
    alt="../_images/fe_triangles1.png" /></a>
    <figcaption><p><span class="caption-text">Two triangles in two separate
    zones, stitched together using global face neighbors, showing the edge
    and mesh.</span><a href="#id19" class="headerlink"
    title="Link to this image">¶</a></p></figcaption>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------
      [[`c_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.c_type "tecplot.data.FaceNeighbors.c_type"){.reference .internal}   Underlying storage type used by the Tecplot Engine.
      [[`mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.mode "tecplot.data.FaceNeighbors.mode"){.reference .internal}         Relative locality of the face neighbors.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------
      [[`add_local_neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.add_local_neighbors "tecplot.data.FaceNeighbors.add_local_neighbors"){.reference .internal}(neighbors\[, offset\])   Assign all local one-to-one face neighbors at once.
      [[`add_neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.add_neighbors "tecplot.data.FaceNeighbors.add_neighbors"){.reference .internal}(element, face, neighbors\[, \...\])        Connect boundary of an element\'s face to a neighboring face.
      [[`assignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.assignment "tecplot.data.FaceNeighbors.assignment"){.reference .internal}()                                                   Context manager for assigning face neighbors.
      [[`is_obscured`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.is_obscured "tecplot.data.FaceNeighbors.is_obscured"){.reference .internal}(element, face\[, active_zones\])                 Obscuration of the specified face.
      [[`neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.neighbors "tecplot.data.FaceNeighbors.neighbors"){.reference .internal}(element, face)                                         Get the neighboring elements and zones of a specific face.
      [[`set_neighbors`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.set_neighbors "tecplot.data.FaceNeighbors.set_neighbors"){.reference .internal}(neighbors\[, zones, obscures\])            Clear and set face neighbors from the given array.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[add_local_neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[neighbors]{.pre}]{.n}*, *[[offset]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors.add_local_neighbors){.reference .internal}[¶](#tecplot.data.FaceNeighbors.add_local_neighbors "Link to this definition"){.headerlink}

:   Assign all local one-to-one face neighbors at once.

    Parameters[:]{.colon}

    :   - **neighbors** (2D array of [[`integers`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- [\\((E,F)\\)]{.math .notranslate .nohighlight}
          Array of the face neighbors where [\\(E\\)]{.math .notranslate
          .nohighlight} is the number of elements and [\\(F\\)]{.math
          .notranslate .nohighlight} is the number of faces per element.

        - **offset** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Offset in Tecplot's face neighbor
          array to begin assigning the supplied neighbor elements.
          (default: 0)

    This method must be called from within a
    [[`FaceNeighbors.assignment()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.assignment "tecplot.data.FaceNeighbors.assignment"){.reference
    .internal} context which will clear any previously existing face
    neighbor data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> with zone.face_neighbors.assigment():
        ...     zone.face_neighbors.add_local_neighbors(neighbors)
    :::
    ::::

    See the example code for [[`FaceNeighbors`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
    .internal} class object for more details on how to set up
    user-defined face neighbors.

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[add_neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*, *[[face]{.pre}]{.n}*, *[[neighbors]{.pre}]{.n}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[obscure]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors.add_neighbors){.reference .internal}[¶](#tecplot.data.FaceNeighbors.add_neighbors "Link to this definition"){.headerlink}

:   Connect boundary of an element's face to a neighboring face.

    This sets the boundary connection face neighbors within an open face
    neighbor assignment sequence for the specified element and face.

    Parameters[:]{.colon}

    :   - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The element number (zero-based).

        - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The face number on the element (zero-based).

        - **neighbors** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[`integers`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} or [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}) -- List of zero-based indices of the neighboring
          faces.

        - **zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of zone objects, optional) -- List of zones for
          global neighbors. This must be the same length as
          [`neighbors`{.docutils .literal .notranslate}]{.pre}. Use
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} to indicate these are local neighbors. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **obscure** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Indicates that the neighbors
          completely obscure the face. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    This method must be called from within a
    [[`FaceNeighbors.assignment()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.assignment "tecplot.data.FaceNeighbors.assignment"){.reference
    .internal} context which will clear any previously existing face
    neighbor data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> with zone.face_neighbors.assigment():
        ...     for elem, face, neighbors, zn in face_neighbor_data:
        ...         zone.face_neighbors.add_neighbors(elem, face,
        ...                                           neighbors, zn)
    :::
    ::::

    See the example code for [[`FaceNeighbors`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
    .internal} class object for more details on how to set up
    user-defined face neighbors.

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[assignment]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors.assignment){.reference .internal}[¶](#tecplot.data.FaceNeighbors.assignment "Link to this definition"){.headerlink}

:   Context manager for assigning face neighbors.

    This context ensures the proper book keeping is done when setting
    face neighbors. After the face neighbors are specified, this context
    will valid the connections and make appropriate changes to the zone
    metadata. It must be used with the
    [[`FaceNeighbors.add_local_neighbors()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.add_local_neighbors "tecplot.data.FaceNeighbors.add_local_neighbors"){.reference
    .internal} and/or [[`FaceNeighbors.add_neighbors()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.add_neighbors "tecplot.data.FaceNeighbors.add_neighbors"){.reference
    .internal} methods. See the [[`FaceNeighbors`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
    .internal} example code for more details on how to set up
    user-defined face neighbors.

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[c_type]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FaceNeighbors.c_type "Link to this definition"){.headerlink}

:   Underlying storage type used by the Tecplot Engine.

    Possible values: [[`ctypes.c_int32`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "(in Python v3.13)"){.reference
    .external}, ctypes.c_int64\`.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[is_obscured]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*, *[[face]{.pre}]{.n}*, *[[active_zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors.is_obscured){.reference .internal}[¶](#tecplot.data.FaceNeighbors.is_obscured "Link to this definition"){.headerlink}

:   Obscuration of the specified face.

    Parameters[:]{.colon}

    :   - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the element.

        - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face on the
          element.

        - **active_zones** ([[`list`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
          .external} of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}) -- List of
          zones to consider when global face neighbors are present. If
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, the active zones of the dataset's parent frame
          will be used.

    Returns[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

    ::: {.admonition .note}
    Note

    Because datasets can be shared between frames, the default frame
    used to identify the active zones may not be the one you want. In
    this case, you can use the [[`Frame.active_zones()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.active_zones "tecplot.layout.Frame.active_zones"){.reference
    .internal} method to provide the active zones for a specific frame.
    Furthermore, the plot type of the frame must have the concept of
    active zones - i.e. it must not be in "sketch" mode.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone.face_neighbors.is_obscured(element=0, face=1)
        True
    :::
    ::::

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[mode]{.pre}]{.sig-name .descname}[¶](#tecplot.data.FaceNeighbors.mode "Link to this definition"){.headerlink}

:   Relative locality of the face neighbors.

    Possible values: [[`FaceNeighborMode.LocalOneToOne`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.LocalOneToOne "tecplot.constant.FaceNeighborMode.LocalOneToOne"){.reference .internal},

    :   [[`FaceNeighborMode.LocalOneToMany`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.LocalOneToMany "tecplot.constant.FaceNeighborMode.LocalOneToMany"){.reference
        .internal}, [[`FaceNeighborMode.GlobalOneToOne`{.xref .any .py
        .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.GlobalOneToOne "tecplot.constant.FaceNeighborMode.GlobalOneToOne"){.reference
        .internal}, [[`FaceNeighborMode.GlobalOneToMany`{.xref .any .py
        .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode.GlobalOneToMany "tecplot.constant.FaceNeighborMode.GlobalOneToMany"){.reference
        .internal}.

    ::: {.admonition .note}
    Note

    This property is read-only.
    :::

    Face neighbors are used when the face of an element overlaps with
    another face from another element. The neighbors can be completely
    "local", within a single zone, or "global" conntecting two or more
    zones together. Furthermore, the connections made can be one-to-one
    meaning there any given face can only neighbor one other face, or
    one-to-many where a single face can neighbor several other faces.
    The face neighbor mode is set on zone creation and can not be
    changed afterwards:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> zone = dataset.add_fe_zone(ZoneType.FETriangle, 'Zone', 4, 2,
        ...    face_neighbor_mode=FaceNeighborMode.LocalOneToMany)
        >>> print(zone.face_neighbors.mode)
        FaceNeighborMode.LocalOneToMany
    :::
    ::::

    Type[:]{.colon}

    :   [[`FaceNeighborMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FaceNeighborMode "tecplot.constant.FaceNeighborMode"){.reference
        .internal}

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[element]{.pre}]{.n}*, *[[face]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors.neighbors){.reference .internal}[¶](#tecplot.data.FaceNeighbors.neighbors "Link to this definition"){.headerlink}

:   Get the neighboring elements and zones of a specific face.

    Parameters[:]{.colon}

    :   - **element** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the element.

        - **face** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- The zero-based index of the face on this
          element.

    Returns[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`namedtuples`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)"){.reference
        .external} --

        [`(element,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`zone)`{.docutils .literal .notranslate}]{.pre}:

        :   

            [`element`{.docutils .literal .notranslate}]{.pre}:

            :   The zero-based index of the neighboring element.

            [`zone`{.docutils .literal .notranslate}]{.pre}:

            :   The zone holding the neighboring element. A value of
                [[`None`{.xref .any .docutils .literal
                .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
                .external} indicates this is a local (intra-zone)
                neighbor connection.

    Example getting the neighboring faces of a zone's first element,
    second face:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> neighbors = zone.face_neighbors.neighbors(element=0, face=1)
        >>> for neighbor in neighbors:
        ...     elem, zn = neighbor
        ...     print(elem, zn.index)
        21 2
    :::
    ::::

<!-- -->

[[FaceNeighbors.]{.pre}]{.sig-prename .descclassname}[[set_neighbors]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[neighbors]{.pre}]{.n}*, *[[zones]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[obscures]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/data/face_neighbors.html#FaceNeighbors.set_neighbors){.reference .internal}[¶](#tecplot.data.FaceNeighbors.set_neighbors "Link to this definition"){.headerlink}

:   Clear and set face neighbors from the given array.

    Parameters[:]{.colon}

    :   - **neighbors** (array of [[`integers`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Zero-based Element indices of the neighbors for
          each face in the zone. A value of [\\(-1\\)]{.math
          .notranslate .nohighlight} or [[`None`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external} indicates no neighbor.

        - **zones** (array of [[Zones]{.std
          .std-ref}](#data-access){.reference .internal}, optional) --
          This parameter is only used when the face neighbor mode is
          global one-to-one or global one-to-many. (default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **obscures** (array of [[`booleans`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Indicates that the neighbors
          completely obscure the face. (default: [[`False`{.xref .any
          .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    This method uses the [[`FaceNeighbors.assignment()`{.xref .any .py
    .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors.assignment "tecplot.data.FaceNeighbors.assignment"){.reference
    .internal} context internally to ensure the proper book keeping is
    done. See the example code for [[`FaceNeighbors`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.data.FaceNeighbors "tecplot.data.FaceNeighbors"){.reference
    .internal} class object for details on how to use this method.
:::
:::::::::::::::::::

:::: {#auxiliary-data .section}
## [Auxiliary Data](#id73){.toc-backref role="doc-backlink"}[¶](#auxiliary-data "Link to this heading"){.headerlink}

::: {#auxdata .section}
### [AuxData](#id74){.toc-backref role="doc-backlink"}[¶](#auxdata "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.session.]{.pre}]{.sig-prename .descclassname}[[AuxData]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[parent]{.pre}]{.n}*, *[[object_type]{.pre}]{.n}*, *[[object_index]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData){.reference .internal}[¶](#tecplot.session.AuxData "Link to this definition"){.headerlink}

:   Auxiliary data.

    The Tecplot Engine can hold auxiliary data attached to one of the
    following objects:

    > <div>
    >
    > - [[`Layout`{.xref .any .py .py-func .docutils .literal
    >   .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.aux_data "tecplot.layout.aux_data"){.reference
    >   .internal}
    >
    > - [[`Page`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Page.aux_data "tecplot.layout.Page.aux_data"){.reference
    >   .internal}
    >
    > - [[`Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.aux_data "tecplot.layout.Frame.aux_data"){.reference
    >   .internal}
    >
    > - [[`Dataset`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.data.Dataset.aux_data "tecplot.data.Dataset.aux_data"){.reference
    >   .internal}
    >
    > - [[`Variable`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.data.Variable.aux_data "tecplot.data.Variable.aux_data"){.reference
    >   .internal}
    >
    > - [[`Zone`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.data.OrderedZone.aux_data "tecplot.data.OrderedZone.aux_data"){.reference
    >   .internal}
    >
    > - [[`Linemap`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinemap.aux_data "tecplot.plot.XYLinemap.aux_data"){.reference
    >   .internal}
    >
    > </div>

    Auxiliary data is an ordered key-value pair that behaves like an
    ordered dictionary, or [[`OrderedDict`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/collections.html#collections.OrderedDict "(in Python v3.13)"){.reference
    .external}. Keys are strings which are ordered alphabetically and
    values can additionally be access by index. The keys must be
    alphanumeric (special characters "." and "\_" are allowed), must not
    contain spaces, and must begin with a non-numeric character or
    underscore. Values, on the other hand, are arbitrary strings and can
    contain anything except the null character. In this example, we
    query the auxiliary data attached to the dataset and add some
    information to it. Notice that the stored order is alphabetical:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp

        aux = tp.active_frame().aux_data
        aux['info'] = 'Here is some information.'
        aux['Xavg'] = 3.14159
        aux['note'] = 'Aux data values are always converted to strings.'

        '''
        The following code will print:
            info: Here is some information.
            note: Aux data values are always converted to strings.
            Xavg: 3.14159
        '''
        for k, v in aux.items():
            print('{}: {}'.format(k,v))
    :::
    ::::

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------
      [[`as_dict`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.as_dict "tecplot.session.AuxData.as_dict"){.reference .internal}()                   Returns a Python dict of the Aux Data attached to the parent.
      [[`clear`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.clear "tecplot.session.AuxData.clear"){.reference .internal}()                         Deletes all Aux Data from the associated object.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.index "tecplot.session.AuxData.index"){.reference .internal}(key)                      Returns the zero-based index of the element based on key.
      [[`items`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.items "tecplot.session.AuxData.items"){.reference .internal}()                         Yields all key/value pairs of the Aux Data attached to the parent.
      [[`key`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.key "tecplot.session.AuxData.key"){.reference .internal}(index)                          Returns the key at a specific zero-based index.
      [[`keys`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.keys "tecplot.session.AuxData.keys"){.reference .internal}()                            Yields all keys of the Aux Data attached to the parent.
      [[`update`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.update "tecplot.session.AuxData.update"){.reference .internal}(\*other, \*\*kwargs)   Update Aux Data with key/value pairs from another Aux Data or dict.
      [[`values`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.session.AuxData.values "tecplot.session.AuxData.values"){.reference .internal}()                      Yields all values of the Aux Data attached to the parent.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[as_dict]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.as_dict){.reference .internal}[¶](#tecplot.session.AuxData.as_dict "Link to this definition"){.headerlink}

:   Returns a Python dict of the Aux Data attached to the parent.

    Note that this will remove the alphabetical ordering guarantee that
    Aux Data has since Python dict objects are unordered. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data['result'] = '3.1415'
        >>> frame.aux_data['other_info'] = '128'
        >>> aux = frame.aux_data.as_dict()
        >>> print(aux)
        {'result': '3.1415', 'other_info': '128'}
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[clear]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.clear){.reference .internal}[¶](#tecplot.session.AuxData.clear "Link to this definition"){.headerlink}

:   Deletes all Aux Data from the associated object.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(frame.aux_data)
        {'bb': 'test bb', 'cc': 'test cc', 'aa': 'test aa'}
        >>> frame.aux_data.clear()
        >>> print(frame.aux_data)
        {}
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[key]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.index){.reference .internal}[¶](#tecplot.session.AuxData.index "Link to this definition"){.headerlink}

:   Returns the zero-based index of the element based on key.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data['result'] = '3.1415'
        >>> frame.aux_data['other_info'] = '128'
        >>> print(frame.aux_data.index('other_info'))
        0
        >>> print(frame.aux_data.index('result'))
        1
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[items]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.items){.reference .internal}[¶](#tecplot.session.AuxData.items "Link to this definition"){.headerlink}

:   Yields all key/value pairs of the Aux Data attached to the parent.

    Elements are always ordered alphabetically by the keys. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data['result'] = '3.1415'
        >>> frame.aux_data['other_info'] = '128'
        >>> for key, value in frame.aux_data.items():
        ...     print(key, value)
        other_info 128
        result 3.1415
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[key]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.key){.reference .internal}[¶](#tecplot.session.AuxData.key "Link to this definition"){.headerlink}

:   Returns the key at a specific zero-based index.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data['result'] = '3.1415'
        >>> frame.aux_data['other_info'] = '128'
        >>> print(frame.aux_data.key(0))
        other_info
        >>> print(frame.aux_data.key(1))
        result
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[keys]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.keys){.reference .internal}[¶](#tecplot.session.AuxData.keys "Link to this definition"){.headerlink}

:   Yields all keys of the Aux Data attached to the parent.

    Elements are always ordered alphabetically by the keys. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data['result'] = '3.1415'
        >>> frame.aux_data['other_info'] = '128'
        >>> for value in frame.aux_data.keys():
        ...     print(value)
        other_info
        result
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[update]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[other]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.update){.reference .internal}[¶](#tecplot.session.AuxData.update "Link to this definition"){.headerlink}

:   Update Aux Data with key/value pairs from another Aux Data or dict.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data.update({'result': '3.1415', 'other_info': '128'})
        >>> print(frame.aux_data)
        {'result': '3.1415', 'other_info': '128'}
    :::
    ::::

<!-- -->

[[AuxData.]{.pre}]{.sig-prename .descclassname}[[values]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/session/aux_data.html#AuxData.values){.reference .internal}[¶](#tecplot.session.AuxData.values "Link to this definition"){.headerlink}

:   Yields all values of the Aux Data attached to the parent.

    Elements are always ordered alphabetically by the keys. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tp.active_frame()
        >>> frame.aux_data['result'] = '3.1415'
        >>> frame.aux_data['other_info'] = '128'
        >>> for value in frame.aux_data.values():
        ...     print(value)
        128
        3.1415
    :::
    ::::
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::: clearer
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
