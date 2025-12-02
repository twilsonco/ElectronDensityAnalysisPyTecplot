:::::::::::::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::::::::::::: {#axes .section}
# Axes[¶](#axes "Link to this heading"){.headerlink}

- [Field Axes](#field-axes){#id8 .reference .internal}

  - [Cartesian2DFieldAxes](#cartesian2dfieldaxes){#id9 .reference
    .internal}

  - [Cartesian2DFieldAxis](#cartesian2dfieldaxis){#id10 .reference
    .internal}

  - [Cartesian3DFieldAxes](#cartesian3dfieldaxes){#id11 .reference
    .internal}

  - [Cartesian3DFieldAxis](#cartesian3dfieldaxis){#id12 .reference
    .internal}

- [Line Axes](#line-axes){#id13 .reference .internal}

  - [XYLineAxes](#xylineaxes){#id14 .reference .internal}

  - [XYLineAxis](#xylineaxis){#id15 .reference .internal}

  - [PolarLineAxes](#polarlineaxes){#id16 .reference .internal}

  - [RadialLineAxis](#radiallineaxis){#id17 .reference .internal}

  - [PolarAngleLineAxis](#polaranglelineaxis){#id18 .reference
    .internal}

- [Sketch Axes](#sketch-axes){#id19 .reference .internal}

  - [SketchAxes](#sketchaxes){#id20 .reference .internal}

  - [SketchAxis](#sketchaxis){#id21 .reference .internal}

- [Axis Elements](#axis-elements){#id22 .reference .internal}

  - [Axis Line](#axis-line){#id23 .reference .internal}

    - [AxisLine2D](#axisline2d){#id24 .reference .internal}

    - [Cartesian2DAxisLine](#cartesian2daxisline){#id25 .reference
      .internal}

    - [AxisLine3D](#axisline3d){#id26 .reference .internal}

    - [RadialAxisLine2D](#radialaxisline2d){#id27 .reference .internal}

  - [Ticks and Labels](#ticks-and-labels){#id28 .reference .internal}

    - [Ticks2D](#ticks2d){#id29 .reference .internal}

    - [Ticks3D](#ticks3d){#id30 .reference .internal}

    - [RadialTicks](#radialticks){#id31 .reference .internal}

    - [TickLabels2D](#ticklabels2d){#id32 .reference .internal}

    - [TickLabels3D](#ticklabels3d){#id33 .reference .internal}

    - [RadialTickLabels](#radialticklabels){#id34 .reference .internal}

  - [Axis Title](#axis-title){#id35 .reference .internal}

    - [Axis2DTitle](#axis2dtitle){#id36 .reference .internal}

    - [DataAxis2DTitle](#dataaxis2dtitle){#id37 .reference .internal}

    - [DataAxis3DTitle](#dataaxis3dtitle){#id38 .reference .internal}

    - [RadialAxisTitle](#radialaxistitle){#id39 .reference .internal}

  - [Grid Area](#grid-area){#id40 .reference .internal}

    - [GridArea](#gridarea){#id41 .reference .internal}

    - [Cartesian2DGridArea](#cartesian2dgridarea){#id42 .reference
      .internal}

    - [Cartesian3DGridArea](#cartesian3dgridarea){#id43 .reference
      .internal}

    - [PreciseGrid](#precisegrid){#id44 .reference .internal}

    - [GridLines](#gridlines){#id45 .reference .internal}

    - [GridLines2D](#gridlines2d){#id46 .reference .internal}

    - [MinorGridLines](#minorgridlines){#id47 .reference .internal}

    - [MinorGridLines2D](#minorgridlines2d){#id48 .reference .internal}

    - [PolarAngleGridLines](#polaranglegridlines){#id49 .reference
      .internal}

    - [PolarAngleMinorGridLines](#polarangleminorgridlines){#id50
      .reference .internal}

    - [MarkerGridLine](#markergridline){#id51 .reference .internal}

    - [MarkerGridLine2D](#markergridline2d){#id52 .reference .internal}

    - [PolarAngleMarkerGridLine](#polaranglemarkergridline){#id53
      .reference .internal}

  - [OrientationAxis](#orientationaxis){#id54 .reference .internal}

::::::: {#field-axes .section}
[]{#fieldaxis}[]{#fieldaxes}

## [Field Axes](#id8){.toc-backref role="doc-backlink"}[¶](#field-axes "Link to this heading"){.headerlink}

- [Cartesian2DFieldAxes](#cartesian2dfieldaxes){#id55 .reference
  .internal}

- [Cartesian2DFieldAxis](#cartesian2dfieldaxis){#id56 .reference
  .internal}

- [Cartesian3DFieldAxes](#cartesian3dfieldaxes){#id57 .reference
  .internal}

- [Cartesian3DFieldAxis](#cartesian3dfieldaxis){#id58 .reference
  .internal}

::: {#cartesian2dfieldaxes .section}
### [Cartesian2DFieldAxes](#id55){.toc-backref role="doc-backlink"}[¶](#cartesian2dfieldaxes "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DFieldAxes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#Cartesian2DFieldAxes){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldAxes "Link to this definition"){.headerlink}

:   (X, Y) axes style control for 2D field plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian2D)

        plot.show_shade = False
        plot.show_contour = True

        plot.axes.auto_adjust_ranges = True
        plot.axes.precise_grid.show = True
        plot.axes.precise_grid.size = 0.05

        plot.view.fit()

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('axes_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axes_2d.png"
    class="reference internal image-reference"><img
    src="../_images/axes_2d.png" style="width: 300px;"
    alt="../_images/axes_2d.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------
      [[`auto_adjust_ranges`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.auto_adjust_ranges "tecplot.plot.Cartesian2DFieldAxes.auto_adjust_ranges"){.reference .internal}   Automatically adjust axis ranges to nice values.
      [[`axis_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.axis_mode "tecplot.plot.Cartesian2DFieldAxes.axis_mode"){.reference .internal}                              Controls automatic adjustment of axis ranges.
      [[`grid_area`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.grid_area "tecplot.plot.Cartesian2DFieldAxes.grid_area"){.reference .internal}                              Area bounded by the axes.
      [[`precise_grid`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.precise_grid "tecplot.plot.Cartesian2DFieldAxes.precise_grid"){.reference .internal}                     Precise dot grid.
      [[`preserve_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.preserve_scale "tecplot.plot.Cartesian2DFieldAxes.preserve_scale"){.reference .internal}               Preserve scale (spacing between ticks) on range change.
      [[`viewport`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.viewport "tecplot.plot.Cartesian2DFieldAxes.viewport"){.reference .internal}                                 Area of the frame used by the plot axes.
      [[`x_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.x_axis "tecplot.plot.Cartesian2DFieldAxes.x_axis"){.reference .internal}                                       X-axis style control.
      [[`xy_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.xy_ratio "tecplot.plot.Cartesian2DFieldAxes.xy_ratio"){.reference .internal}                                 X:Y axis scaling ratio in percent.
      [[`y_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxes.y_axis "tecplot.plot.Cartesian2DFieldAxes.y_axis"){.reference .internal}                                       Y-axis style control.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[auto_adjust_ranges]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.auto_adjust_ranges "Link to this definition"){.headerlink}

:   Automatically adjust axis ranges to nice values.

    Axes limits will be adjusted to have the smallest number of
    significant digits possible:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.auto_adjust_ranges = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[axis_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.axis_mode "Link to this definition"){.headerlink}

:   Controls automatic adjustment of axis ranges.

    Possible values: [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, [[`XYDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}.

    If set to [[`XYDependent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}, then setting the range of one axis automatically scales
    the other indicated axes proportionally to maintain the aspect ratio
    of the plot, effectively zooming in or out. If set to
    [[`Independent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, adjusting the range of one axis has no effect on other
    axes. Defaults to [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal} for XY line plots, [[`XYDependent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal} for 2D Cartesian plots. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.Independent
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode "tecplot.constant.AxisMode"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[grid_area]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.grid_area "Link to this definition"){.headerlink}

:   Area bounded by the axes.

    This controls the background color and border of the axes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridArea`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridArea "tecplot.plot.GridArea"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[precise_grid]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.precise_grid "Link to this definition"){.headerlink}

:   Precise dot grid.

    This is a set of small dots drawn at the intersection of every minor
    gridline. In line plots, the axis assignments for the first active
    mapping govern the precise dot grid. The precise dot grid option is
    disabled for the 3D Cartesian plots and Line plots when either axis
    for the first active line mapping uses a log scale:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PreciseGrid`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.PreciseGrid "tecplot.plot.PreciseGrid"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[preserve_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.preserve_scale "Link to this definition"){.headerlink}

:   Preserve scale (spacing between ticks) on range change.

    This maintains the axis scaling, i.e. the distance between values
    along the axis. If [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the axes length will be preserved when the range
    changes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.preserve_scale = False
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 10 # axis scale is changed (length is preserved)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[viewport]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.viewport "Link to this definition"){.headerlink}

:   Area of the frame used by the plot axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.viewport.left = 5
        >>> plot.axes.viewport.right = 95
        >>> plot.axes.viewport.top = 95
        >>> plot.axes.viewport.bottom = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DViewport`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian2DViewport "tecplot.plot.Cartesian2DViewport"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[x_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.x_axis "Link to this definition"){.headerlink}

:   X-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DFieldAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis "tecplot.plot.Cartesian2DFieldAxis"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[xy_ratio]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.xy_ratio "Link to this definition"){.headerlink}

:   X:Y axis scaling ratio in percent.

    This requires the axes to be in dependent mode:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.XYDependent
        >>> plot.axes.xy_ratio = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[y_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxes.y_axis "Link to this definition"){.headerlink}

:   Y-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.y_axis.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DFieldAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis "tecplot.plot.Cartesian2DFieldAxis"){.reference
        .internal}
:::

::: {#cartesian2dfieldaxis .section}
### [Cartesian2DFieldAxis](#id56){.toc-backref role="doc-backlink"}[¶](#cartesian2dfieldaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DFieldAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#Cartesian2DFieldAxis){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldAxis "Link to this definition"){.headerlink}

:   X or Y axis for 2D field plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, AxisMode, AxisTitleMode

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian2D)

        plot.show_contour = True

        plot.axes.axis_mode = AxisMode.Independent
        plot.axes.viewport.right = 75
        plot.axes.preserve_scale = False

        xaxis = plot.axes.x_axis
        xaxis.title.text = 'Longitudinal (m)'
        xaxis.title.title_mode = AxisTitleMode.UseText
        xaxis.min = 3.8
        xaxis.max = 5.3
        xaxis.grid_lines.show = True
        xaxis.grid_lines.draw_last = True

        yaxis = plot.axes.y_axis
        yaxis.title.text = 'Transverse (m)'
        yaxis.title.title_mode = AxisTitleMode.UseText
        yaxis.min = 2.8
        yaxis.max = 4.3
        yaxis.grid_lines.show = True
        yaxis.minor_grid_lines.show = True
        yaxis.minor_grid_lines.draw_last = True

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('axis_2d.png',600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_2d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_2d.png" style="width: 300px;"
    alt="../_images/axis_2d.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.grid_lines "tecplot.plot.Cartesian2DFieldAxis.grid_lines"){.reference .internal}                     Major grid lines style control.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.line "tecplot.plot.Cartesian2DFieldAxis.line"){.reference .internal}                                       Axis line style control.
      [[`log_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.log_scale "tecplot.plot.Cartesian2DFieldAxis.log_scale"){.reference .internal}                        Use logarithmic scale for this axis.
      [[`marker_grid_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.marker_grid_line "tecplot.plot.Cartesian2DFieldAxis.marker_grid_line"){.reference .internal}   Marker line to indicate a particular position along an axis.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.max "tecplot.plot.Cartesian2DFieldAxis.max"){.reference .internal}                                          Upper bound of this axis\' range.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.min "tecplot.plot.Cartesian2DFieldAxis.min"){.reference .internal}                                          Lower bound of this axis\' range.
      [[`minor_grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.minor_grid_lines "tecplot.plot.Cartesian2DFieldAxis.minor_grid_lines"){.reference .internal}   Minor grid lines style control.
      [[`reverse`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.reverse "tecplot.plot.Cartesian2DFieldAxis.reverse"){.reference .internal}                              Reverse the direction of the axis scale.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.show "tecplot.plot.Cartesian2DFieldAxis.show"){.reference .internal}                                       Enable drawing of this axis.
      [[`tick_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.tick_labels "tecplot.plot.Cartesian2DFieldAxis.tick_labels"){.reference .internal}                  Axis ticks labels style control.
      [[`ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.ticks "tecplot.plot.Cartesian2DFieldAxis.ticks"){.reference .internal}                                    Axis major and minor ticks style control.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.title "tecplot.plot.Cartesian2DFieldAxis.title"){.reference .internal}                                    Axis title.
      [[`variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.variable "tecplot.plot.Cartesian2DFieldAxis.variable"){.reference .internal}                           The [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} assigned to this axis.
      [[`variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.variable_index "tecplot.plot.Cartesian2DFieldAxis.variable_index"){.reference .internal}         Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} assigned to this axis.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
      [[`adjust_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.adjust_range_to_nice "tecplot.plot.Cartesian2DFieldAxis.adjust_range_to_nice"){.reference .internal}()               Rounds the axis range to the nearest major axis increment.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.fit_range "tecplot.plot.Cartesian2DFieldAxis.fit_range"){.reference .internal}(\[consider_blanking\])                           Set range of axis to variable minimum and maximum.
      [[`fit_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldAxis.fit_range_to_nice "tecplot.plot.Cartesian2DFieldAxis.fit_range_to_nice"){.reference .internal}(\[consider_blanking\])   Set range of axis to nice values near variable minimum and maximum.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[adjust_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.Cartesian2DFieldAxis.adjust_range_to_nice "Link to this definition"){.headerlink}

:   Rounds the axis range to the nearest major axis increment.

    This method resets the axis-line label values such that all
    currently displayed label values are set to have the smallest number
    of significant digits possible.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.adjust_range_to_nice()
    :::
    ::::

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[consider_blanking]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian2DFieldAxis.fit_range "Link to this definition"){.headerlink}

:   Set range of axis to variable minimum and maximum.

    ::: {.admonition .note}
    Note

    If the axis dependency is not [[`Independent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, then this action may also affect the range on another
    axis.
    :::

    Parameters[:]{.colon}

    :   **consider_blanking** ([[`Boolean`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}, optional) -- If [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} and blanking is enabled, the resulting view excludes
        blanked cells at the edges of the plot. If [[`False`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}, then the resulting view will ignore blanked cells at
        the edges of the plot. (default: [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external})

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range()
    :::
    ::::

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[consider_blanking]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian2DFieldAxis.fit_range_to_nice "Link to this definition"){.headerlink}

:   Set range of axis to nice values near variable minimum and maximum.

    This method resets the range to equal the minimum and maximum of the
    data being plotted, but makes the axis values "nice" by setting
    labels to have the smallest number of significant digits possible,

    ::: {.admonition .note}
    Note

    If the axis dependency is not independent then this method may also
    affect the range on another axis.
    :::

    Parameters[:]{.colon}

    :   **consider_blanking** ([[`Boolean`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}, optional) -- If [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} and blanking is enabled, the resulting view excludes
        blanked cells at the edges of the plot. If [[`False`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}, then the resulting view will ignore blanked cells at
        the edges of the plot. (default: [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external})

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range_to_nice()
    :::
    ::::

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.grid_lines "Link to this definition"){.headerlink}

:   Major grid lines style control.

    Major grid lines are attached to the locations of the major ticks.
    See [[`minor_grid_lines`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.minor_grid_lines "tecplot.plot.XYLineAxis.minor_grid_lines"){.reference
    .internal} for lines attached to minor ticks. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridLines2D "tecplot.plot.GridLines2D"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.line "Link to this definition"){.headerlink}

:   Axis line style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DAxisLine`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine "tecplot.plot.Cartesian2DAxisLine"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[log_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.log_scale "Link to this definition"){.headerlink}

:   Use logarithmic scale for this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> # or "plot.axes.r_axis" for the radial axis in polar plots
        >>> axis.log_scale = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[marker_grid_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.marker_grid_line "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.marker_grid_line.show = True
        >>> axis.marker_grid_line.position = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`MarkerGridLine2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D "tecplot.plot.MarkerGridLine2D"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.max "Link to this definition"){.headerlink}

:   Upper bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 1.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.min "Link to this definition"){.headerlink}

:   Lower bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.min = 0.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[minor_grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.minor_grid_lines "Link to this definition"){.headerlink}

:   Minor grid lines style control.

    Minor grid lines are attached to the locations of the minor ticks.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.minor_grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`MinorGridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D "tecplot.plot.MinorGridLines2D"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[reverse]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.reverse "Link to this definition"){.headerlink}

:   Reverse the direction of the axis scale.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.reverse = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[tick_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.tick_labels "Link to this definition"){.headerlink}

:   Axis ticks labels style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.tick_labels.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickLabels2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.TickLabels2D "tecplot.plot.TickLabels2D"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.ticks "Link to this definition"){.headerlink}

:   Axis major and minor ticks style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.ticks.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`Ticks2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Ticks2D "tecplot.plot.Ticks2D"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.title "Link to this definition"){.headerlink}

:   Axis title.

    This is the primary label for the axis and usually includes units:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.variable "Link to this definition"){.headerlink}

:   The [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} assigned to this axis.

    This is the spatial variable associated with this axis and is
    usually one of [`(X,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Y,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Z)`{.docutils .literal .notranslate}]{.pre}. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import PlotType

        fr = tp.active_frame()
        ds = fr.create_dataset('D', ['X', 'Y', 'Z', 'U', 'V'])
        axes = fr.plot(PlotType.Cartesian3D).axes

        # prints: ('X', 'Y')
        print(axes.x_axis.variable.name, axes.y_axis.variable.name)

        axes.x_axis.variable = ds.variable('U')
        axes.y_axis.variable = ds.variable('V')

        # prints: ('U', 'V)
        print(axes.x_axis.variable.name, axes.y_axis.variable.name)
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldAxis.variable_index "Link to this definition"){.headerlink}

:   Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} assigned to this axis.

    Example usage, interchanging the (x, y) axes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> v0 = plot.axes.x_axis.variable_index
        >>> v1 = plot.axes.y_axis.variable_index
        >>> plot.axes.x_axis.variable_index = v1
        >>> plot.axes.y_axis.variable_index = v0
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} (zero-based)
:::

::: {#cartesian3dfieldaxes .section}
### [Cartesian3DFieldAxes](#id57){.toc-backref role="doc-backlink"}[¶](#cartesian3dfieldaxes "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian3DFieldAxes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#Cartesian3DFieldAxes){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldAxes "Link to this definition"){.headerlink}

:   (X, Y, Z) axes style control for 3D field plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        dataset = tp.load_layout(infile)

        frame = tp.active_frame()
        plot = frame.plot()

        plot.axes.x_axis.show = True
        plot.axes.y_axis.show = True
        plot.axes.z_axis.show = True
        plot.axes.grid_area.fill_color = Color.SkyBlue
        plot.axes.padding = 20

        plot.view.fit()

        tp.export.save_png('axes_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axes_3d.png"
    class="reference internal image-reference"><img
    src="../_images/axes_3d.png" style="width: 300px;"
    alt="../_images/axes_3d.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aspect_ratio_limit`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit"){.reference .internal}                     Scale limit of the axes aspect ratio.
      [[`aspect_ratio_reset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_reset "tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_reset"){.reference .internal}                     Axes scale aspect ratio used when [[`aspect_ratio_limit`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit"){.reference .internal} is exceeded.
      [[`auto_edge_assignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.auto_edge_assignment "tecplot.plot.Cartesian3DFieldAxes.auto_edge_assignment"){.reference .internal}               Enable automatically choosing which edges to label.
      [[`axis_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.axis_mode "tecplot.plot.Cartesian3DFieldAxes.axis_mode"){.reference .internal}                                                Scale dependencies along each axis.
      [[`grid_area`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.grid_area "tecplot.plot.Cartesian3DFieldAxes.grid_area"){.reference .internal}                                                Area of the viewport used by the axes.
      [[`orientation_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.orientation_axis "tecplot.plot.Cartesian3DFieldAxes.orientation_axis"){.reference .internal}                           Get the 3D Orientation Axes.
      [[`padding`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.padding "tecplot.plot.Cartesian3DFieldAxes.padding"){.reference .internal}                                                      Margin of axis padding around data in percent of data extent.
      [[`preserve_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.preserve_scale "tecplot.plot.Cartesian3DFieldAxes.preserve_scale"){.reference .internal}                                 Preserve scale (spacing between ticks) on range change.
      [[`range_aspect_ratio_limit`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit"){.reference .internal}   Range limit of the axes aspect ratio.
      [[`range_aspect_ratio_reset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_reset "tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_reset"){.reference .internal}   Axes range aspect ratio used [[`range_aspect_ratio_limit`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit"){.reference .internal} is exceeded.
      [[`viewport`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.viewport "tecplot.plot.Cartesian3DFieldAxes.viewport"){.reference .internal}                                                   Area of the frame used by the plot axes.
      [[`x_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.x_axis "tecplot.plot.Cartesian3DFieldAxes.x_axis"){.reference .internal}                                                         X-axis style control.
      [[`xy_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.xy_ratio "tecplot.plot.Cartesian3DFieldAxes.xy_ratio"){.reference .internal}                                                   X:Y axis scaling ratio in percent.
      [[`xz_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.xz_ratio "tecplot.plot.Cartesian3DFieldAxes.xz_ratio"){.reference .internal}                                                   X:Z axis scaling ratio in percent.
      [[`y_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.y_axis "tecplot.plot.Cartesian3DFieldAxes.y_axis"){.reference .internal}                                                         Y-axis style control.
      [[`z_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.z_axis "tecplot.plot.Cartesian3DFieldAxes.z_axis"){.reference .internal}                                                         Z-axis style control.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------
      [[`reset_origin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.reset_origin "tecplot.plot.Cartesian3DFieldAxes.reset_origin"){.reference .internal}(\[location\])   Set the origin to the specified location.
      [[`reset_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.reset_range "tecplot.plot.Cartesian3DFieldAxes.reset_range"){.reference .internal}()                  Recalculate and set the ranges for each axis.
      [[`reset_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.reset_scale "tecplot.plot.Cartesian3DFieldAxes.reset_scale"){.reference .internal}()                  Recalculate and set the scale factors for each axis.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[aspect_ratio_limit]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit "Link to this definition"){.headerlink}

:   Scale limit of the axes aspect ratio.

    This is the limit above which the axes relative scales will be
    pegged to [[`aspect_ratio_reset`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_reset "tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_reset"){.reference
    .internal}. The following example will set the aspect ratio between
    scales to 1 if they first exceed a ratio of 10:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.aspect_ratio_limit = 10
        >>> plot.axes.aspect_ratio_reset = 1
        >>> plot.axes.reset_scale()
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[aspect_ratio_reset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_reset "Link to this definition"){.headerlink}

:   Axes scale aspect ratio used when [[`aspect_ratio_limit`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit"){.reference
    .internal} is exceeded.

    This is the aspect ratio used to scale the axes when the data's
    aspect ratio exceeds the value set to [[`aspect_ratio_limit`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.aspect_ratio_limit"){.reference
    .internal}. The following example will set the aspect ratio between
    scales to 10 if they first exceed a ratio of 15:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.aspect_ratio_limit = 15
        >>> plot.axes.aspect_ratio_reset = 10
        >>> plot.axes.reset_scale()
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[auto_edge_assignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.auto_edge_assignment "Link to this definition"){.headerlink}

:   Enable automatically choosing which edges to label.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.auto_edge_assignment = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[axis_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.axis_mode "Link to this definition"){.headerlink}

:   Scale dependencies along each axis.

    Possible values: [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, [[`XYDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}, [[`XYZDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYZDependent "tecplot.constant.AxisMode.XYZDependent"){.reference
    .internal}.

    If set to [[`XYDependent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal} or [[`XYZDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYZDependent "tecplot.constant.AxisMode.XYZDependent"){.reference
    .internal}, then setting the range of one axis automatically scales
    the other indicated axes proportionally to maintain the aspect ratio
    of the plot, effectively zooming in or out. If set to
    [[`Independent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, adjusting the range of one axis has no effect on other
    axes. Defaults to [[`XYZDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYZDependent "tecplot.constant.AxisMode.XYZDependent"){.reference
    .internal} for 3D Cartesian plots. Both dependent modes allow
    specifying the axes scaling ratios:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.XYZDependent
        >>> plot.axes.xy_ratio = 2
        >>> plot.axes.xz_ratio = 20
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode "tecplot.constant.AxisMode"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[grid_area]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.grid_area "Link to this definition"){.headerlink}

:   Area of the viewport used by the axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DGridArea`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian3DGridArea "tecplot.plot.Cartesian3DGridArea"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[orientation_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.orientation_axis "Link to this definition"){.headerlink}

:   Get the 3D Orientation Axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # Hide the orientation axes
        >>> plot.axes.orientation_axis.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`OrientationAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.OrientationAxis "tecplot.plot.OrientationAxis"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[padding]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.padding "Link to this definition"){.headerlink}

:   Margin of axis padding around data in percent of data extent.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.padding = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[preserve_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.preserve_scale "Link to this definition"){.headerlink}

:   Preserve scale (spacing between ticks) on range change.

    This maintains the axis scaling, i.e. the distance between values
    along the axis. If [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the axes length will be preserved when the range
    changes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.preserve_scale = False
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 10 # axis scale is changed (length is preserved)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[range_aspect_ratio_limit]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit "Link to this definition"){.headerlink}

:   Range limit of the axes aspect ratio.

    This is the limit above which the axes' relative ranges will be
    pegged to [[`range_aspect_ratio_reset`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_reset "tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_reset"){.reference
    .internal}. The following example will set the aspect ratio between
    ranges to 1 if they first exceed a ratio of 10:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.range_aspect_ratio_limit = 10
        >>> plot.axes.range_aspect_ratio_reset = 1
        >>> plot.axes.reset_range()
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[range_aspect_ratio_reset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_reset "Link to this definition"){.headerlink}

:   Axes range aspect ratio used [[`range_aspect_ratio_limit`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit"){.reference
    .internal} is exceeded.

    This is the aspect ratio used to set the ranges of the axes when the
    axes' aspect ratios exceed the value of
    [[`range_aspect_ratio_limit`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit "tecplot.plot.Cartesian3DFieldAxes.range_aspect_ratio_limit"){.reference
    .internal}. The following example will set the aspect ratio between
    ranges to 10 if they first exceed a ratio of 15:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.range_aspect_ratio_limit = 15
        >>> plot.axes.range_aspect_ratio_reset = 10
        >>> plot.axes.reset_range()
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[reset_origin]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[location]{.pre}]{.n}[[=]{.pre}]{.o}[[OriginResetLocation.DataCenter]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldAxes.reset_origin "Link to this definition"){.headerlink}

:   Set the origin to the specified location.

    Parameters[:]{.colon}

    :   **location** ([[`OriginResetLocation`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.OriginResetLocation "tecplot.constant.OriginResetLocation"){.reference
        .internal}, optional) -- Either the center of the data with
        [[`OriginResetLocation.DataCenter`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.OriginResetLocation.DataCenter "tecplot.constant.OriginResetLocation.DataCenter"){.reference
        .internal} (default) or the center of the viewport with
        [[`OriginResetLocation.ViewCenter`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.OriginResetLocation.ViewCenter "tecplot.constant.OriginResetLocation.ViewCenter"){.reference
        .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import OriginResetLocation
        >>> plot.axes.reset_origin(OriginResetLocation.ViewCenter)
    :::
    ::::

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[reset_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldAxes.reset_range "Link to this definition"){.headerlink}

:   Recalculate and set the ranges for each axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.reset_range()
    :::
    ::::

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[reset_scale]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldAxes.reset_scale "Link to this definition"){.headerlink}

:   Recalculate and set the scale factors for each axis.

    Aspect ratio limits are taken into account:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.reset_scale()
    :::
    ::::

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[viewport]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.viewport "Link to this definition"){.headerlink}

:   Area of the frame used by the plot axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.axes.viewport.bottom)
        5
    :::
    ::::

    Type[:]{.colon}

    :   [[`ReadOnlyViewport`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ReadOnlyViewport "tecplot.plot.ReadOnlyViewport"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[x_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.x_axis "Link to this definition"){.headerlink}

:   X-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DFieldAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis "tecplot.plot.Cartesian3DFieldAxis"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[xy_ratio]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.xy_ratio "Link to this definition"){.headerlink}

:   X:Y axis scaling ratio in percent.

    This requires the axes to be in dependent mode:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.XYDependent
        >>> plot.axes.xy_ratio = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[xz_ratio]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.xz_ratio "Link to this definition"){.headerlink}

:   X:Z axis scaling ratio in percent.

    This requires the axes to be in dependent mode:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.XYZDependent
        >>> plot.axes.xy_ratio = 2
        >>> plot.axes.xz_ratio = 20
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[y_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.y_axis "Link to this definition"){.headerlink}

:   Y-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.y_axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DFieldAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis "tecplot.plot.Cartesian3DFieldAxis"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxes.]{.pre}]{.sig-prename .descclassname}[[z_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxes.z_axis "Link to this definition"){.headerlink}

:   Z-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.z_axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DFieldAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis "tecplot.plot.Cartesian3DFieldAxis"){.reference
        .internal}
:::

::: {#cartesian3dfieldaxis .section}
### [Cartesian3DFieldAxis](#id58){.toc-backref role="doc-backlink"}[¶](#cartesian3dfieldaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian3DFieldAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#Cartesian3DFieldAxis){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldAxis "Link to this definition"){.headerlink}

:   X, Y or Z axis on 3D field plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, AxisLine3DAssignment

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'RainierElevation.lay')
        tp.load_layout(infile)

        frame = tp.active_frame()
        dataset = frame.dataset
        plot = frame.plot(PlotType.Cartesian3D)
        plot.activate()

        plot.show_contour = True

        plot.axes.grid_area.filled = False

        axes = [plot.axes.x_axis, plot.axes.y_axis, plot.axes.z_axis]
        assignments = [AxisLine3DAssignment.YMinZMax,
                       AxisLine3DAssignment.ZMaxXMin,
                       AxisLine3DAssignment.XMaxYMin]

        for ax, asgn in zip(axes, assignments):
            ax.show = True
            ax.grid_lines.show = False
            ax.title.show = False
            ax.line.show = False
            ax.line.edge_assignment = asgn

        plot.axes.z_axis.grid_lines.show = True
        plot.axes.y_axis.min=-2000
        plot.axes.y_axis.max=1000
        plot.axes.x_axis.min=-9500
        plot.axes.x_axis.max=-7200
        plot.axes.z_axis.min=0
        plot.axes.x_axis.scale_factor=1.9

        plot.view.width = 7830
        plot.view.alpha = 0
        plot.view.theta = -147.5
        plot.view.psi   = 70
        plot.view.position = (1975, 15620, 115930)

        tp.export.save_png('axis_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_3d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_3d.png" style="width: 300px;"
    alt="../_images/axis_3d.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.grid_lines "tecplot.plot.Cartesian3DFieldAxis.grid_lines"){.reference .internal}                     Major grid lines style control.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.line "tecplot.plot.Cartesian3DFieldAxis.line"){.reference .internal}                                       Axis line style control.
      [[`marker_grid_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.marker_grid_line "tecplot.plot.Cartesian3DFieldAxis.marker_grid_line"){.reference .internal}   Marker line to indicate a particular position along an axis.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.max "tecplot.plot.Cartesian3DFieldAxis.max"){.reference .internal}                                          Upper bound of this axis\' range.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.min "tecplot.plot.Cartesian3DFieldAxis.min"){.reference .internal}                                          Lower bound of this axis\' range.
      [[`minor_grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.minor_grid_lines "tecplot.plot.Cartesian3DFieldAxis.minor_grid_lines"){.reference .internal}   Minor grid lines style control.
      [[`scale_factor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.scale_factor "tecplot.plot.Cartesian3DFieldAxis.scale_factor"){.reference .internal}               Factor used for axis scaling.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.show "tecplot.plot.Cartesian3DFieldAxis.show"){.reference .internal}                                       Enable drawing of this axis.
      [[`tick_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.tick_labels "tecplot.plot.Cartesian3DFieldAxis.tick_labels"){.reference .internal}                  Axis ticks labels style control.
      [[`ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.ticks "tecplot.plot.Cartesian3DFieldAxis.ticks"){.reference .internal}                                    Axis major and minor ticks style control.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.title "tecplot.plot.Cartesian3DFieldAxis.title"){.reference .internal}                                    Axis title.
      [[`variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.variable "tecplot.plot.Cartesian3DFieldAxis.variable"){.reference .internal}                           The [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} assigned to this axis.
      [[`variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.variable_index "tecplot.plot.Cartesian3DFieldAxis.variable_index"){.reference .internal}         Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} assigned to this axis.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
      [[`adjust_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.adjust_range_to_nice "tecplot.plot.Cartesian3DFieldAxis.adjust_range_to_nice"){.reference .internal}()               Rounds the axis range to the nearest major axis increment.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.fit_range "tecplot.plot.Cartesian3DFieldAxis.fit_range"){.reference .internal}(\[consider_blanking\])                           Set range of axis to variable minimum and maximum.
      [[`fit_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.fit_range_to_nice "tecplot.plot.Cartesian3DFieldAxis.fit_range_to_nice"){.reference .internal}(\[consider_blanking\])   Set range of axis to nice values near variable minimum and maximum.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[adjust_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldAxis.adjust_range_to_nice "Link to this definition"){.headerlink}

:   Rounds the axis range to the nearest major axis increment.

    This method resets the axis-line label values such that all
    currently displayed label values are set to have the smallest number
    of significant digits possible.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.adjust_range_to_nice()
    :::
    ::::

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[consider_blanking]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldAxis.fit_range "Link to this definition"){.headerlink}

:   Set range of axis to variable minimum and maximum.

    ::: {.admonition .note}
    Note

    If the axis dependency is not [[`Independent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, then this action may also affect the range on another
    axis.
    :::

    Parameters[:]{.colon}

    :   **consider_blanking** ([[`Boolean`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}, optional) -- If [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} and blanking is enabled, the resulting view excludes
        blanked cells at the edges of the plot. If [[`False`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}, then the resulting view will ignore blanked cells at
        the edges of the plot. (default: [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external})

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range()
    :::
    ::::

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[consider_blanking]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldAxis.fit_range_to_nice "Link to this definition"){.headerlink}

:   Set range of axis to nice values near variable minimum and maximum.

    This method resets the range to equal the minimum and maximum of the
    data being plotted, but makes the axis values "nice" by setting
    labels to have the smallest number of significant digits possible,

    ::: {.admonition .note}
    Note

    If the axis dependency is not independent then this method may also
    affect the range on another axis.
    :::

    Parameters[:]{.colon}

    :   **consider_blanking** ([[`Boolean`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}, optional) -- If [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external} and blanking is enabled, the resulting view excludes
        blanked cells at the edges of the plot. If [[`False`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
        .external}, then the resulting view will ignore blanked cells at
        the edges of the plot. (default: [[`True`{.xref .any .docutils
        .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
        .external})

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range_to_nice()
    :::
    ::::

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.grid_lines "Link to this definition"){.headerlink}

:   Major grid lines style control.

    Major grid lines are attached to the locations of the major ticks.
    See [[`minor_grid_lines`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldAxis.minor_grid_lines "tecplot.plot.Cartesian3DFieldAxis.minor_grid_lines"){.reference
    .internal} for lines attached to minor ticks. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridLines`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridLines "tecplot.plot.GridLines"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.line "Link to this definition"){.headerlink}

:   Axis line style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.line.line_thickness = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisLine3D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.AxisLine3D "tecplot.plot.AxisLine3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[marker_grid_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.marker_grid_line "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.marker_grid_line.show = True
        >>> plot.axes.x_axis.marker_grid_line.position = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`MarkerGridLine`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine "tecplot.plot.MarkerGridLine"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.max "Link to this definition"){.headerlink}

:   Upper bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 1.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.min "Link to this definition"){.headerlink}

:   Lower bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.min = 0.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[minor_grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.minor_grid_lines "Link to this definition"){.headerlink}

:   Minor grid lines style control.

    Minor grid lines are attached to the locations of the minor ticks.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.minor_grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`MinorGridLines`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MinorGridLines "tecplot.plot.MinorGridLines"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[scale_factor]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.scale_factor "Link to this definition"){.headerlink}

:   Factor used for axis scaling.

    This will automatically scale the other axes if axis mode dependent.
    Setting the axis mode to independent allows each axis to have their
    own scale factor:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.Independent
        >>> plot.axes.x_axis.scale_factor = 1
        >>> plot.axes.y_axis.scale_factor = 2
        >>> plot.axes.z_axis.scale_factor = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[tick_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.tick_labels "Link to this definition"){.headerlink}

:   Axis ticks labels style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.tick_labels.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickLabels3D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.TickLabels3D "tecplot.plot.TickLabels3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.ticks "Link to this definition"){.headerlink}

:   Axis major and minor ticks style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.ticks.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`Ticks3D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Ticks3D "tecplot.plot.Ticks3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.title "Link to this definition"){.headerlink}

:   Axis title.

    This is the primary label for the axis and usually includes units:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.variable "Link to this definition"){.headerlink}

:   The [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} assigned to this axis.

    This is the spatial variable associated with this axis and is
    usually one of [`(X,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Y,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Z)`{.docutils .literal .notranslate}]{.pre}. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import PlotType

        fr = tp.active_frame()
        ds = fr.create_dataset('D', ['X', 'Y', 'Z', 'U', 'V'])
        axes = fr.plot(PlotType.Cartesian3D).axes

        # prints: ('X', 'Y')
        print(axes.x_axis.variable.name, axes.y_axis.variable.name)

        axes.x_axis.variable = ds.variable('U')
        axes.y_axis.variable = ds.variable('V')

        # prints: ('U', 'V)
        print(axes.x_axis.variable.name, axes.y_axis.variable.name)
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldAxis.]{.pre}]{.sig-prename .descclassname}[[variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldAxis.variable_index "Link to this definition"){.headerlink}

:   Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} assigned to this axis.

    Example usage, interchanging the (x, y) axes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> v0 = plot.axes.x_axis.variable_index
        >>> v1 = plot.axes.y_axis.variable_index
        >>> plot.axes.x_axis.variable_index = v1
        >>> plot.axes.y_axis.variable_index = v0
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} (zero-based)
:::
:::::::

:::::::: {#line-axes .section}
[]{#lineaxis}[]{#lineaxes}

## [Line Axes](#id13){.toc-backref role="doc-backlink"}[¶](#line-axes "Link to this heading"){.headerlink}

- [XYLineAxes](#xylineaxes){#id59 .reference .internal}

- [XYLineAxis](#xylineaxis){#id60 .reference .internal}

- [PolarLineAxes](#polarlineaxes){#id61 .reference .internal}

- [RadialLineAxis](#radiallineaxis){#id62 .reference .internal}

- [PolarAngleLineAxis](#polaranglelineaxis){#id63 .reference .internal}

::: {#xylineaxes .section}
### [XYLineAxes](#id59){.toc-backref role="doc-backlink"}[¶](#xylineaxes "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[XYLineAxes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#XYLineAxes){.reference .internal}[¶](#tecplot.plot.XYLineAxes "Link to this definition"){.headerlink}

:   (X, Y) axes style control for line plots.

    The [`axes`{.docutils .literal .notranslate}]{.pre} property of a
    [[`XYLinePlot`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinePlot "tecplot.plot.XYLinePlot"){.reference
    .internal} allows access to the several [`x`{.docutils .literal
    .notranslate}]{.pre} and [`y`{.docutils .literal
    .notranslate}]{.pre} axes by index. Linemaps can use any of the five
    such axes. In this example, we create two sets of data with
    different scales and the second y-axis is used on the right side of
    the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        frame = tp.active_frame()

        npoints = 100
        x = np.linspace(-10,10,npoints)
        t = x**2
        p = 0.1 * np.sin(x)

        dataset = frame.create_dataset('data', ['Position (m)', 'Temperature (K)',
                                                'Pressure (Pa)'])
        zone = dataset.add_ordered_zone('zone', (100,))
        zone.values('Position (m)')[:] = x
        zone.values('Temperature (K)')[:] = t
        zone.values('Pressure (Pa)')[:] = p

        plot = frame.plot(PlotType.XYLine)
        plot.activate()
        plot.delete_linemaps()

        temp = plot.add_linemap('temp', zone, dataset.variable('Position (m)'),
                         dataset.variable('Temperature (K)'))
        press = plot.add_linemap('press', zone, dataset.variable('Position (m)'),
                                 dataset.variable('Pressure (Pa)'))

        # Color the line and the y-axis for temperature
        temp.line.color = Color.RedOrange
        temp.line.line_thickness = 0.8

        ax = plot.axes.y_axis(0)
        ax.line.color = temp.line.color
        ax.tick_labels.color = temp.line.color
        ax.title.color = temp.line.color

        # set pressure linemap to second x-axis
        press.y_axis_index = 1

        # Color the line and the y-axis for pressure
        press.line.color = Color.Chartreuse
        press.line.line_thickness = 0.8

        ax = plot.axes.y_axis(1)
        ax.line.color = press.line.color
        ax.tick_labels.color = press.line.color
        ax.title.color = press.line.color

        tp.export.save_png('axes_line.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axes_line.png"
    class="reference internal image-reference"><img
    src="../_images/axes_line.png" style="width: 300px;"
    alt="../_images/axes_line.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------
      [[`auto_adjust_ranges`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.auto_adjust_ranges "tecplot.plot.XYLineAxes.auto_adjust_ranges"){.reference .internal}   Automatically adjust axis ranges to nice values.
      [[`axis_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.axis_mode "tecplot.plot.XYLineAxes.axis_mode"){.reference .internal}                              Controls automatic adjustment of axis ranges.
      [[`grid_area`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.grid_area "tecplot.plot.XYLineAxes.grid_area"){.reference .internal}                              Area bounded by the axes.
      [[`precise_grid`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.precise_grid "tecplot.plot.XYLineAxes.precise_grid"){.reference .internal}                     Precise dot grid.
      [[`preserve_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.preserve_scale "tecplot.plot.XYLineAxes.preserve_scale"){.reference .internal}               Preserve scale (spacing between ticks) on range change.
      [[`viewport`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.viewport "tecplot.plot.XYLineAxes.viewport"){.reference .internal}                                 Area of the frame used by the plot axes.
      [[`xy_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.xy_ratio "tecplot.plot.XYLineAxes.xy_ratio"){.reference .internal}                                 X:Y axis scaling ratio in percent.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------

    **Methods**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`x_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.x_axis "tecplot.plot.XYLineAxes.x_axis"){.reference .internal}(index)   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference .internal}: X-axis style control.
      [[`y_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxes.y_axis "tecplot.plot.XYLineAxes.y_axis"){.reference .internal}(index)   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference .internal}: Y-axis style control.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[auto_adjust_ranges]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.auto_adjust_ranges "Link to this definition"){.headerlink}

:   Automatically adjust axis ranges to nice values.

    Axes limits will be adjusted to have the smallest number of
    significant digits possible:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.auto_adjust_ranges = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[axis_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.axis_mode "Link to this definition"){.headerlink}

:   Controls automatic adjustment of axis ranges.

    Possible values: [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, [[`XYDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}.

    If set to [[`XYDependent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}, then setting the range of one axis automatically scales
    the other indicated axes proportionally to maintain the aspect ratio
    of the plot, effectively zooming in or out. If set to
    [[`Independent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, adjusting the range of one axis has no effect on other
    axes. Defaults to [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal} for XY line plots, [[`XYDependent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal} for 2D Cartesian plots. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.Independent
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode "tecplot.constant.AxisMode"){.reference
        .internal}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[grid_area]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.grid_area "Link to this definition"){.headerlink}

:   Area bounded by the axes.

    This controls the background color and border of the axes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridArea`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridArea "tecplot.plot.GridArea"){.reference
        .internal}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[precise_grid]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.precise_grid "Link to this definition"){.headerlink}

:   Precise dot grid.

    This is a set of small dots drawn at the intersection of every minor
    gridline. In line plots, the axis assignments for the first active
    mapping govern the precise dot grid. The precise dot grid option is
    disabled for the 3D Cartesian plots and Line plots when either axis
    for the first active line mapping uses a log scale:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PreciseGrid`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.PreciseGrid "tecplot.plot.PreciseGrid"){.reference
        .internal}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[preserve_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.preserve_scale "Link to this definition"){.headerlink}

:   Preserve scale (spacing between ticks) on range change.

    This maintains the axis scaling, i.e. the distance between values
    along the axis. If [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the axes length will be preserved when the range
    changes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.preserve_scale = False
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 10 # axis scale is changed (length is preserved)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[viewport]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.viewport "Link to this definition"){.headerlink}

:   Area of the frame used by the plot axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.viewport.left = 5
        >>> plot.axes.viewport.right = 95
        >>> plot.axes.viewport.top = 95
        >>> plot.axes.viewport.bottom = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DViewport`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian2DViewport "tecplot.plot.Cartesian2DViewport"){.reference
        .internal}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[x_axis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#XYLineAxes.x_axis){.reference .internal}[¶](#tecplot.plot.XYLineAxes.x_axis "Link to this definition"){.headerlink}

:   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference
    .internal}: X-axis style control.

    There are five x-axes for each [[`XYLinePlot`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinePlot "tecplot.plot.XYLinePlot"){.reference
    .internal}, indexed from 0 to 4 inclusive:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis(0).show = True
    :::
    ::::

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[xy_ratio]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxes.xy_ratio "Link to this definition"){.headerlink}

:   X:Y axis scaling ratio in percent.

    This requires the axes to be in dependent mode:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.XYDependent
        >>> plot.axes.xy_ratio = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxes.]{.pre}]{.sig-prename .descclassname}[[y_axis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#XYLineAxes.y_axis){.reference .internal}[¶](#tecplot.plot.XYLineAxes.y_axis "Link to this definition"){.headerlink}

:   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference
    .internal}: Y-axis style control.

    There are five y-axes for each [[`XYLinePlot`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot.html#tecplot.plot.XYLinePlot "tecplot.plot.XYLinePlot"){.reference
    .internal}, indexed from 0 to 4 inclusive:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.y_axis(0).show = True
    :::
    ::::
:::

::: {#xylineaxis .section}
### [XYLineAxis](#id60){.toc-backref role="doc-backlink"}[¶](#xylineaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[XYLineAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#XYLineAxis){.reference .internal}[¶](#tecplot.plot.XYLineAxis "Link to this definition"){.headerlink}

:   X or Y axis for line plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        plot = tp.active_frame().plot(PlotType.XYLine)
        plot.activate()

        for i in range(2):
            lmap = plot.linemap(i)
            lmap.show = True
            lmap.line.line_thickness = 0.6
            lmap.y_axis_index = i

            yax = plot.axes.y_axis(i)
            yax.line.color = lmap.line.color
            yax.title.color = lmap.line.color
            yax.tick_labels.color = lmap.line.color
            yax.line.line_thickness = 0.6
            if i == 0:
                yax.grid_lines.show = True
                yax.grid_lines.color = lmap.line.color
            elif i == 1:
                yax.minor_grid_lines.show = True
                yax.minor_grid_lines.color = lmap.line.color

        tp.export.save_png('axis_line.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_line.png"
    class="reference internal image-reference"><img
    src="../_images/axis_line.png" style="width: 300px;"
    alt="../_images/axis_line.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------
      [[`grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.grid_lines "tecplot.plot.XYLineAxis.grid_lines"){.reference .internal}                     Major grid lines style control.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.line "tecplot.plot.XYLineAxis.line"){.reference .internal}                                       Axis line style control.
      [[`log_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.log_scale "tecplot.plot.XYLineAxis.log_scale"){.reference .internal}                        Use logarithmic scale for this axis.
      [[`marker_grid_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.marker_grid_line "tecplot.plot.XYLineAxis.marker_grid_line"){.reference .internal}   Marker line to indicate a particular position along an axis.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.max "tecplot.plot.XYLineAxis.max"){.reference .internal}                                          Upper bound of this axis\' range.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.min "tecplot.plot.XYLineAxis.min"){.reference .internal}                                          Lower bound of this axis\' range.
      [[`minor_grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.minor_grid_lines "tecplot.plot.XYLineAxis.minor_grid_lines"){.reference .internal}   Minor grid lines style control.
      [[`reverse`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.reverse "tecplot.plot.XYLineAxis.reverse"){.reference .internal}                              Reverse the direction of the axis scale.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.show "tecplot.plot.XYLineAxis.show"){.reference .internal}                                       Enable drawing of this axis.
      [[`tick_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.tick_labels "tecplot.plot.XYLineAxis.tick_labels"){.reference .internal}                  Axis ticks labels style control.
      [[`ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.ticks "tecplot.plot.XYLineAxis.ticks"){.reference .internal}                                    Axis major and minor ticks style control.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.title "tecplot.plot.XYLineAxis.title"){.reference .internal}                                    Axis title.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
      [[`adjust_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.adjust_range_to_nice "tecplot.plot.XYLineAxis.adjust_range_to_nice"){.reference .internal}()   Rounds the axis range to the nearest major axis increment.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.fit_range "tecplot.plot.XYLineAxis.fit_range"){.reference .internal}()                                    Set range of axis to variable minimum and maximum.
      [[`fit_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.fit_range_to_nice "tecplot.plot.XYLineAxis.fit_range_to_nice"){.reference .internal}()            Set range of axis to nice values near variable minimum and maximum.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[adjust_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.XYLineAxis.adjust_range_to_nice "Link to this definition"){.headerlink}

:   Rounds the axis range to the nearest major axis increment.

    This method resets the axis-line label values such that all
    currently displayed label values are set to have the smallest number
    of significant digits possible.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.adjust_range_to_nice()
    :::
    ::::

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.XYLineAxis.fit_range "Link to this definition"){.headerlink}

:   Set range of axis to variable minimum and maximum.

    ::: {.admonition .note}
    Note

    If the axis dependency is not [[`Independent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, then this action may also affect the range on another
    axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range()
    :::
    ::::

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.XYLineAxis.fit_range_to_nice "Link to this definition"){.headerlink}

:   Set range of axis to nice values near variable minimum and maximum.

    This method resets the range to equal the minimum and maximum of the
    data being plotted, but makes the axis values "nice" by setting
    labels to have the smallest number of significant digits possible,

    ::: {.admonition .note}
    Note

    If the axis dependency is not independent then this method may also
    affect the range on another axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range_to_nice()
    :::
    ::::

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.grid_lines "Link to this definition"){.headerlink}

:   Major grid lines style control.

    Major grid lines are attached to the locations of the major ticks.
    See [[`minor_grid_lines`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.minor_grid_lines "tecplot.plot.XYLineAxis.minor_grid_lines"){.reference
    .internal} for lines attached to minor ticks. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridLines2D "tecplot.plot.GridLines2D"){.reference
        .internal}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.line "Link to this definition"){.headerlink}

:   Axis line style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DAxisLine`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine "tecplot.plot.Cartesian2DAxisLine"){.reference
        .internal}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[log_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.log_scale "Link to this definition"){.headerlink}

:   Use logarithmic scale for this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> # or "plot.axes.r_axis" for the radial axis in polar plots
        >>> axis.log_scale = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[marker_grid_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.marker_grid_line "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.marker_grid_line.show = True
        >>> axis.marker_grid_line.position = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`MarkerGridLine2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D "tecplot.plot.MarkerGridLine2D"){.reference
        .internal}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.max "Link to this definition"){.headerlink}

:   Upper bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 1.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.min "Link to this definition"){.headerlink}

:   Lower bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.min = 0.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[minor_grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.minor_grid_lines "Link to this definition"){.headerlink}

:   Minor grid lines style control.

    Minor grid lines are attached to the locations of the minor ticks.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.minor_grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`MinorGridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D "tecplot.plot.MinorGridLines2D"){.reference
        .internal}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[reverse]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.reverse "Link to this definition"){.headerlink}

:   Reverse the direction of the axis scale.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.reverse = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[tick_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.tick_labels "Link to this definition"){.headerlink}

:   Axis ticks labels style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.tick_labels.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickLabels2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.TickLabels2D "tecplot.plot.TickLabels2D"){.reference
        .internal}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.ticks "Link to this definition"){.headerlink}

:   Axis major and minor ticks style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.ticks.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`Ticks2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Ticks2D "tecplot.plot.Ticks2D"){.reference
        .internal}

<!-- -->

[[XYLineAxis.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLineAxis.title "Link to this definition"){.headerlink}

:   Axis title.

    This is the primary label for the axis and usually includes units:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}
:::

::: {#polarlineaxes .section}
### [PolarLineAxes](#id61){.toc-backref role="doc-backlink"}[¶](#polarlineaxes "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarLineAxes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#PolarLineAxes){.reference .internal}[¶](#tecplot.plot.PolarLineAxes "Link to this definition"){.headerlink}

:   (R, Theta) axes style control for polar plots.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode

        frame = tp.active_frame()

        npoints = 300
        r = np.linspace(0, 2000, npoints)
        theta = np.linspace(0, 10, npoints)

        dataset = frame.create_dataset('Data', ['R', 'Theta'])
        zone = dataset.add_ordered_zone('Zone', (300,))
        zone.values('R')[:] = r
        zone.values('Theta')[:] = theta

        plot = frame.plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.r_axis.max = np.max(r)
        plot.axes.theta_axis.mode = ThetaMode.Radians

        plot.delete_linemaps()
        lmap = plot.add_linemap('Linemap', zone, dataset.variable('R'),
                                dataset.variable('Theta'))
        lmap.line.line_thickness = 0.8

        plot.view.fit()

        tp.export.save_png('axes_polar.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axes_polar.png"
    class="reference internal image-reference"><img
    src="../_images/axes_polar.png" style="width: 300px;"
    alt="../_images/axes_polar.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------
      [[`grid_area`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLineAxes.grid_area "tecplot.plot.PolarLineAxes.grid_area"){.reference .internal}                  Area bounded by the axes.
      [[`precise_grid`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLineAxes.precise_grid "tecplot.plot.PolarLineAxes.precise_grid"){.reference .internal}         Precise dot grid.
      [[`preserve_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLineAxes.preserve_scale "tecplot.plot.PolarLineAxes.preserve_scale"){.reference .internal}   Preserve scale (spacing between ticks) on range change.
      [[`r_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLineAxes.r_axis "tecplot.plot.PolarLineAxes.r_axis"){.reference .internal}                           Radial axis style control.
      [[`theta_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLineAxes.theta_axis "tecplot.plot.PolarLineAxes.theta_axis"){.reference .internal}               Polar-angle axis style control.
      [[`viewport`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLineAxes.viewport "tecplot.plot.PolarLineAxes.viewport"){.reference .internal}                     Area of the frame used by the plot axes outside the grid area.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------

<!-- -->

[[PolarLineAxes.]{.pre}]{.sig-prename .descclassname}[[grid_area]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLineAxes.grid_area "Link to this definition"){.headerlink}

:   Area bounded by the axes.

    This controls the background color and border of the axes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridArea`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridArea "tecplot.plot.GridArea"){.reference
        .internal}

<!-- -->

[[PolarLineAxes.]{.pre}]{.sig-prename .descclassname}[[precise_grid]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLineAxes.precise_grid "Link to this definition"){.headerlink}

:   Precise dot grid.

    This is a set of small dots drawn at the intersection of every minor
    gridline. In line plots, the axis assignments for the first active
    mapping govern the precise dot grid. The precise dot grid option is
    disabled for the 3D Cartesian plots and Line plots when either axis
    for the first active line mapping uses a log scale:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PreciseGrid`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.PreciseGrid "tecplot.plot.PreciseGrid"){.reference
        .internal}

<!-- -->

[[PolarLineAxes.]{.pre}]{.sig-prename .descclassname}[[preserve_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLineAxes.preserve_scale "Link to this definition"){.headerlink}

:   Preserve scale (spacing between ticks) on range change.

    This maintains the axis scaling, i.e. the distance between values
    along the axis. If [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the axes length will be preserved when the range
    changes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.preserve_scale = False
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 10 # axis scale is changed (length is preserved)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLineAxes.]{.pre}]{.sig-prename .descclassname}[[r_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLineAxes.r_axis "Link to this definition"){.headerlink}

:   Radial axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.title.text = 'R (meters)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`RadialLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis "tecplot.plot.RadialLineAxis"){.reference
        .internal}

<!-- -->

[[PolarLineAxes.]{.pre}]{.sig-prename .descclassname}[[theta_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLineAxes.theta_axis "Link to this definition"){.headerlink}

:   Polar-angle axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.title.text = 'Theta (radians)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarAngleLineAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis "tecplot.plot.PolarAngleLineAxis"){.reference
        .internal}

<!-- -->

[[PolarLineAxes.]{.pre}]{.sig-prename .descclassname}[[viewport]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLineAxes.viewport "Link to this definition"){.headerlink}

:   Area of the frame used by the plot axes outside the grid area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.viewport.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarViewport`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.PolarViewport "tecplot.plot.PolarViewport"){.reference
        .internal}
:::

::: {#radiallineaxis .section}
### [RadialLineAxis](#id62){.toc-backref role="doc-backlink"}[¶](#radiallineaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[RadialLineAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#RadialLineAxis){.reference .internal}[¶](#tecplot.plot.RadialLineAxis "Link to this definition"){.headerlink}

:   The R axis for polar plots

    See the example shown for the [[`theta`{.xref .any .py .py-class
    .docutils .literal .notranslate}]{.pre}` `{.xref .any .py .py-class
    .docutils .literal .notranslate}[`axis`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis "tecplot.plot.PolarAngleLineAxis"){.reference
    .internal}.

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------
      [[`clip_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.clip_data "tecplot.plot.RadialLineAxis.clip_data"){.reference .internal}                        Do not show data outside the axes area.
      [[`grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.grid_lines "tecplot.plot.RadialLineAxis.grid_lines"){.reference .internal}                     Major grid lines style control.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.line "tecplot.plot.RadialLineAxis.line"){.reference .internal}                                       Radial axis line style control.
      [[`log_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.log_scale "tecplot.plot.RadialLineAxis.log_scale"){.reference .internal}                        Use logarithmic scale for this axis.
      [[`marker_grid_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.marker_grid_line "tecplot.plot.RadialLineAxis.marker_grid_line"){.reference .internal}   Marker line to indicate a particular position along an axis.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.max "tecplot.plot.RadialLineAxis.max"){.reference .internal}                                          Upper bound of this axis\' range.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.min "tecplot.plot.RadialLineAxis.min"){.reference .internal}                                          Lower bound of this axis\' range.
      [[`minor_grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.minor_grid_lines "tecplot.plot.RadialLineAxis.minor_grid_lines"){.reference .internal}   Minor grid lines style control.
      [[`origin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.origin "tecplot.plot.RadialLineAxis.origin"){.reference .internal}                                 Value at the origin of the axis.
      [[`reverse`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.reverse "tecplot.plot.RadialLineAxis.reverse"){.reference .internal}                              Reverse the direction of the axis scale.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.show "tecplot.plot.RadialLineAxis.show"){.reference .internal}                                       Enable drawing of this axis.
      [[`tick_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.tick_labels "tecplot.plot.RadialLineAxis.tick_labels"){.reference .internal}                  Axis ticks labels style control.
      [[`ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.ticks "tecplot.plot.RadialLineAxis.ticks"){.reference .internal}                                    Axis major and minor ticks style control.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.title "tecplot.plot.RadialLineAxis.title"){.reference .internal}                                    Axis title.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
      [[`adjust_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.adjust_range_to_nice "tecplot.plot.RadialLineAxis.adjust_range_to_nice"){.reference .internal}()   Rounds the axis range to the nearest major axis increment.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.fit_range "tecplot.plot.RadialLineAxis.fit_range"){.reference .internal}()                                    Set range of axis to variable minimum and maximum.
      [[`fit_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialLineAxis.fit_range_to_nice "tecplot.plot.RadialLineAxis.fit_range_to_nice"){.reference .internal}()            Set range of axis to nice values near variable minimum and maximum.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[adjust_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.RadialLineAxis.adjust_range_to_nice "Link to this definition"){.headerlink}

:   Rounds the axis range to the nearest major axis increment.

    This method resets the axis-line label values such that all
    currently displayed label values are set to have the smallest number
    of significant digits possible.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.adjust_range_to_nice()
    :::
    ::::

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[clip_data]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.clip_data "Link to this definition"){.headerlink}

:   Do not show data outside the axes area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.clip_data = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.RadialLineAxis.fit_range "Link to this definition"){.headerlink}

:   Set range of axis to variable minimum and maximum.

    ::: {.admonition .note}
    Note

    If the axis dependency is not [[`Independent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, then this action may also affect the range on another
    axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range()
    :::
    ::::

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.RadialLineAxis.fit_range_to_nice "Link to this definition"){.headerlink}

:   Set range of axis to nice values near variable minimum and maximum.

    This method resets the range to equal the minimum and maximum of the
    data being plotted, but makes the axis values "nice" by setting
    labels to have the smallest number of significant digits possible,

    ::: {.admonition .note}
    Note

    If the axis dependency is not independent then this method may also
    affect the range on another axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range_to_nice()
    :::
    ::::

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.grid_lines "Link to this definition"){.headerlink}

:   Major grid lines style control.

    Major grid lines are attached to the locations of the major ticks.
    See [[`minor_grid_lines`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.minor_grid_lines "tecplot.plot.XYLineAxis.minor_grid_lines"){.reference
    .internal} for lines attached to minor ticks. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridLines2D "tecplot.plot.GridLines2D"){.reference
        .internal}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.line "Link to this definition"){.headerlink}

:   Radial axis line style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.line.line_thickness = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`RadialAxisLine2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D "tecplot.plot.RadialAxisLine2D"){.reference
        .internal}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[log_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.log_scale "Link to this definition"){.headerlink}

:   Use logarithmic scale for this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> # or "plot.axes.r_axis" for the radial axis in polar plots
        >>> axis.log_scale = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[marker_grid_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.marker_grid_line "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.marker_grid_line.show = True
        >>> axis.marker_grid_line.position = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`MarkerGridLine2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D "tecplot.plot.MarkerGridLine2D"){.reference
        .internal}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.max "Link to this definition"){.headerlink}

:   Upper bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 1.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.min "Link to this definition"){.headerlink}

:   Lower bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.min = 0.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[minor_grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.minor_grid_lines "Link to this definition"){.headerlink}

:   Minor grid lines style control.

    Minor grid lines are attached to the locations of the minor ticks.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.minor_grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`MinorGridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D "tecplot.plot.MinorGridLines2D"){.reference
        .internal}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[origin]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.origin "Link to this definition"){.headerlink}

:   Value at the origin of the axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        # value at center of plot equal to 10
        >>> plot.axes.r_axis.origin = 10
        # rotate theta axis 45 degrees clockwise
        >>> plot.axes.theta_axis.origin = 45
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[reverse]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.reverse "Link to this definition"){.headerlink}

:   Reverse the direction of the axis scale.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.reverse = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[tick_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.tick_labels "Link to this definition"){.headerlink}

:   Axis ticks labels style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.tick_labels.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`RadialTickLabels`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels "tecplot.plot.RadialTickLabels"){.reference
        .internal}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.ticks "Link to this definition"){.headerlink}

:   Axis major and minor ticks style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.ticks.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`RadialTicks`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.RadialTicks "tecplot.plot.RadialTicks"){.reference
        .internal}

<!-- -->

[[RadialLineAxis.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialLineAxis.title "Link to this definition"){.headerlink}

:   Axis title.

    This is the primary label for the axis and usually includes units:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}
:::

::: {#polaranglelineaxis .section}
### [PolarAngleLineAxis](#id63){.toc-backref role="doc-backlink"}[¶](#polaranglelineaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarAngleLineAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#PolarAngleLineAxis){.reference .internal}[¶](#tecplot.plot.PolarAngleLineAxis "Link to this definition"){.headerlink}

:   Theta axis for polar plots.

    This example manipulates both the theta and radial axes to produce a
    star plot. Custom labels are created for each data point:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode, NumberFormat, AxisAlignment

        np.random.seed(2)
        npoints = 7
        theta = np.linspace(0, npoints, npoints+1)

        frame = tp.active_frame()
        dataset = frame.create_dataset('Data', ['Magnitude', 'Property'])

        for i in range(3):
            r = list(np.random.uniform(0.01, 0.99, npoints))
            r.append(r[0])
            zone = dataset.add_ordered_zone('Zone {}'.format(i), (npoints+1,))
            zone.values('Magnitude')[:] = r
            zone.values('Property')[:] = theta

        plot = frame.plot(PlotType.PolarLine)
        plot.activate()
        plot.delete_linemaps()

        for i, zone in enumerate(dataset.zones()):
            lmap = plot.add_linemap('Linemap {}'.format(i), zone,
                                    dataset.variable('Magnitude'),
                                    dataset.variable('Property'))
            lmap.line.line_thickness = 0.8

        r_axis = plot.axes.r_axis
        r_axis.max = 1
        r_axis.line.show = False
        r_axis.title.position = 85
        r_axis.line.alignment = AxisAlignment.WithOpposingAxisValue
        r_axis.line.opposing_axis_value = 1

        theta_axis = plot.axes.theta_axis
        theta_axis.origin = 1
        theta_axis.mode = ThetaMode.Arbitrary
        theta_axis.min = 0
        theta_axis.max = theta.max()
        theta_axis.period = npoints
        theta_axis.ticks.auto_spacing = False
        theta_axis.ticks.spacing = 1
        theta_axis.ticks.minor_num_ticks = 0
        theta_axis.title.show = False

        theta_labels = theta_axis.tick_labels.format
        theta_labels.format_type = NumberFormat.CustomLabel
        theta_labels.add_custom_labels('A', 'B', 'C', 'D', 'E', 'F', 'G')
        theta_labels.custom_labels_index = 0

        plot.view.fit()

        tp.export.save_png('star_plot.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/star_plot.png"
    class="reference internal image-reference"><img
    src="../_images/star_plot.png" style="width: 300px;"
    alt="../_images/star_plot.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------
      [[`clip_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.clip_data "tecplot.plot.PolarAngleLineAxis.clip_data"){.reference .internal}                        Do not show data outside the axes area.
      [[`grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.grid_lines "tecplot.plot.PolarAngleLineAxis.grid_lines"){.reference .internal}                     Theta angle major grid lines.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.line "tecplot.plot.PolarAngleLineAxis.line"){.reference .internal}                                       Axis line style control.
      [[`marker_grid_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.marker_grid_line "tecplot.plot.PolarAngleLineAxis.marker_grid_line"){.reference .internal}   Theta angle marker grid line.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.max "tecplot.plot.PolarAngleLineAxis.max"){.reference .internal}                                          Upper bound of this axis\' range.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.min "tecplot.plot.PolarAngleLineAxis.min"){.reference .internal}                                          Lower bound of this axis\' range.
      [[`minor_grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.minor_grid_lines "tecplot.plot.PolarAngleLineAxis.minor_grid_lines"){.reference .internal}   Theta angle minor grid lines.
      [[`mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.mode "tecplot.plot.PolarAngleLineAxis.mode"){.reference .internal}                                       Units or scale used for the theta axis.
      [[`origin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.origin "tecplot.plot.PolarAngleLineAxis.origin"){.reference .internal}                                 Value at the origin of the axis.
      [[`period`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.period "tecplot.plot.PolarAngleLineAxis.period"){.reference .internal}                                 Number of (min, max) cycles to include in 360 degrees.
      [[`reverse`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.reverse "tecplot.plot.PolarAngleLineAxis.reverse"){.reference .internal}                              Reverse the direction of the axis scale.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.show "tecplot.plot.PolarAngleLineAxis.show"){.reference .internal}                                       Enable drawing of this axis.
      [[`tick_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.tick_labels "tecplot.plot.PolarAngleLineAxis.tick_labels"){.reference .internal}                  Axis ticks labels style control.
      [[`ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.ticks "tecplot.plot.PolarAngleLineAxis.ticks"){.reference .internal}                                    Axis major and minor ticks style control.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.title "tecplot.plot.PolarAngleLineAxis.title"){.reference .internal}                                    Axis title.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------

    **Methods**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
      [[`adjust_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.adjust_range_to_nice "tecplot.plot.PolarAngleLineAxis.adjust_range_to_nice"){.reference .internal}()                     Rounds the axis range to the nearest major axis increment.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.fit_range "tecplot.plot.PolarAngleLineAxis.fit_range"){.reference .internal}()                                                      Set range of axis to variable minimum and maximum.
      [[`fit_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.fit_range_to_nice "tecplot.plot.PolarAngleLineAxis.fit_range_to_nice"){.reference .internal}()                              Set range of axis to nice values near variable minimum and maximum.
      [[`set_range_to_entire_circle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleLineAxis.set_range_to_entire_circle "tecplot.plot.PolarAngleLineAxis.set_range_to_entire_circle"){.reference .internal}()   Set theta range to entire circle.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[adjust_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.PolarAngleLineAxis.adjust_range_to_nice "Link to this definition"){.headerlink}

:   Rounds the axis range to the nearest major axis increment.

    This method resets the axis-line label values such that all
    currently displayed label values are set to have the smallest number
    of significant digits possible.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.adjust_range_to_nice()
    :::
    ::::

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[clip_data]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.clip_data "Link to this definition"){.headerlink}

:   Do not show data outside the axes area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.clip_data = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.PolarAngleLineAxis.fit_range "Link to this definition"){.headerlink}

:   Set range of axis to variable minimum and maximum.

    ::: {.admonition .note}
    Note

    If the axis dependency is not [[`Independent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, then this action may also affect the range on another
    axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range()
    :::
    ::::

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.PolarAngleLineAxis.fit_range_to_nice "Link to this definition"){.headerlink}

:   Set range of axis to nice values near variable minimum and maximum.

    This method resets the range to equal the minimum and maximum of the
    data being plotted, but makes the axis values "nice" by setting
    labels to have the smallest number of significant digits possible,

    ::: {.admonition .note}
    Note

    If the axis dependency is not independent then this method may also
    affect the range on another axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range_to_nice()
    :::
    ::::

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.grid_lines "Link to this definition"){.headerlink}

:   Theta angle major grid lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarAngleGridLines`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines "tecplot.plot.PolarAngleGridLines"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.line "Link to this definition"){.headerlink}

:   Axis line style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.line.line_thickness = 0.6
        >>> plot.axes.theta_axis.line.line_thickness = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisLine2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.AxisLine2D "tecplot.plot.AxisLine2D"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[marker_grid_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.marker_grid_line "Link to this definition"){.headerlink}

:   Theta angle marker grid line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.marker_grid_line.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarAngleMarkerGridLine`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine "tecplot.plot.PolarAngleMarkerGridLine"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.max "Link to this definition"){.headerlink}

:   Upper bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 1.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.min "Link to this definition"){.headerlink}

:   Lower bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.min = 0.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[minor_grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.minor_grid_lines "Link to this definition"){.headerlink}

:   Theta angle minor grid lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.minor_grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarAngleMinorGridLines`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines "tecplot.plot.PolarAngleMinorGridLines"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.mode "Link to this definition"){.headerlink}

:   Units or scale used for the theta axis.

    Possible values: [[`ThetaMode.Degrees`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ThetaMode.Degrees "tecplot.constant.ThetaMode.Degrees"){.reference
    .internal}, [[`ThetaMode.Radians`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ThetaMode.Radians "tecplot.constant.ThetaMode.Radians"){.reference
    .internal}, [[`ThetaMode.Arbitrary`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ThetaMode.Arbitrary "tecplot.constant.ThetaMode.Arbitrary"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ThetaMode
        >>> plot.axes.theta_axis.mode = ThetaMode.Radians
    :::
    ::::

    Type[:]{.colon}

    :   [[`ThetaMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ThetaMode "tecplot.constant.ThetaMode"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[origin]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.origin "Link to this definition"){.headerlink}

:   Value at the origin of the axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        # value at center of plot equal to 10
        >>> plot.axes.r_axis.origin = 10
        # rotate theta axis 45 degrees clockwise
        >>> plot.axes.theta_axis.origin = 45
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[period]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.period "Link to this definition"){.headerlink}

:   Number of (min, max) cycles to include in 360 degrees.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.period = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[reverse]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.reverse "Link to this definition"){.headerlink}

:   Reverse the direction of the axis scale.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.reverse = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[set_range_to_entire_circle]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#PolarAngleLineAxis.set_range_to_entire_circle){.reference .internal}[¶](#tecplot.plot.PolarAngleLineAxis.set_range_to_entire_circle "Link to this definition"){.headerlink}

:   Set theta range to entire circle.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.set_range_to_entire_circle()
    :::
    ::::

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[tick_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.tick_labels "Link to this definition"){.headerlink}

:   Axis ticks labels style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.tick_labels.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickLabels2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.TickLabels2D "tecplot.plot.TickLabels2D"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.ticks "Link to this definition"){.headerlink}

:   Axis major and minor ticks style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.ticks.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`Ticks2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Ticks2D "tecplot.plot.Ticks2D"){.reference
        .internal}

<!-- -->

[[PolarAngleLineAxis.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleLineAxis.title "Link to this definition"){.headerlink}

:   Axis title.

    This is the primary label for the axis and usually includes units:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}
:::
::::::::

::::: {#sketch-axes .section}
## [Sketch Axes](#id19){.toc-backref role="doc-backlink"}[¶](#sketch-axes "Link to this heading"){.headerlink}

::: {#sketchaxes .section}
### [SketchAxes](#id20){.toc-backref role="doc-backlink"}[¶](#sketchaxes "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[SketchAxes]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#SketchAxes){.reference .internal}[¶](#tecplot.plot.SketchAxes "Link to this definition"){.headerlink}

:   (X, Y) axes style control for sketch plots.

    Sketch plots have cartesian *x* and *y* axes which can be adjusted
    using the viewport:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import PlotType

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Sketch)

        plot.axes.x_axis.show = True
        plot.axes.y_axis.show = True

        plot.axes.viewport.left = 10
        plot.axes.viewport.right = 90
        plot.axes.viewport.bottom = 10
        plot.axes.viewport.top = 90

        tp.export.save_png('axes_sketch.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axes_sketch.png"
    class="reference internal image-reference"><img
    src="../_images/axes_sketch.png" style="width: 300px;"
    alt="../_images/axes_sketch.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------
      [[`auto_adjust_ranges`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.auto_adjust_ranges "tecplot.plot.SketchAxes.auto_adjust_ranges"){.reference .internal}   Automatically adjust axis ranges to nice values.
      [[`axis_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.axis_mode "tecplot.plot.SketchAxes.axis_mode"){.reference .internal}                              Controls automatic adjustment of axis ranges.
      [[`grid_area`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.grid_area "tecplot.plot.SketchAxes.grid_area"){.reference .internal}                              Area bounded by the axes.
      [[`precise_grid`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.precise_grid "tecplot.plot.SketchAxes.precise_grid"){.reference .internal}                     Precise dot grid.
      [[`preserve_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.preserve_scale "tecplot.plot.SketchAxes.preserve_scale"){.reference .internal}               Preserve scale (spacing between ticks) on range change.
      [[`viewport`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.viewport "tecplot.plot.SketchAxes.viewport"){.reference .internal}                                 Area of the frame used by the plot axes.
      [[`x_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.x_axis "tecplot.plot.SketchAxes.x_axis"){.reference .internal}                                       X-axis style control.
      [[`xy_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.xy_ratio "tecplot.plot.SketchAxes.xy_ratio"){.reference .internal}                                 X:Y axis scaling ratio in percent.
      [[`y_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxes.y_axis "tecplot.plot.SketchAxes.y_axis"){.reference .internal}                                       Y-axis style control.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[auto_adjust_ranges]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.auto_adjust_ranges "Link to this definition"){.headerlink}

:   Automatically adjust axis ranges to nice values.

    Axes limits will be adjusted to have the smallest number of
    significant digits possible:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.auto_adjust_ranges = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[axis_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.axis_mode "Link to this definition"){.headerlink}

:   Controls automatic adjustment of axis ranges.

    Possible values: [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, [[`XYDependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}.

    If set to [[`XYDependent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal}, then setting the range of one axis automatically scales
    the other indicated axes proportionally to maintain the aspect ratio
    of the plot, effectively zooming in or out. If set to
    [[`Independent`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, adjusting the range of one axis has no effect on other
    axes. Defaults to [[`Independent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal} for XY line plots, [[`XYDependent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.XYDependent "tecplot.constant.AxisMode.XYDependent"){.reference
    .internal} for 2D Cartesian plots. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.Independent
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode "tecplot.constant.AxisMode"){.reference
        .internal}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[grid_area]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.grid_area "Link to this definition"){.headerlink}

:   Area bounded by the axes.

    This controls the background color and border of the axes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridArea`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridArea "tecplot.plot.GridArea"){.reference
        .internal}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[precise_grid]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.precise_grid "Link to this definition"){.headerlink}

:   Precise dot grid.

    This is a set of small dots drawn at the intersection of every minor
    gridline. In line plots, the axis assignments for the first active
    mapping govern the precise dot grid. The precise dot grid option is
    disabled for the 3D Cartesian plots and Line plots when either axis
    for the first active line mapping uses a log scale:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PreciseGrid`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.PreciseGrid "tecplot.plot.PreciseGrid"){.reference
        .internal}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[preserve_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.preserve_scale "Link to this definition"){.headerlink}

:   Preserve scale (spacing between ticks) on range change.

    This maintains the axis scaling, i.e. the distance between values
    along the axis. If [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the axes length will be preserved when the range
    changes:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.preserve_scale = False
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 10 # axis scale is changed (length is preserved)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[viewport]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.viewport "Link to this definition"){.headerlink}

:   Area of the frame used by the plot axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.viewport.left = 5
        >>> plot.axes.viewport.right = 95
        >>> plot.axes.viewport.top = 95
        >>> plot.axes.viewport.bottom = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DViewport`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian2DViewport "tecplot.plot.Cartesian2DViewport"){.reference
        .internal}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[x_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.x_axis "Link to this definition"){.headerlink}

:   X-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`SketchAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.SketchAxis "tecplot.plot.SketchAxis"){.reference
        .internal}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[xy_ratio]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.xy_ratio "Link to this definition"){.headerlink}

:   X:Y axis scaling ratio in percent.

    This requires the axes to be in dependent mode:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisMode
        >>> plot.axes.axis_mode = AxisMode.XYDependent
        >>> plot.axes.xy_ratio = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxes.]{.pre}]{.sig-prename .descclassname}[[y_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxes.y_axis "Link to this definition"){.headerlink}

:   Y-axis style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.y_axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`SketchAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.SketchAxis "tecplot.plot.SketchAxis"){.reference
        .internal}
:::

::: {#sketchaxis .section}
### [SketchAxis](#id21){.toc-backref role="doc-backlink"}[¶](#sketchaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[SketchAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*, *[[name]{.pre}]{.n}*, *[[\*\*]{.pre}]{.o}[[kwargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#SketchAxis){.reference .internal}[¶](#tecplot.plot.SketchAxis "Link to this definition"){.headerlink}

:   X or Y axis for sketch plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import PlotType

        plot = tp.active_frame().plot(PlotType.Sketch)

        viewport = plot.axes.viewport
        viewport.left = 10
        viewport.right = 90
        viewport.bottom = 10

        xaxis = plot.axes.x_axis
        xaxis.show = True
        xaxis.min = 0
        xaxis.max = 360
        xaxis.title.text = 'Angle (Degrees)'

        xaxis.ticks.auto_spacing = False
        xaxis.ticks.spacing = 60

        tp.export.save_png('axis_sketch.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_sketch.png"
    class="reference internal image-reference"><img
    src="../_images/axis_sketch.png" style="width: 300px;"
    alt="../_images/axis_sketch.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------
      [[`grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.grid_lines "tecplot.plot.SketchAxis.grid_lines"){.reference .internal}                     Major grid lines style control.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.line "tecplot.plot.SketchAxis.line"){.reference .internal}                                       Axis line style control.
      [[`log_scale`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.log_scale "tecplot.plot.SketchAxis.log_scale"){.reference .internal}                        Use logarithmic scale for this axis.
      [[`marker_grid_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.marker_grid_line "tecplot.plot.SketchAxis.marker_grid_line"){.reference .internal}   Marker line to indicate a particular position along an axis.
      [[`max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.max "tecplot.plot.SketchAxis.max"){.reference .internal}                                          Upper bound of this axis\' range.
      [[`min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.min "tecplot.plot.SketchAxis.min"){.reference .internal}                                          Lower bound of this axis\' range.
      [[`minor_grid_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.minor_grid_lines "tecplot.plot.SketchAxis.minor_grid_lines"){.reference .internal}   Minor grid lines style control.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.show "tecplot.plot.SketchAxis.show"){.reference .internal}                                       Enable drawing of this axis.
      [[`tick_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.tick_labels "tecplot.plot.SketchAxis.tick_labels"){.reference .internal}                  Axis ticks labels style control.
      [[`ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.ticks "tecplot.plot.SketchAxis.ticks"){.reference .internal}                                    Axis major and minor ticks style control.
      [[`title`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.title "tecplot.plot.SketchAxis.title"){.reference .internal}                                    Axis title.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------
      [[`adjust_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.adjust_range_to_nice "tecplot.plot.SketchAxis.adjust_range_to_nice"){.reference .internal}()   Rounds the axis range to the nearest major axis increment.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.fit_range "tecplot.plot.SketchAxis.fit_range"){.reference .internal}()                                    Set range of axis to variable minimum and maximum.
      [[`fit_range_to_nice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchAxis.fit_range_to_nice "tecplot.plot.SketchAxis.fit_range_to_nice"){.reference .internal}()            Set range of axis to nice values near variable minimum and maximum.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[adjust_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.SketchAxis.adjust_range_to_nice "Link to this definition"){.headerlink}

:   Rounds the axis range to the nearest major axis increment.

    This method resets the axis-line label values such that all
    currently displayed label values are set to have the smallest number
    of significant digits possible.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.adjust_range_to_nice()
    :::
    ::::

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.SketchAxis.fit_range "Link to this definition"){.headerlink}

:   Set range of axis to variable minimum and maximum.

    ::: {.admonition .note}
    Note

    If the axis dependency is not [[`Independent`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisMode.Independent "tecplot.constant.AxisMode.Independent"){.reference
    .internal}, then this action may also affect the range on another
    axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range()
    :::
    ::::

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[fit_range_to_nice]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.SketchAxis.fit_range_to_nice "Link to this definition"){.headerlink}

:   Set range of axis to nice values near variable minimum and maximum.

    This method resets the range to equal the minimum and maximum of the
    data being plotted, but makes the axis values "nice" by setting
    labels to have the smallest number of significant digits possible,

    ::: {.admonition .note}
    Note

    If the axis dependency is not independent then this method may also
    affect the range on another axis.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.fit_range_to_nice()
    :::
    ::::

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.grid_lines "Link to this definition"){.headerlink}

:   Major grid lines style control.

    Major grid lines are attached to the locations of the major ticks.
    See [[`minor_grid_lines`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLineAxis.minor_grid_lines "tecplot.plot.XYLineAxis.minor_grid_lines"){.reference
    .internal} for lines attached to minor ticks. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`GridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.GridLines2D "tecplot.plot.GridLines2D"){.reference
        .internal}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.line "Link to this definition"){.headerlink}

:   Axis line style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DAxisLine`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine "tecplot.plot.Cartesian2DAxisLine"){.reference
        .internal}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[log_scale]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.log_scale "Link to this definition"){.headerlink}

:   Use logarithmic scale for this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> # or "plot.axes.r_axis" for the radial axis in polar plots
        >>> axis.log_scale = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[marker_grid_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.marker_grid_line "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.marker_grid_line.show = True
        >>> axis.marker_grid_line.position = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`MarkerGridLine2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D "tecplot.plot.MarkerGridLine2D"){.reference
        .internal}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.max "Link to this definition"){.headerlink}

:   Upper bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.max = 1.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.min "Link to this definition"){.headerlink}

:   Lower bound of this axis' range.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.min = 0.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[minor_grid_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.minor_grid_lines "Link to this definition"){.headerlink}

:   Minor grid lines style control.

    Minor grid lines are attached to the locations of the minor ticks.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.minor_grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`MinorGridLines2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D "tecplot.plot.MinorGridLines2D"){.reference
        .internal}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[tick_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.tick_labels "Link to this definition"){.headerlink}

:   Axis ticks labels style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.tick_labels.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickLabels2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.TickLabels2D "tecplot.plot.TickLabels2D"){.reference
        .internal}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.ticks "Link to this definition"){.headerlink}

:   Axis major and minor ticks style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.ticks.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`Ticks2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Ticks2D "tecplot.plot.Ticks2D"){.reference
        .internal}

<!-- -->

[[SketchAxis.]{.pre}]{.sig-prename .descclassname}[[title]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchAxis.title "Link to this definition"){.headerlink}

:   Axis title.

    This is the primary label for the axis and usually includes units:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}
:::
:::::

::::::::::::::::::::::::::::::::::: {#axis-elements .section}
## [Axis Elements](#id22){.toc-backref role="doc-backlink"}[¶](#axis-elements "Link to this heading"){.headerlink}

- [Axis Line](#axis-line){#id64 .reference .internal}

  - [AxisLine2D](#axisline2d){#id65 .reference .internal}

  - [Cartesian2DAxisLine](#cartesian2daxisline){#id66 .reference
    .internal}

  - [AxisLine3D](#axisline3d){#id67 .reference .internal}

  - [RadialAxisLine2D](#radialaxisline2d){#id68 .reference .internal}

- [Ticks and Labels](#ticks-and-labels){#id69 .reference .internal}

  - [Ticks2D](#ticks2d){#id70 .reference .internal}

  - [Ticks3D](#ticks3d){#id71 .reference .internal}

  - [RadialTicks](#radialticks){#id72 .reference .internal}

  - [TickLabels2D](#ticklabels2d){#id73 .reference .internal}

  - [TickLabels3D](#ticklabels3d){#id74 .reference .internal}

  - [RadialTickLabels](#radialticklabels){#id75 .reference .internal}

- [Axis Title](#axis-title){#id76 .reference .internal}

  - [Axis2DTitle](#axis2dtitle){#id77 .reference .internal}

  - [DataAxis2DTitle](#dataaxis2dtitle){#id78 .reference .internal}

  - [DataAxis3DTitle](#dataaxis3dtitle){#id79 .reference .internal}

  - [RadialAxisTitle](#radialaxistitle){#id80 .reference .internal}

- [Grid Area](#grid-area){#id81 .reference .internal}

  - [GridArea](#gridarea){#id82 .reference .internal}

  - [Cartesian2DGridArea](#cartesian2dgridarea){#id83 .reference
    .internal}

  - [Cartesian3DGridArea](#cartesian3dgridarea){#id84 .reference
    .internal}

  - [PreciseGrid](#precisegrid){#id85 .reference .internal}

  - [GridLines](#gridlines){#id86 .reference .internal}

  - [GridLines2D](#gridlines2d){#id87 .reference .internal}

  - [MinorGridLines](#minorgridlines){#id88 .reference .internal}

  - [MinorGridLines2D](#minorgridlines2d){#id89 .reference .internal}

  - [PolarAngleGridLines](#polaranglegridlines){#id90 .reference
    .internal}

  - [PolarAngleMinorGridLines](#polarangleminorgridlines){#id91
    .reference .internal}

  - [MarkerGridLine](#markergridline){#id92 .reference .internal}

  - [MarkerGridLine2D](#markergridline2d){#id93 .reference .internal}

  - [PolarAngleMarkerGridLine](#polaranglemarkergridline){#id94
    .reference .internal}

- [OrientationAxis](#orientationaxis){#id95 .reference .internal}

::::::: {#axis-line .section}
### [Axis Line](#id64){.toc-backref role="doc-backlink"}[¶](#axis-line "Link to this heading"){.headerlink}

- [AxisLine2D](#axisline2d){#id96 .reference .internal}

- [Cartesian2DAxisLine](#cartesian2daxisline){#id97 .reference
  .internal}

- [AxisLine3D](#axisline3d){#id98 .reference .internal}

- [RadialAxisLine2D](#radialaxisline2d){#id99 .reference .internal}

::: {#axisline2d .section}
#### [AxisLine2D](#id96){.toc-backref role="doc-backlink"}[¶](#axisline2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[AxisLine2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#AxisLine2D){.reference .internal}[¶](#tecplot.plot.AxisLine2D "Link to this definition"){.headerlink}

:   Graduated axis line for 2D plots.

    Cartesian *(x, y)* plots use an extension of this class
    ([[`Cartesian2DAxisLine`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine "tecplot.plot.Cartesian2DAxisLine"){.reference
    .internal}). Polar plots use this class directly:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode

        npoints = 300
        r = np.linspace(0, 2000, npoints)
        theta = np.linspace(0, 10, npoints)

        frame = tp.active_frame()
        dataset = frame.create_dataset('Data', ['R', 'Theta'])
        zone = dataset.add_ordered_zone('Zone', (300,))
        zone.values('R')[:] = r
        zone.values('Theta')[:] = theta
        plot = frame.plot(PlotType.PolarLine)
        plot.activate()

        plot.delete_linemaps()
        lmap = plot.add_linemap('Linemap', zone, dataset.variable('R'),
                                dataset.variable('Theta'))
        lmap.line.line_thickness = 0.8

        r_axis = plot.axes.r_axis
        r_axis.max = np.max(r)
        r_axis.tick_labels.angle = 45
        r_axis.tick_labels.font.size *= 2

        theta_axis = plot.axes.theta_axis
        theta_axis.mode = ThetaMode.Radians
        theta_axis.tick_labels.font.size *= 2

        plot.view.fit()

        tp.export.save_png('axis_line_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_line_2d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_line_2d.png" style="width: 300px;"
    alt="../_images/axis_line_2d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------
      [[`alignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.alignment "tecplot.plot.AxisLine2D.alignment"){.reference .internal}                                 Axis line placement.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.color "tecplot.plot.AxisLine2D.color"){.reference .internal}                                             Color of the axis line.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.line_thickness "tecplot.plot.AxisLine2D.line_thickness"){.reference .internal}                  Width of the axis line to be drawn.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.offset "tecplot.plot.AxisLine2D.offset"){.reference .internal}                                          Axis line placement with respect to the grid border.
      [[`opposing_axis_value`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.opposing_axis_value "tecplot.plot.AxisLine2D.opposing_axis_value"){.reference .internal}   Axis line placement with respect to the opposing axis.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.show "tecplot.plot.AxisLine2D.show"){.reference .internal}                                                Draw the primary axis line on the plot.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------

<!-- -->

[[AxisLine2D.]{.pre}]{.sig-prename .descclassname}[[alignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine2D.alignment "Link to this definition"){.headerlink}

:   Axis line placement.

    Possible values: [[`WithViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithViewport "tecplot.constant.AxisAlignment.WithViewport"){.reference
    .internal}, [[`WithOpposingAxisValue`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithOpposingAxisValue "tecplot.constant.AxisAlignment.WithOpposingAxisValue"){.reference
    .internal}, [[`WithGridMin`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridMin "tecplot.constant.AxisAlignment.WithGridMin"){.reference
    .internal}, [[`WithGridMax`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridMax "tecplot.constant.AxisAlignment.WithGridMax"){.reference
    .internal}, [[`WithGridAreaTop`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaTop "tecplot.constant.AxisAlignment.WithGridAreaTop"){.reference
    .internal}, [[`WithGridAreaBottom`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaBottom "tecplot.constant.AxisAlignment.WithGridAreaBottom"){.reference
    .internal}, [[`WithGridAreaLeft`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaLeft "tecplot.constant.AxisAlignment.WithGridAreaLeft"){.reference
    .internal} or [[`WithGridAreaRight`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaRight "tecplot.constant.AxisAlignment.WithGridAreaRight"){.reference
    .internal}.

    Not all values will be available for every plot type. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.alignment = AxisAlignment.WithGridMin
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisAlignment`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment "tecplot.constant.AxisAlignment"){.reference
        .internal}

<!-- -->

[[AxisLine2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine2D.color "Link to this definition"){.headerlink}

:   Color of the axis line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[AxisLine2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the axis line to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[AxisLine2D.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine2D.offset "Link to this definition"){.headerlink}

:   Axis line placement with respect to the grid border.

    This is the offset from the grid border-aligned position dictated by
    properties such as [[`AxisLine2D.alignment`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.alignment "tecplot.plot.AxisLine2D.alignment"){.reference
    .internal}. The example moves the axis line into the plot by 5% of
    the frame height:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.offset = -5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[AxisLine2D.]{.pre}]{.sig-prename .descclassname}[[opposing_axis_value]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine2D.opposing_axis_value "Link to this definition"){.headerlink}

:   Axis line placement with respect to the opposing axis.

    The axis alignment must be set to
    [[`AxisAlignment.WithOpposingAxisValue`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithOpposingAxisValue "tecplot.constant.AxisAlignment.WithOpposingAxisValue"){.reference
    .internal} to make this property relevant:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.alignment = AxisAlignment.WithOpposingAxisValue
        >>> axis.line.opposing_axis_value = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[AxisLine2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine2D.show "Link to this definition"){.headerlink}

:   Draw the primary axis line on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#cartesian2daxisline .section}
#### [Cartesian2DAxisLine](#id97){.toc-backref role="doc-backlink"}[¶](#cartesian2daxisline "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DAxisLine]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#Cartesian2DAxisLine){.reference .internal}[¶](#tecplot.plot.Cartesian2DAxisLine "Link to this definition"){.headerlink}

:   Axis line for 2D field plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, AxisAlignment

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'CircularContour.plt')
        dataset = tp.data.load_tecplot(infile)

        plot = tp.active_frame().plot(PlotType.Cartesian2D)
        plot.activate()

        plot.show_contour = True
        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'

        plot.axes.preserve_scale = True
        plot.axes.x_axis.fit_range()

        for ax in plot.axes:
            line = ax.line
            line.color = Color.DeepRed
            line.alignment = AxisAlignment.WithOpposingAxisValue
            line.opposing_axis_value = 0
            ax.title.position = 85

        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('axis_line_cartesian2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_line_cartesian2d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_line_cartesian2d.png" style="width: 300px;"
    alt="../_images/axis_line_cartesian2d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------
      [[`alignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.alignment "tecplot.plot.Cartesian2DAxisLine.alignment"){.reference .internal}                                 Axis line placement.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.color "tecplot.plot.Cartesian2DAxisLine.color"){.reference .internal}                                             Color of the axis line.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.line_thickness "tecplot.plot.Cartesian2DAxisLine.line_thickness"){.reference .internal}                  Width of the axis line to be drawn.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.offset "tecplot.plot.Cartesian2DAxisLine.offset"){.reference .internal}                                          Axis line placement with respect to the grid border.
      [[`opposing_axis_value`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.opposing_axis_value "tecplot.plot.Cartesian2DAxisLine.opposing_axis_value"){.reference .internal}   Axis line placement with respect to the opposing axis.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.position "tecplot.plot.Cartesian2DAxisLine.position"){.reference .internal}                                    Axis line placement with respect to the viewport.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DAxisLine.show "tecplot.plot.Cartesian2DAxisLine.show"){.reference .internal}                                                Draw the primary axis line on the plot.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[alignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.alignment "Link to this definition"){.headerlink}

:   Axis line placement.

    Possible values: [[`WithViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithViewport "tecplot.constant.AxisAlignment.WithViewport"){.reference
    .internal}, [[`WithOpposingAxisValue`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithOpposingAxisValue "tecplot.constant.AxisAlignment.WithOpposingAxisValue"){.reference
    .internal}, [[`WithGridMin`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridMin "tecplot.constant.AxisAlignment.WithGridMin"){.reference
    .internal}, [[`WithGridMax`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridMax "tecplot.constant.AxisAlignment.WithGridMax"){.reference
    .internal}, [[`WithGridAreaTop`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaTop "tecplot.constant.AxisAlignment.WithGridAreaTop"){.reference
    .internal}, [[`WithGridAreaBottom`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaBottom "tecplot.constant.AxisAlignment.WithGridAreaBottom"){.reference
    .internal}, [[`WithGridAreaLeft`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaLeft "tecplot.constant.AxisAlignment.WithGridAreaLeft"){.reference
    .internal} or [[`WithGridAreaRight`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaRight "tecplot.constant.AxisAlignment.WithGridAreaRight"){.reference
    .internal}.

    Not all values will be available for every plot type. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.alignment = AxisAlignment.WithGridMin
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisAlignment`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment "tecplot.constant.AxisAlignment"){.reference
        .internal}

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.color "Link to this definition"){.headerlink}

:   Color of the axis line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.line_thickness "Link to this definition"){.headerlink}

:   Width of the axis line to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.offset "Link to this definition"){.headerlink}

:   Axis line placement with respect to the grid border.

    This is the offset from the grid border-aligned position dictated by
    properties such as [[`AxisLine2D.alignment`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.alignment "tecplot.plot.AxisLine2D.alignment"){.reference
    .internal}. The example moves the axis line into the plot by 5% of
    the frame height:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.offset = -5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[opposing_axis_value]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.opposing_axis_value "Link to this definition"){.headerlink}

:   Axis line placement with respect to the opposing axis.

    The axis alignment must be set to
    [[`AxisAlignment.WithOpposingAxisValue`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithOpposingAxisValue "tecplot.constant.AxisAlignment.WithOpposingAxisValue"){.reference
    .internal} to make this property relevant:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.alignment = AxisAlignment.WithOpposingAxisValue
        >>> axis.line.opposing_axis_value = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.position "Link to this definition"){.headerlink}

:   Axis line placement with respect to the viewport.

    The axis alignment must be set to
    [[`AxisAlignment.WithViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithViewport "tecplot.constant.AxisAlignment.WithViewport"){.reference
    .internal} to make this property relevant:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.alignment = AxisAlignment.WithViewport
        >>> axis.line.position = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DAxisLine.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DAxisLine.show "Link to this definition"){.headerlink}

:   Draw the primary axis line on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#axisline3d .section}
#### [AxisLine3D](#id98){.toc-backref role="doc-backlink"}[¶](#axisline3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[AxisLine3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#AxisLine3D){.reference .internal}[¶](#tecplot.plot.AxisLine3D "Link to this definition"){.headerlink}

:   X, Y or Z axis for 3D field plots.

    This represents the line along which ticks and labels are drawn. The
    color affects the line itself and the associated tick marks but not
    labels or axis titles:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        dataset = tp.load_layout(infile)

        frame = tp.active_frame()
        plot = frame.plot()

        plot.show_mesh = False
        plot.axes.grid_area.fill_color = Color.Grey

        for ax in [plot.axes.x_axis, plot.axes.y_axis, plot.axes.z_axis]:
            ax.show = True
            ax.grid_lines.show = False
            ax.line.color = Color.Cyan
            ax.line.line_thickness = 0.2
            ax.line.show_on_opposite_edge = True

        plot.view.fit()

        tp.export.save_png('axis_line_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_line_3d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_line_3d.png" style="width: 300px;"
    alt="../_images/axis_line_3d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine3D.color "tecplot.plot.AxisLine3D.color"){.reference .internal}                                                   Color of the axis line.
      [[`edge_assignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine3D.edge_assignment "tecplot.plot.AxisLine3D.edge_assignment"){.reference .internal}                     Edge to use when drawing the primary axis line.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine3D.line_thickness "tecplot.plot.AxisLine3D.line_thickness"){.reference .internal}                        Width of the axis line to be drawn.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine3D.show "tecplot.plot.AxisLine3D.show"){.reference .internal}                                                      Draw the primary axis line on the plot.
      [[`show_on_opposite_edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.AxisLine3D.show_on_opposite_edge "tecplot.plot.AxisLine3D.show_on_opposite_edge"){.reference .internal}   Draw axis line on opposite edge of axes box.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------

<!-- -->

[[AxisLine3D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine3D.color "Link to this definition"){.headerlink}

:   Color of the axis line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[AxisLine3D.]{.pre}]{.sig-prename .descclassname}[[edge_assignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine3D.edge_assignment "Link to this definition"){.headerlink}

:   Edge to use when drawing the primary axis line.

    Possible values: [[`AxisLine3DAssignment.Automatic`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisLine3DAssignment.Automatic "tecplot.constant.AxisLine3DAssignment.Automatic"){.reference
    .internal} (aliased to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}), [[`YMinZMin`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisLine3DAssignment.YMinZMin "tecplot.constant.AxisLine3DAssignment.YMinZMin"){.reference
    .internal}, [[`YMaxZMin`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisLine3DAssignment.YMaxZMin "tecplot.constant.AxisLine3DAssignment.YMaxZMin"){.reference
    .internal}, [[`YMinZMax`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisLine3DAssignment.YMinZMax "tecplot.constant.AxisLine3DAssignment.YMinZMax"){.reference
    .internal}, [[`YMaxZMax`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisLine3DAssignment.YMaxZMax "tecplot.constant.AxisLine3DAssignment.YMaxZMax"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisLine3DAssignment
        >>> axis.line.edge_assignment = AxisLine3DAssignment.YMinZMin
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisLine3DAssignment`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisLine3DAssignment "tecplot.constant.AxisLine3DAssignment"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[AxisLine3D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine3D.line_thickness "Link to this definition"){.headerlink}

:   Width of the axis line to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[AxisLine3D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine3D.show "Link to this definition"){.headerlink}

:   Draw the primary axis line on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[AxisLine3D.]{.pre}]{.sig-prename .descclassname}[[show_on_opposite_edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.AxisLine3D.show_on_opposite_edge "Link to this definition"){.headerlink}

:   Draw axis line on opposite edge of axes box.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.x_axis.line.show_on_opposite_edge = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#radialaxisline2d .section}
#### [RadialAxisLine2D](#id99){.toc-backref role="doc-backlink"}[¶](#radialaxisline2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[RadialAxisLine2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axis.html#RadialAxisLine2D){.reference .internal}[¶](#tecplot.plot.RadialAxisLine2D "Link to this definition"){.headerlink}

:   Radial axis line for polar plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        npoints = 300
        r = np.linspace(0, 2000, npoints)
        theta = np.linspace(0, 700, npoints)

        frame = tp.active_frame()
        dataset = frame.create_dataset('Data', ['R', 'Theta'])
        zone = dataset.add_ordered_zone('Zone', (300,))
        zone.values('R')[:] = r
        zone.values('Theta')[:] = theta

        plot = frame.plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.r_axis.max = np.max(r)

        plot.delete_linemaps()
        lmap = plot.add_linemap('Linemap', zone, dataset.variable('R'),
                                dataset.variable('Theta'))
        lmap.line.line_thickness = 0.8

        raxis = plot.axes.r_axis
        raxis.line.show_both_directions = True
        raxis.line.show_perpendicular = True

        plot.view.fit()

        tp.export.save_png('axis_line_radial.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_line_radial.png"
    class="reference internal image-reference"><img
    src="../_images/axis_line_radial.png" style="width: 300px;"
    alt="../_images/axis_line_radial.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
      [[`alignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.alignment "tecplot.plot.RadialAxisLine2D.alignment"){.reference .internal}                                    Axis line placement.
      [[`angle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.angle "tecplot.plot.RadialAxisLine2D.angle"){.reference .internal}                                                Specific angle to place the radial axis line.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.color "tecplot.plot.RadialAxisLine2D.color"){.reference .internal}                                                Color of the axis line.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.line_thickness "tecplot.plot.RadialAxisLine2D.line_thickness"){.reference .internal}                     Width of the axis line to be drawn.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.offset "tecplot.plot.RadialAxisLine2D.offset"){.reference .internal}                                             Axis line placement with respect to the grid border.
      [[`opposing_axis_value`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.opposing_axis_value "tecplot.plot.RadialAxisLine2D.opposing_axis_value"){.reference .internal}      Axis line placement with respect to the opposing axis.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.show "tecplot.plot.RadialAxisLine2D.show"){.reference .internal}                                                   Draw the primary axis line on the plot.
      [[`show_both_directions`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.show_both_directions "tecplot.plot.RadialAxisLine2D.show_both_directions"){.reference .internal}   Mirror the radial axis 180 degrees from the primary line.
      [[`show_perpendicular`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.show_perpendicular "tecplot.plot.RadialAxisLine2D.show_perpendicular"){.reference .internal}         Mirror the radial axis 90 degrees from the primary line.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[alignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.alignment "Link to this definition"){.headerlink}

:   Axis line placement.

    Possible values: [[`WithOpposingAxisValue`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithOpposingAxisValue "tecplot.constant.AxisAlignment.WithOpposingAxisValue"){.reference
    .internal}, [[`WithGridMin`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridMin "tecplot.constant.AxisAlignment.WithGridMin"){.reference
    .internal}, [[`WithGridMax`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridMax "tecplot.constant.AxisAlignment.WithGridMax"){.reference
    .internal}, [[`WithSpecificAngle`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithSpecificAngle "tecplot.constant.AxisAlignment.WithSpecificAngle"){.reference
    .internal}, [[`WithGridAreaTop`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaTop "tecplot.constant.AxisAlignment.WithGridAreaTop"){.reference
    .internal}, [[`WithGridAreaBottom`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaBottom "tecplot.constant.AxisAlignment.WithGridAreaBottom"){.reference
    .internal}, [[`WithGridAreaLeft`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaLeft "tecplot.constant.AxisAlignment.WithGridAreaLeft"){.reference
    .internal} or [[`WithGridAreaRight`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithGridAreaRight "tecplot.constant.AxisAlignment.WithGridAreaRight"){.reference
    .internal}.

    Not all values will be available for every plot type. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> plot.r_axis.line.alignment = AxisAlignment.WithOpposingAxisValue
        >>> plot.r_axis.line.opposing_axis_value = 45
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisAlignment`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment "tecplot.constant.AxisAlignment"){.reference
        .internal}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[angle]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.angle "Link to this definition"){.headerlink}

:   Specific angle to place the radial axis line.

    The alignment must be set to
    [[`AxisAlignment.WithSpecificAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithSpecificAngle "tecplot.constant.AxisAlignment.WithSpecificAngle"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> plot.r_axis.line.alignment = AxisAlignment.WithSpecificAngle
        >>> plot.r_axis.line.angle = 45
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.color "Link to this definition"){.headerlink}

:   Color of the axis line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the axis line to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.offset "Link to this definition"){.headerlink}

:   Axis line placement with respect to the grid border.

    This is the offset from the grid border-aligned position dictated by
    properties such as [[`AxisLine2D.alignment`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.AxisLine2D.alignment "tecplot.plot.AxisLine2D.alignment"){.reference
    .internal}. The example moves the axis line into the plot by 5% of
    the frame height:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.offset = -5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[opposing_axis_value]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.opposing_axis_value "Link to this definition"){.headerlink}

:   Axis line placement with respect to the opposing axis.

    The axis alignment must be set to
    [[`AxisAlignment.WithOpposingAxisValue`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisAlignment.WithOpposingAxisValue "tecplot.constant.AxisAlignment.WithOpposingAxisValue"){.reference
    .internal} to make this property relevant:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisAlignment
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.alignment = AxisAlignment.WithOpposingAxisValue
        >>> axis.line.opposing_axis_value = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.show "Link to this definition"){.headerlink}

:   Draw the primary axis line on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # get axis via "plot.axes.x_axis(0)" for line plots
        >>> # or "plot.axes.x_axis" for field or sketch plots
        >>> axis.line.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[show_both_directions]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.show_both_directions "Link to this definition"){.headerlink}

:   Mirror the radial axis 180 degrees from the primary line.

    If [[`RadialAxisLine2D.show_perpendicular`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.RadialAxisLine2D.show_perpendicular "tecplot.plot.RadialAxisLine2D.show_perpendicular"){.reference
    .internal} is [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}, this will mirror that axis line as well resulting in
    four axis lines, 90 degrees apart. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> r_axis.line.show_both_directions = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisLine2D.]{.pre}]{.sig-prename .descclassname}[[show_perpendicular]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisLine2D.show_perpendicular "Link to this definition"){.headerlink}

:   Mirror the radial axis 90 degrees from the primary line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> r_axis.line.show_perpendicular = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::
:::::::

::::::::: {#ticks-and-labels .section}
### [Ticks and Labels](#id69){.toc-backref role="doc-backlink"}[¶](#ticks-and-labels "Link to this heading"){.headerlink}

- [Ticks2D](#ticks2d){#id100 .reference .internal}

- [Ticks3D](#ticks3d){#id101 .reference .internal}

- [RadialTicks](#radialticks){#id102 .reference .internal}

- [TickLabels2D](#ticklabels2d){#id103 .reference .internal}

- [TickLabels3D](#ticklabels3d){#id104 .reference .internal}

- [RadialTickLabels](#radialticklabels){#id105 .reference .internal}

::: {#ticks2d .section}
#### [Ticks2D](#id100){.toc-backref role="doc-backlink"}[¶](#ticks2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Ticks2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/ticks.html#Ticks2D){.reference .internal}[¶](#tecplot.plot.Ticks2D "Link to this definition"){.headerlink}

:   Tick marks (major and minor) along axes in 2D.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from os import path
        from tecplot.constant import PlotType, AxisMode, AxisAlignment, TickDirection

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'CircularContour.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian2D)

        plot.show_contour = True
        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'

        plot.axes.x_axis.line.show = False

        yaxis = plot.axes.y_axis
        yaxis.max = 0.15
        yaxis.line.show = False
        yaxis.line.alignment = AxisAlignment.WithOpposingAxisValue
        yaxis.line.opposing_axis_value = 0
        yaxis.tick_labels.transparent_background = True
        yaxis.tick_labels.offset = -5

        yticks = yaxis.ticks
        yticks.direction = TickDirection.Centered

        for ticks in [plot.axes.x_axis.ticks, yticks]:
            ticks.auto_spacing = False
            ticks.spacing = 0.5
            ticks.minor_num_ticks = 3
            ticks.length *= 3
            ticks.line_thickness *= 2

        plot.view.fit()

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('ticks_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/ticks_2d.png"
    class="reference internal image-reference"><img
    src="../_images/ticks_2d.png" style="width: 300px;"
    alt="../_images/ticks_2d.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------
      [[`auto_spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.auto_spacing "tecplot.plot.Ticks2D.auto_spacing"){.reference .internal}                           Automatically set the spacing between tick marks.
      [[`direction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.direction "tecplot.plot.Ticks2D.direction"){.reference .internal}                                    How to draw the ticks with respect the axis line.
      [[`length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.length "tecplot.plot.Ticks2D.length"){.reference .internal}                                             Size of the major tick lines to draw.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.line_thickness "tecplot.plot.Ticks2D.line_thickness"){.reference .internal}                     Width of the major tick lines to be drawn.
      [[`minor_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.minor_length "tecplot.plot.Ticks2D.minor_length"){.reference .internal}                           Size of the minor tick lines to draw.
      [[`minor_line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.minor_line_thickness "tecplot.plot.Ticks2D.minor_line_thickness"){.reference .internal}   Width of the minor tick lines to be drawn.
      [[`minor_num_ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.minor_num_ticks "tecplot.plot.Ticks2D.minor_num_ticks"){.reference .internal}                  Number of minor ticks between each major tick.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.show "tecplot.plot.Ticks2D.show"){.reference .internal}                                                   Draw ticks along axis.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.show_on_border_max "tecplot.plot.Ticks2D.show_on_border_max"){.reference .internal}         Draw ticks along the upper border of the axes grid.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.show_on_border_min "tecplot.plot.Ticks2D.show_on_border_min"){.reference .internal}         Draw ticks along the lower border of the axes grid.
      [[`spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.spacing "tecplot.plot.Ticks2D.spacing"){.reference .internal}                                          Distance between major ticks.
      [[`spacing_anchor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks2D.spacing_anchor "tecplot.plot.Ticks2D.spacing_anchor"){.reference .internal}                     Value to place the first major tick mark.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[auto_spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.auto_spacing "Link to this definition"){.headerlink}

:   Automatically set the spacing between tick marks.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.auto_spacing = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[direction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.direction "Link to this definition"){.headerlink}

:   How to draw the ticks with respect the axis line.

    Possible values: [[`TickDirection.In`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.In "tecplot.constant.TickDirection.In"){.reference
    .internal}, [[`TickDirection.Out`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.Out "tecplot.constant.TickDirection.Out"){.reference
    .internal} or [[`TickDirection.Centered`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.Centered "tecplot.constant.TickDirection.Centered"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TickDirection
        >>> axis.ticks.direction = TickDirection.Centered
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickDirection`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection "tecplot.constant.TickDirection"){.reference
        .internal}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.length "Link to this definition"){.headerlink}

:   Size of the major tick lines to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.length = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the major tick lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.line_thickness = 0.4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[minor_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.minor_length "Link to this definition"){.headerlink}

:   Size of the minor tick lines to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[minor_line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.minor_line_thickness "Link to this definition"){.headerlink}

:   Width of the minor tick lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_line_thickness = 0.1
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[minor_num_ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.minor_num_ticks "Link to this definition"){.headerlink}

:   Number of minor ticks between each major tick.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_num_ticks = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.show "Link to this definition"){.headerlink}

:   Draw ticks along axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.show_on_border_max "Link to this definition"){.headerlink}

:   Draw ticks along the upper border of the axes grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.show_on_border_min "Link to this definition"){.headerlink}

:   Draw ticks along the lower border of the axes grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.spacing "Link to this definition"){.headerlink}

:   Distance between major ticks.

    The [`auto_spacing`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.auto_spacing = False
        >>> axis.ticks.spacing = 0.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (axis data units)

<!-- -->

[[Ticks2D.]{.pre}]{.sig-prename .descclassname}[[spacing_anchor]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks2D.spacing_anchor "Link to this definition"){.headerlink}

:   Value to place the first major tick mark.

    All ticks will placed around this anchor position:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.spacing_anchor = 0.05
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::

::: {#ticks3d .section}
#### [Ticks3D](#id101){.toc-backref role="doc-backlink"}[¶](#ticks3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Ticks3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/ticks.html#Ticks3D){.reference .internal}[¶](#tecplot.plot.Ticks3D "Link to this definition"){.headerlink}

:   Tick marks (major and minor) along axes in 3D.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, TickDirection

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian3D)
        plot.activate()

        plot.show_contour = True
        plot.contour(0).legend.show = False
        plot.axes.grid_area.filled = False

        for axis in plot.axes:
            axis.show = True
            axis.grid_lines.show = False

            axis.ticks.length *= 4
            axis.ticks.minor_length *= 4

        plot.view.fit()

        tp.export.save_png('ticks_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/ticks_3d.png"
    class="reference internal image-reference"><img
    src="../_images/ticks_3d.png" style="width: 300px;"
    alt="../_images/ticks_3d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------
      [[`auto_spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.auto_spacing "tecplot.plot.Ticks3D.auto_spacing"){.reference .internal}                              Automatically set the spacing between tick marks.
      [[`direction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.direction "tecplot.plot.Ticks3D.direction"){.reference .internal}                                       How to draw the ticks with respect the axis line.
      [[`length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.length "tecplot.plot.Ticks3D.length"){.reference .internal}                                                Size of the major tick lines to draw.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.line_thickness "tecplot.plot.Ticks3D.line_thickness"){.reference .internal}                        Width of the major tick lines to be drawn.
      [[`minor_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.minor_length "tecplot.plot.Ticks3D.minor_length"){.reference .internal}                              Size of the minor tick lines to draw.
      [[`minor_line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.minor_line_thickness "tecplot.plot.Ticks3D.minor_line_thickness"){.reference .internal}      Width of the minor tick lines to be drawn.
      [[`minor_num_ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.minor_num_ticks "tecplot.plot.Ticks3D.minor_num_ticks"){.reference .internal}                     Number of minor ticks between each major tick.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.show "tecplot.plot.Ticks3D.show"){.reference .internal}                                                      Draw ticks along axis.
      [[`show_on_opposite_edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.show_on_opposite_edge "tecplot.plot.Ticks3D.show_on_opposite_edge"){.reference .internal}   Draw ticks along the opposite border of the axes grid.
      [[`spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.spacing "tecplot.plot.Ticks3D.spacing"){.reference .internal}                                             Distance between major ticks.
      [[`spacing_anchor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Ticks3D.spacing_anchor "tecplot.plot.Ticks3D.spacing_anchor"){.reference .internal}                        Value to place the first major tick mark.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------------------

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[auto_spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.auto_spacing "Link to this definition"){.headerlink}

:   Automatically set the spacing between tick marks.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.auto_spacing = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[direction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.direction "Link to this definition"){.headerlink}

:   How to draw the ticks with respect the axis line.

    Possible values: [[`TickDirection.In`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.In "tecplot.constant.TickDirection.In"){.reference
    .internal}, [[`TickDirection.Out`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.Out "tecplot.constant.TickDirection.Out"){.reference
    .internal} or [[`TickDirection.Centered`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.Centered "tecplot.constant.TickDirection.Centered"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TickDirection
        >>> axis.ticks.direction = TickDirection.Centered
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickDirection`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection "tecplot.constant.TickDirection"){.reference
        .internal}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.length "Link to this definition"){.headerlink}

:   Size of the major tick lines to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.length = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.line_thickness "Link to this definition"){.headerlink}

:   Width of the major tick lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.line_thickness = 0.4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[minor_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.minor_length "Link to this definition"){.headerlink}

:   Size of the minor tick lines to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[minor_line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.minor_line_thickness "Link to this definition"){.headerlink}

:   Width of the minor tick lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_line_thickness = 0.1
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[minor_num_ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.minor_num_ticks "Link to this definition"){.headerlink}

:   Number of minor ticks between each major tick.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_num_ticks = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.show "Link to this definition"){.headerlink}

:   Draw ticks along axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[show_on_opposite_edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.show_on_opposite_edge "Link to this definition"){.headerlink}

:   Draw ticks along the opposite border of the axes grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show_on_opposite_edge = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.spacing "Link to this definition"){.headerlink}

:   Distance between major ticks.

    The [`auto_spacing`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.auto_spacing = False
        >>> axis.ticks.spacing = 0.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (axis data units)

<!-- -->

[[Ticks3D.]{.pre}]{.sig-prename .descclassname}[[spacing_anchor]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Ticks3D.spacing_anchor "Link to this definition"){.headerlink}

:   Value to place the first major tick mark.

    All ticks will placed around this anchor position:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.spacing_anchor = 0.05
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::

::: {#radialticks .section}
#### [RadialTicks](#id102){.toc-backref role="doc-backlink"}[¶](#radialticks "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[RadialTicks]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/ticks.html#RadialTicks){.reference .internal}[¶](#tecplot.plot.RadialTicks "Link to this definition"){.headerlink}

:   Tick marks (major and minor) along the radial axis.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode, Color, TickDirection

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.theta_axis.mode = ThetaMode.Radians

        raxis = plot.axes.r_axis
        raxis.line.color = Color.Red
        raxis.tick_labels.offset = -4

        raxis.ticks.direction =TickDirection.Centered
        raxis.ticks.line_thickness = 0.8
        raxis.ticks.length = 4
        raxis.ticks.minor_length = 4

        tp.export.save_png('ticks_radial.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/ticks_radial.png"
    class="reference internal image-reference"><img
    src="../_images/ticks_radial.png" style="width: 300px;"
    alt="../_images/ticks_radial.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------
      [[`auto_spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.auto_spacing "tecplot.plot.RadialTicks.auto_spacing"){.reference .internal}                                    Automatically set the spacing between tick marks.
      [[`direction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.direction "tecplot.plot.RadialTicks.direction"){.reference .internal}                                             How to draw the ticks with respect the axis line.
      [[`length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.length "tecplot.plot.RadialTicks.length"){.reference .internal}                                                      Size of the major tick lines to draw.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.line_thickness "tecplot.plot.RadialTicks.line_thickness"){.reference .internal}                              Width of the major tick lines to be drawn.
      [[`minor_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.minor_length "tecplot.plot.RadialTicks.minor_length"){.reference .internal}                                    Size of the minor tick lines to draw.
      [[`minor_line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.minor_line_thickness "tecplot.plot.RadialTicks.minor_line_thickness"){.reference .internal}            Width of the minor tick lines to be drawn.
      [[`minor_num_ticks`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.minor_num_ticks "tecplot.plot.RadialTicks.minor_num_ticks"){.reference .internal}                           Number of minor ticks between each major tick.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.show "tecplot.plot.RadialTicks.show"){.reference .internal}                                                            Draw ticks along axis.
      [[`show_on_all_radial_axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.show_on_all_radial_axes "tecplot.plot.RadialTicks.show_on_all_radial_axes"){.reference .internal}   Draw ticks along all radial axis lines.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.show_on_border_max "tecplot.plot.RadialTicks.show_on_border_max"){.reference .internal}                  Draw ticks along the upper border of the axes grid.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.show_on_border_min "tecplot.plot.RadialTicks.show_on_border_min"){.reference .internal}                  Draw ticks along the lower border of the axes grid.
      [[`spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.spacing "tecplot.plot.RadialTicks.spacing"){.reference .internal}                                                   Distance between major ticks.
      [[`spacing_anchor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTicks.spacing_anchor "tecplot.plot.RadialTicks.spacing_anchor"){.reference .internal}                              Value to place the first major tick mark.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[auto_spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.auto_spacing "Link to this definition"){.headerlink}

:   Automatically set the spacing between tick marks.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.auto_spacing = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[direction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.direction "Link to this definition"){.headerlink}

:   How to draw the ticks with respect the axis line.

    Possible values: [[`TickDirection.In`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.In "tecplot.constant.TickDirection.In"){.reference
    .internal}, [[`TickDirection.Out`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.Out "tecplot.constant.TickDirection.Out"){.reference
    .internal} or [[`TickDirection.Centered`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection.Centered "tecplot.constant.TickDirection.Centered"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TickDirection
        >>> axis.ticks.direction = TickDirection.Centered
    :::
    ::::

    Type[:]{.colon}

    :   [[`TickDirection`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TickDirection "tecplot.constant.TickDirection"){.reference
        .internal}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.length "Link to this definition"){.headerlink}

:   Size of the major tick lines to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.length = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.line_thickness "Link to this definition"){.headerlink}

:   Width of the major tick lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.line_thickness = 0.4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[minor_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.minor_length "Link to this definition"){.headerlink}

:   Size of the minor tick lines to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percent of frame height)

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[minor_line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.minor_line_thickness "Link to this definition"){.headerlink}

:   Width of the minor tick lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_line_thickness = 0.1
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[minor_num_ticks]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.minor_num_ticks "Link to this definition"){.headerlink}

:   Number of minor ticks between each major tick.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.minor_num_ticks = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.show "Link to this definition"){.headerlink}

:   Draw ticks along axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[show_on_all_radial_axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.show_on_all_radial_axes "Link to this definition"){.headerlink}

:   Draw ticks along all radial axis lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.line.show_perpendicular = True
        >>> plot.axes.r_axis.ticks.show_on_all_radial_axes = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.show_on_border_max "Link to this definition"){.headerlink}

:   Draw ticks along the upper border of the axes grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.show_on_border_min "Link to this definition"){.headerlink}

:   Draw ticks along the lower border of the axes grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.spacing "Link to this definition"){.headerlink}

:   Distance between major ticks.

    The [`auto_spacing`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.auto_spacing = False
        >>> axis.ticks.spacing = 0.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (axis data units)

<!-- -->

[[RadialTicks.]{.pre}]{.sig-prename .descclassname}[[spacing_anchor]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTicks.spacing_anchor "Link to this definition"){.headerlink}

:   Value to place the first major tick mark.

    All ticks will placed around this anchor position:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.ticks.spacing_anchor = 0.05
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::

::: {#ticklabels2d .section}
#### [TickLabels2D](#id103){.toc-backref role="doc-backlink"}[¶](#ticklabels2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[TickLabels2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/ticks.html#TickLabels2D){.reference .internal}[¶](#tecplot.plot.TickLabels2D "Link to this definition"){.headerlink}

:   Tick labels along axes in 2D.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from datetime import datetime
        import tecplot as tp
        from tecplot.constant import (PlotType, AxisMode, AxisAlignment, NumberFormat,
                                      Color)

        # tecplot dates are in days after Midnight, Dec 30, 1899
        origin = datetime(1899, 12, 30)
        start = (datetime(1955, 11,  5) - origin).days
        stop  = (datetime(1985, 10, 26) - origin).days

        tp.new_layout()
        plot = tp.active_frame().plot(tp.constant.PlotType.Sketch)
        plot.activate()

        plot.axes.viewport.left = 15
        plot.axes.viewport.right = 95

        xaxis = plot.axes.x_axis
        xaxis.show = True
        xaxis.min, xaxis.max = start, stop
        xaxis.line.alignment = AxisAlignment.WithViewport
        xaxis.line.position = 50
        xaxis.ticks.auto_spacing = False
        xaxis.ticks.spacing = (stop - start) // 4
        xaxis.ticks.spacing_anchor = start

        xaxis.tick_labels.format.format_type = NumberFormat.TimeDate
        xaxis.tick_labels.format.datetime_format = 'mmm d, yyyy'
        xaxis.tick_labels.color = Color.Blue
        xaxis.tick_labels.angle = 45

        tp.export.save_png('tick_labels_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/tick_labels_2d.png"
    class="reference internal image-reference"><img
    src="../_images/tick_labels_2d.png" style="width: 300px;"
    alt="../_images/tick_labels_2d.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------
      [[`alignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.alignment "tecplot.plot.TickLabels2D.alignment"){.reference .internal}                                                   Angle at which to render the label text.
      [[`angle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.angle "tecplot.plot.TickLabels2D.angle"){.reference .internal}                                                               Angle at which to render the label text.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.color "tecplot.plot.TickLabels2D.color"){.reference .internal}                                                               Color of the tick labels.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.font "tecplot.plot.TickLabels2D.font"){.reference .internal}                                                                  Text style control including typeface and size.
      [[`format`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.format "tecplot.plot.TickLabels2D.format"){.reference .internal}                                                            Label format and style control.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.offset "tecplot.plot.TickLabels2D.offset"){.reference .internal}                                                            Relative offset of the tick labels.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.show "tecplot.plot.TickLabels2D.show"){.reference .internal}                                                                  Draw labels for the major tick marks.
      [[`show_at_axis_intersection`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.show_at_axis_intersection "tecplot.plot.TickLabels2D.show_at_axis_intersection"){.reference .internal}   Include the labels at the intersection of other axes.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.show_on_border_max "tecplot.plot.TickLabels2D.show_on_border_max"){.reference .internal}                        Draw labels along the upper grid area border.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.show_on_border_min "tecplot.plot.TickLabels2D.show_on_border_min"){.reference .internal}                        Draw labels along the lower grid area border.
      [[`step`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.step "tecplot.plot.TickLabels2D.step"){.reference .internal}                                                                  Step for labels placed on major ticks.
      [[`transparent_background`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels2D.transparent_background "tecplot.plot.TickLabels2D.transparent_background"){.reference .internal}            Make the text box around each label transparent.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[alignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.alignment "Link to this definition"){.headerlink}

:   Angle at which to render the label text.

    Possible values: [[`LabelAlignment.ByAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.ByAngle "tecplot.constant.LabelAlignment.ByAngle"){.reference
    .internal}, [[`LabelAlignment.AlongAxis`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.AlongAxis "tecplot.constant.LabelAlignment.AlongAxis"){.reference
    .internal} or [[`LabelAlignment.PerpendicularToAxis`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.PerpendicularToAxis "tecplot.constant.LabelAlignment.PerpendicularToAxis"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LabelAlignment
        >>> axis.tick_labels.alignment = LabelAlignment.AlongAxis
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees) or [[`LabelAlignment`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment "tecplot.constant.LabelAlignment"){.reference
        .internal}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[angle]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.angle "Link to this definition"){.headerlink}

:   Angle at which to render the label text.

    The [`alignment`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LabelAlignment.ByAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.ByAngle "tecplot.constant.LabelAlignment.ByAngle"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LabelAlignment
        >>> axis.tick_labels.alignment = LabelAlignment.ByAngle
        >>> axis.tick_labels.angle = 30
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees)

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.color "Link to this definition"){.headerlink}

:   Color of the tick labels.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.tick_labels.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.font "Link to this definition"){.headerlink}

:   Text style control including typeface and size.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[format]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.format "Link to this definition"){.headerlink}

:   Label format and style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.format.format_type = NumberFormat.BestFloat
    :::
    ::::

    Type[:]{.colon}

    :   [[`LabelFormat`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.LabelFormat "tecplot.text.LabelFormat"){.reference
        .internal}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.offset "Link to this definition"){.headerlink}

:   Relative offset of the tick labels.

    Positive values will be outside the grid area, negative values are
    inside the grid area:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.show "Link to this definition"){.headerlink}

:   Draw labels for the major tick marks.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[show_at_axis_intersection]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.show_at_axis_intersection "Link to this definition"){.headerlink}

:   Include the labels at the intersection of other axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_at_axis_intersection = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.show_on_border_max "Link to this definition"){.headerlink}

:   Draw labels along the upper grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.show_on_border_min "Link to this definition"){.headerlink}

:   Draw labels along the lower grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[step]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.step "Link to this definition"){.headerlink}

:   Step for labels placed on major ticks.

    A value of 1 will place a label on every major tick mark:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.step = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels2D.]{.pre}]{.sig-prename .descclassname}[[transparent_background]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels2D.transparent_background "Link to this definition"){.headerlink}

:   Make the text box around each label transparent.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.transparent_background = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#ticklabels3d .section}
#### [TickLabels3D](#id104){.toc-backref role="doc-backlink"}[¶](#ticklabels3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[TickLabels3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/ticks.html#TickLabels3D){.reference .internal}[¶](#tecplot.plot.TickLabels3D "Link to this definition"){.headerlink}

:   Tick labels along axes in 3D.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian3D)
        plot.activate()

        plot.show_contour = True
        plot.contour(0).legend.show = False

        for ax in [plot.axes.x_axis, plot.axes.y_axis]:
            xaxis = plot.axes.x_axis
            ax.show = True
            ax.title.show = False
            ax.line.show_on_opposite_edge = True
            ax.ticks.show_on_opposite_edge = True

            ax.tick_labels.color = Color.Blue
            ax.tick_labels.show_on_opposite_edge = True
            ax.tick_labels.font.typeface = 'Times'
            ax.tick_labels.font.size = 8
            ax.tick_labels.font.italic = True

        plot.view.fit()

        tp.export.save_png('tick_labels_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/tick_labels_3d.png"
    class="reference internal image-reference"><img
    src="../_images/tick_labels_3d.png" style="width: 300px;"
    alt="../_images/tick_labels_3d.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------
      [[`alignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.alignment "tecplot.plot.TickLabels3D.alignment"){.reference .internal}                                       Angle at which to render the label text.
      [[`angle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.angle "tecplot.plot.TickLabels3D.angle"){.reference .internal}                                                   Angle at which to render the label text.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.color "tecplot.plot.TickLabels3D.color"){.reference .internal}                                                   Color of the tick labels.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.font "tecplot.plot.TickLabels3D.font"){.reference .internal}                                                      Text style control including typeface and size.
      [[`format`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.format "tecplot.plot.TickLabels3D.format"){.reference .internal}                                                Label format and style control.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.offset "tecplot.plot.TickLabels3D.offset"){.reference .internal}                                                Relative offset of the tick labels.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.show "tecplot.plot.TickLabels3D.show"){.reference .internal}                                                      Draw labels for the major tick marks.
      [[`show_on_opposite_edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.show_on_opposite_edge "tecplot.plot.TickLabels3D.show_on_opposite_edge"){.reference .internal}   Draw labels on the opposite edge of the grid.
      [[`step`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TickLabels3D.step "tecplot.plot.TickLabels3D.step"){.reference .internal}                                                      Step for labels placed on major ticks.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[alignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.alignment "Link to this definition"){.headerlink}

:   Angle at which to render the label text.

    Possible values: [[`LabelAlignment.ByAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.ByAngle "tecplot.constant.LabelAlignment.ByAngle"){.reference
    .internal}, [[`LabelAlignment.AlongAxis`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.AlongAxis "tecplot.constant.LabelAlignment.AlongAxis"){.reference
    .internal} or [[`LabelAlignment.PerpendicularToAxis`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.PerpendicularToAxis "tecplot.constant.LabelAlignment.PerpendicularToAxis"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LabelAlignment
        >>> axis.tick_labels.alignment = LabelAlignment.AlongAxis
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees) or [[`LabelAlignment`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment "tecplot.constant.LabelAlignment"){.reference
        .internal}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[angle]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.angle "Link to this definition"){.headerlink}

:   Angle at which to render the label text.

    The [`alignment`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LabelAlignment.ByAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.ByAngle "tecplot.constant.LabelAlignment.ByAngle"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LabelAlignment
        >>> axis.tick_labels.alignment = LabelAlignment.ByAngle
        >>> axis.tick_labels.angle = 30
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees)

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.color "Link to this definition"){.headerlink}

:   Color of the tick labels.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.tick_labels.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.font "Link to this definition"){.headerlink}

:   Text style control including typeface and size.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[format]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.format "Link to this definition"){.headerlink}

:   Label format and style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.format.format_type = NumberFormat.BestFloat
    :::
    ::::

    Type[:]{.colon}

    :   [[`LabelFormat`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.LabelFormat "tecplot.text.LabelFormat"){.reference
        .internal}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.offset "Link to this definition"){.headerlink}

:   Relative offset of the tick labels.

    Positive values will be outside the grid area, negative values are
    inside the grid area:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.show "Link to this definition"){.headerlink}

:   Draw labels for the major tick marks.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[show_on_opposite_edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.show_on_opposite_edge "Link to this definition"){.headerlink}

:   Draw labels on the opposite edge of the grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_on_opposite_edge = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TickLabels3D.]{.pre}]{.sig-prename .descclassname}[[step]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TickLabels3D.step "Link to this definition"){.headerlink}

:   Step for labels placed on major ticks.

    A value of 1 will place a label on every major tick mark:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.step = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}
:::

::: {#radialticklabels .section}
#### [RadialTickLabels](#id105){.toc-backref role="doc-backlink"}[¶](#radialticklabels "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[RadialTickLabels]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/ticks.html#RadialTickLabels){.reference .internal}[¶](#tecplot.plot.RadialTickLabels "Link to this definition"){.headerlink}

:   Tick mark labels along the radial axis.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.theta_axis.mode = ThetaMode.Radians

        raxis = plot.axes.r_axis
        raxis.line.color = Color.Red
        raxis.tick_labels.offset = -4
        raxis.tick_labels.color = Color.Red
        raxis.tick_labels.font.bold = True

        tp.export.save_png('tick_labels_radial.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/tick_labels_radial.png"
    class="reference internal image-reference"><img
    src="../_images/tick_labels_radial.png" style="width: 300px;"
    alt="../_images/tick_labels_radial.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------
      [[`alignment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.alignment "tecplot.plot.RadialTickLabels.alignment"){.reference .internal}                                                   Angle at which to render the label text.
      [[`angle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.angle "tecplot.plot.RadialTickLabels.angle"){.reference .internal}                                                               Angle at which to render the label text.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.color "tecplot.plot.RadialTickLabels.color"){.reference .internal}                                                               Color of the tick labels.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.font "tecplot.plot.RadialTickLabels.font"){.reference .internal}                                                                  Text style control including typeface and size.
      [[`format`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.format "tecplot.plot.RadialTickLabels.format"){.reference .internal}                                                            Label format and style control.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.offset "tecplot.plot.RadialTickLabels.offset"){.reference .internal}                                                            Relative offset of the tick labels.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.show "tecplot.plot.RadialTickLabels.show"){.reference .internal}                                                                  Draw labels for the major tick marks.
      [[`show_at_axis_intersection`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.show_at_axis_intersection "tecplot.plot.RadialTickLabels.show_at_axis_intersection"){.reference .internal}   Include the labels at the intersection of other axes.
      [[`show_on_all_radial_axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.show_on_all_radial_axes "tecplot.plot.RadialTickLabels.show_on_all_radial_axes"){.reference .internal}         Draw labels along all radial axis lines.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.show_on_border_max "tecplot.plot.RadialTickLabels.show_on_border_max"){.reference .internal}                        Draw labels along the upper grid area border.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.show_on_border_min "tecplot.plot.RadialTickLabels.show_on_border_min"){.reference .internal}                        Draw labels along the lower grid area border.
      [[`step`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.step "tecplot.plot.RadialTickLabels.step"){.reference .internal}                                                                  Step for labels placed on major ticks.
      [[`transparent_background`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialTickLabels.transparent_background "tecplot.plot.RadialTickLabels.transparent_background"){.reference .internal}            Make the text box around each label transparent.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[alignment]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.alignment "Link to this definition"){.headerlink}

:   Angle at which to render the label text.

    Possible values: [[`LabelAlignment.ByAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.ByAngle "tecplot.constant.LabelAlignment.ByAngle"){.reference
    .internal}, [[`LabelAlignment.AlongAxis`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.AlongAxis "tecplot.constant.LabelAlignment.AlongAxis"){.reference
    .internal} or [[`LabelAlignment.PerpendicularToAxis`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.PerpendicularToAxis "tecplot.constant.LabelAlignment.PerpendicularToAxis"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LabelAlignment
        >>> axis.tick_labels.alignment = LabelAlignment.AlongAxis
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees) or [[`LabelAlignment`{.xref .any .py
        .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment "tecplot.constant.LabelAlignment"){.reference
        .internal}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[angle]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.angle "Link to this definition"){.headerlink}

:   Angle at which to render the label text.

    The [`alignment`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LabelAlignment.ByAngle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelAlignment.ByAngle "tecplot.constant.LabelAlignment.ByAngle"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LabelAlignment
        >>> axis.tick_labels.alignment = LabelAlignment.ByAngle
        >>> axis.tick_labels.angle = 30
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees)

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.color "Link to this definition"){.headerlink}

:   Color of the tick labels.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.tick_labels.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.font "Link to this definition"){.headerlink}

:   Text style control including typeface and size.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[format]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.format "Link to this definition"){.headerlink}

:   Label format and style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.format.format_type = NumberFormat.BestFloat
    :::
    ::::

    Type[:]{.colon}

    :   [[`LabelFormat`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.LabelFormat "tecplot.text.LabelFormat"){.reference
        .internal}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.offset "Link to this definition"){.headerlink}

:   Relative offset of the tick labels.

    Positive values will be outside the grid area, negative values are
    inside the grid area:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.show "Link to this definition"){.headerlink}

:   Draw labels for the major tick marks.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[show_at_axis_intersection]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.show_at_axis_intersection "Link to this definition"){.headerlink}

:   Include the labels at the intersection of other axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_at_axis_intersection = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[show_on_all_radial_axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.show_on_all_radial_axes "Link to this definition"){.headerlink}

:   Draw labels along all radial axis lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.line.show_perpendicular = True
        >>> plot.axes.r_axis.tick_labels.show_on_all_radial_axes = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.show_on_border_max "Link to this definition"){.headerlink}

:   Draw labels along the upper grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.show_on_border_min "Link to this definition"){.headerlink}

:   Draw labels along the lower grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[step]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.step "Link to this definition"){.headerlink}

:   Step for labels placed on major ticks.

    A value of 1 will place a label on every major tick mark:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.step = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialTickLabels.]{.pre}]{.sig-prename .descclassname}[[transparent_background]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialTickLabels.transparent_background "Link to this definition"){.headerlink}

:   Make the text box around each label transparent.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.tick_labels.transparent_background = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::
:::::::::

::::::: {#axis-title .section}
### [Axis Title](#id76){.toc-backref role="doc-backlink"}[¶](#axis-title "Link to this heading"){.headerlink}

- [Axis2DTitle](#axis2dtitle){#id106 .reference .internal}

- [DataAxis2DTitle](#dataaxis2dtitle){#id107 .reference .internal}

- [DataAxis3DTitle](#dataaxis3dtitle){#id108 .reference .internal}

- [RadialAxisTitle](#radialaxistitle){#id109 .reference .internal}

::: {#axis2dtitle .section}
#### [Axis2DTitle](#id106){.toc-backref role="doc-backlink"}[¶](#axis2dtitle "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Axis2DTitle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/title.html#Axis2DTitle){.reference .internal}[¶](#tecplot.plot.Axis2DTitle "Link to this definition"){.headerlink}

:   Sketch plot axis label string, font and style control.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        plot = tp.active_frame().plot(PlotType.Sketch)

        viewport = plot.axes.viewport
        viewport.left = 10
        viewport.right = 90
        viewport.bottom = 10

        xaxis = plot.axes.x_axis
        xaxis.show = True
        xaxis.title.text = 'distance (m)'
        xaxis.title.color = Color.DarkTurquoise
        xaxis.title.offset = -7

        tp.export.save_png('axis_title_sketch.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_title_sketch.png"
    class="reference internal image-reference"><img
    src="../_images/axis_title_sketch.png" style="width: 300px;"
    alt="../_images/axis_title_sketch.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.color "tecplot.plot.Axis2DTitle.color"){.reference .internal}                                          Text color of axis title.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.font "tecplot.plot.Axis2DTitle.font"){.reference .internal}                                             Typeface and size of the text.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.offset "tecplot.plot.Axis2DTitle.offset"){.reference .internal}                                       Transverse offset of the title from the axis.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.position "tecplot.plot.Axis2DTitle.position"){.reference .internal}                                 Percent along axis line to place title.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.show "tecplot.plot.Axis2DTitle.show"){.reference .internal}                                             Place title along the axis.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.show_on_border_max "tecplot.plot.Axis2DTitle.show_on_border_max"){.reference .internal}   Draw title along the upper grid area border.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.show_on_border_min "tecplot.plot.Axis2DTitle.show_on_border_min"){.reference .internal}   Draw title along the lower grid area border.
      [[`text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Axis2DTitle.text "tecplot.plot.Axis2DTitle.text"){.reference .internal}                                             The text of the title for this axis.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.color "Link to this definition"){.headerlink}

:   Text color of axis title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.title.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.font "Link to this definition"){.headerlink}

:   Typeface and size of the text.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.font.size = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.offset "Link to this definition"){.headerlink}

:   Transverse offset of the title from the axis.

    Positive values are outside the axes, negative numbers are inside
    the axes. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent of frame height.

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.position "Link to this definition"){.headerlink}

:   Percent along axis line to place title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.position = 50
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.show "Link to this definition"){.headerlink}

:   Place title along the axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.show_on_border_max "Link to this definition"){.headerlink}

:   Draw title along the upper grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.show_on_border_min "Link to this definition"){.headerlink}

:   Draw title along the lower grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Axis2DTitle.]{.pre}]{.sig-prename .descclassname}[[text]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Axis2DTitle.text "Link to this definition"){.headerlink}

:   The text of the title for this axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}
:::

::: {#dataaxis2dtitle .section}
#### [DataAxis2DTitle](#id107){.toc-backref role="doc-backlink"}[¶](#dataaxis2dtitle "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[DataAxis2DTitle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/title.html#DataAxis2DTitle){.reference .internal}[¶](#tecplot.plot.DataAxis2DTitle "Link to this definition"){.headerlink}

:   Axis label string, font and style control for 2D data plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, SurfacesToPlot, Color, AxisTitleMode

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(infile)

        plot = tp.active_frame().plot(PlotType.Cartesian2D)
        plot.activate()

        plot.show_contour = True
        plot.contour(0).variable = dataset.variable('S')
        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'
        plot.contour(0).legend.show = False

        plot.fieldmap(0).surfaces.surfaces_to_plot = SurfacesToPlot.BoundaryFaces

        xaxis = plot.axes.x_axis
        xaxis.title.title_mode = AxisTitleMode.UseText
        xaxis.title.text = 'Longitudinal (m)'
        xaxis.title.color = Color.Blue

        # place the x-axis title at the x-coordinate 10.0
        xaxis.title.position = 100 * (10.0 - xaxis.min) / (xaxis.max - xaxis.min)

        yaxis = plot.axes.y_axis
        yaxis.title.title_mode = AxisTitleMode.UseText
        yaxis.title.text = 'Transverse (m)'
        yaxis.title.color = Color.Blue

        # place the y-axis title at the y-coordinate 0.0
        yaxis.title.position = 100 * (0.0 - yaxis.min) / (yaxis.max - yaxis.min)

        tp.export.save_png('axis_title_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_title_2d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_title_2d.png" style="width: 300px;"
    alt="../_images/axis_title_2d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.color "tecplot.plot.DataAxis2DTitle.color"){.reference .internal}                                          Text color of axis title.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.font "tecplot.plot.DataAxis2DTitle.font"){.reference .internal}                                             Typeface and size of the text.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.offset "tecplot.plot.DataAxis2DTitle.offset"){.reference .internal}                                       Transverse offset of the title from the axis.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.position "tecplot.plot.DataAxis2DTitle.position"){.reference .internal}                                 Percent along axis line to place title.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.show "tecplot.plot.DataAxis2DTitle.show"){.reference .internal}                                             Place title along the axis.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.show_on_border_max "tecplot.plot.DataAxis2DTitle.show_on_border_max"){.reference .internal}   Draw title along the upper grid area border.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.show_on_border_min "tecplot.plot.DataAxis2DTitle.show_on_border_min"){.reference .internal}   Draw title along the lower grid area border.
      [[`text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.text "tecplot.plot.DataAxis2DTitle.text"){.reference .internal}                                             The text of the title for this axis.
      [[`title_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis2DTitle.title_mode "tecplot.plot.DataAxis2DTitle.title_mode"){.reference .internal}                           Define the source for the axis title.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.color "Link to this definition"){.headerlink}

:   Text color of axis title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.title.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.font "Link to this definition"){.headerlink}

:   Typeface and size of the text.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.font.size = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.offset "Link to this definition"){.headerlink}

:   Transverse offset of the title from the axis.

    Positive values are outside the axes, negative numbers are inside
    the axes. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent of frame height.

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.position "Link to this definition"){.headerlink}

:   Percent along axis line to place title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.position = 50
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.show "Link to this definition"){.headerlink}

:   Place title along the axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.show_on_border_max "Link to this definition"){.headerlink}

:   Draw title along the upper grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.show_on_border_min "Link to this definition"){.headerlink}

:   Draw title along the lower grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[text]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.text "Link to this definition"){.headerlink}

:   The text of the title for this axis.

    The [`title_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`AxisTitleMode.UseText`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseText "tecplot.constant.AxisTitleMode.UseText"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisTitleMode
        >>> axis.title.title_mode = AxisTitleMode.UseText
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis2DTitle.]{.pre}]{.sig-prename .descclassname}[[title_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis2DTitle.title_mode "Link to this definition"){.headerlink}

:   Define the source for the axis title.

    Possible values: [[`AxisTitleMode.UseText`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseText "tecplot.constant.AxisTitleMode.UseText"){.reference
    .internal} or [[`AxisTitleMode.UseVarName`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseVarName "tecplot.constant.AxisTitleMode.UseVarName"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisTitleMode
        >>> axis.title.title_mode = AxisTitleMode.UseVarName
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisTitleMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode "tecplot.constant.AxisTitleMode"){.reference
        .internal}
:::

::: {#dataaxis3dtitle .section}
#### [DataAxis3DTitle](#id108){.toc-backref role="doc-backlink"}[¶](#dataaxis3dtitle "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[DataAxis3DTitle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/title.html#DataAxis3DTitle){.reference .internal}[¶](#tecplot.plot.DataAxis3DTitle "Link to this definition"){.headerlink}

:   Axis label string, font and style control for 3D plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, SurfacesToPlot, Color, AxisTitleMode

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(infile)

        plot = tp.active_frame().plot(PlotType.Cartesian3D)
        plot.activate()

        plot.show_contour = True
        plot.contour(0).variable = dataset.variable('S')
        plot.contour(0).colormap_name = 'Sequential - Yellow/Green/Blue'
        plot.contour(0).legend.show = False

        plot.fieldmap(0).surfaces.surfaces_to_plot = SurfacesToPlot.BoundaryFaces

        xaxis = plot.axes.x_axis
        xaxis.show = True
        xaxis.title.title_mode = AxisTitleMode.UseText
        xaxis.title.text = 'Longitudinal (m)'
        xaxis.title.color = Color.BluePurple
        xaxis.title.position = 10

        yaxis = plot.axes.y_axis
        yaxis.show = True
        yaxis.title.title_mode = AxisTitleMode.UseText
        yaxis.title.text = 'Transverse (m)'
        yaxis.title.color = Color.BluePurple
        yaxis.title.position = 90

        zaxis = plot.axes.z_axis
        zaxis.show = True
        zaxis.title.title_mode = AxisTitleMode.UseText
        zaxis.title.text = 'Height (m)'
        zaxis.title.color = Color.BluePurple
        zaxis.title.offset = 13

        plot.view.fit()

        tp.export.save_png('axis_title_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_title_3d.png"
    class="reference internal image-reference"><img
    src="../_images/axis_title_3d.png" style="width: 300px;"
    alt="../_images/axis_title_3d.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.color "tecplot.plot.DataAxis3DTitle.color"){.reference .internal}                                                   Text color of axis title.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.font "tecplot.plot.DataAxis3DTitle.font"){.reference .internal}                                                      Typeface and size of the text.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.offset "tecplot.plot.DataAxis3DTitle.offset"){.reference .internal}                                                Transverse offset of the title from the axis.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.position "tecplot.plot.DataAxis3DTitle.position"){.reference .internal}                                          Percent along axis line to place title.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.show "tecplot.plot.DataAxis3DTitle.show"){.reference .internal}                                                      Place title along the axis.
      [[`show_on_opposite_edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.show_on_opposite_edge "tecplot.plot.DataAxis3DTitle.show_on_opposite_edge"){.reference .internal}   Draw the title on the opposite edge of the grid.
      [[`text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.text "tecplot.plot.DataAxis3DTitle.text"){.reference .internal}                                                      The text of the title for this axis.
      [[`title_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.DataAxis3DTitle.title_mode "tecplot.plot.DataAxis3DTitle.title_mode"){.reference .internal}                                    Define the source for the axis title.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.color "Link to this definition"){.headerlink}

:   Text color of axis title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.title.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.font "Link to this definition"){.headerlink}

:   Typeface and size of the text.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.font.size = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.offset "Link to this definition"){.headerlink}

:   Transverse offset of the title from the axis.

    Positive values are outside the axes, negative numbers are inside
    the axes. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent of frame height.

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.position "Link to this definition"){.headerlink}

:   Percent along axis line to place title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.position = 50
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.show "Link to this definition"){.headerlink}

:   Place title along the axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_opposite_edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.show_on_opposite_edge "Link to this definition"){.headerlink}

:   Draw the title on the opposite edge of the grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_opposite_edge = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[text]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.text "Link to this definition"){.headerlink}

:   The text of the title for this axis.

    The [`title_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`AxisTitleMode.UseText`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseText "tecplot.constant.AxisTitleMode.UseText"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisTitleMode
        >>> axis.title.title_mode = AxisTitleMode.UseText
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[DataAxis3DTitle.]{.pre}]{.sig-prename .descclassname}[[title_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.DataAxis3DTitle.title_mode "Link to this definition"){.headerlink}

:   Define the source for the axis title.

    Possible values: [[`AxisTitleMode.UseText`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseText "tecplot.constant.AxisTitleMode.UseText"){.reference
    .internal} or [[`AxisTitleMode.UseVarName`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseVarName "tecplot.constant.AxisTitleMode.UseVarName"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisTitleMode
        >>> axis.title.title_mode = AxisTitleMode.UseVarName
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisTitleMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode "tecplot.constant.AxisTitleMode"){.reference
        .internal}
:::

::: {#radialaxistitle .section}
#### [RadialAxisTitle](#id109){.toc-backref role="doc-backlink"}[¶](#radialaxistitle "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[RadialAxisTitle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/title.html#RadialAxisTitle){.reference .internal}[¶](#tecplot.plot.RadialAxisTitle "Link to this definition"){.headerlink}

:   Radial axis label string, font and style control for polar plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, Color, AxisTitleMode

        npoints = 300
        r = np.linspace(0, 2000, npoints)
        theta = np.linspace(0, 1000, npoints)

        frame = tp.active_frame()
        dataset = frame.create_dataset('Data', ['R', 'Theta'])
        zone = dataset.add_ordered_zone('Zone', (300,))
        zone.values('R')[:] = r
        zone.values('Theta')[:] = theta

        plot = frame.plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.r_axis.max = np.max(r)

        plot.delete_linemaps()
        lmap = plot.add_linemap('Linemap', zone, dataset.variable('R'),
                                dataset.variable('Theta'))
        lmap.line.line_thickness = 0.8

        raxis = plot.axes.r_axis
        raxis.line.show_both_directions = True
        raxis.line.show_perpendicular = True

        raxis.title.title_mode = AxisTitleMode.UseText
        raxis.title.text = 'Radial Position (cm)'
        raxis.title.show_on_all_radial_axes = True
        raxis.title.color = Color.Blue
        raxis.title.position = 80

        plot.view.fit()

        tp.export.save_png('axis_title_radial.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axis_title_radial.png"
    class="reference internal image-reference"><img
    src="../_images/axis_title_radial.png" style="width: 300px;"
    alt="../_images/axis_title_radial.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.color "tecplot.plot.RadialAxisTitle.color"){.reference .internal}                                                         Text color of axis title.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.font "tecplot.plot.RadialAxisTitle.font"){.reference .internal}                                                            Typeface and size of the text.
      [[`offset`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.offset "tecplot.plot.RadialAxisTitle.offset"){.reference .internal}                                                      Transverse offset of the title from the axis.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.position "tecplot.plot.RadialAxisTitle.position"){.reference .internal}                                                Percent along axis line to place title.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.show "tecplot.plot.RadialAxisTitle.show"){.reference .internal}                                                            Place title along the axis.
      [[`show_on_all_radial_axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.show_on_all_radial_axes "tecplot.plot.RadialAxisTitle.show_on_all_radial_axes"){.reference .internal}   Draw title along all radial axis lines.
      [[`show_on_border_max`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.show_on_border_max "tecplot.plot.RadialAxisTitle.show_on_border_max"){.reference .internal}                  Draw title along the upper grid area border.
      [[`show_on_border_min`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.show_on_border_min "tecplot.plot.RadialAxisTitle.show_on_border_min"){.reference .internal}                  Draw title along the lower grid area border.
      [[`text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.text "tecplot.plot.RadialAxisTitle.text"){.reference .internal}                                                            The text of the title for this axis.
      [[`title_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.RadialAxisTitle.title_mode "tecplot.plot.RadialAxisTitle.title_mode"){.reference .internal}                                          Define the source for the axis title.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.color "Link to this definition"){.headerlink}

:   Text color of axis title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> axis.title.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.font "Link to this definition"){.headerlink}

:   Typeface and size of the text.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.font.size = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`text.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.Font "tecplot.text.Font"){.reference
        .internal}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[offset]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.offset "Link to this definition"){.headerlink}

:   Transverse offset of the title from the axis.

    Positive values are outside the axes, negative numbers are inside
    the axes. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.offset = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent of frame height.

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.position "Link to this definition"){.headerlink}

:   Percent along axis line to place title.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.position = 50
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.show "Link to this definition"){.headerlink}

:   Place title along the axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_all_radial_axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.show_on_all_radial_axes "Link to this definition"){.headerlink}

:   Draw title along all radial axis lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.r_axis.line.show_perpendicular = True
        >>> plot.axes.r_axis.title.show_on_all_radial_axes = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_border_max]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.show_on_border_max "Link to this definition"){.headerlink}

:   Draw title along the upper grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_border_max = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[show_on_border_min]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.show_on_border_min "Link to this definition"){.headerlink}

:   Draw title along the lower grid area border.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.title.show_on_border_min = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[text]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.text "Link to this definition"){.headerlink}

:   The text of the title for this axis.

    The [`title_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`AxisTitleMode.UseText`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseText "tecplot.constant.AxisTitleMode.UseText"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisTitleMode
        >>> axis.title.title_mode = AxisTitleMode.UseText
        >>> axis.title.text = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[RadialAxisTitle.]{.pre}]{.sig-prename .descclassname}[[title_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.RadialAxisTitle.title_mode "Link to this definition"){.headerlink}

:   Define the source for the axis title.

    Possible values: [[`AxisTitleMode.UseText`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseText "tecplot.constant.AxisTitleMode.UseText"){.reference
    .internal} or [[`AxisTitleMode.UseVarName`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode.UseVarName "tecplot.constant.AxisTitleMode.UseVarName"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import AxisTitleMode
        >>> axis.title.title_mode = AxisTitleMode.UseVarName
    :::
    ::::

    Type[:]{.colon}

    :   [[`AxisTitleMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AxisTitleMode "tecplot.constant.AxisTitleMode"){.reference
        .internal}
:::
:::::::

:::::::::::::::: {#grid-area .section}
### [Grid Area](#id81){.toc-backref role="doc-backlink"}[¶](#grid-area "Link to this heading"){.headerlink}

- [GridArea](#gridarea){#id110 .reference .internal}

- [Cartesian2DGridArea](#cartesian2dgridarea){#id111 .reference
  .internal}

- [Cartesian3DGridArea](#cartesian3dgridarea){#id112 .reference
  .internal}

- [PreciseGrid](#precisegrid){#id113 .reference .internal}

- [GridLines](#gridlines){#id114 .reference .internal}

- [GridLines2D](#gridlines2d){#id115 .reference .internal}

- [MinorGridLines](#minorgridlines){#id116 .reference .internal}

- [MinorGridLines2D](#minorgridlines2d){#id117 .reference .internal}

- [PolarAngleGridLines](#polaranglegridlines){#id118 .reference
  .internal}

- [PolarAngleMinorGridLines](#polarangleminorgridlines){#id119
  .reference .internal}

- [MarkerGridLine](#markergridline){#id120 .reference .internal}

- [MarkerGridLine2D](#markergridline2d){#id121 .reference .internal}

- [PolarAngleMarkerGridLine](#polaranglemarkergridline){#id122
  .reference .internal}

::: {#gridarea .section}
#### [GridArea](#id110){.toc-backref role="doc-backlink"}[¶](#gridarea "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[GridArea]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#GridArea){.reference .internal}[¶](#tecplot.plot.GridArea "Link to this definition"){.headerlink}

:   Grid area for polar 2D plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.theta_axis.mode = ThetaMode.Radians
        plot.axes.grid_area.fill_color = Color.Creme

        grid_area = plot.axes.grid_area
        grid_area.filled = True
        grid_area.fill_color = Color.SkyBlue
        grid_area.show_border = True

        tp.export.save_png('grid_area_polar.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/grid_area_polar.png"
    class="reference internal image-reference"><img
    src="../_images/grid_area_polar.png" style="width: 300px;"
    alt="../_images/grid_area_polar.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridArea.fill_color "tecplot.plot.GridArea.fill_color"){.reference .internal}      Axes area background color.
      [[`filled`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridArea.filled "tecplot.plot.GridArea.filled"){.reference .internal}                  Fill the axes area background color.
      [[`show_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridArea.show_border "tecplot.plot.GridArea.show_border"){.reference .internal}   Draw border around axes area.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------

<!-- -->

[[GridArea.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridArea.fill_color "Link to this definition"){.headerlink}

:   Axes area background color.

    This requires the [`filled`{.docutils .literal .notranslate}]{.pre}
    attribute to be [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.filled = True
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[GridArea.]{.pre}]{.sig-prename .descclassname}[[filled]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridArea.filled "Link to this definition"){.headerlink}

:   Fill the axes area background color.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.filled = True
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GridArea.]{.pre}]{.sig-prename .descclassname}[[show_border]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridArea.show_border "Link to this definition"){.headerlink}

:   Draw border around axes area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.grid_area.show_border = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#cartesian2dgridarea .section}
#### [Cartesian2DGridArea](#id111){.toc-backref role="doc-backlink"}[¶](#cartesian2dgridarea "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DGridArea]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#Cartesian2DGridArea){.reference .internal}[¶](#tecplot.plot.Cartesian2DGridArea "Link to this definition"){.headerlink}

:   Grid area for cartesian 2D plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'SunSpots.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.XYLine)

        plot.linemap(0).line.color = Color.DarkBlue
        plot.linemap(0).line.line_thickness = 1.0

        grid_area = plot.axes.grid_area
        grid_area.filled = True
        grid_area.fill_color = Color.SkyBlue
        grid_area.show_border = True

        tp.export.save_png('grid_area_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/grid_area_2d.png"
    class="reference internal image-reference"><img
    src="../_images/grid_area_2d.png" style="width: 300px;"
    alt="../_images/grid_area_2d.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------
      [[`border_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DGridArea.border_color "tecplot.plot.Cartesian2DGridArea.border_color"){.reference .internal}               Border line color.
      [[`border_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DGridArea.border_thickness "tecplot.plot.Cartesian2DGridArea.border_thickness"){.reference .internal}   Width of the border lines to be drawn.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DGridArea.fill_color "tecplot.plot.Cartesian2DGridArea.fill_color"){.reference .internal}                     Axes area background color.
      [[`filled`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DGridArea.filled "tecplot.plot.Cartesian2DGridArea.filled"){.reference .internal}                                 Fill the axes area background color.
      [[`show_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DGridArea.show_border "tecplot.plot.Cartesian2DGridArea.show_border"){.reference .internal}                  Draw border around axes area.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------

<!-- -->

[[Cartesian2DGridArea.]{.pre}]{.sig-prename .descclassname}[[border_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DGridArea.border_color "Link to this definition"){.headerlink}

:   Border line color.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.show_border = True
        >>> plot.axes.grid_area.border_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Cartesian2DGridArea.]{.pre}]{.sig-prename .descclassname}[[border_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DGridArea.border_thickness "Link to this definition"){.headerlink}

:   Width of the border lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.grid_area.border_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DGridArea.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DGridArea.fill_color "Link to this definition"){.headerlink}

:   Axes area background color.

    This requires the [`filled`{.docutils .literal .notranslate}]{.pre}
    attribute to be [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.filled = True
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Cartesian2DGridArea.]{.pre}]{.sig-prename .descclassname}[[filled]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DGridArea.filled "Link to this definition"){.headerlink}

:   Fill the axes area background color.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.filled = True
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DGridArea.]{.pre}]{.sig-prename .descclassname}[[show_border]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DGridArea.show_border "Link to this definition"){.headerlink}

:   Draw border around axes area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.grid_area.show_border = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#cartesian3dgridarea .section}
#### [Cartesian3DGridArea](#id112){.toc-backref role="doc-backlink"}[¶](#cartesian3dgridarea "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian3DGridArea]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#Cartesian3DGridArea){.reference .internal}[¶](#tecplot.plot.Cartesian3DGridArea "Link to this definition"){.headerlink}

:   Grid area for 3D field plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, SurfacesToPlot, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Pyramid.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian3D)

        fmaps = plot.fieldmaps()
        fmaps.contour.show = True
        fmaps.surfaces.surfaces_to_plot = SurfacesToPlot.BoundaryFaces
        plot.show_contour = True
        plot.contour(0).legend.show = False

        for axis in plot.axes:
            axis.show = True

        grid_area = plot.axes.grid_area
        grid_area.fill_color = Color.SkyBlue
        grid_area.show_border = True
        grid_area.use_lighting_effect = True

        plot.view.fit()

        tp.export.save_png('grid_area_3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/grid_area_3d.png"
    class="reference internal image-reference"><img
    src="../_images/grid_area_3d.png" style="width: 300px;"
    alt="../_images/grid_area_3d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DGridArea.fill_color "tecplot.plot.Cartesian3DGridArea.fill_color"){.reference .internal}                              Axes area background color.
      [[`filled`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DGridArea.filled "tecplot.plot.Cartesian3DGridArea.filled"){.reference .internal}                                          Fill the axes area background color.
      [[`show_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DGridArea.show_border "tecplot.plot.Cartesian3DGridArea.show_border"){.reference .internal}                           Draw border around axes area.
      [[`use_lighting_effect`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DGridArea.use_lighting_effect "tecplot.plot.Cartesian3DGridArea.use_lighting_effect"){.reference .internal}   Enable lighting effect shading on grid area.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------

<!-- -->

[[Cartesian3DGridArea.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DGridArea.fill_color "Link to this definition"){.headerlink}

:   Axes area background color.

    This requires the [`filled`{.docutils .literal .notranslate}]{.pre}
    attribute to be [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.filled = True
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Cartesian3DGridArea.]{.pre}]{.sig-prename .descclassname}[[filled]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DGridArea.filled "Link to this definition"){.headerlink}

:   Fill the axes area background color.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.grid_area.filled = True
        >>> plot.axes.grid_area.fill_color = Color.LightGreen
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DGridArea.]{.pre}]{.sig-prename .descclassname}[[show_border]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DGridArea.show_border "Link to this definition"){.headerlink}

:   Draw border around axes area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.grid_area.show_border = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DGridArea.]{.pre}]{.sig-prename .descclassname}[[use_lighting_effect]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DGridArea.use_lighting_effect "Link to this definition"){.headerlink}

:   Enable lighting effect shading on grid area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.grid_area.use_lighting_effect = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#precisegrid .section}
#### [PreciseGrid](#id113){.toc-backref role="doc-backlink"}[¶](#precisegrid "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PreciseGrid]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#PreciseGrid){.reference .internal}[¶](#tecplot.plot.PreciseGrid "Link to this definition"){.headerlink}

:   Grid of precise dots aligned with all tick marks.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'RainierElevation.plt')
        dataset = tp.data.load_tecplot(datafile)

        plot = tp.active_frame().plot(PlotType.Cartesian2D)
        plot.activate()

        plot.show_contour = True
        plot.contour(0).colormap_name = 'Elevation - Above Ground Level'

        xaxis = plot.axes.x_axis
        plot.axes.preserve_scale = True
        xaxis.max = xaxis.variable.values(0).max()

        grid = plot.axes.precise_grid
        grid.show = True
        grid.size = 0.05

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('precise_grid.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/precise_grid.png"
    class="reference internal image-reference"><img
    src="../_images/precise_grid.png" style="width: 300px;"
    alt="../_images/precise_grid.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PreciseGrid.color "tecplot.plot.PreciseGrid.color"){.reference .internal}   Color of the dots for precise grid.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PreciseGrid.show "tecplot.plot.PreciseGrid.show"){.reference .internal}      Draw precise grid dots in axes area.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PreciseGrid.size "tecplot.plot.PreciseGrid.size"){.reference .internal}      Size of the dots for precise grid.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------

<!-- -->

[[PreciseGrid.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PreciseGrid.color "Link to this definition"){.headerlink}

:   Color of the dots for precise grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.color = Color.DarkBlue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[PreciseGrid.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PreciseGrid.show "Link to this definition"){.headerlink}

:   Draw precise grid dots in axes area.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PreciseGrid.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PreciseGrid.size "Link to this definition"){.headerlink}

:   Size of the dots for precise grid.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.precise_grid.size = 0.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (cm)
:::

::: {#gridlines .section}
#### [GridLines](#id114){.toc-backref role="doc-backlink"}[¶](#gridlines "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[GridLines]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#GridLines){.reference .internal}[¶](#tecplot.plot.GridLines "Link to this definition"){.headerlink}

:   Major grid lines.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot()

        plot.axes.grid_area.fill_color = Color.Grey

        for axis in (plot.axes.x_axis, plot.axes.y_axis):
            axis.show = True
            grid_lines = axis.grid_lines
            grid_lines.show = True
            grid_lines.line_pattern = LinePattern.LongDash
            grid_lines.color = Color.Cyan

        plot.view.fit()

        tp.export.save_png('grid_lines.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/grid_lines.png"
    class="reference internal image-reference"><img
    src="../_images/grid_lines.png" style="width: 300px;"
    alt="../_images/grid_lines.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines.color "tecplot.plot.GridLines.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines.line_pattern "tecplot.plot.GridLines.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines.line_thickness "tecplot.plot.GridLines.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines.pattern_length "tecplot.plot.GridLines.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines.show "tecplot.plot.GridLines.show"){.reference .internal}                                 Draw grid lines as tick locations.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[GridLines.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[GridLines.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[GridLines.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GridLines.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GridLines.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#gridlines2d .section}
#### [GridLines2D](#id115){.toc-backref role="doc-backlink"}[¶](#gridlines2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[GridLines2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#GridLines2D){.reference .internal}[¶](#tecplot.plot.GridLines2D "Link to this definition"){.headerlink}

:   Major grid lines following the primary tick mark locations.

    The lines drawn are determined by the placement of major tick marks
    along the axis:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        for axis in tp.active_frame().plot().axes:
            grid_lines = axis.grid_lines
            grid_lines.show = True
            grid_lines.line_pattern = LinePattern.LongDash
            grid_lines.color = Color.Green

        tp.export.save_png('grid_lines_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/grid_lines_2d.png"
    class="reference internal image-reference"><img
    src="../_images/grid_lines_2d.png" style="width: 300px;"
    alt="../_images/grid_lines_2d.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines2D.color "tecplot.plot.GridLines2D.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`draw_last`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines2D.draw_last "tecplot.plot.GridLines2D.draw_last"){.reference .internal}                  Draw grid behind all other plot elements.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines2D.line_pattern "tecplot.plot.GridLines2D.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines2D.line_thickness "tecplot.plot.GridLines2D.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines2D.pattern_length "tecplot.plot.GridLines2D.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GridLines2D.show "tecplot.plot.GridLines2D.show"){.reference .internal}                                 Draw grid lines as tick locations.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[GridLines2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines2D.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[GridLines2D.]{.pre}]{.sig-prename .descclassname}[[draw_last]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines2D.draw_last "Link to this definition"){.headerlink}

:   Draw grid behind all other plot elements.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.grid_lines.draw_last = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GridLines2D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines2D.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[GridLines2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GridLines2D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines2D.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GridLines2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GridLines2D.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#minorgridlines .section}
#### [MinorGridLines](#id116){.toc-backref role="doc-backlink"}[¶](#minorgridlines "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[MinorGridLines]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#MinorGridLines){.reference .internal}[¶](#tecplot.plot.MinorGridLines "Link to this definition"){.headerlink}

:   Minor grid lines.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot()

        plot.axes.grid_area.fill_color = Color.Grey

        for axis in (plot.axes.x_axis, plot.axes.y_axis):
            axis.show = True

            grid_lines = axis.grid_lines
            grid_lines.show = True

            minor_grid_lines = axis.minor_grid_lines
            minor_grid_lines.show = True
            minor_grid_lines.line_pattern = LinePattern.Dotted
            minor_grid_lines.color = Color.Cyan

        plot.view.fit()

        tp.export.save_png('minor_grid_lines.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/minor_grid_lines.png"
    class="reference internal image-reference"><img
    src="../_images/minor_grid_lines.png" style="width: 300px;"
    alt="../_images/minor_grid_lines.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines.color "tecplot.plot.MinorGridLines.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines.line_pattern "tecplot.plot.MinorGridLines.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines.line_thickness "tecplot.plot.MinorGridLines.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines.pattern_length "tecplot.plot.MinorGridLines.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines.show "tecplot.plot.MinorGridLines.show"){.reference .internal}                                 Draw grid lines as tick locations.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MinorGridLines.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MinorGridLines.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[MinorGridLines.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MinorGridLines.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MinorGridLines.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#minorgridlines2d .section}
#### [MinorGridLines2D](#id117){.toc-backref role="doc-backlink"}[¶](#minorgridlines2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[MinorGridLines2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#MinorGridLines2D){.reference .internal}[¶](#tecplot.plot.MinorGridLines2D "Link to this definition"){.headerlink}

:   Minor grid lines following the secondary tick mark locations.

    The lines drawn are determined by the placement of minor tick marks
    along the axis. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        for axis in tp.active_frame().plot().axes:
            grid_lines = axis.grid_lines
            grid_lines.show = True

            minor_grid_lines = axis.minor_grid_lines
            minor_grid_lines.show = True
            minor_grid_lines.line_pattern = LinePattern.Dotted
            minor_grid_lines.color = Color.Green

        tp.export.save_png('minor_grid_lines_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/minor_grid_lines_2d.png"
    class="reference internal image-reference"><img
    src="../_images/minor_grid_lines_2d.png" style="width: 300px;"
    alt="../_images/minor_grid_lines_2d.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D.color "tecplot.plot.MinorGridLines2D.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`draw_last`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D.draw_last "tecplot.plot.MinorGridLines2D.draw_last"){.reference .internal}                  Draw grid behind all other plot elements.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D.line_pattern "tecplot.plot.MinorGridLines2D.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D.line_thickness "tecplot.plot.MinorGridLines2D.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D.pattern_length "tecplot.plot.MinorGridLines2D.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MinorGridLines2D.show "tecplot.plot.MinorGridLines2D.show"){.reference .internal}                                 Draw grid lines as tick locations.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MinorGridLines2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines2D.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MinorGridLines2D.]{.pre}]{.sig-prename .descclassname}[[draw_last]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines2D.draw_last "Link to this definition"){.headerlink}

:   Draw grid behind all other plot elements.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.grid_lines.draw_last = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MinorGridLines2D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines2D.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[MinorGridLines2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MinorGridLines2D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines2D.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MinorGridLines2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MinorGridLines2D.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#polaranglegridlines .section}
#### [PolarAngleGridLines](#id118){.toc-backref role="doc-backlink"}[¶](#polaranglegridlines "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarAngleGridLines]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#PolarAngleGridLines){.reference .internal}[¶](#tecplot.plot.PolarAngleGridLines "Link to this definition"){.headerlink}

:   Major grid lines along the theta axis.

    The lines drawn are determined by the placement of minor tick marks
    along the axis. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode, LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.theta_axis.mode = ThetaMode.Radians
        plot.axes.grid_area.filled = True
        plot.axes.grid_area.fill_color = Color.Creme

        for axis in plot.axes:
            grid_lines = axis.grid_lines
            grid_lines.show = True
            grid_lines.line_pattern = LinePattern.LongDash
            grid_lines.color = Color.Green

        for lmap in plot.linemaps():
            lmap.show_in_legend = False
            lmap.line.line_pattern = LinePattern.Solid
            lmap.line.line_thickness = 0.8

        tp.export.save_png('grid_lines_polar.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/grid_lines_polar.png"
    class="reference internal image-reference"><img
    src="../_images/grid_lines_polar.png" style="width: 300px;"
    alt="../_images/grid_lines_polar.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.color "tecplot.plot.PolarAngleGridLines.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`draw_last`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.draw_last "tecplot.plot.PolarAngleGridLines.draw_last"){.reference .internal}                  Draw grid behind all other plot elements.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.line_pattern "tecplot.plot.PolarAngleGridLines.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.line_thickness "tecplot.plot.PolarAngleGridLines.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.pattern_length "tecplot.plot.PolarAngleGridLines.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`radial_cutoff`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.radial_cutoff "tecplot.plot.PolarAngleGridLines.radial_cutoff"){.reference .internal}      Minimum radial position of theta grid lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleGridLines.show "tecplot.plot.PolarAngleGridLines.show"){.reference .internal}                                 Draw grid lines as tick locations.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[draw_last]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.draw_last "Link to this definition"){.headerlink}

:   Draw grid behind all other plot elements.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.grid_lines.draw_last = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[radial_cutoff]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.radial_cutoff "Link to this definition"){.headerlink}

:   Minimum radial position of theta grid lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.grid_lines.radial_cutoff = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent along r-axis.

<!-- -->

[[PolarAngleGridLines.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleGridLines.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#polarangleminorgridlines .section}
#### [PolarAngleMinorGridLines](#id119){.toc-backref role="doc-backlink"}[¶](#polarangleminorgridlines "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarAngleMinorGridLines]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#PolarAngleMinorGridLines){.reference .internal}[¶](#tecplot.plot.PolarAngleMinorGridLines "Link to this definition"){.headerlink}

:   Minor grid lines along the theta axis.

    The lines drawn are determined by the placement of minor tick marks
    along the axis. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, ThetaMode, LinePattern, Color

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.PolarLine)
        plot.activate()

        plot.axes.theta_axis.mode = ThetaMode.Radians
        plot.axes.grid_area.filled = True
        plot.axes.grid_area.fill_color = Color.Creme

        for axis in plot.axes:
            grid_lines = axis.grid_lines
            grid_lines.show = True

            minor_grid_lines = axis.minor_grid_lines
            minor_grid_lines.show = True
            minor_grid_lines.line_pattern = LinePattern.Dotted
            minor_grid_lines.color = Color.Green

        for lmap in plot.linemaps():
            lmap.show_in_legend = False
            lmap.line.line_pattern = LinePattern.Solid
            lmap.line.line_thickness = 0.8

        tp.export.save_png('minor_grid_lines_polar.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/minor_grid_lines_polar.png"
    class="reference internal image-reference"><img
    src="../_images/minor_grid_lines_polar.png" style="width: 300px;"
    alt="../_images/minor_grid_lines_polar.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.color "tecplot.plot.PolarAngleMinorGridLines.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`draw_last`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.draw_last "tecplot.plot.PolarAngleMinorGridLines.draw_last"){.reference .internal}                  Draw grid behind all other plot elements.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.line_pattern "tecplot.plot.PolarAngleMinorGridLines.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.line_thickness "tecplot.plot.PolarAngleMinorGridLines.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.pattern_length "tecplot.plot.PolarAngleMinorGridLines.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`radial_cutoff`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.radial_cutoff "tecplot.plot.PolarAngleMinorGridLines.radial_cutoff"){.reference .internal}      Minimum radial position of theta grid lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMinorGridLines.show "tecplot.plot.PolarAngleMinorGridLines.show"){.reference .internal}                                 Draw grid lines as tick locations.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[draw_last]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.draw_last "Link to this definition"){.headerlink}

:   Draw grid behind all other plot elements.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.grid_lines.draw_last = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[radial_cutoff]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.radial_cutoff "Link to this definition"){.headerlink}

:   Minimum radial position of theta grid lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.grid_lines.radial_cutoff = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent along r-axis.

<!-- -->

[[PolarAngleMinorGridLines.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMinorGridLines.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#markergridline .section}
#### [MarkerGridLine](#id120){.toc-backref role="doc-backlink"}[¶](#markergridline "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[MarkerGridLine]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#MarkerGridLine){.reference .internal}[¶](#tecplot.plot.MarkerGridLine "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, PositionMarkerBy

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.Cartesian3D)
        plot.activate()

        plot.axes.grid_area.fill_color = Color.Grey

        plot.axes.x_axis.show = True
        plot.axes.y_axis.show = True

        marker = plot.axes.x_axis.marker_grid_line
        marker.show = True
        marker.position_by = PositionMarkerBy.Constant
        marker.position = 1.5
        marker.color = Color.Cyan

        marker = plot.axes.y_axis.marker_grid_line
        marker.show = True
        marker.position_by = PositionMarkerBy.Constant
        marker.position = 0.5
        marker.color = Color.Yellow

        plot.view.fit()

        tp.export.save_png('marker_grid_line.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/marker_grid_line.png"
    class="reference internal image-reference"><img
    src="../_images/marker_grid_line.png" style="width: 300px;"
    alt="../_images/marker_grid_line.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.color "tecplot.plot.MarkerGridLine.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.line_pattern "tecplot.plot.MarkerGridLine.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.line_thickness "tecplot.plot.MarkerGridLine.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.pattern_length "tecplot.plot.MarkerGridLine.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.position "tecplot.plot.MarkerGridLine.position"){.reference .internal}                     Position of the marker line in axes coordinates.
      [[`position_by`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.position_by "tecplot.plot.MarkerGridLine.position_by"){.reference .internal}            Position of the marker line in axes coordinates.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine.show "tecplot.plot.MarkerGridLine.show"){.reference .internal}                                 Draw grid lines as tick locations.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.position "Link to this definition"){.headerlink}

:   Position of the marker line in axes coordinates.

    The [`position_by`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`PositionMarkerBy.Constant`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.Constant "tecplot.constant.PositionMarkerBy.Constant"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PositionMarkerBy
        >>> marker_line = plot.axes.x_axis.marker_grid_line
        >>> marker_line.position_by = PositionMarkerBy.Constant
        >>> marker_line.position = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[position_by]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.position_by "Link to this definition"){.headerlink}

:   Position of the marker line in axes coordinates.

    Possible values: [[`PositionMarkerBy.Constant`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.Constant "tecplot.constant.PositionMarkerBy.Constant"){.reference .internal} or

    :   [[`PositionMarkerBy.SolutionTime`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.SolutionTime "tecplot.constant.PositionMarkerBy.SolutionTime"){.reference
        .internal}.

    The position can be set to a constant or to the solution time of the
    linked frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PositionMarkerBy
        >>> marker_line = plot.axes.x_axis.marker_grid_line
        >>> marker_line.position_by = PositionMarkerBy.SolutionTime
    :::
    ::::

    Type[:]{.colon}

    :   [[`PositionMarkerBy`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy "tecplot.constant.PositionMarkerBy"){.reference
        .internal}

<!-- -->

[[MarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#markergridline2d .section}
#### [MarkerGridLine2D](#id121){.toc-backref role="doc-backlink"}[¶](#markergridline2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[MarkerGridLine2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#MarkerGridLine2D){.reference .internal}[¶](#tecplot.plot.MarkerGridLine2D "Link to this definition"){.headerlink}

:   Marker line to indicate a particular position along an axis.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, PositionMarkerBy

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = path.join(examples_dir, 'SimpleData', 'IndependentDependent.lpk')
        dataset = tp.load_layout(datafile)

        plot = tp.active_frame().plot(PlotType.XYLine)
        plot.activate()

        marker = plot.axes.x_axis(0).marker_grid_line
        marker.show = True
        marker.position_by = PositionMarkerBy.Constant
        marker.position = -0.4
        marker.color = Color.Blue

        marker = plot.axes.y_axis(0).marker_grid_line
        marker.show = True
        marker.position_by = PositionMarkerBy.Constant
        marker.position = -0.88
        marker.color = Color.Blue

        tp.export.save_png('marker_grid_line_2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/marker_grid_line_2d.png"
    class="reference internal image-reference"><img
    src="../_images/marker_grid_line_2d.png" style="width: 300px;"
    alt="../_images/marker_grid_line_2d.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.color "tecplot.plot.MarkerGridLine2D.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`draw_last`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.draw_last "tecplot.plot.MarkerGridLine2D.draw_last"){.reference .internal}                  Draw grid behind all other plot elements.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.line_pattern "tecplot.plot.MarkerGridLine2D.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.line_thickness "tecplot.plot.MarkerGridLine2D.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.pattern_length "tecplot.plot.MarkerGridLine2D.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.position "tecplot.plot.MarkerGridLine2D.position"){.reference .internal}                     Position of the marker line in axes coordinates.
      [[`position_by`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.position_by "tecplot.plot.MarkerGridLine2D.position_by"){.reference .internal}            Position of the marker line in axes coordinates.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.MarkerGridLine2D.show "tecplot.plot.MarkerGridLine2D.show"){.reference .internal}                                 Draw grid lines as tick locations.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[draw_last]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.draw_last "Link to this definition"){.headerlink}

:   Draw grid behind all other plot elements.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.grid_lines.draw_last = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.position "Link to this definition"){.headerlink}

:   Position of the marker line in axes coordinates.

    The [`position_by`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`PositionMarkerBy.Constant`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.Constant "tecplot.constant.PositionMarkerBy.Constant"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PositionMarkerBy
        >>> marker_line = plot.axes.x_axis.marker_grid_line
        >>> marker_line.position_by = PositionMarkerBy.Constant
        >>> marker_line.position = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[position_by]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.position_by "Link to this definition"){.headerlink}

:   Position of the marker line in axes coordinates.

    Possible values: [[`PositionMarkerBy.Constant`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.Constant "tecplot.constant.PositionMarkerBy.Constant"){.reference .internal} or

    :   [[`PositionMarkerBy.SolutionTime`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.SolutionTime "tecplot.constant.PositionMarkerBy.SolutionTime"){.reference
        .internal}.

    The position can be set to a constant or to the solution time of the
    linked frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PositionMarkerBy
        >>> marker_line = plot.axes.x_axis.marker_grid_line
        >>> marker_line.position_by = PositionMarkerBy.SolutionTime
    :::
    ::::

    Type[:]{.colon}

    :   [[`PositionMarkerBy`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy "tecplot.constant.PositionMarkerBy"){.reference
        .internal}

<!-- -->

[[MarkerGridLine2D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.MarkerGridLine2D.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#polaranglemarkergridline .section}
#### [PolarAngleMarkerGridLine](#id122){.toc-backref role="doc-backlink"}[¶](#polaranglemarkergridline "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarAngleMarkerGridLine]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axis]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/grid.html#PolarAngleMarkerGridLine){.reference .internal}[¶](#tecplot.plot.PolarAngleMarkerGridLine "Link to this definition"){.headerlink}

:   The marker grid line for the theta axis.

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.color "tecplot.plot.PolarAngleMarkerGridLine.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the grid lines to be drawn.
      [[`draw_last`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.draw_last "tecplot.plot.PolarAngleMarkerGridLine.draw_last"){.reference .internal}                  Draw grid behind all other plot elements.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.line_pattern "tecplot.plot.PolarAngleMarkerGridLine.line_pattern"){.reference .internal}         Pattern style of the grid lines to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.line_thickness "tecplot.plot.PolarAngleMarkerGridLine.line_thickness"){.reference .internal}   Width of the grid lines to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.pattern_length "tecplot.plot.PolarAngleMarkerGridLine.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.position "tecplot.plot.PolarAngleMarkerGridLine.position"){.reference .internal}                     Position of the marker line in axes coordinates.
      [[`position_by`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.position_by "tecplot.plot.PolarAngleMarkerGridLine.position_by"){.reference .internal}            Position of the marker line in axes coordinates.
      [[`radial_cutoff`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.radial_cutoff "tecplot.plot.PolarAngleMarkerGridLine.radial_cutoff"){.reference .internal}      Minimum radial position of theta grid lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarAngleMarkerGridLine.show "tecplot.plot.PolarAngleMarkerGridLine.show"){.reference .internal}                                 Draw grid lines as tick locations.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> grid_lines.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[draw_last]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.draw_last "Link to this definition"){.headerlink}

:   Draw grid behind all other plot elements.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> axis.grid_lines.draw_last = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the grid lines to be drawn.

    Possible values: [[`Solid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Solid "tecplot.constant.LinePattern.Solid"){.reference
    .internal}, [[`Dashed`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dashed "tecplot.constant.LinePattern.Dashed"){.reference
    .internal}, [[`DashDot`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDot "tecplot.constant.LinePattern.DashDot"){.reference
    .internal}, [[`Dotted`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.Dotted "tecplot.constant.LinePattern.Dotted"){.reference
    .internal}, [[`LongDash`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.LongDash "tecplot.constant.LinePattern.LongDash"){.reference
    .internal}, [[`DashDotDot`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern.DashDotDot "tecplot.constant.LinePattern.DashDotDot"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.line_thickness "Link to this definition"){.headerlink}

:   Width of the grid lines to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> grid_lines.line_pattern = LinePattern.LongDash
        >>> grid_lines.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.position "Link to this definition"){.headerlink}

:   Position of the marker line in axes coordinates.

    The [`position_by`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`PositionMarkerBy.Constant`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.Constant "tecplot.constant.PositionMarkerBy.Constant"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PositionMarkerBy
        >>> marker_line = plot.axes.x_axis.marker_grid_line
        >>> marker_line.position_by = PositionMarkerBy.Constant
        >>> marker_line.position = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[position_by]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.position_by "Link to this definition"){.headerlink}

:   Position of the marker line in axes coordinates.

    Possible values: [[`PositionMarkerBy.Constant`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.Constant "tecplot.constant.PositionMarkerBy.Constant"){.reference .internal} or

    :   [[`PositionMarkerBy.SolutionTime`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy.SolutionTime "tecplot.constant.PositionMarkerBy.SolutionTime"){.reference
        .internal}.

    The position can be set to a constant or to the solution time of the
    linked frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PositionMarkerBy
        >>> marker_line = plot.axes.x_axis.marker_grid_line
        >>> marker_line.position_by = PositionMarkerBy.SolutionTime
    :::
    ::::

    Type[:]{.colon}

    :   [[`PositionMarkerBy`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PositionMarkerBy "tecplot.constant.PositionMarkerBy"){.reference
        .internal}

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[radial_cutoff]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.radial_cutoff "Link to this definition"){.headerlink}

:   Minimum radial position of theta grid lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.theta_axis.grid_lines.radial_cutoff = 5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} in percent along r-axis.

<!-- -->

[[PolarAngleMarkerGridLine.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarAngleMarkerGridLine.show "Link to this definition"){.headerlink}

:   Draw grid lines as tick locations.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> grid_lines.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::
::::::::::::::::

::: {#orientationaxis .section}
### [OrientationAxis](#id95){.toc-backref role="doc-backlink"}[¶](#orientationaxis "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[OrientationAxis]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[axes]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/axes.html#OrientationAxis){.reference .internal}[¶](#tecplot.plot.OrientationAxis "Link to this definition"){.headerlink}

:   The orientation axis for 3D Field plots.

    This is the small (x, y, z) reference axis object which can moved,
    resized and modified using this class.

    By default, all 3D plots show the 3D orientation axis in the upper
    right of the frame. It can be repositioned by setting
    [[`position`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.position "tecplot.plot.OrientationAxis.position"){.reference
    .internal} as shown below:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        dataset = tp.load_layout(infile)

        frame = tp.active_frame()
        plot = frame.plot()

        plot.axes.orientation_axis.position = 15, 15
        plot.axes.orientation_axis.color = Color.BrightCyan

        plot.axes.reset_range()
        plot.view.fit()

        tp.export.save_png('axes_orientation.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/axes_orientation.png"
    class="reference internal image-reference"><img
    src="../_images/axes_orientation.png" style="width: 300px;"
    alt="../_images/axes_orientation.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.color "tecplot.plot.OrientationAxis.color"){.reference .internal}                                          [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the orientation axes.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.line_thickness "tecplot.plot.OrientationAxis.line_thickness"){.reference .internal}               Line thickness used when drawing the orientation axis as a percentage of frame height.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.position "tecplot.plot.OrientationAxis.position"){.reference .internal}                                 [`(x,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`y)`{.docutils .literal .notranslate}]{.pre} position of the orientation axis.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.show "tecplot.plot.OrientationAxis.show"){.reference .internal}                                             Enable drawing of the orientation axis.
      [[`show_variable_name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.show_variable_name "tecplot.plot.OrientationAxis.show_variable_name"){.reference .internal}   Use variable names instead of \'X\', \'Y\' and \'Z\'.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.OrientationAxis.size "tecplot.plot.OrientationAxis.size"){.reference .internal}                                             Size of the orientation axis as a percentage of frame size (0-100).
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[OrientationAxis.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.OrientationAxis.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the orientation axes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.axes.orientation_axis.color = Color.Cyan
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[OrientationAxis.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.OrientationAxis.line_thickness "Link to this definition"){.headerlink}

:   Line thickness used when drawing the orientation axis as a
    percentage of frame height.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.orientation_axis.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrientationAxis.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.OrientationAxis.position "Link to this definition"){.headerlink}

:   [`(x,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`y)`{.docutils .literal .notranslate}]{.pre} position
    of the orientation axis.

    The position is in percent from the lower-left corner of the
    viewport:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.orientation_axis.position = (15, 15)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrientationAxis.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.OrientationAxis.show "Link to this definition"){.headerlink}

:   Enable drawing of the orientation axis.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.orientation_axis.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrientationAxis.]{.pre}]{.sig-prename .descclassname}[[show_variable_name]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.OrientationAxis.show_variable_name "Link to this definition"){.headerlink}

:   Use variable names instead of 'X', 'Y' and 'Z'.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.orientation_axis.show_variable_name = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[OrientationAxis.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.OrientationAxis.size "Link to this definition"){.headerlink}

:   Size of the orientation axis as a percentage of frame size (0-100).

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.axes.orientation_axis.size = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::
:::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::

::: clearer
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::
