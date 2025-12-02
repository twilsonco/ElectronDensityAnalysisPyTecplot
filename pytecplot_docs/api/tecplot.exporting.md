::::::::::::::::::::::::::::: {.body role="main"}
::::::::::::::::::::::::::: {#exporting .section}
# Exporting[¶](#exporting "Link to this heading"){.headerlink}

- [Exporting Images](#exporting-images){#id16 .reference .internal}

  - [export.save_bmp()](#export-save-bmp){#id17 .reference .internal}

  - [export.save_eps()](#export-save-eps){#id18 .reference .internal}

  - [export.save_jpeg()](#export-save-jpeg){#id19 .reference .internal}

  - [export.save_png()](#export-save-png){#id20 .reference .internal}

  - [export.save_ps()](#export-save-ps){#id21 .reference .internal}

  - [export.save_tiff()](#export-save-tiff){#id22 .reference .internal}

  - [export.save_wmf()](#export-save-wmf){#id23 .reference .internal}

- [Exporting Video](#exporting-video){#id24 .reference .internal}

  - [export.animation_avi()](#export-animation-avi){#id25 .reference
    .internal}

  - [export.animation_mpeg4()](#export-animation-mpeg4){#id26 .reference
    .internal}

  - [export.animation_wmv()](#export-animation-wmv){#id27 .reference
    .internal}

  - [export.animation_flash()](#export-animation-flash){#id28 .reference
    .internal}

  - [export.animation_raster_metafile()](#export-animation-raster-metafile){#id29
    .reference .internal}

  - [export.animation.animation.export_animation_frame()](#export-animation-animation-export-animation-frame){#id30
    .reference .internal}

  - [export.save_time_animation_avi()](#export-save-time-animation-avi){#id31
    .reference .internal}

  - [export.save_time_animation_mpeg4()](#export-save-time-animation-mpeg4){#id32
    .reference .internal}

  - [export.save_time_animation_wmv()](#export-save-time-animation-wmv){#id33
    .reference .internal}

  - [export.save_time_animation_flash()](#export-save-time-animation-flash){#id34
    .reference .internal}

  - [export.save_time_animation_raster_metafile()](#export-save-time-animation-raster-metafile){#id35
    .reference .internal}

  - [export.save_time_animation_bmp()](#export-save-time-animation-bmp){#id36
    .reference .internal}

  - [export.save_time_animation_jpeg()](#export-save-time-animation-jpeg){#id37
    .reference .internal}

  - [export.save_time_animation_png()](#export-save-time-animation-png){#id38
    .reference .internal}

  - [export.save_time_animation_tiff()](#export-save-time-animation-tiff){#id39
    .reference .internal}

:::::::::: {#exporting-images .section}
## [Exporting Images](#id16){.toc-backref role="doc-backlink"}[¶](#exporting-images "Link to this heading"){.headerlink}

- [export.save_bmp()](#export-save-bmp){#id40 .reference .internal}

- [export.save_eps()](#export-save-eps){#id41 .reference .internal}

- [export.save_jpeg()](#export-save-jpeg){#id42 .reference .internal}

- [export.save_png()](#export-save-png){#id43 .reference .internal}

- [export.save_ps()](#export-save-ps){#id44 .reference .internal}

- [export.save_tiff()](#export-save-tiff){#id45 .reference .internal}

- [export.save_wmf()](#export-save-wmf){#id46 .reference .internal}

::: {#export-save-bmp .section}
### [export.save_bmp()](#id40){.toc-backref role="doc-backlink"}[¶](#export-save-bmp "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_bmp]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[convert_to_256_colors]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_bmp){.reference .internal}[¶](#tecplot.export.save_bmp "Link to this definition"){.headerlink}

:   Save a [BMP
    image](https://en.wikipedia.org/wiki/BMP_file_format){.reference
    .external}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Specify a width in pixels for the generated
          image. A larger width increases the quality of your image.
          However, the greater the width, the longer it will take to
          export the image, and the larger the exported file. (default:
          **800**)

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of antialiasing
          used in the image. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of image output
          formats by the process of supersampling. Some graphics cards
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **convert_to_256_colors** ([[`Boolean`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Pass [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} to generate an image with no more than 256 colors
          (reduced from a possible 16 million colors). Tecplot 360
          selects the best color match. The image will have a greatly
          reduced file size, but for plots with many colors, the results
          may be suboptimal. If this option is used with transparency,
          smooth color gradations, or antialiasing may result in poor
          image quality. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    If exporting is taking an unusually long time, or you get an error
    message saying that the image cannot be exported, the most likely
    cause is that the image width you are trying to export is too large.
    Selecting a smaller image width will greatly speed up the export
    process. For an image export size of Length x Width, the file size
    for an uncompressed true color image is approximately Length x Width
    x 3. Memory requirements to export such an image can be up to twice
    this size. For 256-color images, the maximum file size is
    approximately Length x Width, but is usually less since all
    256-color image files are compressed. However, the memory
    requirements for exporting are the same as they are for a true color
    uncompressed image.
    :::

    Save a BMP image of the entire workspace with supersampling:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ExportRegion
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_bmp('image.bmp', width=600, supersample=3,
        ...                         region=ExportRegion.WorkArea)
    :::
    ::::
:::

::: {#export-save-eps .section}
### [export.save_eps()](#id41){.toc-backref role="doc-backlink"}[¶](#export-save-eps "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_eps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[palette]{.pre}]{.n}[[=]{.pre}]{.o}[[Palette.Color]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[force_extra_3d_sorting]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[extra_precision]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[render_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PrintRenderType.Vector]{.pre}]{.default_value}*, *[[resolution]{.pre}]{.n}[[=]{.pre}]{.o}[[150]{.pre}]{.default_value}*, *[[preview_type]{.pre}]{.n}[[=]{.pre}]{.o}[[EPSPreviewImage.TIFF]{.pre}]{.default_value}*, *[[preview_width]{.pre}]{.n}[[=]{.pre}]{.o}[[128]{.pre}]{.default_value}*, *[[preview_height]{.pre}]{.n}[[=]{.pre}]{.o}[[128]{.pre}]{.default_value}*, *[[preview_gray_scale_depth]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_eps){.reference .internal}[¶](#tecplot.export.save_eps "Link to this definition"){.headerlink}

:   Save an [Encapsulated PostScript
    image](https://en.wikipedia.org/wiki/Encapsulated_PostScript){.reference
    .external}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **palette** ([[`Palette`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette "tecplot.constant.Palette"){.reference
          .internal}, optional) -- Export color image. (default:
          [[`Palette.Color`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette.Color "tecplot.constant.Palette.Color"){.reference
          .internal})

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **force_extra_3d_sorting** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Force extra sorting for all 3D
          frames. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **extra_precision** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Additional digits for all numbers
          written to postscript file. (default: 0)

        - **render_type** ([[`PrintRenderType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType "tecplot.constant.PrintRenderType"){.reference
          .internal}, optional) -- Whether to render the postscript as a
          rasterized or vector image. (default:
          [[`PrintRenderType.Vector`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType.Vector "tecplot.constant.PrintRenderType.Vector"){.reference
          .internal})

        - **resolution** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Resolution of the image in dots per inch.
          Larger values create more accurate plots, but result in larger
          file sizes. Note: this value is ignored if
          [[`PrintRenderType`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType "tecplot.constant.PrintRenderType"){.reference
          .internal} is [[`PrintRenderType.Vector`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType.Vector "tecplot.constant.PrintRenderType.Vector"){.reference
          .internal} (default: **150**)

        - **preview_type** ([[`EPSPreviewImage`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage "tecplot.constant.EPSPreviewImage"){.reference
          .internal}, optional) -- The type of image to use as an
          embedded preview. Possible values are
          [[`EPSPreviewImage.None_`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.None_ "tecplot.constant.EPSPreviewImage.None_"){.reference
          .internal}, [[`EPSPreviewImage.TIFF`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.TIFF "tecplot.constant.EPSPreviewImage.TIFF"){.reference
          .internal} (default), [[`EPSPreviewImage.EPSI2`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.EPSI2 "tecplot.constant.EPSPreviewImage.EPSI2"){.reference
          .internal} or [[`EPSPreviewImage.FRAME`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.FRAME "tecplot.constant.EPSPreviewImage.FRAME"){.reference
          .internal}.

        - **preview_width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Width of the preview image in pixels
          (default: 128). This is only used if *preview_type* is not
          [[`EPSPreviewImage.None_`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.None_ "tecplot.constant.EPSPreviewImage.None_"){.reference
          .internal}.

        - **preview_height** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Height of the preview image in pixels
          (default: 128). This is only used if *preview_type* is not
          [[`EPSPreviewImage.None_`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.None_ "tecplot.constant.EPSPreviewImage.None_"){.reference
          .internal}.

        - **preview_gray_scale_depth** ([[`int`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Gray-scale depth to use for embedded
          TIFF preview images. See documentation for the
          *gray_scale_depth* parameter in [[`save_tiff()`{.xref .any .py
          .py-func .docutils .literal
          .notranslate}]{.pre}](#tecplot.export.save_tiff "tecplot.export.save_tiff"){.reference
          .internal}. This is only used if *preview_type* is not
          [[`EPSPreviewImage.None_`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EPSPreviewImage.None_ "tecplot.constant.EPSPreviewImage.None_"){.reference
          .internal}.

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    Save an Ecapsulated PostScript image of the active frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_eps('image.eps')
    :::
    ::::
:::

::: {#export-save-jpeg .section}
### [export.save_jpeg()](#id42){.toc-backref role="doc-backlink"}[¶](#export-save-jpeg "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_jpeg]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[encoding]{.pre}]{.n}[[=]{.pre}]{.o}[[JPEGEncoding.Standard]{.pre}]{.default_value}*, *[[quality]{.pre}]{.n}[[=]{.pre}]{.o}[[75]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_jpeg){.reference .internal}[¶](#tecplot.export.save_jpeg "Link to this definition"){.headerlink}

:   Save a [JPEG image](https://en.wikipedia.org/wiki/JPEG){.reference
    .external}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Specify a width in pixels for the generated
          image. A larger width increases the quality of your image.
          However, the greater the width, the longer it will take to
          export the image, and the larger the exported file. (default:
          **800**)

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of antialiasing
          used in the image. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of image output
          formats by the process of supersampling. Some graphics cards
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **encoding** ([[`JPEGEncoding`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding "tecplot.constant.JPEGEncoding"){.reference
          .internal}, optional) --

          file which may be one of the following: \*
          [[`JPEGEncoding.Standard`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding.Standard "tecplot.constant.JPEGEncoding.Standard"){.reference
          .internal} Creates a JPEG which downloads one line at a time,
          starting at the top line. \*
          [[`JPEGEncoding.Progressive`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding.Progressive "tecplot.constant.JPEGEncoding.Progressive"){.reference
          .internal} Creates a JPEG image that can be displayed with a
          "fade in" effect in a browser. This is sometimes useful when
          viewing the JPEG in a browser with a slow connection, since it
          allows an approximation of the JPEG to be drawn immediately,
          and the browser does not have to wait for the entire image to
          download.

          (default: [[`JPEGEncoding.Standard`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding.Standard "tecplot.constant.JPEGEncoding.Standard"){.reference
          .internal})

        - **quality** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} 1-100, optional) -- Higher quality settings produce
          larger files and better looking export images. Lower quality
          settings produce smaller files. For best results, use a
          quality setting of **75** or higher. (default: **75**)

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    If exporting is taking an unusually long time, or you get an error
    message saying that the image cannot be exported, the most likely
    cause is that the image width you are trying to export is too large.
    Selecting a smaller image width will greatly speed up the export
    process. For an image export size of Length x Width, the file size
    for an uncompressed true color image is approximately Length x Width
    x 3. Memory requirements to export such an image can be up to twice
    this size. For 256-color images, the maximum file size is
    approximately Length x Width, but is usually less since all
    256-color image files are compressed. However, the memory
    requirements for exporting are the same as they are for a true color
    uncompressed image.
    :::

    Create a new [[`frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} and save a JPEG image of the frame with quality **50**
    and supersampling:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame = tecplot.active_page().add_frame()
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_jpeg('image.jpeg', width=600, supersample=3,
        ...                         region=frame, quality=50)
    :::
    ::::
:::

::: {#export-save-png .section}
### [export.save_png()](#id43){.toc-backref role="doc-backlink"}[¶](#export-save-png "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_png]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[convert_to_256_colors]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_png){.reference .internal}[¶](#tecplot.export.save_png "Link to this definition"){.headerlink}

:   Save a [PNG
    image](https://en.wikipedia.org/wiki/Portable_Network_Graphics){.reference
    .external}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Specify a width in pixels for the generated
          image. A larger width increases the quality of your image.
          However, the greater the width, the longer it will take to
          export the image, and the larger the exported file. (default:
          **800**)

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of antialiasing
          used in the image. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of image output
          formats by the process of supersampling. Some graphics cards
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **convert_to_256_colors** ([[`Boolean`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Pass [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} to generate an image with no more than 256 colors
          (reduced from a possible 16 million colors). Tecplot 360
          selects the best color match. The image will have a greatly
          reduced file size, but for plots with many colors, the results
          may be suboptimal. If this option is used with transparency,
          smooth color gradations, or antialiasing may result in poor
          image quality. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    If exporting is taking an unusually long time, or you get an error
    message saying that the image cannot be exported, the most likely
    cause is that the image width you are trying to export is too large.
    Selecting a smaller image width will greatly speed up the export
    process. For an image export size of Length x Width, the file size
    for an uncompressed true color image is approximately Length x Width
    x 3. Memory requirements to export such an image can be up to twice
    this size. For 256-color images, the maximum file size is
    approximately Length x Width, but is usually less since all
    256-color image files are compressed. However, the memory
    requirements for exporting are the same as they are for a true color
    uncompressed image.
    :::

    Save a PNG image of the entire workspace with supersampling:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ExportRegion
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_png('image.png', width=600, supersample=3,
        ...                         region=ExportRegion.WorkArea)
    :::
    ::::
:::

::: {#export-save-ps .section}
### [export.save_ps()](#id44){.toc-backref role="doc-backlink"}[¶](#export-save-ps "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_ps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[palette]{.pre}]{.n}[[=]{.pre}]{.o}[[Palette.Color]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[force_extra_3d_sorting]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[extra_precision]{.pre}]{.n}[[=]{.pre}]{.o}[[0]{.pre}]{.default_value}*, *[[render_type]{.pre}]{.n}[[=]{.pre}]{.o}[[PrintRenderType.Vector]{.pre}]{.default_value}*, *[[resolution]{.pre}]{.n}[[=]{.pre}]{.o}[[150]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_ps){.reference .internal}[¶](#tecplot.export.save_ps "Link to this definition"){.headerlink}

:   Save a [PostScript
    image](https://en.wikipedia.org/wiki/PostScript){.reference
    .external}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **palette** ([[`Palette`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette "tecplot.constant.Palette"){.reference
          .internal}, optional) -- Export color image. (default:
          [[`Palette.Color`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette.Color "tecplot.constant.Palette.Color"){.reference
          .internal})

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **force_extra_3d_sorting** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Force extra sorting for all 3D
          frames. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **extra_precision** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Additional digits for all numbers
          written to postscript file. (default: 0)

        - **render_type** ([[`PrintRenderType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType "tecplot.constant.PrintRenderType"){.reference
          .internal}, optional) -- Whether to render the postscript as a
          rasterized or vector image. (default:
          [[`PrintRenderType.Vector`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType.Vector "tecplot.constant.PrintRenderType.Vector"){.reference
          .internal})

        - **resolution** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Resolution of the image in dots per inch.
          Larger values create more accurate plots, but result in larger
          file sizes. Note: this value is ignored if
          [[`PrintRenderType`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType "tecplot.constant.PrintRenderType"){.reference
          .internal} is [[`PrintRenderType.Vector`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PrintRenderType.Vector "tecplot.constant.PrintRenderType.Vector"){.reference
          .internal} (default: **150**)

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    Save a PostScript image of the active frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_ps('image.ps')
    :::
    ::::
:::

::: {#export-save-tiff .section}
### [export.save_tiff()](#id45){.toc-backref role="doc-backlink"}[¶](#export-save-tiff "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_tiff]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[convert_to_256_colors]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[gray_scale_depth]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[byte_order]{.pre}]{.n}[[=]{.pre}]{.o}[[TIFFByteOrder.Intel]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_tiff){.reference .internal}[¶](#tecplot.export.save_tiff "Link to this definition"){.headerlink}

:   Save a [TIFF image](https://en.wikipedia.org/wiki/TIFF){.reference
    .external}.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}) -- Specify a width in pixels for the generated
          image. A larger width increases the quality of your image.
          However, the greater the width, the longer it will take to
          export the image, and the larger the exported file. (default:
          **800**)

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of antialiasing
          used in the image. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of image output
          formats by the process of supersampling. Some graphics cards
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **convert_to_256_colors** ([[`Boolean`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Pass [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} to generate an image with no more than 256 colors
          (reduced from a possible 16 million colors). Tecplot 360
          selects the best color match. The image will have a greatly
          reduced file size, but for plots with many colors, the results
          may be suboptimal. If this option is used with transparency,
          smooth color gradations, or antialiasing may result in poor
          image quality. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **gray_scale_depth** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) --

          The [`gray_scale_depth`{.docutils .literal
          .notranslate}]{.pre} parameter may be set to a depth of
          **1-8**

          [`gray_scale_depth`{.docutils .literal .notranslate}]{.pre}
          specifies the number of shades of gray by how many bits of
          gray scale information is used per pixel. The larger the
          number of bits per pixel, the larger the resulting file.

          Options are: \* **0**: On/Off One bit per pixel using an
          on/off strategy. All background pixels are made white (on),
          and all foreground pixels, black (off). This setting creates
          small files and is good for images with lots of background,
          such as line plots and contour lines. \* **1**: 1 Bit per
          Pixel One bit per pixel using gray scale values of pixels to
          determine black or white. Those pixels that are more than 50
          percent gray are black; the rest are white. This setting
          creates small files that might be useful for a rough draft or
          a preview image. \* **4**: 4 Bits per Pixel Four bits per
          pixel resulting in sixteen levels of gray scale. This setting
          generates fairly small image files with a fair number of gray
          levels. This setting works well for most preview image
          purposes. \* **8**: 8 Bits per Pixel Eight bits per pixel
          resulting in 256 levels of gray. This setting is useful for
          full image representation, but the files generated by this
          setting can be large.

          (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **byte_order** ([[`TIFFByteOrder`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TIFFByteOrder "tecplot.constant.TIFFByteOrder"){.reference
          .internal}, optional) -- (Intel or Motorola) of the TIFF
          image. (Default: [[`TIFFByteOrder.Intel`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TIFFByteOrder.Intel "tecplot.constant.TIFFByteOrder.Intel"){.reference
          .internal})

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    If exporting is taking an unusually long time, or you get an error
    message saying that the image cannot be exported, the most likely
    cause is that the image width you are trying to export is too large.
    Selecting a smaller image width will greatly speed up the export
    process. For an image export size of Length x Width, the file size
    for an uncompressed true color image is approximately Length x Width
    x 3. Memory requirements to export such an image can be up to twice
    this size. For 256-color images, the maximum file size is
    approximately Length x Width, but is usually less since all
    256-color image files are compressed. However, the memory
    requirements for exporting are the same as they are for a true color
    uncompressed image.
    :::

    Save a 4-bit gray scale TIFF image of the entire workspace with
    supersampling:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ExportRegion
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_tiff('image.tiff', width=600, supersample=2,
        >>>                         region=ExportRegion.WorkArea,
        >>>                         gray_scale_depth=4)
    :::
    ::::
:::

::: {#export-save-wmf .section}
### [export.save_wmf()](#id46){.toc-backref role="doc-backlink"}[¶](#export-save-wmf "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_wmf]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[palette]{.pre}]{.n}[[=]{.pre}]{.o}[[Palette.Color]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[force_extra_3d_sorting]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/image.html#save_wmf){.reference .internal}[¶](#tecplot.export.save_wmf "Link to this definition"){.headerlink}

:   Save a Windows Metafile image

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- filename with or without extension. (See note
          below concerning absolute and relative paths.)

        - **palette** ([[`Palette`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette "tecplot.constant.Palette"){.reference
          .internal}, optional) -- Export color image. (default:
          [[`Palette.Color`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette.Color "tecplot.constant.Palette.Color"){.reference
          .internal}) Note: [[`Palette.PenPlotter`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Palette.PenPlotter "tecplot.constant.Palette.PenPlotter"){.reference
          .internal} cannot be used.

        - **region** ([[`frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- If [`region`{.docutils .literal
          .notranslate}]{.pre} is a [[`frame`{.xref .any .py .py-class
          .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
          .py-class .docutils .literal .notranslate}[`object`{.xref .any
          .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal}, then the contents of the frame will be exported.
          If region is [[`ExportRegion.CurrentFrame`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, then the contents of the currently active frame
          will be exported. If region is
          [[`ExportRegion.AllFrames`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal}, then the smallest rectangle containing all frames
          will be exported. If region is [[`ExportRegion.WorkArea`{.xref
          .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}, then everything shown in the workspace will be
          exported. (default: [[`ExportRegion.AllFrames`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal})

        - **force_extra_3d_sorting** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Force extra sorting for all 3D
          frames. (default: [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    Raises[:]{.colon}

    :   [**TecplotSystemError**](tecplot.exceptions.html#tecplot.exception.TecplotSystemError "tecplot.exception.TecplotSystemError"){.reference
        .internal} -- The image could not be saved due to a file I/O
        error or invalid attribute.

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

    WMF (Windows Metafile) is a Microsoft vector graphics format widely
    accepted by Windows applications. Since WMFs are vector graphics,
    they can be easily resized by the importing application without the
    introduction of visual artifacts, but they cannot accurately
    represent plots with translucency or smooth color gradations
    :::

    Save a WMF image of the active frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.load_layout('mylayout.lay')
        >>> tecplot.export.save_wmf('image.wmf')
    :::
    ::::
:::
::::::::::

:::::::::::::::::: {#exporting-video .section}
## [Exporting Video](#id24){.toc-backref role="doc-backlink"}[¶](#exporting-video "Link to this heading"){.headerlink}

- [export.animation_avi()](#export-animation-avi){#id47 .reference
  .internal}

- [export.animation_mpeg4()](#export-animation-mpeg4){#id48 .reference
  .internal}

- [export.animation_wmv()](#export-animation-wmv){#id49 .reference
  .internal}

- [export.animation_flash()](#export-animation-flash){#id50 .reference
  .internal}

- [export.animation_raster_metafile()](#export-animation-raster-metafile){#id51
  .reference .internal}

- [export.animation.animation.export_animation_frame()](#export-animation-animation-export-animation-frame){#id52
  .reference .internal}

- [export.save_time_animation_avi()](#export-save-time-animation-avi){#id53
  .reference .internal}

- [export.save_time_animation_mpeg4()](#export-save-time-animation-mpeg4){#id54
  .reference .internal}

- [export.save_time_animation_wmv()](#export-save-time-animation-wmv){#id55
  .reference .internal}

- [export.save_time_animation_flash()](#export-save-time-animation-flash){#id56
  .reference .internal}

- [export.save_time_animation_raster_metafile()](#export-save-time-animation-raster-metafile){#id57
  .reference .internal}

- [export.save_time_animation_bmp()](#export-save-time-animation-bmp){#id58
  .reference .internal}

- [export.save_time_animation_jpeg()](#export-save-time-animation-jpeg){#id59
  .reference .internal}

- [export.save_time_animation_png()](#export-save-time-animation-png){#id60
  .reference .internal}

- [export.save_time_animation_tiff()](#export-save-time-animation-tiff){#id61
  .reference .internal}

::: {#export-animation-avi .section}
### [export.animation_avi()](#id47){.toc-backref role="doc-backlink"}[¶](#export-animation-avi "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[animation_avi]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[compression]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[multiple_color_tables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[format_options]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/animation.html#animation_avi){.reference .internal}[¶](#tecplot.export.animation_avi "Link to this definition"){.headerlink}

:   Frame-by-frame AVI animation context.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **format_options** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) -- A string of options passed directly
          to the underlying application
          [FFmpeg](https://www.ffmpeg.org/){.reference .external}. By
          default, this will be "-vcodec mjpeg -q:v 5".

    This is a [context
    manager](https://docs.python.org/3/reference/datamodel.html#context-managers){.reference
    .external} and must be invoked using the
    [with](https://docs.python.org/3/reference/compound_stmts.html#with){.reference
    .external} statement. The returned object of the context manager is
    used to control when each frame of the video is captured. This is
    done using the context method
    [[`animation.export_animation_frame()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation.animation.export_animation_frame "tecplot.export.animation.animation.export_animation_frame"){.reference
    .internal} as shown in the example below, at which point the
    specified region or plot is rendered. The actual video file is
    produced upon exit of the context.

    Typical code looks like the following (see the example under
    [[`animation_mpeg4`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation_mpeg4 "tecplot.export.animation_mpeg4"){.reference
    .internal} for a complete working example):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> with tp.export.animation_avi('output.avi') as ani:
        ...     # make some view changes here
        ...     ani.export_animation_frame()
    :::
    ::::
:::

::: {#export-animation-mpeg4 .section}
### [export.animation_mpeg4()](#id48){.toc-backref role="doc-backlink"}[¶](#export-animation-mpeg4 "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[animation_mpeg4]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[format_options]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/animation.html#animation_mpeg4){.reference .internal}[¶](#tecplot.export.animation_mpeg4 "Link to this definition"){.headerlink}

:   Frame-by-frame MPEG4 animation context.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **format_options** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) --

          A string of options passed directly to the underlying
          application [FFmpeg](https://www.ffmpeg.org/){.reference
          .external}. By default, this will be "-c:v libx264 -profile:v
          high -crf 20 -pix_fmt yuv420p".

    This is a [context
    manager](https://docs.python.org/3/reference/datamodel.html#context-managers){.reference
    .external} and must be invoked using the
    [with](https://docs.python.org/3/reference/compound_stmts.html#with){.reference
    .external} statement. The returned object of the context manager is
    used to control when each frame of the video is captured. This is
    done using the context method
    [[`animation.export_animation_frame()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation.animation.export_animation_frame "tecplot.export.animation.animation.export_animation_frame"){.reference
    .internal} as shown in the example below, at which point the
    specified region or plot is rendered. The actual video file is
    produced upon exit of the context.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import argparse, os

        import tecplot as tp
        from tecplot.constant import *

        def parse_args():
            """
            This script is to be run from the command line and accepts the
            following command line arguments. Run this script with "--help"
            to see usage and help information.
            """
            parser = argparse.ArgumentParser()
            parser.add_argument('-c', '--connect', action='store_true',
                                help='connect to TecUtil Server')
            parser.add_argument('-p', '--port', type=int, default=7600,
                                help='port to use when connecting to TecUtil Server')
            parser.add_argument('-n', '--nframes', type=int, default=360,
                                help='number of frames to produce in video')
            parser.add_argument('outfile', nargs='?', default='aileron_roll.mp4',
                                help='output file name')
            return parser.parse_args()

        def setup_plot():
            """
            Load the F-18 dataset from Tecplot 360's examples and show the
            jet surface in 3D.
            """
            tp.new_layout()
            exdir = tp.session.tecplot_examples_directory()
            datafile = os.path.join(exdir, 'SimpleData', 'F18.plt')
            ds = tp.data.load_tecplot(datafile)

            frame = tp.active_frame()
            frame.show_border = False
            plot = frame.plot(PlotType.Cartesian3D)
            plot.activate()

            plot.contour(0).variable = ds.variable('S')
            plot.show_contour = True
            return plot

        def translate_view(view, x=0, y=0, z=0):
            """
            Translate the viewer with respect to the data.
            """
            p = view.position
            view.position = p.x + x, p.y + y, p.z + z

        def create_animation(outfile, plot, nframes):
            """
            Using the tp.export.animation_mpeg4() context manager, the F-18 is
            recorded doing an "aileron roll" by rotating and translating the
            viewer with respect to the data by a small amount and capturing
            each frame of the animation with a call to ani.export_animation_frame()
            """
            with tp.session.suspend():
                opts = dict(
                    width=400,
                    animation_speed=30,
                    supersample=3,
                )
                view = plot.view
                translate_view(view, -15)
                with tp.export.animation_mpeg4(outfile, **opts) as ani:
                  for i in range(args.nframes):
                    view.rotate_axes(5, (1, 0, 0))
                    translate_view(view, 30 / args.nframes)
                    ani.export_animation_frame()

        """
        This script is meant to run on the command line. Run with "--help" to see
        usage and help information about the options it understands. It loads
        the F-18 dataset from Tecplot 360's examples directory and produces a
        video of the model doing an "aileron roll" by manipulating the viewer
        position.
        """
        args = parse_args()
        if args.connect:
            tp.session.connect(port=args.port)
        plot = setup_plot()
        create_animation(args.outfile, plot, args.nframes)
        print('video file created:', args.outfile)
    :::
    ::::

    I\'m sorry; your browser doesn\'t support HTML5 MPEG4/H.264 video.
:::

::: {#export-animation-wmv .section}
### [export.animation_wmv()](#id49){.toc-backref role="doc-backlink"}[¶](#export-animation-wmv "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[animation_wmv]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[format_options]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/animation.html#animation_wmv){.reference .internal}[¶](#tecplot.export.animation_wmv "Link to this definition"){.headerlink}

:   Frame-by-frame WMV animation context.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **format_options** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) --

          A string of options passed directly to the underlying
          application [FFmpeg](https://www.ffmpeg.org/){.reference
          .external}. By default, this will be "-qscale 4".

    This is a [context
    manager](https://docs.python.org/3/reference/datamodel.html#context-managers){.reference
    .external} and must be invoked using the
    [with](https://docs.python.org/3/reference/compound_stmts.html#with){.reference
    .external} statement. The returned object of the context manager is
    used to control when each frame of the video is captured. This is
    done using the context method
    [[`animation.export_animation_frame()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation.animation.export_animation_frame "tecplot.export.animation.animation.export_animation_frame"){.reference
    .internal} as shown in the example below, at which point the
    specified region or plot is rendered. The actual video file is
    produced upon exit of the context.

    Typical code looks like the following (see the example under
    [[`animation_mpeg4`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation_mpeg4 "tecplot.export.animation_mpeg4"){.reference
    .internal} for a complete working example):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> with tp.export.animation_wmv('output.wmv') as ani:
        ...     # make some view changes here
        ...     ani.export_animation_frame()
    :::
    ::::
:::

::: {#export-animation-flash .section}
### [export.animation_flash()](#id50){.toc-backref role="doc-backlink"}[¶](#export-animation-flash "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[animation_flash]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[compression]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[image_type]{.pre}]{.n}[[=]{.pre}]{.o}[[FlashImageType.Lossless]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/animation.html#animation_flash){.reference .internal}[¶](#tecplot.export.animation_flash "Link to this definition"){.headerlink}

:   Frame-by-frame Flash animation context.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **compression** ([[`FlashCompressionType`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashCompressionType "tecplot.constant.FlashCompressionType"){.reference
          .internal}, optional) -- The compression scheme to use when
          creating the video stream. Options are:
          [[`FlashCompressionType.BestSpeed`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashCompressionType.BestSpeed "tecplot.constant.FlashCompressionType.BestSpeed"){.reference
          .internal} (default) and
          [[`FlashCompressionType.SmallestSize`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashCompressionType.SmallestSize "tecplot.constant.FlashCompressionType.SmallestSize"){.reference
          .internal}.

        - **image_type** ([[`FlashImageType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType "tecplot.constant.FlashImageType"){.reference
          .internal}, optional) -- The type of images to generate for
          each frame of the animation. Options are:
          [[`FlashImageType.Color256`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType.Color256 "tecplot.constant.FlashImageType.Color256"){.reference
          .internal}, [[`FlashImageType.JPEG`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType.JPEG "tecplot.constant.FlashImageType.JPEG"){.reference
          .internal} and [[`FlashImageType.Lossless`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType.Lossless "tecplot.constant.FlashImageType.Lossless"){.reference
          .internal} (default).

    This is a [context
    manager](https://docs.python.org/3/reference/datamodel.html#context-managers){.reference
    .external} and must be invoked using the
    [with](https://docs.python.org/3/reference/compound_stmts.html#with){.reference
    .external} statement. The returned object of the context manager is
    used to control when each frame of the video is captured. This is
    done using the context method
    [[`animation.export_animation_frame()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation.animation.export_animation_frame "tecplot.export.animation.animation.export_animation_frame"){.reference
    .internal} as shown in the example below, at which point the
    specified region or plot is rendered. The actual video file is
    produced upon exit of the context.

    Typical code looks like the following (see the example under
    [[`animation_mpeg4`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation_mpeg4 "tecplot.export.animation_mpeg4"){.reference
    .internal} for a complete working example):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> with tp.export.animation_flash('output.flv') as ani:
        ...     # make some view changes here
        ...     ani.export_animation_frame()
    :::
    ::::
:::

::: {#export-animation-raster-metafile .section}
### [export.animation_raster_metafile()](#id51){.toc-backref role="doc-backlink"}[¶](#export-animation-raster-metafile "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[animation_raster_metafile]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[multiple_color_tables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/animation.html#animation_raster_metafile){.reference .internal}[¶](#tecplot.export.animation_raster_metafile "Link to this definition"){.headerlink}

:   Frame-by-frame Raster Metafile animation context.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **multiple_color_tables** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Create a color table for each frame
          of the animation. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external} (default), the whole animation will be scanned in
          an attempt to create a single table of 256 colors.

    This is a [context
    manager](https://docs.python.org/3/reference/datamodel.html#context-managers){.reference
    .external} and must be invoked using the
    [with](https://docs.python.org/3/reference/compound_stmts.html#with){.reference
    .external} statement. The returned object of the context manager is
    used to control when each frame of the video is captured. This is
    done using the context method
    [[`animation.export_animation_frame()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation.animation.export_animation_frame "tecplot.export.animation.animation.export_animation_frame"){.reference
    .internal} as shown in the example below, at which point the
    specified region or plot is rendered. The actual video file is
    produced upon exit of the context.

    Typical code looks like the following (see the example under
    [[`animation_mpeg4`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation_mpeg4 "tecplot.export.animation_mpeg4"){.reference
    .internal} for a complete working example):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> with tp.export.animation_raster_metafile('output.rm') as ani:
        ...     # make some view changes here
        ...     ani.export_animation_frame()
    :::
    ::::
:::

::: {#export-animation-animation-export-animation-frame .section}
### [export.animation.animation.export_animation_frame()](#id52){.toc-backref role="doc-backlink"}[¶](#export-animation-animation-export-animation-frame "Link to this heading"){.headerlink}

[[tecplot.export.animation.animation.]{.pre}]{.sig-prename .descclassname}[[export_animation_frame]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[self]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.export.animation.animation.export_animation_frame "Link to this definition"){.headerlink}

:   Append a frame to the current animation.

    This function is available as a method on the object returned by the
    animation contexts:

    > <div>
    >
    > - [[`animation_avi`{.xref .any .py .py-func .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.export.animation_avi "tecplot.export.animation_avi"){.reference
    >   .internal}
    >
    > - [[`animation_flash`{.xref .any .py .py-func .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.export.animation_flash "tecplot.export.animation_flash"){.reference
    >   .internal}
    >
    > - [[`animation_mpeg4`{.xref .any .py .py-func .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.export.animation_mpeg4 "tecplot.export.animation_mpeg4"){.reference
    >   .internal}
    >
    > - [[`animation_raster_metafile`{.xref .any .py .py-func .docutils
    >   .literal
    >   .notranslate}]{.pre}](#tecplot.export.animation_raster_metafile "tecplot.export.animation_raster_metafile"){.reference
    >   .internal}
    >
    > - [[`animation_wmv`{.xref .any .py .py-func .docutils .literal
    >   .notranslate}]{.pre}](#tecplot.export.animation_wmv "tecplot.export.animation_wmv"){.reference
    >   .internal}
    >
    > </div>

    It instructs Tecplot 360 to capture the current state of the plot or
    workspace (see the *region* parameter in the contexts above) as a
    single frame in the resulting animation. Typical usage is to make
    small changes to the plot, calling
    [[`animation.export_animation_frame()`{.xref .any .py .py-func
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation.animation.export_animation_frame "tecplot.export.animation.animation.export_animation_frame"){.reference
    .internal} after each change to create a smooth transition from one
    view to another. For a detailed example, see
    [[`animation_mpeg4`{.xref .any .py .py-func .docutils .literal
    .notranslate}]{.pre}](#tecplot.export.animation_mpeg4 "tecplot.export.animation_mpeg4"){.reference
    .internal}. The following example is an excerpt from the MPEG-4
    example code:

    :::: {.highlight-python .notranslate}
    ::: highlight
        with tp.export.animation_mpeg4(outfile, **opts) as ani:
            for i in range(args.nframes):
                view.rotate_axes(5, (1, 0, 0))
                translate_view(view, 30 / args.nframes)
                ani.export_animation_frame()
    :::
    ::::
:::

::: {#export-save-time-animation-avi .section}
### [export.save_time_animation_avi()](#id53){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-avi "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_avi]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[compression]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[multiple_color_tables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[format_options]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_avi){.reference .internal}[¶](#tecplot.export.save_time_animation_avi "Link to this definition"){.headerlink}

:   Export transient data time-series AVI animation to a file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **format_options** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) --

          A string of options passed directly to the underlying
          application [FFmpeg](https://www.ffmpeg.org/){.reference
          .external}. By default, this will be "-vcodec mjpeg -q:v 5".

    Example usage, see the example under
    [[`save_time_animation_mpeg4`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.export.save_time_animation_mpeg4 "tecplot.export.save_time_animation_mpeg4"){.reference
    .internal} for a complete working example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.export.save_time_animation_avi('output.avi')
    :::
    ::::
:::

::: {#export-save-time-animation-mpeg4 .section}
### [export.save_time_animation_mpeg4()](#id54){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-mpeg4 "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_mpeg4]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[format_options]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_mpeg4){.reference .internal}[¶](#tecplot.export.save_time_animation_mpeg4 "Link to this definition"){.headerlink}

:   Export transient data time-series MPEG-4 animation to a file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **format_options** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) --

          A string of options passed directly to the underlying
          application [FFmpeg](https://www.ffmpeg.org/){.reference
          .external}. By default, this will be "-c:v libx264 -profile:v
          high -crf 20 -pix_fmt yuv420p".

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os

        import tecplot as tp
        from tecplot.constant import *

        examples = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples, 'SimpleData', 'VortexShedding.plt')
        dataset = tp.data.load_tecplot(datafile)

        plot = tp.active_frame().plot(PlotType.Cartesian2D)
        plot.activate()
        plot.show_contour = True

        plot.axes.x_axis.min = -0.002
        plot.axes.x_axis.max = 0.012
        plot.axes.y_axis.min = -0.006
        plot.axes.y_axis.max = 0.006

        tp.export.save_time_animation_mpeg4('vortex_shedding.mp4',
                                            start_time=0, end_time=0.0006,
                                            width=400, supersample=3)
    :::
    ::::

    I\'m sorry; your browser doesn\'t support HTML5 MPEG4/H.264 video.
:::

::: {#export-save-time-animation-wmv .section}
### [export.save_time_animation_wmv()](#id55){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-wmv "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_wmv]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[format_options]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_wmv){.reference .internal}[¶](#tecplot.export.save_time_animation_wmv "Link to this definition"){.headerlink}

:   Export transient data time-series Windows Media Video (WMV) to a
    file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **format_options** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}, optional) --

          A string of options passed directly to the underlying
          application [FFmpeg](https://www.ffmpeg.org/){.reference
          .external}. By default, this will be "-qscale 4".

    Example usage, see the example under
    [[`save_time_animation_mpeg4`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.export.save_time_animation_mpeg4 "tecplot.export.save_time_animation_mpeg4"){.reference
    .internal} for a complete working example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.export.save_time_animation_wmv('output.wmv')
    :::
    ::::
:::

::: {#export-save-time-animation-flash .section}
### [export.save_time_animation_flash()](#id56){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-flash "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_flash]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[compression]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[image_type]{.pre}]{.n}[[=]{.pre}]{.o}[[FlashImageType.Lossless]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_flash){.reference .internal}[¶](#tecplot.export.save_time_animation_flash "Link to this definition"){.headerlink}

:   Export transient data time-series Flash animation to a file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **compression** ([[`FlashCompressionType`{.xref .any .py
          .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashCompressionType "tecplot.constant.FlashCompressionType"){.reference
          .internal}, optional) -- The compression scheme to use when
          creating the video stream. Options are:
          [[`FlashCompressionType.BestSpeed`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashCompressionType.BestSpeed "tecplot.constant.FlashCompressionType.BestSpeed"){.reference
          .internal} (default) and
          [[`FlashCompressionType.SmallestSize`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashCompressionType.SmallestSize "tecplot.constant.FlashCompressionType.SmallestSize"){.reference
          .internal}.

        - **image_type** ([[`FlashImageType`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType "tecplot.constant.FlashImageType"){.reference
          .internal}, optional) -- The type of images to generate for
          each frame of the animation. Options are:
          [[`FlashImageType.Color256`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType.Color256 "tecplot.constant.FlashImageType.Color256"){.reference
          .internal}, [[`FlashImageType.JPEG`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType.JPEG "tecplot.constant.FlashImageType.JPEG"){.reference
          .internal} and [[`FlashImageType.Lossless`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FlashImageType.Lossless "tecplot.constant.FlashImageType.Lossless"){.reference
          .internal} (default).

    Example usage, see the example under
    [[`save_time_animation_mpeg4`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.export.save_time_animation_mpeg4 "tecplot.export.save_time_animation_mpeg4"){.reference
    .internal} for a complete working example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.export.save_time_animation_flash('output.flv')
    :::
    ::::
:::

::: {#export-save-time-animation-raster-metafile .section}
### [export.save_time_animation_raster_metafile()](#id57){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-raster-metafile "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_raster_metafile]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[animation_speed]{.pre}]{.n}[[=]{.pre}]{.o}[[10]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[multiple_color_tables]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_raster_metafile){.reference .internal}[¶](#tecplot.export.save_time_animation_raster_metafile "Link to this definition"){.headerlink}

:   Export transient data time-series Raster Metafile animation to a
    file.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- The resulting video file name or path, relative
          to Python's current working directory.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **animation_speed** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The frame-rate of the video in frames
          per second. (default: 10)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **multiple_color_tables** ([[`bool`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Create a color table for each frame
          of the animation. If [[`False`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external} (default), the whole animation will be scanned in
          an attempt to create a single table of 256 colors.

    Example usage, see the example under
    [[`save_time_animation_mpeg4`{.xref .any .py .py-func .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.export.save_time_animation_mpeg4 "tecplot.export.save_time_animation_mpeg4"){.reference
    .internal} for a complete working example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tp.export.save_time_animation_raster_metafile('output.rm')
    :::
    ::::
:::

::: {#export-save-time-animation-bmp .section}
### [export.save_time_animation_bmp()](#id58){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-bmp "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_bmp]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[convert_to_256_colors]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_bmp){.reference .internal}[¶](#tecplot.export.save_time_animation_bmp "Link to this definition"){.headerlink}

:   Export transient data time-series animation as BMP image files.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Each frame of the animation will be exported to
          image files that will include and underscore followed by the
          frame number padded to six digits with zeros just before the
          last period. For example, a **filename** of
          [`img.ext`{.docutils .literal .notranslate}]{.pre} that
          exports three frames will create the files:
          [`img_000001.ext`{.docutils .literal .notranslate}]{.pre},
          [`img_000002.ext`{.docutils .literal .notranslate}]{.pre} and
          [`img_000003.ext`{.docutils .literal .notranslate}]{.pre}.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **convert_to_256_colors** ([[`Boolean`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Pass [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} to generate an image with no more than 256 colors
          (reduced from a possible 16 million colors). Tecplot 360
          selects the best color match. The image will have a greatly
          reduced file size, but for plots with many colors, the results
          may be suboptimal. If this option is used with transparency,
          smooth color gradations, or antialiasing may result in poor
          image quality. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    The following example will create a series of image files named
    [`img_000001.bmp`{.docutils .literal .notranslate}]{.pre},
    [`img_000002.bmp`{.docutils .literal .notranslate}]{.pre}, etc.:

    :::: {.highlight-python .notranslate}
    ::: highlight
        tp.export.save_time_animation_bmp('img.bmp')
    :::
    ::::

    ::: versionadded
    [New in version 2018.2: ]{.versionmodified .added}Exporting
    animations as images requires Tecplot 360 2018 R2 or later.
    :::
:::

::: {#export-save-time-animation-jpeg .section}
### [export.save_time_animation_jpeg()](#id59){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-jpeg "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_jpeg]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[encoding]{.pre}]{.n}[[=]{.pre}]{.o}[[JPEGEncoding.Standard]{.pre}]{.default_value}*, *[[quality]{.pre}]{.n}[[=]{.pre}]{.o}[[75]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_jpeg){.reference .internal}[¶](#tecplot.export.save_time_animation_jpeg "Link to this definition"){.headerlink}

:   Export transient data time-series animation as JPEG image files.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Each frame of the animation will be exported to
          image files that will include and underscore followed by the
          frame number padded to six digits with zeros just before the
          last period. For example, a **filename** of
          [`img.ext`{.docutils .literal .notranslate}]{.pre} that
          exports three frames will create the files:
          [`img_000001.ext`{.docutils .literal .notranslate}]{.pre},
          [`img_000002.ext`{.docutils .literal .notranslate}]{.pre} and
          [`img_000003.ext`{.docutils .literal .notranslate}]{.pre}.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **encoding** ([[`JPEGEncoding`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding "tecplot.constant.JPEGEncoding"){.reference
          .internal}, optional) --

          file which may be one of the following: \*
          [[`JPEGEncoding.Standard`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding.Standard "tecplot.constant.JPEGEncoding.Standard"){.reference
          .internal} Creates a JPEG which downloads one line at a time,
          starting at the top line. \*
          [[`JPEGEncoding.Progressive`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding.Progressive "tecplot.constant.JPEGEncoding.Progressive"){.reference
          .internal} Creates a JPEG image that can be displayed with a
          "fade in" effect in a browser. This is sometimes useful when
          viewing the JPEG in a browser with a slow connection, since it
          allows an approximation of the JPEG to be drawn immediately,
          and the browser does not have to wait for the entire image to
          download.

          (default: [[`JPEGEncoding.Standard`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.JPEGEncoding.Standard "tecplot.constant.JPEGEncoding.Standard"){.reference
          .internal})

        - **quality** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external} 1-100, optional) -- Higher quality settings produce
          larger files and better looking export images. Lower quality
          settings produce smaller files. For best results, use a
          quality setting of **75** or higher. (default: **75**)

    The following example will create a series of image files named
    [`img_000001.jpeg`{.docutils .literal .notranslate}]{.pre},
    [`img_000002.jpeg`{.docutils .literal .notranslate}]{.pre}, etc.:

    :::: {.highlight-python .notranslate}
    ::: highlight
        tp.export.save_time_animation_jpeg('img.jpeg')
    :::
    ::::

    ::: versionadded
    [New in version 2018.2: ]{.versionmodified .added}Exporting
    animations as images requires Tecplot 360 2018 R2 or later.
    :::
:::

::: {#export-save-time-animation-png .section}
### [export.save_time_animation_png()](#id60){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-png "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_png]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[convert_to_256_colors]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_png){.reference .internal}[¶](#tecplot.export.save_time_animation_png "Link to this definition"){.headerlink}

:   Export transient data time-series animation as PNG image files.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Each frame of the animation will be exported to
          image files that will include and underscore followed by the
          frame number padded to six digits with zeros just before the
          last period. For example, a **filename** of
          [`img.ext`{.docutils .literal .notranslate}]{.pre} that
          exports three frames will create the files:
          [`img_000001.ext`{.docutils .literal .notranslate}]{.pre},
          [`img_000002.ext`{.docutils .literal .notranslate}]{.pre} and
          [`img_000003.ext`{.docutils .literal .notranslate}]{.pre}.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **convert_to_256_colors** ([[`Boolean`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Pass [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} to generate an image with no more than 256 colors
          (reduced from a possible 16 million colors). Tecplot 360
          selects the best color match. The image will have a greatly
          reduced file size, but for plots with many colors, the results
          may be suboptimal. If this option is used with transparency,
          smooth color gradations, or antialiasing may result in poor
          image quality. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

    The following example will create a series of image files named
    [`img_000001.png`{.docutils .literal .notranslate}]{.pre},
    [`img_000002.png`{.docutils .literal .notranslate}]{.pre}, etc.:

    :::: {.highlight-python .notranslate}
    ::: highlight
        tp.export.save_time_animation_png('img.png')
    :::
    ::::

    ::: versionadded
    [New in version 2018.2: ]{.versionmodified .added}Exporting
    animations as images requires Tecplot 360 2018 R2 or later.
    :::
:::

::: {#export-save-time-animation-tiff .section}
### [export.save_time_animation_tiff()](#id61){.toc-backref role="doc-backlink"}[¶](#export-save-time-animation-tiff "Link to this heading"){.headerlink}

[[tecplot.export.]{.pre}]{.sig-prename .descclassname}[[save_time_animation_tiff]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[filename]{.pre}]{.n}*, *[[start_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[end_time]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[timestep_step]{.pre}]{.n}[[=]{.pre}]{.o}[[1]{.pre}]{.default_value}*, *[[width]{.pre}]{.n}[[=]{.pre}]{.o}[[800]{.pre}]{.default_value}*, *[[region]{.pre}]{.n}[[=]{.pre}]{.o}[[ExportRegion.AllFrames]{.pre}]{.default_value}*, *[[supersample]{.pre}]{.n}[[=]{.pre}]{.o}[[3]{.pre}]{.default_value}*, *[[convert_to_256_colors]{.pre}]{.n}[[=]{.pre}]{.o}[[False]{.pre}]{.default_value}*, *[[gray_scale_depth]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[byte_order]{.pre}]{.n}[[=]{.pre}]{.o}[[TIFFByteOrder.Intel]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/export/time_animation.html#save_time_animation_tiff){.reference .internal}[¶](#tecplot.export.save_time_animation_tiff "Link to this definition"){.headerlink}

:   Export transient data time-series animation as TIFF image files.

    Parameters[:]{.colon}

    :   - **filename** ([[`pathlib.Path`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
          .external} or [[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Each frame of the animation will be exported to
          image files that will include and underscore followed by the
          frame number padded to six digits with zeros just before the
          last period. For example, a **filename** of
          [`img.ext`{.docutils .literal .notranslate}]{.pre} that
          exports three frames will create the files:
          [`img_000001.ext`{.docutils .literal .notranslate}]{.pre},
          [`img_000002.ext`{.docutils .literal .notranslate}]{.pre} and
          [`img_000003.ext`{.docutils .literal .notranslate}]{.pre}.

        - **start_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The beginning solution time of the
          animation. This defaults to the earliest solution time in the
          dataset.

        - **end_time** ([[`float`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
          .external}, optional) -- The ending solution time of the
          animation. This defaults to the latest solution time in the
          dataset.

        - **timestep_step** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The number of timesteps to increments
          for each frame of the animation. (default: 1)

        - **width** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- The width of the video in pixels.
          (default: 800)

        - **region** ([[`Frame`{.xref .any .py .py-class .docutils
          .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} or [[`ExportRegion`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion "tecplot.constant.ExportRegion"){.reference
          .internal}, optional) -- The rectangular area to be exported.
          This can be a specific [[`Frame`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
          .internal} object or one of
          [[`ExportRegion.CurrentFrame`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.CurrentFrame "tecplot.constant.ExportRegion.CurrentFrame"){.reference
          .internal}, [[`ExportRegion.AllFrames`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.AllFrames "tecplot.constant.ExportRegion.AllFrames"){.reference
          .internal} (default) or [[`ExportRegion.WorkArea`{.xref .any
          .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ExportRegion.WorkArea "tecplot.constant.ExportRegion.WorkArea"){.reference
          .internal}.

        - **supersample** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) -- Controls the amount of anti-aliasing
          used in each frame. Valid values are 1-16. A value of **1**
          indicates that no antialiasing will be used. Antialiasing
          smooths jagged edges on text, lines, and edges of the video
          output by the process of supersampling. *Some graphics cards*
          can cause Tecplot 360 to crash when larger anti-aliasing
          values are used. If this occurs on your machine, try updating
          your graphics driver or using a lower anti-aliasing value.
          (default: **3**)

        - **convert_to_256_colors** ([[`Boolean`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Pass [[`True`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external} to generate an image with no more than 256 colors
          (reduced from a possible 16 million colors). Tecplot 360
          selects the best color match. The image will have a greatly
          reduced file size, but for plots with many colors, the results
          may be suboptimal. If this option is used with transparency,
          smooth color gradations, or antialiasing may result in poor
          image quality. (default: [[`False`{.xref .any .docutils
          .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
          .external})

        - **gray_scale_depth** ([[`int`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
          .external}, optional) --

          The [`gray_scale_depth`{.docutils .literal
          .notranslate}]{.pre} parameter may be set to a depth of
          **1-8**

          [`gray_scale_depth`{.docutils .literal .notranslate}]{.pre}
          specifies the number of shades of gray by how many bits of
          gray scale information is used per pixel. The larger the
          number of bits per pixel, the larger the resulting file.

          Options are: \* **0**: On/Off One bit per pixel using an
          on/off strategy. All background pixels are made white (on),
          and all foreground pixels, black (off). This setting creates
          small files and is good for images with lots of background,
          such as line plots and contour lines. \* **1**: 1 Bit per
          Pixel One bit per pixel using gray scale values of pixels to
          determine black or white. Those pixels that are more than 50
          percent gray are black; the rest are white. This setting
          creates small files that might be useful for a rough draft or
          a preview image. \* **4**: 4 Bits per Pixel Four bits per
          pixel resulting in sixteen levels of gray scale. This setting
          generates fairly small image files with a fair number of gray
          levels. This setting works well for most preview image
          purposes. \* **8**: 8 Bits per Pixel Eight bits per pixel
          resulting in 256 levels of gray. This setting is useful for
          full image representation, but the files generated by this
          setting can be large.

          (default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external})

        - **byte_order** ([[`TIFFByteOrder`{.xref .any .py .py-class
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TIFFByteOrder "tecplot.constant.TIFFByteOrder"){.reference
          .internal}, optional) -- (Intel or Motorola) of the TIFF
          image. (Default: [[`TIFFByteOrder.Intel`{.xref .any .py
          .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TIFFByteOrder.Intel "tecplot.constant.TIFFByteOrder.Intel"){.reference
          .internal})

    The following example will create a series of image files named
    [`img_000001.tiff`{.docutils .literal .notranslate}]{.pre},
    [`img_000002.tiff`{.docutils .literal .notranslate}]{.pre}, etc.:

    :::: {.highlight-python .notranslate}
    ::: highlight
        tp.export.save_time_animation_tiff('img.tiff')
    :::
    ::::

    ::: versionadded
    [New in version 2018.2: ]{.versionmodified .added}Exporting
    animations as images requires Tecplot 360 2018 R2 or later.
    :::
:::
::::::::::::::::::
:::::::::::::::::::::::::::

::: clearer
:::
:::::::::::::::::::::::::::::
