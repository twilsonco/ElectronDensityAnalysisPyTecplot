:::::::::::::::::::::::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::::::::::::::::::::::: {#plot .section}
[]{#id1}

# Plot[¶](#plot "Link to this heading"){.headerlink}

- [Plots](#plots){#id5 .reference .internal}

  - [Cartesian2DFieldPlot](#cartesian2dfieldplot){#id6 .reference
    .internal}

  - [Cartesian3DFieldPlot](#cartesian3dfieldplot){#id7 .reference
    .internal}

  - [PolarLinePlot](#polarlineplot){#id8 .reference .internal}

  - [XYLinePlot](#xylineplot){#id9 .reference .internal}

  - [SketchPlot](#sketchplot){#id10 .reference .internal}

- [Fieldmaps](#fieldmaps){#id11 .reference .internal}

  - [Cartesian2DFieldmap](#cartesian2dfieldmap){#id12 .reference
    .internal}

  - [Cartesian2DFieldmapCollection](#cartesian2dfieldmapcollection){#id13
    .reference .internal}

  - [Cartesian3DFieldmap](#cartesian3dfieldmap){#id14 .reference
    .internal}

  - [Cartesian3DFieldmapCollection](#cartesian3dfieldmapcollection){#id15
    .reference .internal}

  - [FieldmapContour](#fieldmapcontour){#id16 .reference .internal}

  - [FieldmapEdge](#fieldmapedge){#id17 .reference .internal}

  - [FieldmapEffects](#fieldmapeffects){#id18 .reference .internal}

  - [FieldmapEffects3D](#fieldmapeffects3d){#id19 .reference .internal}

  - [FieldmapMesh](#fieldmapmesh){#id20 .reference .internal}

  - [FieldmapPoints](#fieldmappoints){#id21 .reference .internal}

  - [FieldmapScatter](#fieldmapscatter){#id22 .reference .internal}

  - [GeometryScatterSymbol](#geometryscattersymbol){#id23 .reference
    .internal}

  - [TextScatterSymbol](#textscattersymbol){#id24 .reference .internal}

  - [FieldmapShade](#fieldmapshade){#id25 .reference .internal}

  - [FieldmapShade3D](#fieldmapshade3d){#id26 .reference .internal}

  - [FieldmapSurfaces](#fieldmapsurfaces){#id27 .reference .internal}

  - [FieldmapVector](#fieldmapvector){#id28 .reference .internal}

- [Linemaps](#linemaps){#id29 .reference .internal}

  - [PolarLinemap](#polarlinemap){#id30 .reference .internal}

  - [PolarLinemapCollection](#polarlinemapcollection){#id31 .reference
    .internal}

  - [XYLinemap](#xylinemap){#id32 .reference .internal}

  - [XYLinemapCollection](#xylinemapcollection){#id33 .reference
    .internal}

  - [LinemapLine](#linemapline){#id34 .reference .internal}

  - [LinemapCurve](#linemapcurve){#id35 .reference .internal}

  - [LinemapBars](#linemapbars){#id36 .reference .internal}

  - [LinemapErrorBars](#linemaperrorbars){#id37 .reference .internal}

  - [LinemapIndices](#linemapindices){#id38 .reference .internal}

  - [LinemapSymbols](#linemapsymbols){#id39 .reference .internal}

  - [GeometrySymbol](#geometrysymbol){#id40 .reference .internal}

  - [TextSymbol](#textsymbol){#id41 .reference .internal}

:::::::: {#plots .section}
## [Plots](#id5){.toc-backref role="doc-backlink"}[¶](#plots "Link to this heading"){.headerlink}

- [Cartesian2DFieldPlot](#cartesian2dfieldplot){#id42 .reference
  .internal}

- [Cartesian3DFieldPlot](#cartesian3dfieldplot){#id43 .reference
  .internal}

- [PolarLinePlot](#polarlineplot){#id44 .reference .internal}

- [XYLinePlot](#xylineplot){#id45 .reference .internal}

- [SketchPlot](#sketchplot){#id46 .reference .internal}

::: {#cartesian2dfieldplot .section}
### [Cartesian2DFieldPlot](#id42){.toc-backref role="doc-backlink"}[¶](#cartesian2dfieldplot "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DFieldPlot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian2DFieldPlot){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldPlot "Link to this definition"){.headerlink}

:   2D plot containing field data associated with style through
    fieldmaps.

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
        plot.activate()

        plot.vector.u_variable = dataset.variable('U(M/S)')
        plot.vector.v_variable = dataset.variable('V(M/S)')

        plot.contour(2).variable = dataset.variable('T(K)')
        plot.contour(2).colormap_name = 'Sequential - Yellow/Green/Blue'

        for z in dataset.zones():
            fmap = plot.fieldmap(z)
            fmap.contour.flood_contour_group = plot.contour(2)

        plot.show_contour = True
        plot.show_vector = True

        # ensure consistent output between interactive (connected) and batch
        plot.contour(2).levels.reset_to_nice()

        # save image to file
        tp.export.save_png('plot_field2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/plot_field2d.png"
    class="reference internal image-reference"><img
    src="../_images/plot_field2d.png" style="width: 300px;"
    alt="../_images/plot_field2d.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active_fieldmap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.active_fieldmap_indices "tecplot.plot.Cartesian2DFieldPlot.active_fieldmap_indices"){.reference .internal}         Set of active fieldmaps by index.
      [[`active_fieldmaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.active_fieldmaps "tecplot.plot.Cartesian2DFieldPlot.active_fieldmaps"){.reference .internal}                              Active fieldmaps in this plot.
      [[`axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.axes "tecplot.plot.Cartesian2DFieldPlot.axes"){.reference .internal}                                                                  Axes style control for this plot.
      [[`data_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.data_labels "tecplot.plot.Cartesian2DFieldPlot.data_labels"){.reference .internal}                                             Node and cell labels.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.draw_order "tecplot.plot.Cartesian2DFieldPlot.draw_order"){.reference .internal}                                                The order in which objects are drawn to the screen.
      [[`hoe_settings`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.hoe_settings "tecplot.plot.Cartesian2DFieldPlot.hoe_settings"){.reference .internal}                                          High order element settings.
      [[`ijk_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.ijk_blanking "tecplot.plot.Cartesian2DFieldPlot.ijk_blanking"){.reference .internal}                                          Mask off cells by [\\((i, j, k)\\)]{.math .notranslate .nohighlight} index.
      [[`linking_between_frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.linking_between_frames "tecplot.plot.Cartesian2DFieldPlot.linking_between_frames"){.reference .internal}            Style linking between frames.
      [[`num_fieldmaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.num_fieldmaps "tecplot.plot.Cartesian2DFieldPlot.num_fieldmaps"){.reference .internal}                                       Number of all fieldmaps in this plot.
      [[`num_solution_times`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.num_solution_times "tecplot.plot.Cartesian2DFieldPlot.num_solution_times"){.reference .internal}                        Number of solution times for all active fieldmaps.
      [[`rgb_coloring`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.rgb_coloring "tecplot.plot.Cartesian2DFieldPlot.rgb_coloring"){.reference .internal}                                          RGB contour flooding style control.
      [[`scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.scatter "tecplot.plot.Cartesian2DFieldPlot.scatter"){.reference .internal}                                                         Plot-local [[`Scatter`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter "tecplot.plot.Scatter"){.reference .internal} style control.
      [[`show_contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_contour "tecplot.plot.Cartesian2DFieldPlot.show_contour"){.reference .internal}                                          Enable contours for this plot.
      [[`show_edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_edge "tecplot.plot.Cartesian2DFieldPlot.show_edge"){.reference .internal}                                                   Enable zone edge lines for this plot.
      [[`show_isosurfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_isosurfaces "tecplot.plot.Cartesian2DFieldPlot.show_isosurfaces"){.reference .internal}                              Show isosurfaces for this plot.
      [[`show_mesh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_mesh "tecplot.plot.Cartesian2DFieldPlot.show_mesh"){.reference .internal}                                                   Enable mesh lines for this plot.
      [[`show_scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_scatter "tecplot.plot.Cartesian2DFieldPlot.show_scatter"){.reference .internal}                                          Enable scatter symbols for this plot.
      [[`show_shade`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_shade "tecplot.plot.Cartesian2DFieldPlot.show_shade"){.reference .internal}                                                Enable surface shading effect for this plot.
      [[`show_slices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_slices "tecplot.plot.Cartesian2DFieldPlot.show_slices"){.reference .internal}                                             Show slices for this plot.
      [[`show_streamtraces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_streamtraces "tecplot.plot.Cartesian2DFieldPlot.show_streamtraces"){.reference .internal}                           Enable drawing [[`Streamtraces`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference .internal} on this plot.
      [[`show_vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.show_vector "tecplot.plot.Cartesian2DFieldPlot.show_vector"){.reference .internal}                                             Enable drawing of vectors.
      [[`solution_time`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.solution_time "tecplot.plot.Cartesian2DFieldPlot.solution_time"){.reference .internal}                                       The current solution time.
      [[`solution_times`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.solution_times "tecplot.plot.Cartesian2DFieldPlot.solution_times"){.reference .internal}                                    [[`List`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of active solution times.
      [[`solution_timestep`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.solution_timestep "tecplot.plot.Cartesian2DFieldPlot.solution_timestep"){.reference .internal}                           The zero-based index of the current solution time.
      [[`streamtraces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.streamtraces "tecplot.plot.Cartesian2DFieldPlot.streamtraces"){.reference .internal}                                          [[`Streamtraces`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference .internal}: Plot-local [[`streamtrace`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference .internal} attributes.
      [[`transient_zone_visibility`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.transient_zone_visibility "tecplot.plot.Cartesian2DFieldPlot.transient_zone_visibility"){.reference .internal}   Policy to determine transient visibility of zones.
      [[`value_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.value_blanking "tecplot.plot.Cartesian2DFieldPlot.value_blanking"){.reference .internal}                                    Mask off cells by value.
      [[`vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.vector "tecplot.plot.Cartesian2DFieldPlot.vector"){.reference .internal}                                                            Vector variable and style control for this plot.
      [[`view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.view "tecplot.plot.Cartesian2DFieldPlot.view"){.reference .internal}                                                                  Axes orientation and limits adjustments.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.activate "tecplot.plot.Cartesian2DFieldPlot.activate"){.reference .internal}()                         Make this the active plot type on the parent frame.
      [[`activated`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.activated "tecplot.plot.Cartesian2DFieldPlot.activated"){.reference .internal}()                      Context to ensure this plot is active.
      [[`contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.contour "tecplot.plot.Cartesian2DFieldPlot.contour"){.reference .internal}(index)                       [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal}: Plot-local [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} style control.
      [[`fieldmap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.fieldmap "tecplot.plot.Cartesian2DFieldPlot.fieldmap"){.reference .internal}(key)                      Returns a [[`Cartesian2DFieldmap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap "tecplot.plot.Cartesian2DFieldmap"){.reference .internal} by [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} or index.
      [[`fieldmap_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.fieldmap_index "tecplot.plot.Cartesian2DFieldPlot.fieldmap_index"){.reference .internal}(zone)   The index of the fieldmap associated with a [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal}.
      [[`fieldmaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.fieldmaps "tecplot.plot.Cartesian2DFieldPlot.fieldmaps"){.reference .internal}(\*keys)                [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference .internal} by [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} or indices.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian2DFieldPlot.activate){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldPlot.activate "Link to this definition"){.headerlink}

:   Make this the active plot type on the parent frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.Cartesian2D)
        >>> plot.activate()
    :::
    ::::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[activated]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.Cartesian2DFieldPlot.activated "Link to this definition"){.headerlink}

:   Context to ensure this plot is active.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame = tecplot.active_frame()
        >>> frame.plot_type = PlotType.XYLine  # set active plot type
        >>> plot = frame.plot(PlotType.Cartesian3D)  # get inactive plot
        >>> print(frame.plot_type)
        PlotType.XYLine
        >>> with plot.activated():
        ...     print(frame.plot_type)  # 3D plot temporarily active
        PlotType.Cartesian3D
        >>> print(frame.plot_type)  # original plot type restored
        PlotType.XYLine
    :::
    ::::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[active_fieldmap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.active_fieldmap_indices "Link to this definition"){.headerlink}

:   Set of active fieldmaps by index.

    This example sets the first three fieldmaps active, disabling all
    others. It then turns on scatter symbols for just these three:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.active_fieldmap_indices = [0, 1, 2]
        >>> plot.fieldmaps(0, 1, 2).scatter.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`set`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[active_fieldmaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.active_fieldmaps "Link to this definition"){.headerlink}

:   Active fieldmaps in this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.active_fieldmaps.vector.show = True
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
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.axes "Link to this definition"){.headerlink}

:   Axes style control for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame.plot_type = PlotType.Cartesian2D
        >>> axes = frame.plot().axes
        >>> axes.x_axis.variable = dataset.variable('U')
        >>> axes.y_axis.variable = dataset.variable('V')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DFieldAxes`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.Cartesian2DFieldAxes "tecplot.plot.Cartesian2DFieldAxes"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[contour]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian2DFieldPlot.contour "Link to this definition"){.headerlink}

:   [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}: Plot-local [[`ContourGroup`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = frame.plot().contour(0)
        >>> contour.colormap_name = 'Magma'
    :::
    ::::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[data_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.data_labels "Link to this definition"){.headerlink}

:   Node and cell labels.

    This object controls displaying labels for every node and/or cell in
    the dataset. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.data_labels.show_cell_labels = True
        >>> plot.data_labels.step_index = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`FieldPlotDataLabels`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.FieldPlotDataLabels "tecplot.plot.FieldPlotDataLabels"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.draw_order "Link to this definition"){.headerlink}

:   The order in which objects are drawn to the screen.

    Possible values: [[`TwoDDrawOrder.ByZone`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TwoDDrawOrder.ByZone "tecplot.constant.TwoDDrawOrder.ByZone"){.reference
    .internal}, [[`TwoDDrawOrder.ByLayer`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TwoDDrawOrder.ByLayer "tecplot.constant.TwoDDrawOrder.ByLayer"){.reference
    .internal}.

    The order is either by [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} or
    by visual layer (contour, mesh, etc.):

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.draw_order = TwoDDrawOrder.ByZone
    :::
    ::::

    Type[:]{.colon}

    :   [[`TwoDDrawOrder`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TwoDDrawOrder "tecplot.constant.TwoDDrawOrder"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[fieldmap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[key]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian2DFieldPlot.fieldmap){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldPlot.fieldmap "Link to this definition"){.headerlink}

:   Returns a [[`Cartesian2DFieldmap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap "tecplot.plot.Cartesian2DFieldmap"){.reference
    .internal} by [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} or
    index.

    Parameters[:]{.colon}

    :   **key** ([[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        or [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- be in the [[`Dataset`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} attached to the associated frame of this plot. A
        negative index is interpreted as counting from the end of the
        available fieldmaps.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap = plot.fieldmap(dataset.zone(0))
        >>> fmap.scatter.show = True
    :::
    ::::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[fieldmap_index]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian2DFieldPlot.fieldmap_index "Link to this definition"){.headerlink}

:   The index of the fieldmap associated with a [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    Parameters[:]{.colon}

    :   **zone** ([[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal})
        -- The [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        object that belongs to the [[`Dataset`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} associated with this plot.

    Returns[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap_index = plot.fieldmap_index(dataset.zone('Zone'))
        >>> plot.fieldmap(fmap_index).show_mesh = True
    :::
    ::::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[fieldmaps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[keys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian2DFieldPlot.fieldmaps){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldPlot.fieldmaps "Link to this definition"){.headerlink}

:   [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
    .internal} by [[Zones]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} or
    indices.

    Parameters[:]{.colon}

    :   **keys** ([[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        or [[`ints`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        must be in the [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} attached to the associated frame of this plot.
        Negative indices are interpreted as counting from the end of the
        available fieldmaps.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmaps = plot.fieldmaps(dataset.zone(0), dataset.zone(1))
        >>> fmaps.scatter.show = True
    :::
    ::::

    ::: versionchanged
    [Changed in version 0.9: ]{.versionmodified
    .changed}[[`fieldmaps`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldPlot.fieldmaps "tecplot.plot.Cartesian2DFieldPlot.fieldmaps"){.reference
    .internal} was changed from a property (0.8 and earlier) to a method
    requiring parentheses.
    :::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[hoe_settings]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.hoe_settings "Link to this definition"){.headerlink}

:   High order element settings.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.hoe_settings.num_subdivision_levels = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`FieldPlotHOESettings`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.FieldPlotHOESettings "tecplot.plot.FieldPlotHOESettings"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[ijk_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.ijk_blanking "Link to this definition"){.headerlink}

:   Mask off cells by [\\((i, j, k)\\)]{.math .notranslate .nohighlight}
    index.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.ijk_blanking.min_percent = (50, 50)
        >>> plot.ijk_blanking.active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`IJKBlanking`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AnimationType.IJKBlanking "tecplot.constant.AnimationType.IJKBlanking"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[linking_between_frames]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.linking_between_frames "Link to this definition"){.headerlink}

:   Style linking between frames.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linking_between_frames.group = 1
        >>> plot.linking_between_frames.link_solution_time = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DPlotLinkingBetweenFrames`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian2DPlotLinkingBetweenFrames "tecplot.plot.Cartesian2DPlotLinkingBetweenFrames"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[num_fieldmaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.num_fieldmaps "Link to this definition"){.headerlink}

:   Number of all fieldmaps in this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(frame.plot().num_fieldmaps)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[num_solution_times]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.num_solution_times "Link to this definition"){.headerlink}

:   Number of solution times for all active fieldmaps.

    ::: {.admonition .note}
    Note

    This only returns the number of *active* solution times. When
    assigning strands and solution times to zones, the zones are placed
    into an *inactive* fieldmap that must be subsequently activated. See
    example below.
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # place all zones into a single fieldmap (strand: 1)
        >>> # with incrementing solution times
        >>> for time, zone in enumerate(dataset.zones()):
        ...     zone.strand = 1
        ...     zone.solution_time = time
        ...
        >>> # We must activate the fieldmap to ensure the plot's
        >>> # solution times have been updated. Since we placed
        >>> # all zones into a single fieldmap, we can assume the
        >>> # first fieldmap (index: 0) is the one we want.
        >>> plot.active_fieldmaps += [0]
        >>>
        >>> # now the plot's solution times are available.
        >>> print(plot.num_solution_times)
        10
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    :::
    ::::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[rgb_coloring]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.rgb_coloring "Link to this definition"){.headerlink}

:   RGB contour flooding style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.rgb_coloring.red_variable = dataset.variable('gas')
        >>> plot.rgb_coloring.green_variable = dataset.variable('oil')
        >>> plot.rgb_coloring.blue_variable = dataset.variable('water')
        >>> plot.show_contour = True
        >>> plot.fieldmaps().contour.flood_contour_group = plot.rgb_coloring
    :::
    ::::

    Type[:]{.colon}

    :   [[`RGBColoring`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.scatter "Link to this definition"){.headerlink}

:   Plot-local [[`Scatter`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter "tecplot.plot.Scatter"){.reference
    .internal} style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> scatter = frame.plot().scatter
        >>> scatter.variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scatter`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter "tecplot.plot.Scatter"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_contour]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_contour "Link to this definition"){.headerlink}

:   Enable contours for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_contour = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_edge "Link to this definition"){.headerlink}

:   Enable zone edge lines for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_edge = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_isosurfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_isosurfaces "Link to this definition"){.headerlink}

:   Show isosurfaces for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_isosurfaces(True)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_mesh]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_mesh "Link to this definition"){.headerlink}

:   Enable mesh lines for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_mesh = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_scatter "Link to this definition"){.headerlink}

:   Enable scatter symbols for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_scatter = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_shade]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_shade "Link to this definition"){.headerlink}

:   Enable surface shading effect for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_shade = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_slices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_slices "Link to this definition"){.headerlink}

:   Show slices for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_slices(True)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_streamtraces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_streamtraces "Link to this definition"){.headerlink}

:   Enable drawing [[`Streamtraces`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference
    .internal} on this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_streamtraces = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.show_vector "Link to this definition"){.headerlink}

:   Enable drawing of vectors.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_vector = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[solution_time]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.solution_time "Link to this definition"){.headerlink}

:   The current solution time.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0]
        >>> plot.solution_time = 1.0
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
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[solution_times]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.solution_times "Link to this definition"){.headerlink}

:   [[`List`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of active solution times.

    ::: {.admonition .note}
    Note

    This only returns the list of *active* solution times. When
    assigning strands and solution times to zones, the zones are placed
    into an *inactive* fieldmap that must be subsequently activated. See
    example below.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0]
    :::
    ::::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`floats`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[solution_timestep]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.solution_timestep "Link to this definition"){.headerlink}

:   The zero-based index of the current solution time.

    A negative index is interpreted as counting from the end of the
    available solution timesteps. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0]
        >>> print(plot.solution_time)
        0.0
        >>> plot.solution_timestep += 1
        >>> print(plot.solution_time)
        1.0
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
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[streamtraces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.streamtraces "Link to this definition"){.headerlink}

:   [[`Streamtraces`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference
    .internal}: Plot-local [[`streamtrace`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference
    .internal} attributes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> streamtraces = frame.plot().streamtraces
        >>> streamtraces.color = Color.Blue
    :::
    ::::

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[transient_zone_visibility]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.transient_zone_visibility "Link to this definition"){.headerlink}

:   Policy to determine transient visibility of zones.

    Possible values: [[`ZonesAtOrBeforeSolutionTime`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientZoneVisibility.ZonesAtOrBeforeSolutionTime "tecplot.constant.TransientZoneVisibility.ZonesAtOrBeforeSolutionTime"){.reference
    .internal}, [[`ZonesAtSolutionTime`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientZoneVisibility.ZonesAtSolutionTime "tecplot.constant.TransientZoneVisibility.ZonesAtSolutionTime"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TransientZoneVisibility
        >>> plot.transient_zone_visibility = \
        ...     TransientZoneVisibility.ZonesAtSolutionTime
    :::
    ::::

    ::: versionadded
    [New in version 2021.2: ]{.versionmodified .added}Transient zone
    visibility requires Tecplot 360 2021 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`TransientZoneVisibility`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientZoneVisibility "tecplot.constant.TransientZoneVisibility"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[value_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.value_blanking "Link to this definition"){.headerlink}

:   Mask off cells by value.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).comparison_value = 3.14
        >>> plot.value_blanking.constraint(0).active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueBlanking`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.blanking.html#tecplot.plot.ValueBlanking "tecplot.plot.ValueBlanking"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.vector "Link to this definition"){.headerlink}

:   Vector variable and style control for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.vector.u_variable = dataset.variable('U')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Vector2D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Vector2D "tecplot.plot.Vector2D"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[view]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldPlot.view "Link to this definition"){.headerlink}

:   Axes orientation and limits adjustments.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.view.fit()
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian2DFieldView`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian2DFieldView "tecplot.plot.Cartesian2DFieldView"){.reference
        .internal}
:::

::: {#cartesian3dfieldplot .section}
### [Cartesian3DFieldPlot](#id43){.toc-backref role="doc-backlink"}[¶](#cartesian3dfieldplot "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian3DFieldPlot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot "Link to this definition"){.headerlink}

:   3D plot containing field data associated with style through
    fieldmaps.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'SpaceShip.lpk')
        dataset = tp.load_layout(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian3D)
        plot.activate()
        plot.use_lighting_effect = False
        plot.show_streamtraces = False
        plot.use_translucency = True

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        # save image to file
        tp.export.save_png('plot_field3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/plot_field3d.png"
    class="reference internal image-reference"><img
    src="../_images/plot_field3d.png" style="width: 300px;"
    alt="../_images/plot_field3d.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active_fieldmap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.active_fieldmap_indices "tecplot.plot.Cartesian3DFieldPlot.active_fieldmap_indices"){.reference .internal}         Set of active fieldmaps by index.
      [[`active_fieldmaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.active_fieldmaps "tecplot.plot.Cartesian3DFieldPlot.active_fieldmaps"){.reference .internal}                              Active fieldmaps in this plot.
      [[`axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.axes "tecplot.plot.Cartesian3DFieldPlot.axes"){.reference .internal}                                                                  Axes style control for this plot.
      [[`data_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.data_labels "tecplot.plot.Cartesian3DFieldPlot.data_labels"){.reference .internal}                                             Node and cell labels.
      [[`hoe_settings`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.hoe_settings "tecplot.plot.Cartesian3DFieldPlot.hoe_settings"){.reference .internal}                                          High order element settings.
      [[`ijk_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.ijk_blanking "tecplot.plot.Cartesian3DFieldPlot.ijk_blanking"){.reference .internal}                                          Mask off cells by [\\((i, j, k)\\)]{.math .notranslate .nohighlight} index.
      [[`light_source`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.light_source "tecplot.plot.Cartesian3DFieldPlot.light_source"){.reference .internal}                                          Control the direction and effects of lighting.
      [[`line_lift_fraction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.line_lift_fraction "tecplot.plot.Cartesian3DFieldPlot.line_lift_fraction"){.reference .internal}                        Lift lines above plot by percentage distance to the eye.
      [[`linking_between_frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.linking_between_frames "tecplot.plot.Cartesian3DFieldPlot.linking_between_frames"){.reference .internal}            Style linking between frames.
      [[`near_plane_fraction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.near_plane_fraction "tecplot.plot.Cartesian3DFieldPlot.near_plane_fraction"){.reference .internal}                     position of the \"near plane\".
      [[`num_fieldmaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.num_fieldmaps "tecplot.plot.Cartesian3DFieldPlot.num_fieldmaps"){.reference .internal}                                       Number of all fieldmaps in this plot.
      [[`num_solution_times`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.num_solution_times "tecplot.plot.Cartesian3DFieldPlot.num_solution_times"){.reference .internal}                        Number of solution times for all active fieldmaps.
      [[`perform_extra_sorting`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.perform_extra_sorting "tecplot.plot.Cartesian3DFieldPlot.perform_extra_sorting"){.reference .internal}               Use a more robust depth sorting algorithm for display.
      [[`rgb_coloring`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.rgb_coloring "tecplot.plot.Cartesian3DFieldPlot.rgb_coloring"){.reference .internal}                                          RGB contour flooding style control.
      [[`scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.scatter "tecplot.plot.Cartesian3DFieldPlot.scatter"){.reference .internal}                                                         Plot-local [[`Scatter`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter "tecplot.plot.Scatter"){.reference .internal} style control.
      [[`show_contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_contour "tecplot.plot.Cartesian3DFieldPlot.show_contour"){.reference .internal}                                          Enable contours for this plot.
      [[`show_edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_edge "tecplot.plot.Cartesian3DFieldPlot.show_edge"){.reference .internal}                                                   Enable zone edge lines for this plot.
      [[`show_isosurfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_isosurfaces "tecplot.plot.Cartesian3DFieldPlot.show_isosurfaces"){.reference .internal}                              Show isosurfaces for this plot.
      [[`show_mesh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_mesh "tecplot.plot.Cartesian3DFieldPlot.show_mesh"){.reference .internal}                                                   Enable mesh lines for this plot.
      [[`show_scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_scatter "tecplot.plot.Cartesian3DFieldPlot.show_scatter"){.reference .internal}                                          Enable scatter symbols for this plot.
      [[`show_shade`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_shade "tecplot.plot.Cartesian3DFieldPlot.show_shade"){.reference .internal}                                                Enable surface shading effect for this plot.
      [[`show_slices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_slices "tecplot.plot.Cartesian3DFieldPlot.show_slices"){.reference .internal}                                             Show slices for this plot.
      [[`show_streamtraces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_streamtraces "tecplot.plot.Cartesian3DFieldPlot.show_streamtraces"){.reference .internal}                           Enable drawing [[`Streamtraces`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference .internal} on this plot.
      [[`show_vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.show_vector "tecplot.plot.Cartesian3DFieldPlot.show_vector"){.reference .internal}                                             Enable drawing of vectors.
      [[`solution_time`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference .internal}                                       The current solution time.
      [[`solution_times`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_times "tecplot.plot.Cartesian3DFieldPlot.solution_times"){.reference .internal}                                    [[`List`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of active solution times.
      [[`solution_timestep`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference .internal}                           The zero-based index of the current solution time.
      [[`streamtraces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.streamtraces "tecplot.plot.Cartesian3DFieldPlot.streamtraces"){.reference .internal}                                          [[`Streamtraces`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference .internal}: Plot-local [[`streamtrace`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference .internal} attributes.
      [[`symbol_lift_fraction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.symbol_lift_fraction "tecplot.plot.Cartesian3DFieldPlot.symbol_lift_fraction"){.reference .internal}                  Lift symbols above plot by percentage distance to the eye.
      [[`transient_zone_visibility`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.transient_zone_visibility "tecplot.plot.Cartesian3DFieldPlot.transient_zone_visibility"){.reference .internal}   Policy to determine transient visibility of zones.
      [[`use_lighting_effect`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.use_lighting_effect "tecplot.plot.Cartesian3DFieldPlot.use_lighting_effect"){.reference .internal}                     Enable lighting effect for all objects within this plot.
      [[`use_translucency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.use_translucency "tecplot.plot.Cartesian3DFieldPlot.use_translucency"){.reference .internal}                              Enable translucent effect for all objects within this plot.
      [[`value_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.value_blanking "tecplot.plot.Cartesian3DFieldPlot.value_blanking"){.reference .internal}                                    Mask off cells by value.
      [[`vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.vector "tecplot.plot.Cartesian3DFieldPlot.vector"){.reference .internal}                                                            Vector variable and style control for this plot.
      [[`vector_lift_fraction`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.vector_lift_fraction "tecplot.plot.Cartesian3DFieldPlot.vector_lift_fraction"){.reference .internal}                  Lift vectors above plot by percentage distance to the eye.
      [[`view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.view "tecplot.plot.Cartesian3DFieldPlot.view"){.reference .internal}                                                                  Viewport, axes orientation and limits adjustments.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.activate "tecplot.plot.Cartesian3DFieldPlot.activate"){.reference .internal}()                         Make this the active plot type on the parent frame.
      [[`activated`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.activated "tecplot.plot.Cartesian3DFieldPlot.activated"){.reference .internal}()                      Context to ensure this plot is active.
      [[`contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.contour "tecplot.plot.Cartesian3DFieldPlot.contour"){.reference .internal}(index)                       [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal}: Plot-local [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} style control.
      [[`fieldmap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.fieldmap "tecplot.plot.Cartesian3DFieldPlot.fieldmap"){.reference .internal}(key)                      Returns a [[`Cartesian3DFieldmap`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap "tecplot.plot.Cartesian3DFieldmap"){.reference .internal} by [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} or index.
      [[`fieldmap_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.fieldmap_index "tecplot.plot.Cartesian3DFieldPlot.fieldmap_index"){.reference .internal}(zone)   The index of the fieldmap associated with a [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal}.
      [[`fieldmaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.fieldmaps "tecplot.plot.Cartesian3DFieldPlot.fieldmaps"){.reference .internal}(\*keys)                [[`Cartesian3DFieldmapCollection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference .internal} by [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} or indices.
      [[`isosurface`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.isosurface "tecplot.plot.Cartesian3DFieldPlot.isosurface"){.reference .internal}(index)              [[`IsosurfaceGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.IsosurfaceGroup "tecplot.plot.IsosurfaceGroup"){.reference .internal}: Plot-local [[`isosurface`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.IsosurfaceGroup "tecplot.plot.IsosurfaceGroup"){.reference .internal} settings.
      [[`slice`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.slice "tecplot.plot.Cartesian3DFieldPlot.slice"){.reference .internal}(index)                             [[`SliceGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroup "tecplot.plot.SliceGroup"){.reference .internal}: Plot-local [[`slice`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroup "tecplot.plot.SliceGroup"){.reference .internal} style control.
      [[`slices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.slices "tecplot.plot.Cartesian3DFieldPlot.slices"){.reference .internal}(\*indices)                      [[`SliceGroupCollection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroupCollection "tecplot.plot.SliceGroupCollection"){.reference .internal}: Plot-local slice style control.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot.activate){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot.activate "Link to this definition"){.headerlink}

:   Make this the active plot type on the parent frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.Cartesian3D)
        >>> plot.activate()
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[activated]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldPlot.activated "Link to this definition"){.headerlink}

:   Context to ensure this plot is active.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame = tecplot.active_frame()
        >>> frame.plot_type = PlotType.XYLine  # set active plot type
        >>> plot = frame.plot(PlotType.Cartesian3D)  # get inactive plot
        >>> print(frame.plot_type)
        PlotType.XYLine
        >>> with plot.activated():
        ...     print(frame.plot_type)  # 3D plot temporarily active
        PlotType.Cartesian3D
        >>> print(frame.plot_type)  # original plot type restored
        PlotType.XYLine
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[active_fieldmap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.active_fieldmap_indices "Link to this definition"){.headerlink}

:   Set of active fieldmaps by index.

    This example sets the first three fieldmaps active, disabling all
    others. It then turns on scatter symbols for just these three:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.active_fieldmap_indices = [0, 1, 2]
        >>> plot.fieldmaps(0, 1, 2).scatter.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`set`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[active_fieldmaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.active_fieldmaps "Link to this definition"){.headerlink}

:   Active fieldmaps in this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.active_fieldmaps.vector.show = True
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
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    Type[:]{.colon}

    :   [[`Cartesian3DFieldmapCollection`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.axes "Link to this definition"){.headerlink}

:   Axes style control for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame.plot_type = PlotType.Cartesian3D
        >>> axes = frame.plot().axes
        >>> axes.x_axis.variable = dataset.variable('U')
        >>> axes.y_axis.variable = dataset.variable('V')
        >>> axes.z_axis.variable = dataset.variable('W')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DFieldAxes`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.Cartesian3DFieldAxes "tecplot.plot.Cartesian3DFieldAxes"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[contour]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldPlot.contour "Link to this definition"){.headerlink}

:   [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}: Plot-local [[`ContourGroup`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = frame.plot().contour(0)
        >>> contour.colormap_name = 'Magma'
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[data_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.data_labels "Link to this definition"){.headerlink}

:   Node and cell labels.

    This object controls displaying labels for every node and/or cell in
    the dataset. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.data_labels.show_cell_labels = True
        >>> plot.data_labels.step_index = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`FieldPlotDataLabels`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.FieldPlotDataLabels "tecplot.plot.FieldPlotDataLabels"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[fieldmap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[key]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot.fieldmap){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot.fieldmap "Link to this definition"){.headerlink}

:   Returns a [[`Cartesian3DFieldmap`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap "tecplot.plot.Cartesian3DFieldmap"){.reference
    .internal} by [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} or
    index.

    Parameters[:]{.colon}

    :   **key** ([[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        or [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        must be in the [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} attached to the associated frame of this plot. A
        negative index is interpreted as counting from the end of the
        available fieldmaps.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap = plot.fieldmap(dataset.zone(0))
        >>> fmap.scatter.show = True
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[fieldmap_index]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[zone]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.Cartesian3DFieldPlot.fieldmap_index "Link to this definition"){.headerlink}

:   The index of the fieldmap associated with a [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    Parameters[:]{.colon}

    :   **zone** ([[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal})
        -- The [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        object that belongs to the [[`Dataset`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} associated with this plot.

    Returns[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmap_index = plot.fieldmap_index(dataset.zone('Zone'))
        >>> plot.fieldmap(fmap_index).show_mesh = True
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[fieldmaps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[keys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot.fieldmaps){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot.fieldmaps "Link to this definition"){.headerlink}

:   [[`Cartesian3DFieldmapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
    .internal} by [[Zones]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} or
    indices.

    Parameters[:]{.colon}

    :   **keys** ([[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        or [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}) -- The [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}
        must be in the [[`Dataset`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
        .internal} attached to the associated frame of this plot.
        Negative indices are interpreted as counting from the end of the
        available fieldmaps.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmaps = plot.fieldmaps(dataset.zone(0), dataset.zone(1))
        >>> fmaps.scatter.show = True
    :::
    ::::

    ::: versionchanged
    [Changed in version 0.9: ]{.versionmodified
    .changed}[[`fieldmaps`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.fieldmaps "tecplot.plot.Cartesian3DFieldPlot.fieldmaps"){.reference
    .internal} was changed from a property (0.8 and earlier) to a method
    requiring parentheses.
    :::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[hoe_settings]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.hoe_settings "Link to this definition"){.headerlink}

:   High order element settings.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.hoe_settings.num_subdivision_levels = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`FieldPlotHOESettings`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.FieldPlotHOESettings "tecplot.plot.FieldPlotHOESettings"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[ijk_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.ijk_blanking "Link to this definition"){.headerlink}

:   Mask off cells by [\\((i, j, k)\\)]{.math .notranslate .nohighlight}
    index.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.ijk_blanking.min_percent = (50, 50)
        >>> plot.ijk_blanking.active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`IJKBlanking`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AnimationType.IJKBlanking "tecplot.constant.AnimationType.IJKBlanking"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[isosurface]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot.isosurface){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot.isosurface "Link to this definition"){.headerlink}

:   [[`IsosurfaceGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.IsosurfaceGroup "tecplot.plot.IsosurfaceGroup"){.reference
    .internal}: Plot-local [[`isosurface`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.IsosurfaceGroup "tecplot.plot.IsosurfaceGroup"){.reference
    .internal} settings.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> isosurface_0 = frame.plot().isosurface(0)
        >>> isosurface_0.mesh.color = Color.Blue
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[light_source]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.light_source "Link to this definition"){.headerlink}

:   Control the direction and effects of lighting.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.light_source.intensity = 70.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`LightSource`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.LightSource "tecplot.plot.LightSource"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[line_lift_fraction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.line_lift_fraction "Link to this definition"){.headerlink}

:   Lift lines above plot by percentage distance to the eye.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.line_lift_fraction = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[linking_between_frames]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.linking_between_frames "Link to this definition"){.headerlink}

:   Style linking between frames.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linking_between_frames.group = 1
        >>> plot.linking_between_frames.link_solution_time = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DPlotLinkingBetweenFrames`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian3DPlotLinkingBetweenFrames "tecplot.plot.Cartesian3DPlotLinkingBetweenFrames"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[near_plane_fraction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.near_plane_fraction "Link to this definition"){.headerlink}

:   position of the "near plane".

    In a 3D plot, the "near plane" acts as a windshield. Anything in
    front of this plane does not display. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.near_plane_fraction = 0.1
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[num_fieldmaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.num_fieldmaps "Link to this definition"){.headerlink}

:   Number of all fieldmaps in this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(frame.plot().num_fieldmaps)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[num_solution_times]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.num_solution_times "Link to this definition"){.headerlink}

:   Number of solution times for all active fieldmaps.

    ::: {.admonition .note}
    Note

    This only returns the number of *active* solution times. When
    assigning strands and solution times to zones, the zones are placed
    into an *inactive* fieldmap that must be subsequently activated. See
    example below.
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> # place all zones into a single fieldmap (strand: 1)
        >>> # with incrementing solution times
        >>> for time, zone in enumerate(dataset.zones()):
        ...     zone.strand = 1
        ...     zone.solution_time = time
        ...
        >>> # We must activate the fieldmap to ensure the plot's
        >>> # solution times have been updated. Since we placed
        >>> # all zones into a single fieldmap, we can assume the
        >>> # first fieldmap (index: 0) is the one we want.
        >>> plot.active_fieldmaps += [0]
        >>>
        >>> # now the plot's solution times are available.
        >>> print(plot.num_solution_times)
        10
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    :::
    ::::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[perform_extra_sorting]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.perform_extra_sorting "Link to this definition"){.headerlink}

:   Use a more robust depth sorting algorithm for display.

    When printing 3D plots in a vector graphics format, Tecplot 360 must
    sort the objects so that it can draw those farthest from the screen
    first and those closest to the screen last. By default, Tecplot 360
    uses a quick sorting algorithm. This is not always accurate and does
    not detect problems such as intersecting objects. When
    [`perform_extra_sorting`{.docutils .literal .notranslate}]{.pre} set
    to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}, Tecplot 360 uses a slower, more accurate approach that
    detects and resolves such problems. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.perform_extra_sorting = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[rgb_coloring]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.rgb_coloring "Link to this definition"){.headerlink}

:   RGB contour flooding style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.rgb_coloring.red_variable = dataset.variable('gas')
        >>> plot.rgb_coloring.green_variable = dataset.variable('oil')
        >>> plot.rgb_coloring.blue_variable = dataset.variable('water')
        >>> plot.show_contour = True
        >>> plot.fieldmaps().contour.flood_contour_group = plot.rgb_coloring
    :::
    ::::

    Type[:]{.colon}

    :   [[`RGBColoring`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.scatter "Link to this definition"){.headerlink}

:   Plot-local [[`Scatter`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter "tecplot.plot.Scatter"){.reference
    .internal} style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> scatter = frame.plot().scatter
        >>> scatter.variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scatter`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter "tecplot.plot.Scatter"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_contour]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_contour "Link to this definition"){.headerlink}

:   Enable contours for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_contour = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_edge "Link to this definition"){.headerlink}

:   Enable zone edge lines for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_edge = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_isosurfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_isosurfaces "Link to this definition"){.headerlink}

:   Show isosurfaces for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_isosurfaces(True)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_mesh]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_mesh "Link to this definition"){.headerlink}

:   Enable mesh lines for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_mesh = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_scatter "Link to this definition"){.headerlink}

:   Enable scatter symbols for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_scatter = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_shade]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_shade "Link to this definition"){.headerlink}

:   Enable surface shading effect for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_shade = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_slices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_slices "Link to this definition"){.headerlink}

:   Show slices for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_slices(True)
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_streamtraces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_streamtraces "Link to this definition"){.headerlink}

:   Enable drawing [[`Streamtraces`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference
    .internal} on this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_streamtraces = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[show_vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.show_vector "Link to this definition"){.headerlink}

:   Enable drawing of vectors.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().show_vector = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[slice]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot.slice){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot.slice "Link to this definition"){.headerlink}

:   [[`SliceGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroup "tecplot.plot.SliceGroup"){.reference
    .internal}: Plot-local [[`slice`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroup "tecplot.plot.SliceGroup"){.reference
    .internal} style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> slice0 = frame.plot().slice(0)
        >>> slice0.mesh.show = True
        >>> slice0.mesh.color = Color.Blue
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[slices]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#Cartesian3DFieldPlot.slices){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldPlot.slices "Link to this definition"){.headerlink}

:   [[`SliceGroupCollection`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroupCollection "tecplot.plot.SliceGroupCollection"){.reference
    .internal}: Plot-local slice style control.

    Example setting setting mesh color of all slices to blue:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> slices = frame.plot().slices()
        >>> slices.mesh.show = True
        >>> slices.mesh.color = Color.Blue
    :::
    ::::

    Example turning on the first two slice's contour layer:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> slices = frame.plot().slices(0, 1)
        >>> slices.contour.show = True
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[solution_time]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.solution_time "Link to this definition"){.headerlink}

:   The current solution time.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0]
        >>> plot.solution_time = 1.0
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
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[solution_times]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.solution_times "Link to this definition"){.headerlink}

:   [[`List`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of active solution times.

    ::: {.admonition .note}
    Note

    This only returns the list of *active* solution times. When
    assigning strands and solution times to zones, the zones are placed
    into an *inactive* fieldmap that must be subsequently activated. See
    example below.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0]
    :::
    ::::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`floats`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[solution_timestep]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "Link to this definition"){.headerlink}

:   The zero-based index of the current solution time.

    A negative index is interpreted as counting from the end of the
    available solution timesteps. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.solution_times)
        [0.0, 1.0, 2.0]
        >>> print(plot.solution_time)
        0.0
        >>> plot.solution_timestep += 1
        >>> print(plot.solution_time)
        1.0
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
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_time "tecplot.plot.Cartesian3DFieldPlot.solution_time"){.reference
    .internal} or [[`plot.solution_timestep`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldPlot.solution_timestep "tecplot.plot.Cartesian3DFieldPlot.solution_timestep"){.reference
    .internal} properties.
    :::

    ::: versionadded
    [New in version 2017.2: ]{.versionmodified .added}Solution time
    manipulation requires Tecplot 360 2017 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[streamtraces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.streamtraces "Link to this definition"){.headerlink}

:   [[`Streamtraces`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference
    .internal}: Plot-local [[`streamtrace`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Streamtraces "tecplot.plot.Streamtraces"){.reference
    .internal} attributes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> streamtraces = frame.plot().streamtraces
        >>> streamtraces.color = Color.Blue
    :::
    ::::

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[symbol_lift_fraction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.symbol_lift_fraction "Link to this definition"){.headerlink}

:   Lift symbols above plot by percentage distance to the eye.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.symbol_lift_fraction = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[transient_zone_visibility]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.transient_zone_visibility "Link to this definition"){.headerlink}

:   Policy to determine transient visibility of zones.

    Possible values: [[`ZonesAtOrBeforeSolutionTime`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientZoneVisibility.ZonesAtOrBeforeSolutionTime "tecplot.constant.TransientZoneVisibility.ZonesAtOrBeforeSolutionTime"){.reference
    .internal}, [[`ZonesAtSolutionTime`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientZoneVisibility.ZonesAtSolutionTime "tecplot.constant.TransientZoneVisibility.ZonesAtSolutionTime"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import TransientZoneVisibility
        >>> plot.transient_zone_visibility = \
        ...     TransientZoneVisibility.ZonesAtSolutionTime
    :::
    ::::

    ::: versionadded
    [New in version 2021.2: ]{.versionmodified .added}Transient zone
    visibility requires Tecplot 360 2021 R2 or later.
    :::

    Type[:]{.colon}

    :   [[`TransientZoneVisibility`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TransientZoneVisibility "tecplot.constant.TransientZoneVisibility"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[use_lighting_effect]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.use_lighting_effect "Link to this definition"){.headerlink}

:   Enable lighting effect for all objects within this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().use_lighting_effect = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[use_translucency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.use_translucency "Link to this definition"){.headerlink}

:   Enable translucent effect for all objects within this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.plot().use_translucency = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[value_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.value_blanking "Link to this definition"){.headerlink}

:   Mask off cells by value.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).comparison_value = 3.14
        >>> plot.value_blanking.constraint(0).active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueBlanking`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.blanking.html#tecplot.plot.ValueBlanking "tecplot.plot.ValueBlanking"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.vector "Link to this definition"){.headerlink}

:   Vector variable and style control for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.vector.u_variable = dataset.variable('U')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Vector3D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Vector3D "tecplot.plot.Vector3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[vector_lift_fraction]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.vector_lift_fraction "Link to this definition"){.headerlink}

:   Lift vectors above plot by percentage distance to the eye.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.vector_lift_fraction = 0.6
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldPlot.]{.pre}]{.sig-prename .descclassname}[[view]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldPlot.view "Link to this definition"){.headerlink}

:   Viewport, axes orientation and limits adjustments.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.view.fit()
    :::
    ::::

    Type[:]{.colon}

    :   [[`Cartesian3DView`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Cartesian3DView "tecplot.plot.Cartesian3DView"){.reference
        .internal}
:::

::: {#polarlineplot .section}
### [PolarLinePlot](#id44){.toc-backref role="doc-backlink"}[¶](#polarlineplot "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarLinePlot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#PolarLinePlot){.reference .internal}[¶](#tecplot.plot.PolarLinePlot "Link to this definition"){.headerlink}

:   Polar plot with line data and associated style through linemaps.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.constant import *

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
        plot.axes.r_axis.max = r.max()
        plot.axes.theta_axis.mode = ThetaMode.Radians
        plot.delete_linemaps()
        lmap = plot.add_linemap('Linemap', zone, dataset.variable('R'),
                                    dataset.variable('Theta'))
        lmap.line.line_thickness = 0.8
        lmap.line.color = Color.Green

        plot.view.fit()

        tp.export.save_png('plot_polar.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/plot_polar.png"
    class="reference internal image-reference"><img
    src="../_images/plot_polar.png" style="width: 300px;"
    alt="../_images/plot_polar.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active_linemap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.active_linemap_indices "tecplot.plot.PolarLinePlot.active_linemap_indices"){.reference .internal}   [[`set`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference .external} of all active linemaps by index.
      [[`active_linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.active_linemaps "tecplot.plot.PolarLinePlot.active_linemaps"){.reference .internal}                        Active linemaps in this plot.
      [[`axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.axes "tecplot.plot.PolarLinePlot.axes"){.reference .internal}                                                         Axes style control for this plot.
      [[`base_font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.base_font "tecplot.plot.PolarLinePlot.base_font"){.reference .internal}                                          Default typeface style control.
      [[`data_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.data_labels "tecplot.plot.PolarLinePlot.data_labels"){.reference .internal}                                    Node and cell labels.
      [[`legend`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.legend "tecplot.plot.PolarLinePlot.legend"){.reference .internal}                                                   Line plot legend style and placement control.
      [[`linking_between_frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.linking_between_frames "tecplot.plot.PolarLinePlot.linking_between_frames"){.reference .internal}   Style linking between frames.
      [[`num_linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.num_linemaps "tecplot.plot.PolarLinePlot.num_linemaps"){.reference .internal}                                 Number of linemaps held by this plot.
      [[`show_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.show_lines "tecplot.plot.PolarLinePlot.show_lines"){.reference .internal}                                       Enable lines for this plot.
      [[`show_symbols`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.show_symbols "tecplot.plot.PolarLinePlot.show_symbols"){.reference .internal}                                 Enable symbols at line vertices for this plot.
      [[`value_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.value_blanking "tecplot.plot.PolarLinePlot.value_blanking"){.reference .internal}                           Mask off points by value.
      [[`view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.view "tecplot.plot.PolarLinePlot.view"){.reference .internal}                                                         View control of the plot relative to the frame.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.activate "tecplot.plot.PolarLinePlot.activate"){.reference .internal}()                                          Make this the active plot type on the parent frame.
      [[`activated`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.activated "tecplot.plot.PolarLinePlot.activated"){.reference .internal}()                                       Context to ensure this plot is active.
      [[`add_linemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.add_linemap "tecplot.plot.PolarLinePlot.add_linemap"){.reference .internal}(\[name, zone, r, theta, show\])   Add a linemap using the specified zone and variables.
      [[`delete_linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.delete_linemaps "tecplot.plot.PolarLinePlot.delete_linemaps"){.reference .internal}(\*linemaps)           Clear all linemaps within this plot.
      [[`linemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.linemap "tecplot.plot.PolarLinePlot.linemap"){.reference .internal}(pattern)                                      Returns a specific linemap within this plot.
      [[`linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.linemaps "tecplot.plot.PolarLinePlot.linemaps"){.reference .internal}(\*keys)                                    [[`PolarLinemapCollection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection "tecplot.plot.PolarLinemapCollection"){.reference .internal} by index or name.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#PolarLinePlot.activate){.reference .internal}[¶](#tecplot.plot.PolarLinePlot.activate "Link to this definition"){.headerlink}

:   Make this the active plot type on the parent frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.activate()
    :::
    ::::

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[activated]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.PolarLinePlot.activated "Link to this definition"){.headerlink}

:   Context to ensure this plot is active.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame = tecplot.active_frame()
        >>> frame.plot_type = PlotType.XYLine  # set active plot type
        >>> plot = frame.plot(PlotType.Cartesian3D)  # get inactive plot
        >>> print(frame.plot_type)
        PlotType.XYLine
        >>> with plot.activated():
        ...     print(frame.plot_type)  # 3D plot temporarily active
        PlotType.Cartesian3D
        >>> print(frame.plot_type)  # original plot type restored
        PlotType.XYLine
    :::
    ::::

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[active_linemap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.active_linemap_indices "Link to this definition"){.headerlink}

:   [[`set`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
    .external} of all active linemaps by index.

    Numbers are zero-based indices to the linemaps:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> active_indices = plot.active_linemap_indices
        >>> active_lmaps = [plot.linemap(i) for i in active_indices]
    :::
    ::::

    Type[:]{.colon}

    :   [[`set`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[active_linemaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.active_linemaps "Link to this definition"){.headerlink}

:   Active linemaps in this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.active_linemaps.show_symbols = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarLinemapCollection`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection "tecplot.plot.PolarLinemapCollection"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[add_linemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zone]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[r]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[theta]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[show]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#PolarLinePlot.add_linemap){.reference .internal}[¶](#tecplot.plot.PolarLinePlot.add_linemap "Link to this definition"){.headerlink}

:   Add a linemap using the specified zone and variables.

    Parameters[:]{.colon}

    :   - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Name of the linemap which can be used for
          retrieving with [[`PolarLinePlot.linemap`{.xref .any .py
          .py-meth .docutils .literal
          .notranslate}]{.pre}](#tecplot.plot.PolarLinePlot.linemap "tecplot.plot.PolarLinePlot.linemap"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then the linemap will not have a name. Default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **zone** ([[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal}) -- The data to be used when drawing this linemap.
          If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will select a [[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal}. Default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **r** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The [`r`{.docutils .literal
          .notranslate}]{.pre} variable which must be from the same
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} as [`theta`{.docutils .literal .notranslate}]{.pre}
          and [`zone`{.docutils .literal .notranslate}]{.pre}. If
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will select a variable.
          Default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **theta** ([[`Variable`{.xref .any .py .py-attr .docutils
          .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The [`theta`{.docutils .literal
          .notranslate}]{.pre} variable which must be from the same
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} as [`r`{.docutils .literal .notranslate}]{.pre} and
          [`zone`{.docutils .literal .notranslate}]{.pre}. If
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will select a variable.
          Default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **show** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Enable this linemap as soon as it's
          added. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external})

    Returns[:]{.colon}

    :   [[`PolarLinemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarLinemap "tecplot.plot.PolarLinemap"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> lmap = plot.add_linemap('Line 1', dataset.zone('Zone'),
        ...                         dataset.variable('R'),
        ...                         dataset.variable('Theta'))
        >>> lmap.line.line_thickness = 0.8
    :::
    ::::

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.axes "Link to this definition"){.headerlink}

:   Axes style control for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType, ThetaMode
        >>> frame.plot_type = PlotType.PolarLine
        >>> axes = frame.plot().axes
        >>> axes.theta_mode = ThetaMode.Radians
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarLineAxes`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.PolarLineAxes "tecplot.plot.PolarLineAxes"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[base_font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.base_font "Link to this definition"){.headerlink}

:   Default typeface style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.base_font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`BaseFont`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.BaseFont "tecplot.text.BaseFont"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[data_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.data_labels "Link to this definition"){.headerlink}

:   Node and cell labels.

    This object controls displaying labels for every node and/or cell in
    the dataset. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.data_labels.show_node_labels = True
        >>> plot.data_labels.step_index = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePlotDataLabels`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.LinePlotDataLabels "tecplot.plot.LinePlotDataLabels"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[delete_linemaps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[linemaps]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.PolarLinePlot.delete_linemaps "Link to this definition"){.headerlink}

:   Clear all linemaps within this plot.

    Parameters[:]{.colon}

    :   **\*linemaps** ([[Linemaps]{.std .std-ref}](#linemap){.reference
        .internal}, [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} or [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}) -- One or more of the following: [[Linemaps]{.std
        .std-ref}](#linemap){.reference .internal} objects, linemap
        indices (zero-based) or linemap names. If none are given, all
        linemaps will be deleted.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.delete_linemaps()
        >>> print(plot.num_linemaps)
        0
    :::
    ::::

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[legend]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.legend "Link to this definition"){.headerlink}

:   Line plot legend style and placement control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.legend.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`LineLegend`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.legend.LineLegend "tecplot.legend.LineLegend"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[linemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#PolarLinePlot.linemap){.reference .internal}[¶](#tecplot.plot.PolarLinePlot.linemap "Link to this definition"){.headerlink}

:   Returns a specific linemap within this plot.

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
        .external} used to match the linemaps by name. A negative index
        is interpreted as counting from the end of the available
        linemaps.

    Returns[:]{.colon}

    :   [[`PolarLinemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.PolarLinemap "tecplot.plot.PolarLinemap"){.reference
        .internal} corresponding to *pattern* or [[`None`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external} if *pattern* was passed in as a [[`str`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} and no matching linemap was found.

    ::: {.admonition .note}
    Note

    Plots can contain linemaps with identical names and only the first
    match found is returned. This is not guaranteed to be deterministic
    and care should be taken to have only linemaps with unique names
    when this feature is used.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bar.show = True
    :::
    ::::

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[linemaps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[keys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#PolarLinePlot.linemaps){.reference .internal}[¶](#tecplot.plot.PolarLinePlot.linemaps "Link to this definition"){.headerlink}

:   [[`PolarLinemapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection "tecplot.plot.PolarLinemapCollection"){.reference
    .internal} by index or name.

    Parameters[:]{.colon}

    :   **keys** ([[`int`{.xref .any .docutils .literal
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
        .external} used to match the linemaps by name. A negative index
        is interpreted as counting from the end of the available
        linemaps.

    Example usage, adjusting the line thickness for all lines in the
    plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemaps().line.line_thickness = 1.4
    :::
    ::::

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[linking_between_frames]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.linking_between_frames "Link to this definition"){.headerlink}

:   Style linking between frames.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linking_between_frames.group = 1
        >>> plot.linking_between_frames.link_solution_time = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarPlotLinkingBetweenFrames`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.PolarPlotLinkingBetweenFrames "tecplot.plot.PolarPlotLinkingBetweenFrames"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[num_linemaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.num_linemaps "Link to this definition"){.headerlink}

:   Number of linemaps held by this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.num_linemaps)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[show_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.show_lines "Link to this definition"){.headerlink}

:   Enable lines for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_lines = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[show_symbols]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.show_symbols "Link to this definition"){.headerlink}

:   Enable symbols at line vertices for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_symbols = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[value_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.value_blanking "Link to this definition"){.headerlink}

:   Mask off points by value.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).comparison_value = 3.14
        >>> plot.value_blanking.constraint(0).active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueBlanking`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.blanking.html#tecplot.plot.ValueBlanking "tecplot.plot.ValueBlanking"){.reference
        .internal}

<!-- -->

[[PolarLinePlot.]{.pre}]{.sig-prename .descclassname}[[view]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinePlot.view "Link to this definition"){.headerlink}

:   View control of the plot relative to the frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.view.fit()
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarView`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.PolarView "tecplot.plot.PolarView"){.reference
        .internal}
:::

::: {#xylineplot .section}
### [XYLinePlot](#id45){.toc-backref role="doc-backlink"}[¶](#xylineplot "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[XYLinePlot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#XYLinePlot){.reference .internal}[¶](#tecplot.plot.XYLinePlot "Link to this definition"){.headerlink}

:   Cartesian plot with line data and associated style through linemaps.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, FillMode

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'SunSpots.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.XYLine)
        plot.activate()
        plot.show_symbols = True
        plot.linemap(0).symbols.fill_mode = FillMode.UseLineColor
        plot.linemap(0).symbols.size = 1

        tp.export.save_png('plot_xyline.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/plot_xyline.png"
    class="reference internal image-reference"><img
    src="../_images/plot_xyline.png" style="width: 300px;"
    alt="../_images/plot_xyline.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active_linemap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.active_linemap_indices "tecplot.plot.XYLinePlot.active_linemap_indices"){.reference .internal}   [[`set`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference .external} of all active linemaps by index.
      [[`active_linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.active_linemaps "tecplot.plot.XYLinePlot.active_linemaps"){.reference .internal}                        Active linemaps in this plot.
      [[`axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.axes "tecplot.plot.XYLinePlot.axes"){.reference .internal}                                                         Axes style control for this plot.
      [[`base_font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.base_font "tecplot.plot.XYLinePlot.base_font"){.reference .internal}                                          Default typeface style control.
      [[`data_labels`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.data_labels "tecplot.plot.XYLinePlot.data_labels"){.reference .internal}                                    Node and cell labels.
      [[`legend`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.legend "tecplot.plot.XYLinePlot.legend"){.reference .internal}                                                   Line plot legend style and placement control.
      [[`linking_between_frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.linking_between_frames "tecplot.plot.XYLinePlot.linking_between_frames"){.reference .internal}   Style linking between frames.
      [[`num_linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.num_linemaps "tecplot.plot.XYLinePlot.num_linemaps"){.reference .internal}                                 Number of linemaps held by this plot.
      [[`show_bars`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.show_bars "tecplot.plot.XYLinePlot.show_bars"){.reference .internal}                                          Enable bar chart drawing mode for this plot.
      [[`show_error_bars`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.show_error_bars "tecplot.plot.XYLinePlot.show_error_bars"){.reference .internal}                        Enable error bars for this plot.
      [[`show_lines`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.show_lines "tecplot.plot.XYLinePlot.show_lines"){.reference .internal}                                       Enable lines for this plot.
      [[`show_symbols`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.show_symbols "tecplot.plot.XYLinePlot.show_symbols"){.reference .internal}                                 Enable symbols at line vertices for this plot.
      [[`value_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.value_blanking "tecplot.plot.XYLinePlot.value_blanking"){.reference .internal}                           Mask off points by value.
      [[`view`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.view "tecplot.plot.XYLinePlot.view"){.reference .internal}                                                         View control of the plot relative to the frame.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.activate "tecplot.plot.XYLinePlot.activate"){.reference .internal}()                                      Make this the active plot type on the parent frame.
      [[`activated`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.activated "tecplot.plot.XYLinePlot.activated"){.reference .internal}()                                   Context to ensure this plot is active.
      [[`add_linemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.add_linemap "tecplot.plot.XYLinePlot.add_linemap"){.reference .internal}(\[name, zone, x, y, show\])   Add a linemap using the specified zone and variables.
      [[`delete_linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.delete_linemaps "tecplot.plot.XYLinePlot.delete_linemaps"){.reference .internal}(\*linemaps)       Clear all linemaps within this plot.
      [[`linemap`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.linemap "tecplot.plot.XYLinePlot.linemap"){.reference .internal}(pattern)                                  Returns a specific linemap within this plot.
      [[`linemaps`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.linemaps "tecplot.plot.XYLinePlot.linemaps"){.reference .internal}(\*keys)                                [[`XYLinemapCollection`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection "tecplot.plot.XYLinemapCollection"){.reference .internal} by index or name.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#XYLinePlot.activate){.reference .internal}[¶](#tecplot.plot.XYLinePlot.activate "Link to this definition"){.headerlink}

:   Make this the active plot type on the parent frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.XYLine)
        >>> plot.activate()
    :::
    ::::

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[activated]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.XYLinePlot.activated "Link to this definition"){.headerlink}

:   Context to ensure this plot is active.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame = tecplot.active_frame()
        >>> frame.plot_type = PlotType.XYLine  # set active plot type
        >>> plot = frame.plot(PlotType.Cartesian3D)  # get inactive plot
        >>> print(frame.plot_type)
        PlotType.XYLine
        >>> with plot.activated():
        ...     print(frame.plot_type)  # 3D plot temporarily active
        PlotType.Cartesian3D
        >>> print(frame.plot_type)  # original plot type restored
        PlotType.XYLine
    :::
    ::::

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[active_linemap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.active_linemap_indices "Link to this definition"){.headerlink}

:   [[`set`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
    .external} of all active linemaps by index.

    Numbers are zero-based indices to the linemaps:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> active_indices = plot.active_linemap_indices
        >>> active_lmaps = [plot.linemap(i) for i in active_indices]
    :::
    ::::

    Type[:]{.colon}

    :   [[`set`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[active_linemaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.active_linemaps "Link to this definition"){.headerlink}

:   Active linemaps in this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.active_linemaps.show_symbols = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLinemapCollection`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection "tecplot.plot.XYLinemapCollection"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[add_linemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[name]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[zone]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[x]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[y]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*, *[[show]{.pre}]{.n}[[=]{.pre}]{.o}[[True]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#XYLinePlot.add_linemap){.reference .internal}[¶](#tecplot.plot.XYLinePlot.add_linemap "Link to this definition"){.headerlink}

:   Add a linemap using the specified zone and variables.

    Parameters[:]{.colon}

    :   - **name** ([[`str`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
          .external}) -- Name of the linemap which can be used for
          retrieving with [[`XYLinePlot.linemap`{.xref .any .py .py-meth
          .docutils .literal
          .notranslate}]{.pre}](#tecplot.plot.XYLinePlot.linemap "tecplot.plot.XYLinePlot.linemap"){.reference
          .internal}. If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then the linemap will not have a name. Default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **zone** ([[Zone]{.std
          .std-ref}](tecplot.data.html#data-access){.reference
          .internal}) -- The data to be used when drawing this linemap.
          If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will select a zone. Default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **x** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The [`x`{.docutils .literal
          .notranslate}]{.pre} variable which must be from the same
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} as [`y`{.docutils .literal .notranslate}]{.pre} and
          [`zone`{.docutils .literal .notranslate}]{.pre}. If
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will select an x variable.
          Default: [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **y** ([[`Variable`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
          .internal}) -- The [`y`{.docutils .literal
          .notranslate}]{.pre} variable which must be from the same
          [[`Dataset`{.xref .any .py .py-class .docutils .literal
          .notranslate}]{.pre}](tecplot.data.html#tecplot.data.Dataset "tecplot.data.Dataset"){.reference
          .internal} as [`x`{.docutils .literal .notranslate}]{.pre} and
          [`zone`{.docutils .literal .notranslate}]{.pre}. If
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will select a [`y`{.docutils
          .literal .notranslate}]{.pre} variable. Default:
          [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}.

        - **show** ([[`bool`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
          .external}, optional) -- Enable this linemap as soon as it's
          added. (default: [[`True`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
          .external}). If [[`None`{.xref .any .docutils .literal
          .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
          .external}, then Tecplot Engine will determine if the linemap
          should be enabled.

    Returns[:]{.colon}

    :   [[`XYLinemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
        .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> lmap = plot.add_linemap('Line 1', dataset.zone('Zone'),
        ...                         dataset.variable('X'),
        ...                         dataset.variable('Y'))
        >>> lmap.line.line_thickness = 0.8
    :::
    ::::

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.axes "Link to this definition"){.headerlink}

:   Axes style control for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType, AxisMode
        >>> frame.plot_type = PlotType.XYLine
        >>> axes = frame.plot().axes
        >>> axes.axis_mode = AxisMode.XYDependent
        >>> axes.xy_ratio = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLineAxes`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.XYLineAxes "tecplot.plot.XYLineAxes"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[base_font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.base_font "Link to this definition"){.headerlink}

:   Default typeface style control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.base_font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`BaseFont`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.text.BaseFont "tecplot.text.BaseFont"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[data_labels]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.data_labels "Link to this definition"){.headerlink}

:   Node and cell labels.

    This object controls displaying labels for every node and/or cell in
    the dataset. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.data_labels.show_node_labels = True
        >>> plot.data_labels.step_index = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePlotDataLabels`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.LinePlotDataLabels "tecplot.plot.LinePlotDataLabels"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[delete_linemaps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[linemaps]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.XYLinePlot.delete_linemaps "Link to this definition"){.headerlink}

:   Clear all linemaps within this plot.

    Parameters[:]{.colon}

    :   **\*linemaps** ([[Linemaps]{.std .std-ref}](#linemap){.reference
        .internal}, [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} or [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}) -- One or more of the following: [[Linemaps]{.std
        .std-ref}](#linemap){.reference .internal} objects, linemap
        indices (zero-based) or linemap names. If none are given, all
        linemaps will be deleted.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.delete_linemaps()
        >>> print(plot.num_linemaps)
        0
    :::
    ::::

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[legend]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.legend "Link to this definition"){.headerlink}

:   Line plot legend style and placement control.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.legend.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`LineLegend`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.legend.LineLegend "tecplot.legend.LineLegend"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[linemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[pattern]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#XYLinePlot.linemap){.reference .internal}[¶](#tecplot.plot.XYLinePlot.linemap "Link to this definition"){.headerlink}

:   Returns a specific linemap within this plot.

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
        .external} used to match the linemaps by name. A negative index
        is interpreted as counting from the end of the available
        linemaps.

    Returns[:]{.colon}

    :   [[`XYLinemap`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
        .internal} corresponding to *pattern* or [[`None`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external} if *pattern* was passed in as a [[`str`{.xref .any
        .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external} or [[`regex`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`pattern`{.xref .any .docutils .literal
        .notranslate}]{.pre}` `{.xref .any .docutils .literal
        .notranslate}[`instance`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/re.html#re.compile "(in Python v3.13)"){.reference
        .external} and no matching linemap was found.

    ::: {.admonition .note}
    Note

    Plots can contain linemaps with identical names and only the first
    match found is returned. This is not guaranteed to be deterministic
    and care should be taken to have only linemaps with unique names
    when this feature is used.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bar.show = True
    :::
    ::::

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[linemaps]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[\*]{.pre}]{.o}[[keys]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#XYLinePlot.linemaps){.reference .internal}[¶](#tecplot.plot.XYLinePlot.linemaps "Link to this definition"){.headerlink}

:   [[`XYLinemapCollection`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection "tecplot.plot.XYLinemapCollection"){.reference
    .internal} by index or name.

    Parameters[:]{.colon}

    :   **keys** ([[`int`{.xref .any .docutils .literal
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
        .external} used to match the linemaps by name. A negative index
        is interpreted as counting from the end of the available
        linemaps.

    Example usage, adjusting the line thickness for all lines in the
    plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemaps().line.line_thickness = 1.4
    :::
    ::::

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[linking_between_frames]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.linking_between_frames "Link to this definition"){.headerlink}

:   Style linking between frames.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linking_between_frames.group = 1
        >>> plot.linking_between_frames.link_solution_time = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLinePlotLinkingBetweenFrames`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.XYLinePlotLinkingBetweenFrames "tecplot.plot.XYLinePlotLinkingBetweenFrames"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[num_linemaps]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.num_linemaps "Link to this definition"){.headerlink}

:   Number of linemaps held by this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(plot.num_linemaps)
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[show_bars]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.show_bars "Link to this definition"){.headerlink}

:   Enable bar chart drawing mode for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_bars = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[show_error_bars]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.show_error_bars "Link to this definition"){.headerlink}

:   Enable error bars for this plot.

    The variable to be used for error bars must be set first on at least
    one linemap within this plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bars.variable = dataset.variable('E')
        >>> plot.show_error_bars = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[show_lines]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.show_lines "Link to this definition"){.headerlink}

:   Enable lines for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_lines = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[show_symbols]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.show_symbols "Link to this definition"){.headerlink}

:   Enable symbols at line vertices for this plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_symbols = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[value_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.value_blanking "Link to this definition"){.headerlink}

:   Mask off points by value.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).comparison_value = 3.14
        >>> plot.value_blanking.constraint(0).active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueBlanking`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.blanking.html#tecplot.plot.ValueBlanking "tecplot.plot.ValueBlanking"){.reference
        .internal}

<!-- -->

[[XYLinePlot.]{.pre}]{.sig-prename .descclassname}[[view]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinePlot.view "Link to this definition"){.headerlink}

:   View control of the plot relative to the frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.view.fit()
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLineView`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.XYLineView "tecplot.plot.XYLineView"){.reference
        .internal}
:::

::: {#sketchplot .section}
### [SketchPlot](#id46){.toc-backref role="doc-backlink"}[¶](#sketchplot "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[SketchPlot]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[frame]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[svargs]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#SketchPlot){.reference .internal}[¶](#tecplot.plot.SketchPlot "Link to this definition"){.headerlink}

:   A plot space with no data attached.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import PlotType

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Sketch)

        frame.add_text('Hello, World!', (36, 50), size=34)
        plot.axes.x_axis.show = True
        plot.axes.y_axis.show = True

        tp.export.save_png('plot_sketch.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/plot_sketch.png"
    class="reference internal image-reference"><img
    src="../_images/plot_sketch.png" style="width: 300px;"
    alt="../_images/plot_sketch.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------
      [[`axes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchPlot.axes "tecplot.plot.SketchPlot.axes"){.reference .internal}                                                         Axes (x and y) for the sketch plot.
      [[`linking_between_frames`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchPlot.linking_between_frames "tecplot.plot.SketchPlot.linking_between_frames"){.reference .internal}   Style linking between frames.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------

    **Methods**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------
      [[`activate`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchPlot.activate "tecplot.plot.SketchPlot.activate"){.reference .internal}()      Make this the active plot type on the parent frame.
      [[`activated`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.SketchPlot.activated "tecplot.plot.SketchPlot.activated"){.reference .internal}()   Context to ensure this plot is active.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------

<!-- -->

[[SketchPlot.]{.pre}]{.sig-prename .descclassname}[[activate]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/plot.html#SketchPlot.activate){.reference .internal}[¶](#tecplot.plot.SketchPlot.activate "Link to this definition"){.headerlink}

:   Make this the active plot type on the parent frame.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.Sketch)
        >>> plot.activate()
    :::
    ::::

<!-- -->

[[SketchPlot.]{.pre}]{.sig-prename .descclassname}[[activated]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[¶](#tecplot.plot.SketchPlot.activated "Link to this definition"){.headerlink}

:   Context to ensure this plot is active.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame = tecplot.active_frame()
        >>> frame.plot_type = PlotType.XYLine  # set active plot type
        >>> plot = frame.plot(PlotType.Cartesian3D)  # get inactive plot
        >>> print(frame.plot_type)
        PlotType.XYLine
        >>> with plot.activated():
        ...     print(frame.plot_type)  # 3D plot temporarily active
        PlotType.Cartesian3D
        >>> print(frame.plot_type)  # original plot type restored
        PlotType.XYLine
    :::
    ::::

<!-- -->

[[SketchPlot.]{.pre}]{.sig-prename .descclassname}[[axes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchPlot.axes "Link to this definition"){.headerlink}

:   Axes (x and y) for the sketch plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> frame.plot_type = PlotType.Sketch
        >>> frame.plot().axes.x_axis.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`SketchAxes`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.SketchAxes "tecplot.plot.SketchAxes"){.reference
        .internal}

<!-- -->

[[SketchPlot.]{.pre}]{.sig-prename .descclassname}[[linking_between_frames]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.SketchPlot.linking_between_frames "Link to this definition"){.headerlink}

:   Style linking between frames.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linking_between_frames.group = 1
        >>> plot.linking_between_frames.link_solution_time = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`SketchPlotLinkingBetweenFrames`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SketchPlotLinkingBetweenFrames "tecplot.plot.SketchPlotLinkingBetweenFrames"){.reference
        .internal}
:::
::::::::

:::::::::::::::::::: {#fieldmaps .section}
[]{#fieldmap}

## [Fieldmaps](#id11){.toc-backref role="doc-backlink"}[¶](#fieldmaps "Link to this heading"){.headerlink}

- [Cartesian2DFieldmap](#cartesian2dfieldmap){#id47 .reference
  .internal}

- [Cartesian2DFieldmapCollection](#cartesian2dfieldmapcollection){#id48
  .reference .internal}

- [Cartesian3DFieldmap](#cartesian3dfieldmap){#id49 .reference
  .internal}

- [Cartesian3DFieldmapCollection](#cartesian3dfieldmapcollection){#id50
  .reference .internal}

- [FieldmapContour](#fieldmapcontour){#id51 .reference .internal}

- [FieldmapEdge](#fieldmapedge){#id52 .reference .internal}

- [FieldmapEffects](#fieldmapeffects){#id53 .reference .internal}

- [FieldmapEffects3D](#fieldmapeffects3d){#id54 .reference .internal}

- [FieldmapMesh](#fieldmapmesh){#id55 .reference .internal}

- [FieldmapPoints](#fieldmappoints){#id56 .reference .internal}

- [FieldmapScatter](#fieldmapscatter){#id57 .reference .internal}

- [GeometryScatterSymbol](#geometryscattersymbol){#id58 .reference
  .internal}

- [TextScatterSymbol](#textscattersymbol){#id59 .reference .internal}

- [FieldmapShade](#fieldmapshade){#id60 .reference .internal}

- [FieldmapShade3D](#fieldmapshade3d){#id61 .reference .internal}

- [FieldmapSurfaces](#fieldmapsurfaces){#id62 .reference .internal}

- [FieldmapVector](#fieldmapvector){#id63 .reference .internal}

::: {#cartesian2dfieldmap .section}
### [Cartesian2DFieldmap](#id47){.toc-backref role="doc-backlink"}[¶](#cartesian2dfieldmap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DFieldmap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#Cartesian2DFieldmap){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldmap "Link to this definition"){.headerlink}

:   Style control for a single 2D fieldmap.

    ::: {.admonition .seealso}
    See also

    [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
    .internal}
    :::

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.contour "tecplot.plot.Cartesian2DFieldmap.contour"){.reference .internal}                              Style including flooding, lines and line coloring.
      [[`edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.edge "tecplot.plot.Cartesian2DFieldmap.edge"){.reference .internal}                                       Style control for boundary lines.
      [[`effects`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.effects "tecplot.plot.Cartesian2DFieldmap.effects"){.reference .internal}                              Style control for clipping and blanking effects.
      [[`fieldmap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.fieldmap_indices "tecplot.plot.Cartesian2DFieldmap.fieldmap_indices"){.reference .internal}   Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.group "tecplot.plot.Cartesian2DFieldmap.group"){.reference .internal}                                    Zero-based group number for this [[Fieldmaps]{.std .std-ref}](#fieldmap){.reference .internal}.
      [[`mesh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.mesh "tecplot.plot.Cartesian2DFieldmap.mesh"){.reference .internal}                                       Style lines connecting neighboring data points.
      [[`points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.points "tecplot.plot.Cartesian2DFieldmap.points"){.reference .internal}                                 Control which points to draw.
      [[`scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.scatter "tecplot.plot.Cartesian2DFieldmap.scatter"){.reference .internal}                              Style for scatter plots.
      [[`shade`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.shade "tecplot.plot.Cartesian2DFieldmap.shade"){.reference .internal}                                    Style control for surface shading.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.show "tecplot.plot.Cartesian2DFieldmap.show"){.reference .internal}                                       Display this fieldmap on the plot.
      [[`surfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.surfaces "tecplot.plot.Cartesian2DFieldmap.surfaces"){.reference .internal}                           Control which surfaces to draw.
      [[`vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.vector "tecplot.plot.Cartesian2DFieldmap.vector"){.reference .internal}                                 Style for vector field plots using arrows.
      [[`zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap.zones "tecplot.plot.Cartesian2DFieldmap.zones"){.reference .internal}                                    List of [[zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} used by this fieldmap.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[contour]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.contour "Link to this definition"){.headerlink}

:   Style including flooding, lines and line coloring.

    Type[:]{.colon}

    :   [[`FieldmapContour`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapContour "tecplot.plot.FieldmapContour"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.edge "Link to this definition"){.headerlink}

:   Style control for boundary lines.

    Type[:]{.colon}

    :   [[`FieldmapEdge`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge "tecplot.plot.FieldmapEdge"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[effects]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.effects "Link to this definition"){.headerlink}

:   Style control for clipping and blanking effects.

    Type[:]{.colon}

    :   [[`FieldmapEffects`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects "tecplot.plot.FieldmapEffects"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[fieldmap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.fieldmap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[group]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.group "Link to this definition"){.headerlink}

:   Zero-based group number for this [[Fieldmaps]{.std
    .std-ref}](#fieldmap){.reference .internal}.

    This is a piece of auxiliary data and can be useful for identifying
    a subset of fieldmaps. For example, to loop over all fieldmaps that
    have group set to 4:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps(0, 3).group = 4
        >>> for fmap in filter(lambda f: f.group == 4, plot.fieldmaps()):
        ...     print(fmap.index)
        0
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[mesh]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.mesh "Link to this definition"){.headerlink}

:   Style lines connecting neighboring data points.

    Type[:]{.colon}

    :   [[`FieldmapMesh`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh "tecplot.plot.FieldmapMesh"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[points]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.points "Link to this definition"){.headerlink}

:   Control which points to draw.

    Type[:]{.colon}

    :   [[`FieldmapPoints`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapPoints "tecplot.plot.FieldmapPoints"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.scatter "Link to this definition"){.headerlink}

:   Style for scatter plots.

    Type[:]{.colon}

    :   [[`FieldmapScatter`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter "tecplot.plot.FieldmapScatter"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[shade]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.shade "Link to this definition"){.headerlink}

:   Style control for surface shading.

    Type[:]{.colon}

    :   [[`FieldmapShade`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapShade "tecplot.plot.FieldmapShade"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.show "Link to this definition"){.headerlink}

:   Display this fieldmap on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).show = True
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
    .internal} or [[`Cartesian3DFieldmapCollection`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
    .internal}

    For optimized style control of several fieldmaps, it is recommended
    to use [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
    .internal} or [[`Cartesian3DFieldmapCollection`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
    .internal} objects.
    :::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[surfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.surfaces "Link to this definition"){.headerlink}

:   Control which surfaces to draw.

    Type[:]{.colon}

    :   [[`FieldmapSurfaces`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces "tecplot.plot.FieldmapSurfaces"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.vector "Link to this definition"){.headerlink}

:   Style for vector field plots using arrows.

    Type[:]{.colon}

    :   [[`FieldmapVector`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapVector "tecplot.plot.FieldmapVector"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmap.]{.pre}]{.sig-prename .descclassname}[[zones]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmap.zones "Link to this definition"){.headerlink}

:   List of [[zones]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} used
    by this fieldmap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for zone in fieldmap.zones:
        ...     print(zone.name)
        Zone 1
        Zone 2
    :::
    ::::
:::

::: {#cartesian2dfieldmapcollection .section}
### [Cartesian2DFieldmapCollection](#id48){.toc-backref role="doc-backlink"}[¶](#cartesian2dfieldmapcollection "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian2DFieldmapCollection]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#Cartesian2DFieldmapCollection){.reference .internal}[¶](#tecplot.plot.Cartesian2DFieldmapCollection "Link to this definition"){.headerlink}

:   Style control for one or more 2D fieldmaps.

    This class behaves like [[`Cartesian2DFieldmap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap "tecplot.plot.Cartesian2DFieldmap"){.reference
    .internal} except that setting any underlying style will do so for
    all of the represented fieldmaps. The style properties are then
    always returned as a [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external} of properties, one for each fieldmap, ordered by index
    number. This means there is an asymmetry between setting and getting
    any property under this object, illustrated by the following
    example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmaps = plot.fieldmaps(0, 1, 2)
        >>> fmaps.show = True
        >>> print(fmaps.show)
        (True, True, True)
    :::
    ::::

    This is the preferred way to control the style of many fieldmaps as
    it is much faster to execute. All examples that set style on a
    single fieldmap like the following:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).contour.show = True
    :::
    ::::

    may be converted to setting the same style on all fieldmaps like so:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps().contour.show = True
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Cartesian2DFieldmap`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmap "tecplot.plot.Cartesian2DFieldmap"){.reference
    .internal}
    :::

    ::: versionadded
    [New in version 1.1: ]{.versionmodified .added}Fieldmap collection
    objects.
    :::

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.contour "tecplot.plot.Cartesian2DFieldmapCollection.contour"){.reference .internal}                              Style including flooding, lines and line coloring.
      [[`edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.edge "tecplot.plot.Cartesian2DFieldmapCollection.edge"){.reference .internal}                                       Style control for boundary lines.
      [[`effects`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.effects "tecplot.plot.Cartesian2DFieldmapCollection.effects"){.reference .internal}                              Style control for clipping and blanking effects.
      [[`fieldmap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.fieldmap_indices "tecplot.plot.Cartesian2DFieldmapCollection.fieldmap_indices"){.reference .internal}   Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.group "tecplot.plot.Cartesian2DFieldmapCollection.group"){.reference .internal}                                    Zero-based group number for this [[Fieldmaps]{.std .std-ref}](#fieldmap){.reference .internal}.
      [[`mesh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.mesh "tecplot.plot.Cartesian2DFieldmapCollection.mesh"){.reference .internal}                                       Style lines connecting neighboring data points.
      [[`points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.points "tecplot.plot.Cartesian2DFieldmapCollection.points"){.reference .internal}                                 Control which points to draw.
      [[`scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.scatter "tecplot.plot.Cartesian2DFieldmapCollection.scatter"){.reference .internal}                              Style for scatter plots.
      [[`shade`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.shade "tecplot.plot.Cartesian2DFieldmapCollection.shade"){.reference .internal}                                    Style control for surface shading.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.show "tecplot.plot.Cartesian2DFieldmapCollection.show"){.reference .internal}                                       Display the fielmaps in this collection on the plot.
      [[`surfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.surfaces "tecplot.plot.Cartesian2DFieldmapCollection.surfaces"){.reference .internal}                           Control which surfaces to draw.
      [[`vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection.vector "tecplot.plot.Cartesian2DFieldmapCollection.vector"){.reference .internal}                                 Style for vector field plots using arrows.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[contour]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.contour "Link to this definition"){.headerlink}

:   Style including flooding, lines and line coloring.

    Type[:]{.colon}

    :   [[`FieldmapContour`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapContour "tecplot.plot.FieldmapContour"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.edge "Link to this definition"){.headerlink}

:   Style control for boundary lines.

    Type[:]{.colon}

    :   [[`FieldmapEdge`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge "tecplot.plot.FieldmapEdge"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[effects]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.effects "Link to this definition"){.headerlink}

:   Style control for clipping and blanking effects.

    Type[:]{.colon}

    :   [[`FieldmapEffects`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects "tecplot.plot.FieldmapEffects"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[fieldmap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.fieldmap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[group]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.group "Link to this definition"){.headerlink}

:   Zero-based group number for this [[Fieldmaps]{.std
    .std-ref}](#fieldmap){.reference .internal}.

    This is a piece of auxiliary data and can be useful for identifying
    a subset of fieldmaps. For example, to loop over all fieldmaps that
    have group set to 4:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps(0, 3).group = 4
        >>> for fmap in filter(lambda f: f.group == 4, plot.fieldmaps()):
        ...     print(fmap.index)
        0
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[mesh]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.mesh "Link to this definition"){.headerlink}

:   Style lines connecting neighboring data points.

    Type[:]{.colon}

    :   [[`FieldmapMesh`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh "tecplot.plot.FieldmapMesh"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[points]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.points "Link to this definition"){.headerlink}

:   Control which points to draw.

    Type[:]{.colon}

    :   [[`FieldmapPoints`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapPoints "tecplot.plot.FieldmapPoints"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.scatter "Link to this definition"){.headerlink}

:   Style for scatter plots.

    Type[:]{.colon}

    :   [[`FieldmapScatter`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter "tecplot.plot.FieldmapScatter"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[shade]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.shade "Link to this definition"){.headerlink}

:   Style control for surface shading.

    Type[:]{.colon}

    :   [[`FieldmapShade`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapShade "tecplot.plot.FieldmapShade"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.show "Link to this definition"){.headerlink}

:   Display the fielmaps in this collection on the plot.

    Example turning on all fieldmaps on the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps().show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[surfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.surfaces "Link to this definition"){.headerlink}

:   Control which surfaces to draw.

    Type[:]{.colon}

    :   [[`FieldmapSurfaces`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces "tecplot.plot.FieldmapSurfaces"){.reference
        .internal}

<!-- -->

[[Cartesian2DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian2DFieldmapCollection.vector "Link to this definition"){.headerlink}

:   Style for vector field plots using arrows.

    Type[:]{.colon}

    :   [[`FieldmapVector`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapVector "tecplot.plot.FieldmapVector"){.reference
        .internal}
:::

::: {#cartesian3dfieldmap .section}
### [Cartesian3DFieldmap](#id49){.toc-backref role="doc-backlink"}[¶](#cartesian3dfieldmap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian3DFieldmap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#Cartesian3DFieldmap){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldmap "Link to this definition"){.headerlink}

:   Style control for a single 3D fieldmap.

    ::: {.admonition .seealso}
    See also

    [[`Cartesian3DFieldmapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
    .internal}
    :::

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.contour "tecplot.plot.Cartesian3DFieldmap.contour"){.reference .internal}                                 Style including flooding, lines and line coloring.
      [[`edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.edge "tecplot.plot.Cartesian3DFieldmap.edge"){.reference .internal}                                          Style control for boundary lines.
      [[`effects`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.effects "tecplot.plot.Cartesian3DFieldmap.effects"){.reference .internal}                                 Style control for blanking and lighting effects.
      [[`fieldmap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.fieldmap_indices "tecplot.plot.Cartesian3DFieldmap.fieldmap_indices"){.reference .internal}      Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.group "tecplot.plot.Cartesian3DFieldmap.group"){.reference .internal}                                       Zero-based group number for this [[Fieldmaps]{.std .std-ref}](#fieldmap){.reference .internal}.
      [[`mesh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.mesh "tecplot.plot.Cartesian3DFieldmap.mesh"){.reference .internal}                                          Style lines connecting neighboring data points.
      [[`points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.points "tecplot.plot.Cartesian3DFieldmap.points"){.reference .internal}                                    Control which points to draw.
      [[`scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.scatter "tecplot.plot.Cartesian3DFieldmap.scatter"){.reference .internal}                                 Style for scatter plots.
      [[`shade`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.shade "tecplot.plot.Cartesian3DFieldmap.shade"){.reference .internal}                                       Style control for surface shading.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.show "tecplot.plot.Cartesian3DFieldmap.show"){.reference .internal}                                          Display this fieldmap on the plot.
      [[`show_isosurfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.show_isosurfaces "tecplot.plot.Cartesian3DFieldmap.show_isosurfaces"){.reference .internal}      Enable drawing of Iso-surfaces.
      [[`show_slices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.show_slices "tecplot.plot.Cartesian3DFieldmap.show_slices"){.reference .internal}                     Enable drawing of slice surfaces.
      [[`show_streamtraces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.show_streamtraces "tecplot.plot.Cartesian3DFieldmap.show_streamtraces"){.reference .internal}   Enable drawing of streamtraces.
      [[`surfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.surfaces "tecplot.plot.Cartesian3DFieldmap.surfaces"){.reference .internal}                              Control which surfaces to draw.
      [[`vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.vector "tecplot.plot.Cartesian3DFieldmap.vector"){.reference .internal}                                    Style for vector field plots using arrows.
      [[`zones`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap.zones "tecplot.plot.Cartesian3DFieldmap.zones"){.reference .internal}                                       List of [[zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} used by this fieldmap.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[contour]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.contour "Link to this definition"){.headerlink}

:   Style including flooding, lines and line coloring.

    Type[:]{.colon}

    :   [[`FieldmapContour`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapContour "tecplot.plot.FieldmapContour"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.edge "Link to this definition"){.headerlink}

:   Style control for boundary lines.

    Type[:]{.colon}

    :   [[`FieldmapEdge`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge "tecplot.plot.FieldmapEdge"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[effects]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.effects "Link to this definition"){.headerlink}

:   Style control for blanking and lighting effects.

    Type[:]{.colon}

    :   [[`FieldmapEffects3D`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D "tecplot.plot.FieldmapEffects3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[fieldmap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.fieldmap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[group]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.group "Link to this definition"){.headerlink}

:   Zero-based group number for this [[Fieldmaps]{.std
    .std-ref}](#fieldmap){.reference .internal}.

    This is a piece of auxiliary data and can be useful for identifying
    a subset of fieldmaps. For example, to loop over all fieldmaps that
    have group set to 4:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps(0, 3).group = 4
        >>> for fmap in filter(lambda f: f.group == 4, plot.fieldmaps()):
        ...     print(fmap.index)
        0
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[mesh]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.mesh "Link to this definition"){.headerlink}

:   Style lines connecting neighboring data points.

    Type[:]{.colon}

    :   [[`FieldmapMesh`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh "tecplot.plot.FieldmapMesh"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[points]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.points "Link to this definition"){.headerlink}

:   Control which points to draw.

    Type[:]{.colon}

    :   [[`FieldmapPoints`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapPoints "tecplot.plot.FieldmapPoints"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.scatter "Link to this definition"){.headerlink}

:   Style for scatter plots.

    Type[:]{.colon}

    :   [[`FieldmapScatter`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter "tecplot.plot.FieldmapScatter"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[shade]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.shade "Link to this definition"){.headerlink}

:   Style control for surface shading.

    Type[:]{.colon}

    :   [[`FieldmapShade3D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapShade3D "tecplot.plot.FieldmapShade3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.show "Link to this definition"){.headerlink}

:   Display this fieldmap on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).show = True
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
    .internal} or [[`Cartesian3DFieldmapCollection`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
    .internal}

    For optimized style control of several fieldmaps, it is recommended
    to use [[`Cartesian2DFieldmapCollection`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian2DFieldmapCollection "tecplot.plot.Cartesian2DFieldmapCollection"){.reference
    .internal} or [[`Cartesian3DFieldmapCollection`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection "tecplot.plot.Cartesian3DFieldmapCollection"){.reference
    .internal} objects.
    :::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[show_isosurfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.show_isosurfaces "Link to this definition"){.headerlink}

:   Enable drawing of Iso-surfaces.

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[show_slices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.show_slices "Link to this definition"){.headerlink}

:   Enable drawing of slice surfaces.

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[show_streamtraces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.show_streamtraces "Link to this definition"){.headerlink}

:   Enable drawing of streamtraces.

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[surfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.surfaces "Link to this definition"){.headerlink}

:   Control which surfaces to draw.

    Type[:]{.colon}

    :   [[`FieldmapSurfaces`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces "tecplot.plot.FieldmapSurfaces"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.vector "Link to this definition"){.headerlink}

:   Style for vector field plots using arrows.

    Type[:]{.colon}

    :   [[`FieldmapVector`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapVector "tecplot.plot.FieldmapVector"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmap.]{.pre}]{.sig-prename .descclassname}[[zones]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmap.zones "Link to this definition"){.headerlink}

:   List of [[zones]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} used
    by this fieldmap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for zone in fieldmap.zones:
        ...     print(zone.name)
        Zone 1
        Zone 2
    :::
    ::::
:::

::: {#cartesian3dfieldmapcollection .section}
### [Cartesian3DFieldmapCollection](#id50){.toc-backref role="doc-backlink"}[¶](#cartesian3dfieldmapcollection "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[Cartesian3DFieldmapCollection]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#Cartesian3DFieldmapCollection){.reference .internal}[¶](#tecplot.plot.Cartesian3DFieldmapCollection "Link to this definition"){.headerlink}

:   Style control for one or more 3D fieldmaps.

    This class behaves like [[`Cartesian3DFieldmap`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap "tecplot.plot.Cartesian3DFieldmap"){.reference
    .internal} except that setting any underlying style will do so for
    all of the represented fieldmaps. The style properties are then
    always returned as a [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external} of properties, one for each fieldmap, ordered by index
    number. This means there is an asymmetry between setting and getting
    any property under this object, illustrated by the following
    example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> fmaps = plot.fieldmaps(0, 1, 2)
        >>> fmaps.show = True
        >>> print(fmaps.show)
        (True, True, True)
    :::
    ::::

    This is the preferred way to control the style of many fieldmaps as
    it is much faster to execute. All examples that set style on a
    single fieldmap like the following:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).contour.show = True
    :::
    ::::

    may be converted to setting the same style on all fieldmaps like so:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps().contour.show = True
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Cartesian3DFieldmap`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmap "tecplot.plot.Cartesian3DFieldmap"){.reference
    .internal}
    :::

    ::: versionadded
    [New in version 1.1: ]{.versionmodified .added}Fieldmap collection
    objects.
    :::

    The following example illustrates manipulating the style for a
    selection of fieldmaps associated with specific zones:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import numpy
        import tecplot

        examples_dir = tecplot.session.tecplot_examples_directory()
        infile = os.path.join(examples_dir, 'SimpleData', 'F18.lay')
        tecplot.load_layout(infile)
        frame = tecplot.active_frame()
        plot = frame.plot()
        dataset = frame.dataset

        plot.contour(0).colormap_name = 'GrayScale'
        plot.contour(0).legend.show = False

        wings = [dataset.zone(name) for name in ['left wing', 'right wing']]
        fmaps = frame.plot().fieldmaps(wings)
        fmaps.contour.flood_contour_group = plot.contour(1)

        plot.contour(1).colormap_name = 'Sequential - Yellow/Green/Blue'
        plot.contour(1).levels.reset_levels(numpy.linspace(-0.07, 0.07, 50))

        tecplot.export.save_png('F18_wings.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/F18_wings.png"
    class="reference internal image-reference"><img
    src="../_images/F18_wings.png" style="width: 300px;"
    alt="../_images/F18_wings.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`contour`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.contour "tecplot.plot.Cartesian3DFieldmapCollection.contour"){.reference .internal}                                 Style including flooding, lines and line coloring.
      [[`edge`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.edge "tecplot.plot.Cartesian3DFieldmapCollection.edge"){.reference .internal}                                          Style control for boundary lines.
      [[`effects`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.effects "tecplot.plot.Cartesian3DFieldmapCollection.effects"){.reference .internal}                                 Style control for blanking and lighting effects.
      [[`fieldmap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.fieldmap_indices "tecplot.plot.Cartesian3DFieldmapCollection.fieldmap_indices"){.reference .internal}      Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.group "tecplot.plot.Cartesian3DFieldmapCollection.group"){.reference .internal}                                       Zero-based group number for this [[Fieldmaps]{.std .std-ref}](#fieldmap){.reference .internal}.
      [[`mesh`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.mesh "tecplot.plot.Cartesian3DFieldmapCollection.mesh"){.reference .internal}                                          Style lines connecting neighboring data points.
      [[`points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.points "tecplot.plot.Cartesian3DFieldmapCollection.points"){.reference .internal}                                    Control which points to draw.
      [[`scatter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.scatter "tecplot.plot.Cartesian3DFieldmapCollection.scatter"){.reference .internal}                                 Style for scatter plots.
      [[`shade`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.shade "tecplot.plot.Cartesian3DFieldmapCollection.shade"){.reference .internal}                                       Style control for surface shading.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.show "tecplot.plot.Cartesian3DFieldmapCollection.show"){.reference .internal}                                          Display the fielmaps in this collection on the plot.
      [[`show_isosurfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.show_isosurfaces "tecplot.plot.Cartesian3DFieldmapCollection.show_isosurfaces"){.reference .internal}      Enable drawing of Iso-surfaces.
      [[`show_slices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.show_slices "tecplot.plot.Cartesian3DFieldmapCollection.show_slices"){.reference .internal}                     Enable drawing of slice surfaces.
      [[`show_streamtraces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.show_streamtraces "tecplot.plot.Cartesian3DFieldmapCollection.show_streamtraces"){.reference .internal}   Enable drawing of streamtraces.
      [[`surfaces`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.surfaces "tecplot.plot.Cartesian3DFieldmapCollection.surfaces"){.reference .internal}                              Control which surfaces to draw.
      [[`vector`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.Cartesian3DFieldmapCollection.vector "tecplot.plot.Cartesian3DFieldmapCollection.vector"){.reference .internal}                                    Style for vector field plots using arrows.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[contour]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.contour "Link to this definition"){.headerlink}

:   Style including flooding, lines and line coloring.

    Type[:]{.colon}

    :   [[`FieldmapContour`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapContour "tecplot.plot.FieldmapContour"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[edge]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.edge "Link to this definition"){.headerlink}

:   Style control for boundary lines.

    Type[:]{.colon}

    :   [[`FieldmapEdge`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge "tecplot.plot.FieldmapEdge"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[effects]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.effects "Link to this definition"){.headerlink}

:   Style control for blanking and lighting effects.

    Type[:]{.colon}

    :   [[`FieldmapEffects3D`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D "tecplot.plot.FieldmapEffects3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[fieldmap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.fieldmap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[group]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.group "Link to this definition"){.headerlink}

:   Zero-based group number for this [[Fieldmaps]{.std
    .std-ref}](#fieldmap){.reference .internal}.

    This is a piece of auxiliary data and can be useful for identifying
    a subset of fieldmaps. For example, to loop over all fieldmaps that
    have group set to 4:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps(0, 3).group = 4
        >>> for fmap in filter(lambda f: f.group == 4, plot.fieldmaps()):
        ...     print(fmap.index)
        0
        3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[mesh]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.mesh "Link to this definition"){.headerlink}

:   Style lines connecting neighboring data points.

    Type[:]{.colon}

    :   [[`FieldmapMesh`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh "tecplot.plot.FieldmapMesh"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[points]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.points "Link to this definition"){.headerlink}

:   Control which points to draw.

    Type[:]{.colon}

    :   [[`FieldmapPoints`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapPoints "tecplot.plot.FieldmapPoints"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[scatter]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.scatter "Link to this definition"){.headerlink}

:   Style for scatter plots.

    Type[:]{.colon}

    :   [[`FieldmapScatter`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter "tecplot.plot.FieldmapScatter"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[shade]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.shade "Link to this definition"){.headerlink}

:   Style control for surface shading.

    Type[:]{.colon}

    :   [[`FieldmapShade3D`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapShade3D "tecplot.plot.FieldmapShade3D"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.show "Link to this definition"){.headerlink}

:   Display the fielmaps in this collection on the plot.

    Example turning on all fieldmaps on the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmaps().show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[show_isosurfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.show_isosurfaces "Link to this definition"){.headerlink}

:   Enable drawing of Iso-surfaces.

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[show_slices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.show_slices "Link to this definition"){.headerlink}

:   Enable drawing of slice surfaces.

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[show_streamtraces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.show_streamtraces "Link to this definition"){.headerlink}

:   Enable drawing of streamtraces.

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[surfaces]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.surfaces "Link to this definition"){.headerlink}

:   Control which surfaces to draw.

    Type[:]{.colon}

    :   [[`FieldmapSurfaces`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces "tecplot.plot.FieldmapSurfaces"){.reference
        .internal}

<!-- -->

[[Cartesian3DFieldmapCollection.]{.pre}]{.sig-prename .descclassname}[[vector]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.Cartesian3DFieldmapCollection.vector "Link to this definition"){.headerlink}

:   Style for vector field plots using arrows.

    Type[:]{.colon}

    :   [[`FieldmapVector`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapVector "tecplot.plot.FieldmapVector"){.reference
        .internal}
:::

::: {#fieldmapcontour .section}
### [FieldmapContour](#id51){.toc-backref role="doc-backlink"}[¶](#fieldmapcontour "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapContour]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapContour){.reference .internal}[¶](#tecplot.plot.FieldmapContour "Link to this definition"){.headerlink}

:   Style control for flooding and contour lines.

    This object controls which contour groups are associated with
    flooding, line placement and line coloring. Three different contour
    groups may be used though there are eight total groups that can be
    configured in a single plot. In this example, we flood by the first
    contour group (index: 0):

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np

        import tecplot as tp
        from tecplot.constant import *
        from tecplot.data.operate import execute_equation

        # Get the active frame, setup a grid (30x30x30)
        # where each dimension ranges from 0 to 30.
        # Add variables P,Q,R to the dataset and give
        # values to the data.
        frame = tp.active_frame()
        dataset = frame.dataset
        for v in ['X','Y','Z','P','Q','R']:
            dataset.add_variable(v)
        zone = dataset.add_ordered_zone('Zone', (30,30,30))
        xx = np.linspace(0,30,30)
        for v,arr in zip(['X','Y','Z'],np.meshgrid(xx,xx,xx)):
            zone.values(v)[:] = arr.ravel()
        execute_equation('{P} = -10 * {X}    +      {Y}**2 + {Z}**2')
        execute_equation('{Q} =       {X}    - 10 * {Y}    - {Z}**2')
        execute_equation('{R} =       {X}**2 +      {Y}**2 - {Z}   ')

        # Enable 3D field plot and turn on contouring
        # with boundary faces
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()
        srf = plot.fieldmap(0).surfaces
        srf.surfaces_to_plot = SurfacesToPlot.BoundaryFaces
        plot.show_contour = True

        # get the contour group associated with the
        # newly created zone
        contour = plot.fieldmap(dataset.zone('Zone')).contour

        # assign flooding to the first contour group
        contour.flood_contour_group = plot.contour(0)
        contour.flood_contour_group.variable = dataset.variable('P')
        contour.flood_contour_group.colormap_name = 'Sequential - Yellow/Green/Blue'
        contour.flood_contour_group.legend.show = False

        # save image to PNG file
        tp.export.save_png('fieldmap_contour.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_contour.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_contour.png" style="width: 300px;"
    alt="../_images/fieldmap_contour.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`contour_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.contour_type "tecplot.plot.FieldmapContour.contour_type"){.reference .internal}                                          [[`ContourType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType "tecplot.constant.ContourType"){.reference .internal} to plot.
      [[`flood_contour_group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.flood_contour_group "tecplot.plot.FieldmapContour.flood_contour_group"){.reference .internal}                     The [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} to use for flooding.
      [[`flood_contour_group_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.flood_contour_group_index "tecplot.plot.FieldmapContour.flood_contour_group_index"){.reference .internal}   Zero-based [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal} of the [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} to use for flooding.
      [[`line_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_color "tecplot.plot.FieldmapContour.line_color"){.reference .internal}                                                The [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} for lines.
      [[`line_group`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_group "tecplot.plot.FieldmapContour.line_group"){.reference .internal}                                                [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} to use for line placement and style.
      [[`line_group_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_group_index "tecplot.plot.FieldmapContour.line_group_index"){.reference .internal}                              Zero-based [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal} of the [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} for contour lines.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_pattern "tecplot.plot.FieldmapContour.line_pattern"){.reference .internal}                                          [[`LinePattern`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference .internal} type to use for contour lines.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_thickness "tecplot.plot.FieldmapContour.line_thickness"){.reference .internal}                                    Thickness ([[`float`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference .external}) of the drawn lines.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.pattern_length "tecplot.plot.FieldmapContour.pattern_length"){.reference .internal}                                    Length ([[`float`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference .external}) of the pattern segment for non-solid lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.show "tecplot.plot.FieldmapContour.show"){.reference .internal}                                                                  Enable drawing the contours.
      [[`use_lighting_effect`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.use_lighting_effect "tecplot.plot.FieldmapContour.use_lighting_effect"){.reference .internal}                     Enable lighting effect on this contour.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[contour_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.contour_type "Link to this definition"){.headerlink}

:   [[`ContourType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType "tecplot.constant.ContourType"){.reference
    .internal} to plot.

    Possible values are:

    > <div>
    >
    > [[`ContourType.Flood`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType.Flood "tecplot.constant.ContourType.Flood"){.reference .internal} (default)
    >
    > :   Filled color between the contour levels.
    >
    > [[`ContourType.Lines`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType.Lines "tecplot.constant.ContourType.Lines"){.reference .internal}
    >
    > :   Lines only.
    >
    > [[`ContourType.Overlay`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType.Overlay "tecplot.constant.ContourType.Overlay"){.reference .internal}
    >
    > :   Lines overlayed on flood.
    >
    > [[`ContourType.AverageCell`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType.AverageCell "tecplot.constant.ContourType.AverageCell"){.reference .internal}
    >
    > :   Filled color by the average value within cells.
    >
    > [[`ContourType.PrimaryValue`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType.PrimaryValue "tecplot.constant.ContourType.PrimaryValue"){.reference .internal}
    >
    > :   Filled color by the value at the primary corner of the cells.
    >
    > </div>

    In this example, we enable both flooding and contour lines:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ContourType
        >>> contour = plot.fieldmap(0).contour
        >>> contour.contour_type = ContourType.Overlay
    :::
    ::::

    Type[:]{.colon}

    :   [[`ContourType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ContourType "tecplot.constant.ContourType"){.reference
        .internal}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[flood_contour_group]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.flood_contour_group "Link to this definition"){.headerlink}

:   The [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} to use for flooding.

    This property sets and gets the [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} used for flooding. Changing style on this
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> cmap_name = 'Sequential - Yellow/Green/Blue'
        >>> contour = plot.fieldmap(0).contour
        >>> contour.flood_contour_group = plot.contour(1)
        >>> contour.flood_contour_group.variable = dataset.variable('P')
        >>> contour.flood_contour_group.colormap_name = cmap_name
    :::
    ::::

    Setting this to the [[`RGBColoring`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
    .internal} instance floods this fieldmap contour by the plot's RGB
    coloring settings. This requires that variables are assigned to the
    red, green and blue color channels:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.rgb_coloring.red_variable = dataset.variable('x')
        >>> plot.rgb_coloring.green_variable = dataset.variable('y')
        >>> plot.rgb_coloring.blue_variable = dataset.variable('z')
        >>> contour = plot.fieldmap(0).contour
        >>> contour.flood_contour_group = plot.rgb_coloring
    :::
    ::::

    See [[`RGBColoring`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
    .internal} for more details.

    Type[:]{.colon}

    :   [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal} or [[`RGBColoring`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
        .internal}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[flood_contour_group_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.flood_contour_group_index "Link to this definition"){.headerlink}

:   Zero-based [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal} of the [[`ContourGroup`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} to use for flooding.

    This property sets and gets, by [[`Index`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}, the [[`ContourGroup`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} used for flooding. Changing style on this
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.flood_contour_group_index = 1
        >>> contour.flood_contour_group.variable = dataset.variable('P')
    :::
    ::::

    ::: {.admonition .note}
    Note

    To set the flood contour to RGB (multivariate) coloring, you must
    set the [[`FieldmapContour.flood_contour_group`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.flood_contour_group "tecplot.plot.FieldmapContour.flood_contour_group"){.reference
    .internal} property to [`plot.rgb_coloring`{.docutils .literal
    .notranslate}]{.pre}. See
    [[`FieldmapContour.flood_contour_group`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.flood_contour_group "tecplot.plot.FieldmapContour.flood_contour_group"){.reference
    .internal} for more details.
    :::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[line_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.line_color "Link to this definition"){.headerlink}

:   The [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} for lines.

    FieldmapContour lines can be a solid color or be colored by a
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} as obtained through the [`plot.contour`{.docutils
    .literal .notranslate}]{.pre} property. Note that changing style on
    this [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> contour = plot.fieldmap(1).contour
        >>> contour.line_color = Color.Blue
    :::
    ::::

    Example of setting the color from a [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.line_color = plot.contour(1)
        >>> contour.line_color.variable = dataset.variable('P')
    :::
    ::::

    Setting this to the [[`RGBColoring`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
    .internal} instance colors the lines by the plot's multivariate
    contour settings. This requires that variables are assigned to the
    red, green and blue color channels:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.rgb_coloring.red_variable = dataset.variable('x')
        >>> plot.rgb_coloring.green_variable = dataset.variable('y')
        >>> plot.rgb_coloring.blue_variable = dataset.variable('z')
        >>> plot.fieldmap(0).contour.line_color = plot.rgb_coloring
    :::
    ::::

    See [[`RGBColoring`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.RGBColoring "tecplot.plot.RGBColoring"){.reference
    .internal} for more details.

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal} or [[`ContourGroup`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[line_group]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.line_group "Link to this definition"){.headerlink}

:   [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} to use for line placement and style.

    This property sets and gets the [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} used for line placement and though all properties of the
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} can be manipulated through this object, many of them such
    as color will not effect the lines unless the
    [[`FieldmapContour.line_color`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_color "tecplot.plot.FieldmapContour.line_color"){.reference
    .internal} is set to the same [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}. Note that changing style on this [[`ContourGroup`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.line_group = plot.contour(2)
        >>> contour.line_group.variable = dataset.variable('Z')
    :::
    ::::

    Type[:]{.colon}

    :   [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[line_group_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.line_group_index "Link to this definition"){.headerlink}

:   Zero-based [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal} of the [[`ContourGroup`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} for contour lines.

    This property sets and gets, by [[`Index`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal}, the [[`ContourGroup`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} used for line placement and though all properties of the
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} can be manipulated through this object, many of them such
    as color will not affect the lines unless the
    [[`FieldmapContour.line_color`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapContour.line_color "tecplot.plot.FieldmapContour.line_color"){.reference
    .internal} is set to the same [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}. Note that changing style on this [[`ContourGroup`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.line_group_index = 2
        >>> contour.line_group.variable = dataset.variable('Z')
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.line_pattern "Link to this definition"){.headerlink}

:   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
    .internal} type to use for contour lines.

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
        >>> contour = plot.fieldmap(0).contour
        >>> contour.line_pattern = LinePattern.DashDotDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.line_thickness "Link to this definition"){.headerlink}

:   Thickness ([[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external}) of the drawn lines.

    This is the line thickness in percentage of the [[`Frame`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}'s height. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.line_thickness = 0.7
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.pattern_length "Link to this definition"){.headerlink}

:   Length ([[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external}) of the pattern segment for non-solid lines.

    This is the pattern length in percentage of the [[`Frame`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}'s height. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.show "Link to this definition"){.headerlink}

:   Enable drawing the contours.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapContour.]{.pre}]{.sig-prename .descclassname}[[use_lighting_effect]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapContour.use_lighting_effect "Link to this definition"){.headerlink}

:   Enable lighting effect on this contour.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> contour = plot.fieldmap(0).contour
        >>> contour.use_lighting_effect = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapedge .section}
### [FieldmapEdge](#id52){.toc-backref role="doc-backlink"}[¶](#fieldmapedge "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapEdge]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapEdge){.reference .internal}[¶](#tecplot.plot.FieldmapEdge "Link to this definition"){.headerlink}

:   Volume boundary lines.

    An edge plot layer displays the connections of the outer lines
    ([`IJ`{.docutils .literal .notranslate}]{.pre}-ordered zones),
    finite element surface zones, or planes ([`IJK`{.docutils .literal
    .notranslate}]{.pre}-ordered zones). The FieldmapEdge layer allows
    you to display the edges (creases and borders) of your data. Zone
    edges exist only for ordered zones or 2D finite element zones.
    Three-dimensional finite element zones do not have boundaries:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os

        import tecplot as tp
        from tecplot.constant import Color, EdgeType, PlotType, SurfacesToPlot

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(datafile)
        frame = dataset.frame

        # Enable 3D field plot, turn on contouring and translucency
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()
        plot.show_contour = True
        plot.show_edge = True

        contour = plot.contour(0)
        contour.colormap_name = 'Sequential - Blue'
        contour.variable = dataset.variable('S')

        # adjust effects for every fieldmap in this dataset
        fmaps = plot.fieldmaps()
        fmaps.contour.flood_contour_group = contour
        fmaps.surfaces.surfaces_to_plot = SurfacesToPlot.BoundaryFaces

        edge = fmaps.edge
        edge.edge_type = EdgeType.Creases
        edge.color = Color.RedOrange
        edge.line_thickness = 0.7

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        # save image to file
        tp.export.save_png('fieldmap_edge.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_edge.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_edge.png" style="width: 300px;"
    alt="../_images/fieldmap_edge.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.color "tecplot.plot.FieldmapEdge.color"){.reference .internal}                              Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`edge_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.edge_type "tecplot.plot.FieldmapEdge.edge_type"){.reference .internal}                  Where to draw edge lines.
      [[`i_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.i_border "tecplot.plot.FieldmapEdge.i_border"){.reference .internal}                     Which border lines to draw in the [`I`{.docutils .literal .notranslate}]{.pre}-dimension.
      [[`j_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.j_border "tecplot.plot.FieldmapEdge.j_border"){.reference .internal}                     Which border lines to draw in the [`J`{.docutils .literal .notranslate}]{.pre}-dimension.
      [[`k_border`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.k_border "tecplot.plot.FieldmapEdge.k_border"){.reference .internal}                     Which border lines to draw in the [`K`{.docutils .literal .notranslate}]{.pre}-dimension.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.line_thickness "tecplot.plot.FieldmapEdge.line_thickness"){.reference .internal}   Thickness of the edge lines drawn.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEdge.show "tecplot.plot.FieldmapEdge.show"){.reference .internal}                                 Draw the mesh for this fieldmap.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[edge_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.edge_type "Link to this definition"){.headerlink}

:   Where to draw edge lines.

    Possible values: [[`Borders`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EdgeType.Borders "tecplot.constant.EdgeType.Borders"){.reference
    .internal}, [[`Creases`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EdgeType.Creases "tecplot.constant.EdgeType.Creases"){.reference
    .internal}, [[`BordersAndCreases`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EdgeType.BordersAndCreases "tecplot.constant.EdgeType.BordersAndCreases"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import EdgeType
        >>> plot.show_edge = True
        >>> plot.fieldmap(0).edge.edge_type = EdgeType.Creases
    :::
    ::::

    Type[:]{.colon}

    :   [[`EdgeType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.EdgeType "tecplot.constant.EdgeType"){.reference
        .internal}

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[i_border]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.i_border "Link to this definition"){.headerlink}

:   Which border lines to draw in the [`I`{.docutils .literal
    .notranslate}]{.pre}-dimension.

    Possible values: [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}, [[`Min`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Min "tecplot.constant.BorderLocation.Min"){.reference
    .internal}, [[`Max`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Max "tecplot.constant.BorderLocation.Max"){.reference
    .internal}, [[`Both`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Both "tecplot.constant.BorderLocation.Both"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import BorderLocation
        >>> plot.show_edge = True
        >>> plot.fieldmap(0).edge.i_border = BorderLocation.Min
    :::
    ::::

    Type[:]{.colon}

    :   [[`BorderLocation`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation "tecplot.constant.BorderLocation"){.reference
        .internal}

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[j_border]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.j_border "Link to this definition"){.headerlink}

:   Which border lines to draw in the [`J`{.docutils .literal
    .notranslate}]{.pre}-dimension.

    Possible values: [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}, [[`Min`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Min "tecplot.constant.BorderLocation.Min"){.reference
    .internal}, [[`Max`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Max "tecplot.constant.BorderLocation.Max"){.reference
    .internal}, [[`Both`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Both "tecplot.constant.BorderLocation.Both"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import BorderLocation
        >>> plot.show_edge = True
        >>> plot.fieldmap(0).edge.j_border = BorderLocation.Both
    :::
    ::::

    Type[:]{.colon}

    :   [[`BorderLocation`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation "tecplot.constant.BorderLocation"){.reference
        .internal}

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[k_border]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.k_border "Link to this definition"){.headerlink}

:   Which border lines to draw in the [`K`{.docutils .literal
    .notranslate}]{.pre}-dimension.

    Possible values: [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}, [[`Min`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Min "tecplot.constant.BorderLocation.Min"){.reference
    .internal}, [[`Max`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Max "tecplot.constant.BorderLocation.Max"){.reference
    .internal}, [[`Both`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation.Both "tecplot.constant.BorderLocation.Both"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import BorderLocation
        >>> plot.show_edge = True
        >>> plot.fieldmap(0).edge.k_border = None
    :::
    ::::

    Type[:]{.colon}

    :   [[`BorderLocation`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.BorderLocation "tecplot.constant.BorderLocation"){.reference
        .internal}

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.line_thickness "Link to this definition"){.headerlink}

:   Thickness of the edge lines drawn.

    This is the line thickness in percentage of [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} height. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).edge.line_thickness = 0.4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapEdge.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEdge.show "Link to this definition"){.headerlink}

:   Draw the mesh for this fieldmap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_edge = True
        >>> plot.fieldmap(0).edge.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapeffects .section}
### [FieldmapEffects](#id53){.toc-backref role="doc-backlink"}[¶](#fieldmapeffects "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapEffects]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapEffects){.reference .internal}[¶](#tecplot.plot.FieldmapEffects "Link to this definition"){.headerlink}

:   Clipping and blanking style control.

    This object controls value blanking and clipping from plane slices
    for this fieldmap.

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------
      [[`clip_planes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects.clip_planes "tecplot.plot.FieldmapEffects.clip_planes"){.reference .internal}            
      [[`value_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects.value_blanking "tecplot.plot.FieldmapEffects.value_blanking"){.reference .internal}   Enable value blanking effect for this fieldmap.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------

<!-- -->

[[FieldmapEffects.]{.pre}]{.sig-prename .descclassname}[[clip_planes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects.clip_planes "Link to this definition"){.headerlink}

:   

<!-- -->

[[FieldmapEffects.]{.pre}]{.sig-prename .descclassname}[[value_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects.value_blanking "Link to this definition"){.headerlink}

:   Enable value blanking effect for this fieldmap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).effects.value_blanking = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapeffects3d .section}
### [FieldmapEffects3D](#id54){.toc-backref role="doc-backlink"}[¶](#fieldmapeffects3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapEffects3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapEffects3D){.reference .internal}[¶](#tecplot.plot.FieldmapEffects3D "Link to this definition"){.headerlink}

:   Lighting and translucency style control.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os

        import tecplot as tp
        from tecplot.constant import LightingEffect, PlotType, SurfacesToPlot

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(datafile)
        frame = dataset.frame

        # Enable 3D field plot, turn on contouring and translucency
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()
        plot.show_contour = True
        plot.use_translucency = True

        plot.contour(0).variable = dataset.variable('S')

        # adjust effects for every fieldmap in this dataset
        fmaps = plot.fieldmaps()
        fmaps.contour.flood_contour_group = plot.contour(0)
        fmaps.surfaces.surfaces_to_plot = SurfacesToPlot.BoundaryFaces

        eff = fmaps.effects
        eff.lighting_effect = LightingEffect.Paneled
        eff.surface_translucency = 30

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        # save image to file
        tp.export.save_png('fieldmap_effects3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_effects3d.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_effects3d.png" style="width: 300px;"
    alt="../_images/fieldmap_effects3d.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`clip_planes`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D.clip_planes "tecplot.plot.FieldmapEffects3D.clip_planes"){.reference .internal}                              Slice groups to use for clipping.
      [[`lighting_effect`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D.lighting_effect "tecplot.plot.FieldmapEffects3D.lighting_effect"){.reference .internal}                  The type of lighting effect to render.
      [[`surface_translucency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D.surface_translucency "tecplot.plot.FieldmapEffects3D.surface_translucency"){.reference .internal}   [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external} Translucency of all surfaces for this fieldmap in percent.
      [[`use_translucency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D.use_translucency "tecplot.plot.FieldmapEffects3D.use_translucency"){.reference .internal}               Enable translucency of all drawn surfaces for this fieldmap.
      [[`value_blanking`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapEffects3D.value_blanking "tecplot.plot.FieldmapEffects3D.value_blanking"){.reference .internal}                     Enable value blanking effect for this fieldmap.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapEffects3D.]{.pre}]{.sig-prename .descclassname}[[clip_planes]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects3D.clip_planes "Link to this definition"){.headerlink}

:   Slice groups to use for clipping.

    Only slice groups 0 to 5 are available for clipping. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).effects.clip_planes = [0, 1, 2]
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`SliceGroup.clip`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.SliceGroup.clip "tecplot.plot.SliceGroup.clip"){.reference
    .internal}
    :::

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} \[0-5\]

<!-- -->

[[FieldmapEffects3D.]{.pre}]{.sig-prename .descclassname}[[lighting_effect]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects3D.lighting_effect "Link to this definition"){.headerlink}

:   The type of lighting effect to render.

    Possible values:

    [[`Paneled`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect.Paneled "tecplot.constant.LightingEffect.Paneled"){.reference .internal}

    :   Within each cell, the color assigned to each area by shading or
        contour flooding is tinted by a shade constant across the cell.
        This shade is based on the orientation of the cell relative to
        your 3D light source.

    [[`Gouraud`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect.Gouraud "tecplot.constant.LightingEffect.Gouraud"){.reference .internal}

    :   This plot type offers smoother, more continuous shading than
        [[`Paneled`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect.Paneled "tecplot.constant.LightingEffect.Paneled"){.reference
        .internal} shading, but it results in slower plotting and larger
        vector images. [[`Gouraud`{.xref .any .py .py-attr .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect.Gouraud "tecplot.constant.LightingEffect.Gouraud"){.reference
        .internal} shading is not continuous across zone boundaries
        unless face neighbors are specified in the data and is not
        available for finite element volume zones when blanking is
        active in which case, the zone's lighting effect reverts to
        [[`Paneled`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect.Paneled "tecplot.constant.LightingEffect.Paneled"){.reference
        .internal} shading in this case.

    If [`IJK`{.docutils .literal .notranslate}]{.pre}-ordered data with
    [[`FieldmapSurfaces.surfaces_to_plot`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces.surfaces_to_plot "tecplot.plot.FieldmapSurfaces.surfaces_to_plot"){.reference
    .internal} is set to [[`SurfacesToPlot.ExposedCellFaces`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.ExposedCellFaces "tecplot.constant.SurfacesToPlot.ExposedCellFaces"){.reference
    .internal}, faces exposed by blanking will revert to
    [[`Paneled`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect.Paneled "tecplot.constant.LightingEffect.Paneled"){.reference
    .internal} shading.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LightingEffect
        >>> effects = plot.fieldmap(0).effects
        >>> effects.lighting_effect = LightingEffect.Paneled
    :::
    ::::

    Type[:]{.colon}

    :   [[`LightingEffect`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LightingEffect "tecplot.constant.LightingEffect"){.reference
        .internal}

<!-- -->

[[FieldmapEffects3D.]{.pre}]{.sig-prename .descclassname}[[surface_translucency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects3D.surface_translucency "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external} Translucency of all surfaces for this fieldmap in
    percent.

    The [`use_translucency`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> effects = plot.fieldmap(0).effects
        >>> effects.use_translucency = True
        >>> effects.surface_translucency = 50
    :::
    ::::

<!-- -->

[[FieldmapEffects3D.]{.pre}]{.sig-prename .descclassname}[[use_translucency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects3D.use_translucency "Link to this definition"){.headerlink}

:   Enable translucency of all drawn surfaces for this fieldmap.

    This enables translucency controlled by the
    [`surface_translucency`{.docutils .literal .notranslate}]{.pre}
    attribute:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> effects = plot.fieldmap(0).effects
        >>> effects.use_translucency = True
        >>> effects.surface_translucency = 50
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapEffects3D.]{.pre}]{.sig-prename .descclassname}[[value_blanking]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapEffects3D.value_blanking "Link to this definition"){.headerlink}

:   Enable value blanking effect for this fieldmap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).effects.value_blanking = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapmesh .section}
### [FieldmapMesh](#id55){.toc-backref role="doc-backlink"}[¶](#fieldmapmesh "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapMesh]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapMesh){.reference .internal}[¶](#tecplot.plot.FieldmapMesh "Link to this definition"){.headerlink}

:   Lines connecting neighboring data points.

    The mesh plot layer displays the lines connecting neighboring data
    points within a [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}. For
    [`I`{.docutils .literal .notranslate}]{.pre}-ordered data, the mesh
    is a single line connecting all of the points in order of increasing
    [`I`{.docutils .literal .notranslate}]{.pre}-index. For
    [`IJ`{.docutils .literal .notranslate}]{.pre}-ordered data, the mesh
    consists of two families of lines connecting adjacent data points of
    increasing [`I`{.docutils .literal .notranslate}]{.pre}-index and
    increasing [`J`{.docutils .literal .notranslate}]{.pre}-index. For
    [`IJK`{.docutils .literal .notranslate}]{.pre}-ordered data, the
    mesh consists of three families of lines, one connecting points of
    increasing [`I`{.docutils .literal .notranslate}]{.pre}-index, one
    connecting points of increasing [`J`{.docutils .literal
    .notranslate}]{.pre}-index, and one connecting points of increasing
    [`K`{.docutils .literal .notranslate}]{.pre}-index. For finite
    element zones, the mesh is a plot of every edge of all of the
    elements that are defined by the connectivity list for the node
    points:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import numpy as np
        import tecplot as tp
        from tecplot.constant import PlotType, MeshType

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(infile)

        # Enable 3D field plot and turn on contouring
        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()
        plot.show_mesh = True

        contour = plot.contour(0)
        contour.variable = dataset.variable('S')
        contour.colormap_name = 'Doppler'
        contour.levels.reset_levels(np.linspace(0.02,0.12,11))

        # set the mesh type and color for all zones
        mesh = plot.fieldmaps().mesh
        mesh.mesh_type = MeshType.HiddenLine
        mesh.color = contour

        # save image to file
        tp.export.save_png('fieldmap_mesh.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_mesh.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_mesh.png" style="width: 300px;"
    alt="../_images/fieldmap_mesh.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh.color "tecplot.plot.FieldmapMesh.color"){.reference .internal}                              The [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} for lines.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh.line_pattern "tecplot.plot.FieldmapMesh.line_pattern"){.reference .internal}         [[`LinePattern`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference .internal} type to use for mesh lines.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh.line_thickness "tecplot.plot.FieldmapMesh.line_thickness"){.reference .internal}   Thickness ([[`float`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference .external}) of the drawn lines.
      [[`mesh_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh.mesh_type "tecplot.plot.FieldmapMesh.mesh_type"){.reference .internal}                  [[`MeshType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.MeshType "tecplot.constant.MeshType"){.reference .internal} to show.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh.pattern_length "tecplot.plot.FieldmapMesh.pattern_length"){.reference .internal}   Length ([[`float`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference .external}) of the pattern segment for non-solid lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapMesh.show "tecplot.plot.FieldmapMesh.show"){.reference .internal}                                 Draw the mesh for this fieldmap.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapMesh.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapMesh.color "Link to this definition"){.headerlink}

:   The [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} for lines.

    FieldmapContour lines can be a solid color or be colored by a
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} as obtained through the [`plot.contour`{.docutils
    .literal .notranslate}]{.pre} property. Note that changing style on
    this [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.fieldmap(1).mesh.color = Color.Blue
    :::
    ::::

    Example of setting the color from a [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(1).mesh.color = plot.contour(1)
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal} or [[`ContourGroup`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}

<!-- -->

[[FieldmapMesh.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapMesh.line_pattern "Link to this definition"){.headerlink}

:   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
    .internal} type to use for mesh lines.

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
        >>> mesh = plot.fieldmap(0).mesh
        >>> mesh.line_pattern = LinePattern.Dashed
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[FieldmapMesh.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapMesh.line_thickness "Link to this definition"){.headerlink}

:   Thickness ([[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external}) of the drawn lines.

    This is the line thickness in percentage of the [[`Frame`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}'s height. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).mesh.line_thickness = 0.7
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapMesh.]{.pre}]{.sig-prename .descclassname}[[mesh_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapMesh.mesh_type "Link to this definition"){.headerlink}

:   [[`MeshType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.MeshType "tecplot.constant.MeshType"){.reference
    .internal} to show.

    Possible values:

    [[`Wireframe`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.MeshType.Wireframe "tecplot.constant.MeshType.Wireframe"){.reference .internal}

    :   Wire frame meshes are drawn below any other zone layers on the
        same zone. In 3D Cartesian plots, no hidden lines are removed.
        For 3D volume zones (finite element volume or IJK-ordered), the
        full 3D mesh (consisting of all the connecting lines between
        data points) is not generally drawn because the sheer number of
        lines would make it confusing. The mesh drawn will depend on
        [[`FieldmapSurfaces`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces "tecplot.plot.FieldmapSurfaces"){.reference
        .internal} which can be obtained through the parent fieldmap
        with [`mesh.fieldmap.surfaces`{.docutils .literal
        .notranslate}]{.pre}:

        :::: {.highlight-python .notranslate}
        ::: highlight
            from tecplot.constant import MeshType, SurfacesToPlot
            mesh = plot.fieldmap(0).mesh
            mesh.mesh_type = MeshType.Wireframe
            surfaces = mesh.fieldmap.surfaces
            surfaces.surfaces_to_plot = SurfacesToPlot.IPlanes
        :::
        ::::

        By default, only the mesh on exposed cell faces is shown.

    [[`Overlay`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.MeshType.Overlay "tecplot.constant.MeshType.Overlay"){.reference .internal}

    :   Similar to Wire Frame, mesh lines are drawn over all other zone
        layers except for vectors and scatter symbols. In 3D Cartesian
        plots, the area behind the cells of the plot is still visible
        (unless another plot type such as contour flooding prevents
        this). As with Wire Frame, the mesh drawn will depend on
        [[`FieldmapSurfaces`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces "tecplot.plot.FieldmapSurfaces"){.reference
        .internal} which can be obtained through the parent fieldmap
        with [`mesh.fieldmap.surfaces`{.docutils .literal
        .notranslate}]{.pre}.

    [[`HiddenLine`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.MeshType.HiddenLine "tecplot.constant.MeshType.HiddenLine"){.reference .internal}

    :   Similar to Overlay, except hidden lines are removed from behind
        the mesh. In effect, the cells (elements) of the mesh are
        opaque. FieldmapSurfaces and lines that are hidden behind
        another surface are removed from the plot. For 3D volume zones,
        using this plot type obscures everything inside the zone. If you
        choose this option for 3D volume zones, then choosing to plot
        every surface with:

        :::: {.highlight-python .notranslate}
        ::: highlight
            from tecplot.constant import HiddenLine, SurfacesToPlot
            mesh = plot.fieldmap(0).mesh
            mesh.mesh_type = MeshType.HiddenLine
            surfaces = mesh.fieldmap.surfaces
            surfaces.surfaces_to_plot = SurfacesToPlot.All
        :::
        ::::

        has the same effect as plotting only exposed cell faces with:

        :::: {.highlight-python .notranslate}
        ::: highlight
            surfaces.surfaces_to_plot = SurfacesToPlot.ExposedCellFaces
        :::
        ::::

        but is much slower.

    Type[:]{.colon}

    :   [[`MeshType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.MeshType "tecplot.constant.MeshType"){.reference
        .internal}

<!-- -->

[[FieldmapMesh.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapMesh.pattern_length "Link to this definition"){.headerlink}

:   Length ([[`float`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external}) of the pattern segment for non-solid lines.

    This is the pattern length in percentage of the [[`Frame`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}'s height. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).mesh.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapMesh.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapMesh.show "Link to this definition"){.headerlink}

:   Draw the mesh for this fieldmap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SurfacesToPlot
        >>> plot.show_mesh = True
        >>> surfaces = plot.fieldmap(0).surfaces
        >>> surfaces.surfaces_to_plot = SurfacesToPlot.IPlanes
        >>> plot.fieldmap(0).mesh.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmappoints .section}
### [FieldmapPoints](#id56){.toc-backref role="doc-backlink"}[¶](#fieldmappoints "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapPoints]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapPoints){.reference .internal}[¶](#tecplot.plot.FieldmapPoints "Link to this definition"){.headerlink}

:   Type and density of the points used for vector and scatter plots.

    This object controls the location of the points for
    [[`FieldmapVector`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapVector "tecplot.plot.FieldmapVector"){.reference
    .internal} and [[`FieldmapScatter`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter "tecplot.plot.FieldmapScatter"){.reference
    .internal} plots relative to the cells:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, PointsToPlot

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        # Enable 3D field plot and turn on contouring
        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian2D
        plot = frame.plot()
        plot.vector.u_variable = dataset.variable('U(M/S)')
        plot.vector.v_variable = dataset.variable('V(M/S)')
        plot.show_vector = True

        points = plot.fieldmaps().points
        points.points_to_plot = PointsToPlot.SurfaceCellCenters
        points.step = (2,2)

        # save image to file
        tp.export.save_png('fieldmap_points.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_points.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_points.png" style="width: 300px;"
    alt="../_images/fieldmap_points.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`points_to_plot`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapPoints.points_to_plot "tecplot.plot.FieldmapPoints.points_to_plot"){.reference .internal}   Location of the points to show.
      [[`step`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapPoints.step "tecplot.plot.FieldmapPoints.step"){.reference .internal}                                 Step along the dimensions [`(I,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`J,`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`K)`{.docutils .literal .notranslate}]{.pre}.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapPoints.]{.pre}]{.sig-prename .descclassname}[[points_to_plot]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapPoints.points_to_plot "Link to this definition"){.headerlink}

:   Location of the points to show.

    Possible values:

    [[`SurfaceNodes`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PointsToPlot.SurfaceNodes "tecplot.constant.PointsToPlot.SurfaceNodes"){.reference .internal}

    :   Draws only the nodes that are on the surface of the [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    [[`AllNodes`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PointsToPlot.AllNodes "tecplot.constant.PointsToPlot.AllNodes"){.reference .internal}

    :   Draws all nodes in the [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    [[`SurfaceCellCenters`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PointsToPlot.SurfaceCellCenters "tecplot.constant.PointsToPlot.SurfaceCellCenters"){.reference .internal}

    :   Draws points at the cell centers which are on or near the
        surface of the [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    [[`AllCellCenters`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PointsToPlot.AllCellCenters "tecplot.constant.PointsToPlot.AllCellCenters"){.reference .internal}

    :   Draws points at all cell centers in the [[Zone]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}.

    [[`AllConnected`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PointsToPlot.AllConnected "tecplot.constant.PointsToPlot.AllConnected"){.reference .internal}

    :   Draws all the nodes that are connected by the node map. Nodes
        without any connectivity are not drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PointsToPlot
        >>> pts = plot.fieldmap(0).points
        >>> sts.points_to_plot = PointsToPlot.SurfaceCellCenters
    :::
    ::::

    Type[:]{.colon}

    :   [[`PointsToPlot`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.PointsToPlot "tecplot.constant.PointsToPlot"){.reference
        .internal}

<!-- -->

[[FieldmapPoints.]{.pre}]{.sig-prename .descclassname}[[step]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapPoints.step "Link to this definition"){.headerlink}

:   Step along the dimensions [`(I,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`J,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`K)`{.docutils .literal .notranslate}]{.pre}.

    This property specifies the [`I`{.docutils .literal
    .notranslate}]{.pre}, [`J`{.docutils .literal .notranslate}]{.pre},
    and [`K`{.docutils .literal .notranslate}]{.pre}-step intervals. For
    irregular and finite element data, only the first parameter or
    [`I`{.docutils .literal .notranslate}]{.pre}-Step has an effect.
    This steps through the nodes in the order they are listed in the
    data file. In this case, a single number can be given, but note that
    the return type is always a 3-[[`tuple`{.xref .any .docutils
    .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external} for both ordered and irregular data.

    Example for [`IJK`{.docutils .literal .notranslate}]{.pre} ordered
    data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).points.step = (10,10,None)
        >>> print(plot.fieldmap(0).points.step)
        (10, 10, 1)
    :::
    ::::

    Example for irregular data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).points.step = 10
        >>> print(plot.fieldmap(0).points.step)
        (10, 1, 1)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapscatter .section}
### [FieldmapScatter](#id57){.toc-backref role="doc-backlink"}[¶](#fieldmapscatter "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapScatter]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapScatter){.reference .internal}[¶](#tecplot.plot.FieldmapScatter "Link to this definition"){.headerlink}

:   Plot of nodes using symbols.

    [[`FieldmapScatter`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter "tecplot.plot.FieldmapScatter"){.reference
    .internal} plots display symbols at the data points in a field. The
    symbols may be sized according to the values of a specified
    variable, colored by the values of the contour variable, or may be
    uniformly sized or colored. Unlike contour plots, scatter plots do
    not require any mesh structure connecting the points, allowing
    scatter plots of irregular data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, SymbolType, FillMode

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian2D
        plot = frame.plot()
        plot.show_scatter = True

        scatter = plot.fieldmaps().scatter
        scatter.symbol_type = SymbolType.Geometry
        scatter.fill_mode = FillMode.UseSpecificColor
        scatter.fill_color = plot.contour(0)
        scatter.size = 1

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('fieldmap_scatter.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_scatter.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_scatter.png" style="width: 300px;"
    alt="../_images/fieldmap_scatter.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.color "tecplot.plot.FieldmapScatter.color"){.reference .internal}                                    Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} of the drawn symbols.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.fill_color "tecplot.plot.FieldmapScatter.fill_color"){.reference .internal}                     Fill or background color.
      [[`fill_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.fill_mode "tecplot.plot.FieldmapScatter.fill_mode"){.reference .internal}                        Mode for the background color.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.line_thickness "tecplot.plot.FieldmapScatter.line_thickness"){.reference .internal}         Width of the lines when drawing symbols.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.show "tecplot.plot.FieldmapScatter.show"){.reference .internal}                                       Show the scatter symbols.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.size "tecplot.plot.FieldmapScatter.size"){.reference .internal}                                       Size of the symbols to draw.
      [[`size_by_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.size_by_variable "tecplot.plot.FieldmapScatter.size_by_variable"){.reference .internal}   Use a variable to determine relative size of symbols.
      [[`symbol_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.symbol_type "tecplot.plot.FieldmapScatter.symbol_type"){.reference .internal}                  The [[`SymbolType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference .internal} to use for this scatter plot.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------
      [[`symbol`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.symbol "tecplot.plot.FieldmapScatter.symbol"){.reference .internal}(\[symbol_type\])   Returns a scatter symbol style object.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} of the drawn symbols.

    This can be a solid color or a [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} as obtained through the [`plot.contour`{.docutils
    .literal .notranslate}]{.pre} property. Note that changing style on
    the [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps in the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.fieldmap(1).scatter.color = Color.Blue
    :::
    ::::

    Example of setting the color from a [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(1).scatter.color = plot.contour(1)
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal} or [[`ContourGroup`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.fill_color "Link to this definition"){.headerlink}

:   Fill or background color.

    The [`fill_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set accordingly:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, SymbolType, FillMode
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Geometry
        >>> scatter.fill_mode = FillMode.UseSpecificColor
        >>> scatter.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal} or [[`ContourGroup`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[fill_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.fill_mode "Link to this definition"){.headerlink}

:   Mode for the background color.

    Options include: [[`FillMode.UseSpecificColor`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseSpecificColor "tecplot.constant.FillMode.UseSpecificColor"){.reference
    .internal}, [[`FillMode.UseLineColor`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseLineColor "tecplot.constant.FillMode.UseLineColor"){.reference
    .internal}, [[`FillMode.UseBackgroundColor`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseBackgroundColor "tecplot.constant.FillMode.UseBackgroundColor"){.reference
    .internal} and [[`FillMode.None_`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.None_ "tecplot.constant.FillMode.None_"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, SymbolType, FillMode
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Geometry
        >>> scatter.fill_mode = FillMode.UseSpecificColor
        >>> scatter.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`FillMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode "tecplot.constant.FillMode"){.reference
        .internal}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.line_thickness "Link to this definition"){.headerlink}

:   Width of the lines when drawing symbols.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Geometry
        >>> scatter.line_thickness = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.show "Link to this definition"){.headerlink}

:   Show the scatter symbols.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_scatter = True
        >>> plot.fieldmap(2).scatter.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.size "Link to this definition"){.headerlink}

:   Size of the symbols to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).scatter.size = 4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[size_by_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.size_by_variable "Link to this definition"){.headerlink}

:   Use a variable to determine relative size of symbols.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.scatter.variable = dataset.variable('P')
        >>> plot.fieldmap(0).scatter.size_by_variable = True
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Scatter.variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.Scatter.variable "tecplot.plot.Scatter.variable"){.reference
    .internal}
    :::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[symbol]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[symbol_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapScatter.symbol){.reference .internal}[¶](#tecplot.plot.FieldmapScatter.symbol "Link to this definition"){.headerlink}

:   Returns a scatter symbol style object.

    Parameters[:]{.colon}

    :   **symbol_type** ([[`SymbolType`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference
        .internal}, optional) -- The type of symbol to return. By
        default, this will return the active symbol type which is
        obtained from [[`FieldmapScatter.symbol_type`{.xref .any .py
        .py-attr .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.FieldmapScatter.symbol_type "tecplot.plot.FieldmapScatter.symbol_type"){.reference
        .internal}.

    Returns: [[`TextScatterSymbol`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.TextScatterSymbol "tecplot.plot.TextScatterSymbol"){.reference
    .internal} or [[`GeometryScatterSymbol`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.GeometryScatterSymbol "tecplot.plot.GeometryScatterSymbol"){.reference
    .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> plot.fieldmap(0).scatter.symbol_type = SymbolType.Text
        >>> symbol = plot.fieldmap(0).scatter.symbol()
        >>> symbol.text = 'a'
    :::
    ::::

<!-- -->

[[FieldmapScatter.]{.pre}]{.sig-prename .descclassname}[[symbol_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapScatter.symbol_type "Link to this definition"){.headerlink}

:   The [[`SymbolType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference
    .internal} to use for this scatter plot.

    Possible values are [[`SymbolType.Geometry`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType.Geometry "tecplot.constant.SymbolType.Geometry"){.reference
    .internal} or [[`SymbolType.Text`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType.Text "tecplot.constant.SymbolType.Text"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> plot.fieldmap(0).scatter.symbol_type = SymbolType.Text
    :::
    ::::

    Type[:]{.colon}

    :   [[`SymbolType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference
        .internal}
:::

::: {#geometryscattersymbol .section}
### [GeometryScatterSymbol](#id58){.toc-backref role="doc-backlink"}[¶](#geometryscattersymbol "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[GeometryScatterSymbol]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[parent]{.pre}]{.n}*, *[[svarg]{.pre}]{.n}[[=]{.pre}]{.o}[[\'SYMBOLSHAPE\']{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/symbol.html#GeometryScatterSymbol){.reference .internal}[¶](#tecplot.plot.GeometryScatterSymbol "Link to this definition"){.headerlink}

:   Geometric shape for scatter plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import (Color, PlotType, PointsToPlot, SymbolType,
                                      GeomShape, FillMode)

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian2D
        plot = frame.plot()
        plot.show_scatter = True

        # get handle to a collection of all fieldmaps
        fmaps = plot.fieldmaps()

        points = fmaps.points
        points.points_to_plot = PointsToPlot.SurfaceCellCenters
        points.step = (2,2)

        scatter = fmaps.scatter
        scatter.fill_mode = FillMode.UseSpecificColor
        scatter.size = 2
        scatter.line_thickness = 0.5
        scatter.symbol_type = SymbolType.Geometry

        for i, fmap in enumerate(fmaps):
            fmap.scatter.symbol().shape = GeomShape(i%7)
            fmap.scatter.color = Color(i)
            fmap.scatter.fill_color = Color(i + plot.num_fieldmaps)

        tp.export.save_png('fieldmap_scatter_geometry.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_scatter_geometry.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_scatter_geometry.png" style="width: 300px;"
    alt="../_images/fieldmap_scatter_geometry.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GeometryScatterSymbol.shape "tecplot.plot.GeometryScatterSymbol.shape"){.reference .internal}   Geometric shape to use when plotting scatter points.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------

<!-- -->

[[GeometryScatterSymbol.]{.pre}]{.sig-prename .descclassname}[[shape]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GeometryScatterSymbol.shape "Link to this definition"){.headerlink}

:   Geometric shape to use when plotting scatter points.

    Possible values: [[`Square`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Square "tecplot.constant.GeomShape.Square"){.reference
    .internal}, [[`Del`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Del "tecplot.constant.GeomShape.Del"){.reference
    .internal}, [[`Grad`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Grad "tecplot.constant.GeomShape.Grad"){.reference
    .internal}, [[`RTri`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.RTri "tecplot.constant.GeomShape.RTri"){.reference
    .internal}, [[`LTri`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.LTri "tecplot.constant.GeomShape.LTri"){.reference
    .internal}, [[`Diamond`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Diamond "tecplot.constant.GeomShape.Diamond"){.reference
    .internal}, [[`Circle`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Circle "tecplot.constant.GeomShape.Circle"){.reference
    .internal}, [[`Cube`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Cube "tecplot.constant.GeomShape.Cube"){.reference
    .internal}, [[`Sphere`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Sphere "tecplot.constant.GeomShape.Sphere"){.reference
    .internal}, [[`Octahedron`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Octahedron "tecplot.constant.GeomShape.Octahedron"){.reference
    .internal}, [[`Point`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Point "tecplot.constant.GeomShape.Point"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType, GeomShape
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Geometry
        >>> scatter.symbol().shape = GeomShape.Diamond
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomShape`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape "tecplot.constant.GeomShape"){.reference
        .internal}
:::

::: {#textscattersymbol .section}
### [TextScatterSymbol](#id59){.toc-backref role="doc-backlink"}[¶](#textscattersymbol "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[TextScatterSymbol]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[parent]{.pre}]{.n}*, *[[svarg]{.pre}]{.n}[[=]{.pre}]{.o}[[\'SYMBOLSHAPE\']{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/symbol.html#TextScatterSymbol){.reference .internal}[¶](#tecplot.plot.TextScatterSymbol "Link to this definition"){.headerlink}

:   Text character for scatter plots.

    Only a single character can be used.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import (Color, PlotType, PointsToPlot, SymbolType,
                                          GeomShape, FillMode)

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.Cartesian2D
        plot = frame.plot()
        plot.show_shade = True
        plot.show_scatter = True

        # get handle to a collection of all fieldmaps
        fmaps = plot.fieldmaps()

        fmaps.points.points_to_plot = PointsToPlot.SurfaceCellCenters
        fmaps.points.step = (4,4)
        fmaps.shade.color = Color.LightBlue

        fmaps.scatter.fill_mode = FillMode.UseSpecificColor
        fmaps.scatter.fill_color = Color.Yellow
        fmaps.scatter.size = 3
        fmaps.scatter.symbol_type = SymbolType.Text

        for i, fmap in enumerate(fmaps):
            fmap.scatter.color = Color((i % 4) + 13)
            fmap.scatter.symbol().text = hex(i)[-1]

        tp.export.save_png('fieldmap_scatter_text.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_scatter_text.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_scatter_text.png" style="width: 300px;"
    alt="../_images/fieldmap_scatter_text.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------
      [[`font_override`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TextScatterSymbol.font_override "tecplot.plot.TextScatterSymbol.font_override"){.reference .internal}   Typeface to use when rendering text-based scatter.
      [[`text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TextScatterSymbol.text "tecplot.plot.TextScatterSymbol.text"){.reference .internal}                              The ASCII character to use as the symbol to show
      [[`use_base_font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TextScatterSymbol.use_base_font "tecplot.plot.TextScatterSymbol.use_base_font"){.reference .internal}   Use the base typeface when rendering text-based scatter.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------

<!-- -->

[[TextScatterSymbol.]{.pre}]{.sig-prename .descclassname}[[font_override]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TextScatterSymbol.font_override "Link to this definition"){.headerlink}

:   Typeface to use when rendering text-based scatter.

    Possible values: [[`constant.Font.Greek`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font.Greek "tecplot.constant.Font.Greek"){.reference
    .internal}, [[`constant.Font.Math`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font.Math "tecplot.constant.Font.Math"){.reference
    .internal} or [[`constant.Font.UserDefined`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font.UserDefined "tecplot.constant.Font.UserDefined"){.reference
    .internal}.

    The [`use_base_font`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType, Font
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Text
        >>> scatter.symbol().use_base_font = False
        >>> scatter.symbol().font_override = Font.Math
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font "tecplot.constant.Font"){.reference
        .internal}

<!-- -->

[[TextScatterSymbol.]{.pre}]{.sig-prename .descclassname}[[text]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TextScatterSymbol.text "Link to this definition"){.headerlink}

:   The ASCII character to use as the symbol to show

    ::: {.admonition .note}
    Note

    This is limited to a single character.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Text
        >>> scatter.symbol().text = 'X'
    :::
    ::::

<!-- -->

[[TextScatterSymbol.]{.pre}]{.sig-prename .descclassname}[[use_base_font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TextScatterSymbol.use_base_font "Link to this definition"){.headerlink}

:   Use the base typeface when rendering text-based scatter.

    When [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the [`font_override`{.docutils .literal
    .notranslate}]{.pre} attribute takes effect:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType, Font
        >>> scatter = plot.fieldmap(0).scatter
        >>> scatter.symbol_type = SymbolType.Text
        >>> scatter.symbol().use_base_font = False
        >>> scatter.symbol().font_override = Font.Greek
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapshade .section}
### [FieldmapShade](#id60){.toc-backref role="doc-backlink"}[¶](#fieldmapshade "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapShade]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapShade){.reference .internal}[¶](#tecplot.plot.FieldmapShade "Link to this definition"){.headerlink}

:   Fill color for displayed surfaces on 2D field plots.

    Although most commonly used with 3D surfaces (see
    [[`FieldmapShade3D`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapShade3D "tecplot.plot.FieldmapShade3D"){.reference
    .internal}), shade plots can be used to flood 2D plots with solid
    colors.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import random
        import tecplot
        from tecplot.constant import Color, PlotType

        random.seed(1)

        examples_dir = tecplot.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tecplot.data.load_tecplot(datafile)
        frame = dataset.frame
        frame.plot_type = PlotType.Cartesian2D
        plot = frame.plot()

        for zone in dataset.zones():
            color = Color(random.randint(0,63))
            while color == Color.White:
                color = Color(random.randint(0,63))
            plot.fieldmap(zone).shade.color = color

        tecplot.export.save_png('fieldmap_shade2d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_shade2d.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_shade2d.png" style="width: 300px;"
    alt="../_images/fieldmap_shade2d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapShade.color "tecplot.plot.FieldmapShade.color"){.reference .internal}   Fill [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the shade.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapShade.show "tecplot.plot.FieldmapShade.show"){.reference .internal}      FieldmapShade the drawn surfaces.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapShade.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapShade.color "Link to this definition"){.headerlink}

:   Fill [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the shade.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.fieldmap(0).shade.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[FieldmapShade.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapShade.show "Link to this definition"){.headerlink}

:   FieldmapShade the drawn surfaces.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).shade.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapshade3d .section}
### [FieldmapShade3D](#id61){.toc-backref role="doc-backlink"}[¶](#fieldmapshade3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapShade3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapShade3D){.reference .internal}[¶](#tecplot.plot.FieldmapShade3D "Link to this definition"){.headerlink}

:   Fill color for displayed surfaces on 3D field plots.

    This class inherits all functionality and purpose from
    [[`FieldmapShade`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.FieldmapShade "tecplot.plot.FieldmapShade"){.reference
    .internal} and adds the ability to turn on or off the lighting
    effect. In 3D plots, fieldmap effects (translucency and lighting)
    cause color variation (shading) throughout the zones. Shading can
    can be useful in discerning the shape of the data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os
        import random
        import tecplot
        from tecplot.constant import Color, PlotType, SurfacesToPlot

        random.seed(1)

        examples_dir = tecplot.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tecplot.data.load_tecplot(datafile)
        frame = dataset.frame
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()

        for zone in dataset.zones():
            color = Color(random.randint(0,63))
            while color == Color.White:
                color = Color(random.randint(0,63))
            fmap = plot.fieldmap(zone)
            fmap.surfaces.surfaces_to_plot = SurfacesToPlot.BoundaryFaces
            fmap.shade.color = color
            fmap.shade.use_lighting_effect = False

        tecplot.export.save_png('fieldmap_shade3d.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_shade3d.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_shade3d.png" style="width: 300px;"
    alt="../_images/fieldmap_shade3d.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapShade3D.color "tecplot.plot.FieldmapShade3D.color"){.reference .internal}                                             Fill [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the shade.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapShade3D.show "tecplot.plot.FieldmapShade3D.show"){.reference .internal}                                                FieldmapShade the drawn surfaces.
      [[`use_lighting_effect`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapShade3D.use_lighting_effect "tecplot.plot.FieldmapShade3D.use_lighting_effect"){.reference .internal}   Draw a lighting effect on the shaded surfaces.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapShade3D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapShade3D.color "Link to this definition"){.headerlink}

:   Fill [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the shade.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.fieldmap(0).shade.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[FieldmapShade3D.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapShade3D.show "Link to this definition"){.headerlink}

:   FieldmapShade the drawn surfaces.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).shade.show = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapShade3D.]{.pre}]{.sig-prename .descclassname}[[use_lighting_effect]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapShade3D.use_lighting_effect "Link to this definition"){.headerlink}

:   Draw a lighting effect on the shaded surfaces.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).shade.use_lighting_effect = False
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#fieldmapsurfaces .section}
### [FieldmapSurfaces](#id62){.toc-backref role="doc-backlink"}[¶](#fieldmapsurfaces "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapSurfaces]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapSurfaces){.reference .internal}[¶](#tecplot.plot.FieldmapSurfaces "Link to this definition"){.headerlink}

:   Plot surfaces from volume data.

    This class controls viewing volume data as surfaces, either via a
    boundary surface or one or more planes along the [`I`{.docutils
    .literal .notranslate}]{.pre}, [`J`{.docutils .literal
    .notranslate}]{.pre}, [`K`{.docutils .literal .notranslate}]{.pre}
    dimensions for ordered data:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np

        import tecplot as tp
        from tecplot.constant import *
        from tecplot.data.operate import execute_equation

        # Get the active frame, setup a grid (30x30x30)
        # where each dimension ranges from 0 to 30.
        # Add variable P to the dataset and give
        # values to the data.
        frame = tp.active_frame()
        dataset = frame.dataset
        for v in ['X','Y','Z','P']:
            dataset.add_variable(v)
        zone = dataset.add_ordered_zone('Zone', (30,30,30))
        xx = np.linspace(0,30,30)
        for v,arr in zip(['X','Y','Z'],np.meshgrid(xx,xx,xx)):
            zone.values(v)[:] = arr.ravel()
        execute_equation('{P} = -10*{X} + {Y}**2 + {Z}**2')

        # Enable 3D field plot and turn on contouring
        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()
        plot.show_contour = True

        # get a handle of the fieldmap for this zone
        fmap = plot.fieldmap(dataset.zone('Zone'))

        # set the active contour group to flood by variable P
        fmap.contour.flood_contour_group.variable = dataset.variable('P')
        plot.contour(0).levels.reset_to_nice()

        # show I and J-planes through the surface
        fmap.surfaces.surfaces_to_plot = SurfacesToPlot.IJPlanes

        # show only the first and last I-planes
        # min defaults to 0, max defaults to -1
        # we set step to -1 which is equivalent
        # to the I-dimensions's max
        fmap.surfaces.i_range = None,None,-1

        # show J-planes at indices: [5, 15, 25]
        fmap.surfaces.j_range = 5,25,10

        # save image to file
        tp.export.save_png('fieldmap_surfaces_ij.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_surfaces_ij.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_surfaces_ij.png" style="width: 300px;"
    alt="../_images/fieldmap_surfaces_ij.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`i_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces.i_range "tecplot.plot.FieldmapSurfaces.i_range"){.reference .internal}                              [[`IndexRange`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference .internal} for the *I* dimension of ordered data.
      [[`j_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces.j_range "tecplot.plot.FieldmapSurfaces.j_range"){.reference .internal}                              [[`IndexRange`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference .internal} for the *J* dimension of ordered data.
      [[`k_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces.k_range "tecplot.plot.FieldmapSurfaces.k_range"){.reference .internal}                              [[`IndexRange`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference .internal} for the *K* dimension of ordered data.
      [[`surfaces_to_plot`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapSurfaces.surfaces_to_plot "tecplot.plot.FieldmapSurfaces.surfaces_to_plot"){.reference .internal}   The surfaces to show.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapSurfaces.]{.pre}]{.sig-prename .descclassname}[[i_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapSurfaces.i_range "Link to this definition"){.headerlink}

:   [[`IndexRange`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference
    .internal} for the *I* dimension of ordered data.

    This example shows [`I`{.docutils .literal
    .notranslate}]{.pre}-planes at [`i`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`=`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`[0,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`2,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`4,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`6,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`8,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`10]`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SurfacesToPlot
        >>> srf = frame.plot().fieldmap(0).surfaces
        >>> srf.surfaces_to_plot = SurfacesToPlot.IPlanes
        >>> srf.i_range = 0, 10, 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (min, max, step)

<!-- -->

[[FieldmapSurfaces.]{.pre}]{.sig-prename .descclassname}[[j_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapSurfaces.j_range "Link to this definition"){.headerlink}

:   [[`IndexRange`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference
    .internal} for the *J* dimension of ordered data.

    This example shows all [`J`{.docutils .literal
    .notranslate}]{.pre}-planes starting with [`j`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`=`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`10`{.docutils .literal .notranslate}]{.pre} up to the
    maximum [`J`{.docutils .literal .notranslate}]{.pre}-plane of the
    associated [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SurfacesToPlot
        >>> srf = frame.plot().fieldmap(0).surfaces
        >>> srf.surfaces_to_plot = SurfacesToPlot.JPlanes
        >>> srf.j_range = 10, None, 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (min, max, step)

<!-- -->

[[FieldmapSurfaces.]{.pre}]{.sig-prename .descclassname}[[k_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapSurfaces.k_range "Link to this definition"){.headerlink}

:   [[`IndexRange`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference
    .internal} for the *K* dimension of ordered data.

    This example shows all [`K`{.docutils .literal
    .notranslate}]{.pre}-planes starting with the first up to 5 from the
    last [`K`{.docutils .literal .notranslate}]{.pre}-plane of the
    associated [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SurfacesToPlot
        >>> srf = frame.plot().fieldmap(0).surfaces
        >>> srf.surfaces_to_plot = SurfacesToPlot.KPlanes
        >>> srf.k_range = None, -5
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (min, max, step)

<!-- -->

[[FieldmapSurfaces.]{.pre}]{.sig-prename .descclassname}[[surfaces_to_plot]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapSurfaces.surfaces_to_plot "Link to this definition"){.headerlink}

:   The surfaces to show.

    Possible values: [[`BoundaryFaces`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.BoundaryFaces "tecplot.constant.SurfacesToPlot.BoundaryFaces"){.reference
    .internal}, [[`ExposedCellFaces`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.ExposedCellFaces "tecplot.constant.SurfacesToPlot.ExposedCellFaces"){.reference
    .internal}, [[`IPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.IPlanes "tecplot.constant.SurfacesToPlot.IPlanes"){.reference
    .internal}, [[`JPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.JPlanes "tecplot.constant.SurfacesToPlot.JPlanes"){.reference
    .internal}, [[`KPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.KPlanes "tecplot.constant.SurfacesToPlot.KPlanes"){.reference
    .internal}, [[`IJPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.IJPlanes "tecplot.constant.SurfacesToPlot.IJPlanes"){.reference
    .internal}, [[`JKPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.JKPlanes "tecplot.constant.SurfacesToPlot.JKPlanes"){.reference
    .internal}, [[`IKPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.IKPlanes "tecplot.constant.SurfacesToPlot.IKPlanes"){.reference
    .internal}, [[`IJKPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AnimationType.IJKPlanes "tecplot.constant.AnimationType.IJKPlanes"){.reference
    .internal}, [[`All`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.All "tecplot.constant.SurfacesToPlot.All"){.reference
    .internal}, the python built-in [[`None`{.xref .any .docutils
    .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}.

    Options such as [[`IJKPlanes`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AnimationType.IJKPlanes "tecplot.constant.AnimationType.IJKPlanes"){.reference
    .internal} show planes from multiple dimensions. For example, the
    [[`IJPlanes`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot.IJPlanes "tecplot.constant.SurfacesToPlot.IJPlanes"){.reference
    .internal} value shows both the [`I`{.docutils .literal
    .notranslate}]{.pre}-planes and the [`J`{.docutils .literal
    .notranslate}]{.pre}-planes. The following example shows a 3D field
    plot using faces on the boundary:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SurfacesToPlot
        >>> frame.plot_type = PlotType.Cartesian3D
        >>> srf = frame.plot().fieldmap(0).surfaces
        >>> srf.surfaces_to_plot = SurfacesToPlot.BoundaryFaces
    :::
    ::::

    Type[:]{.colon}

    :   [[`SurfacesToPlot`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SurfacesToPlot "tecplot.constant.SurfacesToPlot"){.reference
        .internal}
:::

::: {#fieldmapvector .section}
### [FieldmapVector](#id63){.toc-backref role="doc-backlink"}[¶](#fieldmapvector "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[FieldmapVector]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[fieldmap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/fieldmap.html#FieldmapVector){.reference .internal}[¶](#tecplot.plot.FieldmapVector "Link to this definition"){.headerlink}

:   Field plot of arrows.

    Before doing anything with vector plots, one must set the variables
    to be used for the [`(U,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`V,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`W)`{.docutils .literal .notranslate}]{.pre}
    coordinates. This is done through the plot object. Once set, the
    vectors can be displayed and manipulated using this class:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        import tecplot as tp
        from tecplot.data.operate import execute_equation
        from tecplot.constant import (PlotType, PointsToPlot, VectorType,
                                      ArrowheadStyle)

        frame = tp.active_frame()
        dataset = frame.dataset
        for v in ['X','Y','Z','P','Q','R']:
            dataset.add_variable(v)
        zone = dataset.add_ordered_zone('Zone', (30,30,30))
        xx = np.linspace(0,30,30)
        for v,arr in zip(['X','Y','Z'],np.meshgrid(xx,xx,xx)):
            zone.values(v)[:] = arr.ravel()
        execute_equation('{P} = -10 * {X}    +      {Y}**2 + {Z}**2')
        execute_equation('{Q} =       {X}    - 10 * {Y}    - {Z}**2')
        execute_equation('{R} =       {X}**2 +      {Y}**2 - {Z}   ')

        frame.plot_type = PlotType.Cartesian3D
        plot = frame.plot()
        plot.contour(0).variable = dataset.variable('P')
        plot.contour(0).colormap_name = 'Two Color'
        plot.contour(0).levels.reset_to_nice()
        plot.vector.u_variable = dataset.variable('P')
        plot.vector.v_variable = dataset.variable('Q')
        plot.vector.w_variable = dataset.variable('R')
        plot.show_vector = True

        points = plot.fieldmap(0).points
        points.points_to_plot = PointsToPlot.AllNodes
        points.step = (5,3,2)

        vector = plot.fieldmap(0).vector
        vector.show = True
        vector.vector_type = VectorType.MidAtPoint
        vector.arrowhead_style = ArrowheadStyle.Filled
        vector.color = plot.contour(0)
        vector.line_thickness = 0.4

        # save image to file
        tp.export.save_png('fieldmap_vector.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/fieldmap_vector.png"
    class="reference internal image-reference"><img
    src="../_images/fieldmap_vector.png" style="width: 300px;"
    alt="../_images/fieldmap_vector.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`arrowhead_style`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.arrowhead_style "tecplot.plot.FieldmapVector.arrowhead_style"){.reference .internal}   The [[`ArrowheadStyle`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle "tecplot.constant.ArrowheadStyle"){.reference .internal} drawn.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.color "tecplot.plot.FieldmapVector.color"){.reference .internal}                                 The [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference .internal} to use when drawing vectors.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.line_pattern "tecplot.plot.FieldmapVector.line_pattern"){.reference .internal}            The [[`LinePattern`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference .internal} used to draw the arrow line.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.line_thickness "tecplot.plot.FieldmapVector.line_thickness"){.reference .internal}      The width of the arrow line.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.pattern_length "tecplot.plot.FieldmapVector.pattern_length"){.reference .internal}      Length of the pattern used when drawing vector lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.show "tecplot.plot.FieldmapVector.show"){.reference .internal}                                    Enable drawing vectors on the plot.
      [[`tangent_only`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.tangent_only "tecplot.plot.FieldmapVector.tangent_only"){.reference .internal}            Show only tangent vectors.
      [[`vector_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.FieldmapVector.vector_type "tecplot.plot.FieldmapVector.vector_type"){.reference .internal}               Anchor point of the drawn vectors.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[arrowhead_style]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.arrowhead_style "Link to this definition"){.headerlink}

:   The [[`ArrowheadStyle`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle "tecplot.constant.ArrowheadStyle"){.reference
    .internal} drawn.

    Possible values: [[`Plain`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle.Plain "tecplot.constant.ArrowheadStyle.Plain"){.reference
    .internal}, [[`Filled`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle.Filled "tecplot.constant.ArrowheadStyle.Filled"){.reference
    .internal}, [[`Hollow`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle.Hollow "tecplot.constant.ArrowheadStyle.Hollow"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadStyle
        >>> plot.fieldmap(0).vector.arrowhead_style = ArrowheadStyle.Filled
    :::
    ::::

    Type[:]{.colon}

    :   [[`ArrowheadStyle`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle "tecplot.constant.ArrowheadStyle"){.reference
        .internal}

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.color "Link to this definition"){.headerlink}

:   The [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} or [[`ContourGroup`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} to use when drawing vectors.

    FieldmapVectors can be a solid color or be colored by a
    [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} as obtained through the [`plot.contour`{.docutils
    .literal .notranslate}]{.pre} property. Note that changing style on
    this [[`ContourGroup`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal} will affect all other fieldmaps on the same
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} that use it. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.fieldmap(1).vector.color = Color.Blue
    :::
    ::::

    Example of setting the color from a [[`ContourGroup`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(1).vector.color = plot.contour(1)
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal} or [[`ContourGroup`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.line_pattern "Link to this definition"){.headerlink}

:   The [[`LinePattern`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
    .internal} used to draw the arrow line.

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
        >>> vector = plot.fieldmap(0).vector
        >>> vector.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.line_thickness "Link to this definition"){.headerlink}

:   The width of the arrow line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> vector = plot.fieldmap(0).vector.line_thickness = 0.7
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percentage of [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} height)

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.pattern_length "Link to this definition"){.headerlink}

:   Length of the pattern used when drawing vector lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> vector = plot.fieldmap(0).vector
        >>> vector.line_pattern = LinePattern.Dashed
        >>> vector.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percentage of [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} height)

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.show "Link to this definition"){.headerlink}

:   Enable drawing vectors on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_vector = True
        >>> plot.fieldmap(0).vector.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[tangent_only]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.tangent_only "Link to this definition"){.headerlink}

:   Show only tangent vectors.

    Set to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external} to display **only** the tangent component of vectors.
    Tangent vectors are drawn on 3D surfaces only where it is possible
    to determine a vector normal to the surface. A plot where multiple
    surfaces intersect each other using common nodes is a case where
    tangent vectors are not drawn because there is more than one normal
    to choose from. An example of this would be a volume
    [`IJK`{.docutils .literal .notranslate}]{.pre}-ordered zone where
    both the [`I`{.docutils .literal .notranslate}]{.pre} and
    [`J`{.docutils .literal .notranslate}]{.pre}-planes are shown. If
    tangent vectors cannot be drawn, then regular vectors are plotted
    instead.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.fieldmap(0).vector.tangent_only = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[FieldmapVector.]{.pre}]{.sig-prename .descclassname}[[vector_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.FieldmapVector.vector_type "Link to this definition"){.headerlink}

:   Anchor point of the drawn vectors.

    Possible values: [[`TailAtPoint`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VectorType.TailAtPoint "tecplot.constant.VectorType.TailAtPoint"){.reference
    .internal}, [[`HeadAtPoint`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VectorType.HeadAtPoint "tecplot.constant.VectorType.HeadAtPoint"){.reference
    .internal}, [[`MidAtPoint`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VectorType.MidAtPoint "tecplot.constant.VectorType.MidAtPoint"){.reference
    .internal}, [[`HeadOnly`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VectorType.HeadOnly "tecplot.constant.VectorType.HeadOnly"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import VectorType
        >>> plot.fieldmap(0).vector.vector_type = VectorType.MidAtPoint
    :::
    ::::

    Type[:]{.colon}

    :   [[`VectorType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.VectorType "tecplot.constant.VectorType"){.reference
        .internal}
:::
::::::::::::::::::::

::::::::::::::: {#linemaps .section}
[]{#linemap}

## [Linemaps](#id29){.toc-backref role="doc-backlink"}[¶](#linemaps "Link to this heading"){.headerlink}

- [PolarLinemap](#polarlinemap){#id64 .reference .internal}

- [PolarLinemapCollection](#polarlinemapcollection){#id65 .reference
  .internal}

- [XYLinemap](#xylinemap){#id66 .reference .internal}

- [XYLinemapCollection](#xylinemapcollection){#id67 .reference
  .internal}

- [LinemapLine](#linemapline){#id68 .reference .internal}

- [LinemapCurve](#linemapcurve){#id69 .reference .internal}

- [LinemapBars](#linemapbars){#id70 .reference .internal}

- [LinemapErrorBars](#linemaperrorbars){#id71 .reference .internal}

- [LinemapIndices](#linemapindices){#id72 .reference .internal}

- [LinemapSymbols](#linemapsymbols){#id73 .reference .internal}

- [GeometrySymbol](#geometrysymbol){#id74 .reference .internal}

- [TextSymbol](#textsymbol){#id75 .reference .internal}

::: {#polarlinemap .section}
### [PolarLinemap](#id64){.toc-backref role="doc-backlink"}[¶](#polarlinemap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarLinemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#PolarLinemap){.reference .internal}[¶](#tecplot.plot.PolarLinemap "Link to this definition"){.headerlink}

:   Data mapping and style control for polar line plots.

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.aux_data "tecplot.plot.PolarLinemap.aux_data"){.reference .internal}                                       Auxiliary data for this linemap.
      [[`curve`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.curve "tecplot.plot.PolarLinemap.curve"){.reference .internal}                                                Style and fitting-method control for lines.
      [[`function_dependency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.function_dependency "tecplot.plot.PolarLinemap.function_dependency"){.reference .internal}      The independent variable for function evalulation.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.index "tecplot.plot.PolarLinemap.index"){.reference .internal}                                                Zero-based integer identifier for this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.indices "tecplot.plot.PolarLinemap.indices"){.reference .internal}                                          Object controlling which lines are shown.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.line "tecplot.plot.PolarLinemap.line"){.reference .internal}                                                   Style for lines to be drawn.
      [[`linemap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.linemap_indices "tecplot.plot.PolarLinemap.linemap_indices"){.reference .internal}                  Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.name "tecplot.plot.PolarLinemap.name"){.reference .internal}                                                   Name identifier of this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`r_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.r_axis "tecplot.plot.PolarLinemap.r_axis"){.reference .internal}                                             Radial axis used by this linemap.
      [[`r_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.r_variable "tecplot.plot.PolarLinemap.r_variable"){.reference .internal}                                 [\\(r\\)]{.math .notranslate .nohighlight}-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} of the plotted line.
      [[`r_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.r_variable_index "tecplot.plot.PolarLinemap.r_variable_index"){.reference .internal}               [\\(r\\)]{.math .notranslate .nohighlight}-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} index of the plotted line.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.show "tecplot.plot.PolarLinemap.show"){.reference .internal}                                                   Display this linemap on the plot.
      [[`show_in_legend`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.show_in_legend "tecplot.plot.PolarLinemap.show_in_legend"){.reference .internal}                     Show this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} in the legend.
      [[`sort_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.sort_mode "tecplot.plot.PolarLinemap.sort_mode"){.reference .internal}                                    Control which [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to use when sorting lines.
      [[`sort_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.sort_variable "tecplot.plot.PolarLinemap.sort_variable"){.reference .internal}                        Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used when listing lines.
      [[`sort_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.sort_variable_index "tecplot.plot.PolarLinemap.sort_variable_index"){.reference .internal}      Zero-based index of the specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for sorting.
      [[`symbols`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.symbols "tecplot.plot.PolarLinemap.symbols"){.reference .internal}                                          Style for markers at points along the lines.
      [[`theta_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.theta_axis "tecplot.plot.PolarLinemap.theta_axis"){.reference .internal}                                 Angular axis used by this linemap.
      [[`theta_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.theta_variable "tecplot.plot.PolarLinemap.theta_variable"){.reference .internal}                     :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} of the plotted line.
      [[`theta_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.theta_variable_index "tecplot.plot.PolarLinemap.theta_variable_index"){.reference .internal}   :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} index of the plotted line.
      [[`zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.zone "tecplot.plot.PolarLinemap.zone"){.reference .internal}                                                   Data source ([[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal}) for this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`zone_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemap.zone_index "tecplot.plot.PolarLinemap.zone_index"){.reference .internal}                                 [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Zero-based index of the [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will draw.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this linemap.

    Returns: [[`AuxData`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
    .internal}

    This is the auxiliary data attached to the linemap. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = tp.active_frame().plot(PlotType.XYLine)
        >>> aux = plot.linemap(0).aux_data
        >>> aux['Result'] = '3.14159'
        >>> print(aux['Result'])
        3.14159
    :::
    ::::

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[curve]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.curve "Link to this definition"){.headerlink}

:   Style and fitting-method control for lines.

    Type[:]{.colon}

    :   [[`LinemapCurve`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapCurve "tecplot.plot.LinemapCurve"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[function_dependency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.function_dependency "Link to this definition"){.headerlink}

:   The independent variable for function evalulation.

    Possible values: [`RIndependent`{.docutils .literal
    .notranslate}]{.pre}, [`ThetaIndependent`{.docutils .literal
    .notranslate}]{.pre}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import FunctionDependency, PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> lmap = plot.linemap(0)
        >>> lmap.function_dependency = FunctionDependency.ThetaIndependent
    :::
    ::::

    Type[:]{.colon}

    :   [[`FunctionDependency`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency "tecplot.constant.FunctionDependency"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.index "Link to this definition"){.headerlink}

:   Zero-based integer identifier for this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> lmap = plot.linemap(1)
        >>> print(lmap.index)
        1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.indices "Link to this definition"){.headerlink}

:   Object controlling which lines are shown.

    Type[:]{.colon}

    :   [[`LinemapIndices`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapIndices "tecplot.plot.LinemapIndices"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.line "Link to this definition"){.headerlink}

:   Style for lines to be drawn.

    Type[:]{.colon}

    :   [[`LinemapLine`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapLine "tecplot.plot.LinemapLine"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[linemap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.linemap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.name "Link to this definition"){.headerlink}

:   Name identifier of this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    Names are automatically assigned to each mapping. The nature of the
    name depends on the type of data used to create the mapping. If your
    data has only one dependent variable, the default is to use the zone
    name for the mapping. If your data has multiple dependent variables,
    then the default is to use the dependent variable name for the
    mapping. In either case each mapping is assigned a special name
    ([`&ZN&`{.docutils .literal .notranslate}]{.pre} or
    [`&DN&`{.docutils .literal .notranslate}]{.pre}) that is replaced
    with the zone or variable name when the name is displayed.

    Selecting variables in a 3D finite element zone may require
    significant time, since the variable must be loaded over the entire
    zone. XY and Polar line plots are best used with linear or ordered
    data, or with two-dimensional finite element data.

    Certain placeholder text will be replaced with values based on
    elements within the plot. By combining static text with these
    placeholders, you can construct a name in any format you like:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(2).name = 'Zone: &ZN&'
    :::
    ::::

    The placeholders available are:

    Zone name ([`&ZN&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the zone assigned
        to that mapping.

    Zone number ([`&Z#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the zone
        assigned to the mapping.

    Independent variable name ([`&IV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the independent
        variable assigned to that mapping.

    Independent variable number ([`&I#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the independent
        variable assigned to the mapping.

    Dependent variable name ([`&DV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the dependent
        variable assigned to that mapping.

    Dependent variable number ([`&D#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the dependent
        variable assigned to the mapping.

    Map number ([`&M#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the mapping.

    X-Axis number ([`&X#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the X-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Y-Axis number ([`&Y#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the Y-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[r_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.r_axis "Link to this definition"){.headerlink}

:   Radial axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).r_axis.title = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`RadialLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.RadialLineAxis "tecplot.plot.RadialLineAxis"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[r_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.r_variable "Link to this definition"){.headerlink}

:   [\\(r\\)]{.math .notranslate .nohighlight}-component
    [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).r_variable = dataset.variable('R')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[r_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.r_variable_index "Link to this definition"){.headerlink}

:   [\\(r\\)]{.math .notranslate .nohighlight}-component
    [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} index of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).r_variable_index = 0
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (Zero-based index)

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.show "Link to this definition"){.headerlink}

:   Display this linemap on the plot.

    Example usage for turning on all linemaps:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for lmap in plot.linemaps():
        ...     lmap.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[show_in_legend]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.show_in_legend "Link to this definition"){.headerlink}

:   Show this [[Linemaps]{.std .std-ref}](#linemap){.reference
    .internal} in the legend.

    Possible values:

    [[`LegendShow.Always`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Always "tecplot.constant.LegendShow.Always"){.reference .internal}

    :   The mapping appears in the legend even if the mapping is turned
        off (deactivated) or its entry in the table looks exactly like
        another mapping's entry.

    [[`LegendShow.Never`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Never "tecplot.constant.LegendShow.Never"){.reference .internal}

    :   The mapping never appears in the legend.

    [[`LegendShow.Auto`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Auto "tecplot.constant.LegendShow.Auto"){.reference .internal} (default)

    :   The mapping appears in the legend only when the mapping is
        turned on. If two mappings would result in the same entry in the
        legend, only one entry is shown.

    Type[:]{.colon}

    :   [[`LegendShow`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow "tecplot.constant.LegendShow"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[sort_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.sort_mode "Link to this definition"){.headerlink}

:   Control which [[`Variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to use when sorting lines.

    Possible values: [[`LineMapSort.BySpecificVar`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}, [[`LineMapSort.ByIndependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByIndependentVar "tecplot.constant.LineMapSort.ByIndependentVar"){.reference
    .internal}, [[`LineMapSort.ByDependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByDependentVar "tecplot.constant.LineMapSort.ByDependentVar"){.reference
    .internal} or [[`LineMapSort.None_`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.None_ "tecplot.constant.LineMapSort.None_"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_mode = LineMapSort.ByDependentVar
    :::
    ::::

    Type[:]{.colon}

    :   [[`LineMapSort`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort "tecplot.constant.LineMapSort"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[sort_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.sort_variable "Link to this definition"){.headerlink}

:   Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used when listing lines.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[sort_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.sort_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the specific [[`Variable`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for sorting.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[symbols]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.symbols "Link to this definition"){.headerlink}

:   Style for markers at points along the lines.

    Type[:]{.colon}

    :   [[`LinemapSymbols`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols "tecplot.plot.LinemapSymbols"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[theta_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.theta_axis "Link to this definition"){.headerlink}

:   Angular axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).theta_axis.title = 'angle (deg)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarAngleLineAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.PolarAngleLineAxis "tecplot.plot.PolarAngleLineAxis"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[theta_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.theta_variable "Link to this definition"){.headerlink}

:   :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).theta_variable = dataset.variable('Theta')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[theta_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.theta_variable_index "Link to this definition"){.headerlink}

:   :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} index of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).theta_variable_index = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (Zero-based index)

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[zone]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.zone "Link to this definition"){.headerlink}

:   Data source ([[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}) for
    this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).zone = dataset.zone('Zone 1')
    :::
    ::::

<!-- -->

[[PolarLinemap.]{.pre}]{.sig-prename .descclassname}[[zone_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemap.zone_index "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Zero-based index of the [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} this
    [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will
    draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).zone_index = 2
    :::
    ::::
:::

::: {#polarlinemapcollection .section}
### [PolarLinemapCollection](#id65){.toc-backref role="doc-backlink"}[¶](#polarlinemapcollection "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[PolarLinemapCollection]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#PolarLinemapCollection){.reference .internal}[¶](#tecplot.plot.PolarLinemapCollection "Link to this definition"){.headerlink}

:   Data mapping and style control for one or more polar line plots.

    ::: versionadded
    [New in version 1.1: ]{.versionmodified .added}Linemap collection
    objects.
    :::

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`curve`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.curve "tecplot.plot.PolarLinemapCollection.curve"){.reference .internal}                                                Style and fitting-method control for lines.
      [[`function_dependency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.function_dependency "tecplot.plot.PolarLinemapCollection.function_dependency"){.reference .internal}      The independent variable for function evalulation.
      [[`indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.indices "tecplot.plot.PolarLinemapCollection.indices"){.reference .internal}                                          Object controlling which lines are shown.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.line "tecplot.plot.PolarLinemapCollection.line"){.reference .internal}                                                   Style for lines to be drawn.
      [[`linemap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.linemap_indices "tecplot.plot.PolarLinemapCollection.linemap_indices"){.reference .internal}                  Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.name "tecplot.plot.PolarLinemapCollection.name"){.reference .internal}                                                   Name identifier of this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`r_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.r_axis "tecplot.plot.PolarLinemapCollection.r_axis"){.reference .internal}                                             Radial axis used by this linemap.
      [[`r_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.r_variable "tecplot.plot.PolarLinemapCollection.r_variable"){.reference .internal}                                 [\\(r\\)]{.math .notranslate .nohighlight}-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} of the plotted line.
      [[`r_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.r_variable_index "tecplot.plot.PolarLinemapCollection.r_variable_index"){.reference .internal}               [\\(r\\)]{.math .notranslate .nohighlight}-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} index of the plotted line.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.show "tecplot.plot.PolarLinemapCollection.show"){.reference .internal}                                                   Display this linemap on the plot.
      [[`show_in_legend`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.show_in_legend "tecplot.plot.PolarLinemapCollection.show_in_legend"){.reference .internal}                     Show this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} in the legend.
      [[`sort_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.sort_mode "tecplot.plot.PolarLinemapCollection.sort_mode"){.reference .internal}                                    Control which [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to use when sorting lines.
      [[`sort_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.sort_variable "tecplot.plot.PolarLinemapCollection.sort_variable"){.reference .internal}                        Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used when listing lines.
      [[`sort_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.sort_variable_index "tecplot.plot.PolarLinemapCollection.sort_variable_index"){.reference .internal}      Zero-based index of the specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for sorting.
      [[`symbols`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.symbols "tecplot.plot.PolarLinemapCollection.symbols"){.reference .internal}                                          Style for markers at points along the lines.
      [[`theta_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.theta_axis "tecplot.plot.PolarLinemapCollection.theta_axis"){.reference .internal}                                 Angular axis used by this linemap.
      [[`theta_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.theta_variable "tecplot.plot.PolarLinemapCollection.theta_variable"){.reference .internal}                     :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} of the plotted line.
      [[`theta_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.theta_variable_index "tecplot.plot.PolarLinemapCollection.theta_variable_index"){.reference .internal}   :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} index of the plotted line.
      [[`zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.zone "tecplot.plot.PolarLinemapCollection.zone"){.reference .internal}                                                   [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} of this linemap collection.
      [[`zone_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.PolarLinemapCollection.zone_index "tecplot.plot.PolarLinemapCollection.zone_index"){.reference .internal}                                 [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Zero-based index of the [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will draw.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[curve]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.curve "Link to this definition"){.headerlink}

:   Style and fitting-method control for lines.

    Type[:]{.colon}

    :   [[`LinemapCurve`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapCurve "tecplot.plot.LinemapCurve"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[function_dependency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.function_dependency "Link to this definition"){.headerlink}

:   The independent variable for function evalulation.

    Possible values: [`RIndependent`{.docutils .literal
    .notranslate}]{.pre}, [`ThetaIndependent`{.docutils .literal
    .notranslate}]{.pre}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import FunctionDependency, PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> lmap = plot.linemap(0)
        >>> lmap.function_dependency = FunctionDependency.ThetaIndependent
    :::
    ::::

    Type[:]{.colon}

    :   [[`FunctionDependency`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency "tecplot.constant.FunctionDependency"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.indices "Link to this definition"){.headerlink}

:   Object controlling which lines are shown.

    Type[:]{.colon}

    :   [[`LinemapIndices`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapIndices "tecplot.plot.LinemapIndices"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.line "Link to this definition"){.headerlink}

:   Style for lines to be drawn.

    Type[:]{.colon}

    :   [[`LinemapLine`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapLine "tecplot.plot.LinemapLine"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[linemap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.linemap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.name "Link to this definition"){.headerlink}

:   Name identifier of this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    Names are automatically assigned to each mapping. The nature of the
    name depends on the type of data used to create the mapping. If your
    data has only one dependent variable, the default is to use the zone
    name for the mapping. If your data has multiple dependent variables,
    then the default is to use the dependent variable name for the
    mapping. In either case each mapping is assigned a special name
    ([`&ZN&`{.docutils .literal .notranslate}]{.pre} or
    [`&DN&`{.docutils .literal .notranslate}]{.pre}) that is replaced
    with the zone or variable name when the name is displayed.

    Selecting variables in a 3D finite element zone may require
    significant time, since the variable must be loaded over the entire
    zone. XY and Polar line plots are best used with linear or ordered
    data, or with two-dimensional finite element data.

    Certain placeholder text will be replaced with values based on
    elements within the plot. By combining static text with these
    placeholders, you can construct a name in any format you like:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(2).name = 'Zone: &ZN&'
    :::
    ::::

    The placeholders available are:

    Zone name ([`&ZN&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the zone assigned
        to that mapping.

    Zone number ([`&Z#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the zone
        assigned to the mapping.

    Independent variable name ([`&IV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the independent
        variable assigned to that mapping.

    Independent variable number ([`&I#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the independent
        variable assigned to the mapping.

    Dependent variable name ([`&DV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the dependent
        variable assigned to that mapping.

    Dependent variable number ([`&D#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the dependent
        variable assigned to the mapping.

    Map number ([`&M#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the mapping.

    X-Axis number ([`&X#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the X-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Y-Axis number ([`&Y#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the Y-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[r_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.r_axis "Link to this definition"){.headerlink}

:   Radial axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).r_axis.title = 'distance (m)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`RadialLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.RadialLineAxis "tecplot.plot.RadialLineAxis"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[r_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.r_variable "Link to this definition"){.headerlink}

:   [\\(r\\)]{.math .notranslate .nohighlight}-component
    [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).r_variable = dataset.variable('R')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[r_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.r_variable_index "Link to this definition"){.headerlink}

:   [\\(r\\)]{.math .notranslate .nohighlight}-component
    [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} index of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).r_variable_index = 0
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (Zero-based index)

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.show "Link to this definition"){.headerlink}

:   Display this linemap on the plot.

    Example usage for turning on all linemaps:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemaps().show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[show_in_legend]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.show_in_legend "Link to this definition"){.headerlink}

:   Show this [[Linemaps]{.std .std-ref}](#linemap){.reference
    .internal} in the legend.

    Possible values:

    [[`LegendShow.Always`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Always "tecplot.constant.LegendShow.Always"){.reference .internal}

    :   The mapping appears in the legend even if the mapping is turned
        off (deactivated) or its entry in the table looks exactly like
        another mapping's entry.

    [[`LegendShow.Never`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Never "tecplot.constant.LegendShow.Never"){.reference .internal}

    :   The mapping never appears in the legend.

    [[`LegendShow.Auto`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Auto "tecplot.constant.LegendShow.Auto"){.reference .internal} (default)

    :   The mapping appears in the legend only when the mapping is
        turned on. If two mappings would result in the same entry in the
        legend, only one entry is shown.

    Type[:]{.colon}

    :   [[`LegendShow`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow "tecplot.constant.LegendShow"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[sort_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.sort_mode "Link to this definition"){.headerlink}

:   Control which [[`Variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to use when sorting lines.

    Possible values: [[`LineMapSort.BySpecificVar`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}, [[`LineMapSort.ByIndependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByIndependentVar "tecplot.constant.LineMapSort.ByIndependentVar"){.reference
    .internal}, [[`LineMapSort.ByDependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByDependentVar "tecplot.constant.LineMapSort.ByDependentVar"){.reference
    .internal} or [[`LineMapSort.None_`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.None_ "tecplot.constant.LineMapSort.None_"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_mode = LineMapSort.ByDependentVar
    :::
    ::::

    Type[:]{.colon}

    :   [[`LineMapSort`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort "tecplot.constant.LineMapSort"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[sort_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.sort_variable "Link to this definition"){.headerlink}

:   Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used when listing lines.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[sort_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.sort_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the specific [[`Variable`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for sorting.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[symbols]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.symbols "Link to this definition"){.headerlink}

:   Style for markers at points along the lines.

    Type[:]{.colon}

    :   [[`LinemapSymbols`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols "tecplot.plot.LinemapSymbols"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[theta_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.theta_axis "Link to this definition"){.headerlink}

:   Angular axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).theta_axis.title = 'angle (deg)'
    :::
    ::::

    Type[:]{.colon}

    :   [[`PolarAngleLineAxis`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.PolarAngleLineAxis "tecplot.plot.PolarAngleLineAxis"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[theta_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.theta_variable "Link to this definition"){.headerlink}

:   :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).theta_variable = dataset.variable('Theta')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[theta_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.theta_variable_index "Link to this definition"){.headerlink}

:   :math:\` heta\`-component [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} index of the plotted line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = frame.plot(PlotType.PolarLine)
        >>> plot.linemap(0).theta_variable_index = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (Zero-based index)

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[zone]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.zone "Link to this definition"){.headerlink}

:   [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference
    .internal} of this linemap collection.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print([z.name for z in plot.linemaps().zone])
        ['Zone 1', 'Zone 2']
    :::
    ::::

    ::: versionadded
    [New in version 1.6: ]{.versionmodified .added}Linemap collection
    *zone* property.
    :::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}

<!-- -->

[[PolarLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[zone_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.PolarLinemapCollection.zone_index "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Zero-based index of the [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} this
    [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will
    draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).zone_index = 2
    :::
    ::::
:::

::: {#xylinemap .section}
### [XYLinemap](#id66){.toc-backref role="doc-backlink"}[¶](#xylinemap "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[XYLinemap]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#XYLinemap){.reference .internal}[¶](#tecplot.plot.XYLinemap "Link to this definition"){.headerlink}

:   Data mapping and style control for 2D Cartesian line plots.

    Linemaps connect a specific [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference
    .internal}/[[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} combination to a line or set of lines, depending on the
    dimension of the data if ordered. Linemaps can share any of the axes
    available in the plot and orientation can be verical or horizontal
    by setting the independent variable with
    [[`XYLinemap.function_dependency`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemap.function_dependency "tecplot.plot.XYLinemap.function_dependency"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()

        lmap = plot.linemap(0)
        lmap.line.line_thickness = 0.8
        lmap.line.color = Color.DeepRed
        lmap.y_axis.title.color = Color.DeepRed

        lmap = plot.linemap(1)
        lmap.show = True
        lmap.y_axis_index = 1
        lmap.line.line_thickness = 0.8
        lmap.line.color = Color.Blue
        lmap.y_axis.title.color = lmap.line.color

        tp.export.save_png('linemap_xy.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_xy.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_xy.png" style="width: 300px;"
    alt="../_images/linemap_xy.png" /></a>
    </figure>

    ::: {.admonition .seealso}
    See also

    [[`XYLinemapCollection`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection "tecplot.plot.XYLinemapCollection"){.reference
    .internal}
    :::

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`aux_data`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.aux_data "tecplot.plot.XYLinemap.aux_data"){.reference .internal}                                    Auxiliary data for this linemap.
      [[`bars`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.bars "tecplot.plot.XYLinemap.bars"){.reference .internal}                                                [[`LinemapBars`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars "tecplot.plot.LinemapBars"){.reference .internal} style for bar charts.
      [[`curve`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.curve "tecplot.plot.XYLinemap.curve"){.reference .internal}                                             Style and fitting-method control for lines.
      [[`error_bars`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.error_bars "tecplot.plot.XYLinemap.error_bars"){.reference .internal}                              [[`LinemapErrorBars`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars "tecplot.plot.LinemapErrorBars"){.reference .internal} style for error bars.
      [[`function_dependency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.function_dependency "tecplot.plot.XYLinemap.function_dependency"){.reference .internal}   The independent variable for function evalulation.
      [[`index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.index "tecplot.plot.XYLinemap.index"){.reference .internal}                                             Zero-based integer identifier for this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.indices "tecplot.plot.XYLinemap.indices"){.reference .internal}                                       Object controlling which lines are shown.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.line "tecplot.plot.XYLinemap.line"){.reference .internal}                                                Style for lines to be drawn.
      [[`linemap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.linemap_indices "tecplot.plot.XYLinemap.linemap_indices"){.reference .internal}               Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.name "tecplot.plot.XYLinemap.name"){.reference .internal}                                                Name identifier of this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.show "tecplot.plot.XYLinemap.show"){.reference .internal}                                                Display this linemap on the plot.
      [[`show_in_legend`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.show_in_legend "tecplot.plot.XYLinemap.show_in_legend"){.reference .internal}                  Show this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} in the legend.
      [[`sort_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.sort_mode "tecplot.plot.XYLinemap.sort_mode"){.reference .internal}                                 Control which [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to use when sorting lines.
      [[`sort_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.sort_variable "tecplot.plot.XYLinemap.sort_variable"){.reference .internal}                     Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used when listing lines.
      [[`sort_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.sort_variable_index "tecplot.plot.XYLinemap.sort_variable_index"){.reference .internal}   Zero-based index of the specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for sorting.
      [[`symbols`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.symbols "tecplot.plot.XYLinemap.symbols"){.reference .internal}                                       Style for markers at points along the lines.
      [[`x_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.x_axis "tecplot.plot.XYLinemap.x_axis"){.reference .internal}                                          The X-axis used by this linemap.
      [[`x_axis_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.x_axis_index "tecplot.plot.XYLinemap.x_axis_index"){.reference .internal}                        Zero-based index of the x-axis used by this linemap.
      [[`x_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.x_variable "tecplot.plot.XYLinemap.x_variable"){.reference .internal}                              [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for x-positions of this linemap.
      [[`x_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.x_variable_index "tecplot.plot.XYLinemap.x_variable_index"){.reference .internal}            Zero-based index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for x-positions.
      [[`y_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.y_axis "tecplot.plot.XYLinemap.y_axis"){.reference .internal}                                          Y-axis used by this linemap.
      [[`y_axis_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.y_axis_index "tecplot.plot.XYLinemap.y_axis_index"){.reference .internal}                        Zero-based index of the y-axis used by this linemap.
      [[`y_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.y_variable "tecplot.plot.XYLinemap.y_variable"){.reference .internal}                              [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for y-positions of this linemap.
      [[`y_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.y_variable_index "tecplot.plot.XYLinemap.y_variable_index"){.reference .internal}            Zero-based index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for y-positions.
      [[`zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.zone "tecplot.plot.XYLinemap.zone"){.reference .internal}                                                Data source ([[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal}) for this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`zone_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemap.zone_index "tecplot.plot.XYLinemap.zone_index"){.reference .internal}                              [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Zero-based index of the [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will draw.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[aux_data]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.aux_data "Link to this definition"){.headerlink}

:   Auxiliary data for this linemap.

    Returns: [[`AuxData`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.data.html#tecplot.session.AuxData "tecplot.session.AuxData"){.reference
    .internal}

    This is the auxiliary data attached to the linemap. Such data is
    written to the layout file by default and can be retrieved later.
    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import PlotType
        >>> plot = tp.active_frame().plot(PlotType.XYLine)
        >>> aux = plot.linemap(0).aux_data
        >>> aux['Result'] = '3.14159'
        >>> print(aux['Result'])
        3.14159
    :::
    ::::

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[bars]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.bars "Link to this definition"){.headerlink}

:   [[`LinemapBars`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapBars "tecplot.plot.LinemapBars"){.reference
    .internal} style for bar charts.

    Type[:]{.colon}

    :   [[`LinemapBars`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapBars "tecplot.plot.LinemapBars"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[curve]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.curve "Link to this definition"){.headerlink}

:   Style and fitting-method control for lines.

    Type[:]{.colon}

    :   [[`LinemapCurve`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapCurve "tecplot.plot.LinemapCurve"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[error_bars]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.error_bars "Link to this definition"){.headerlink}

:   [[`LinemapErrorBars`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars "tecplot.plot.LinemapErrorBars"){.reference
    .internal} style for error bars.

    Type[:]{.colon}

    :   [[`LinemapErrorBars`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars "tecplot.plot.LinemapErrorBars"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[function_dependency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.function_dependency "Link to this definition"){.headerlink}

:   The independent variable for function evalulation.

    Possible values: [[`XIndependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency.XIndependent "tecplot.constant.FunctionDependency.XIndependent"){.reference
    .internal}, [[`YIndependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency.YIndependent "tecplot.constant.FunctionDependency.YIndependent"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import FunctionDependency
        >>> lmap = plot.linemap(0)
        >>> lmap.function_dependency = FunctionDependency.YIndependent
    :::
    ::::

    Type[:]{.colon}

    :   [[`FunctionDependency`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency "tecplot.constant.FunctionDependency"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.index "Link to this definition"){.headerlink}

:   Zero-based integer identifier for this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    Example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> lmap = plot.linemap(1)
        >>> print(lmap.index)
        1
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.indices "Link to this definition"){.headerlink}

:   Object controlling which lines are shown.

    Type[:]{.colon}

    :   [[`LinemapIndices`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapIndices "tecplot.plot.LinemapIndices"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.line "Link to this definition"){.headerlink}

:   Style for lines to be drawn.

    Type[:]{.colon}

    :   [[`LinemapLine`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapLine "tecplot.plot.LinemapLine"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[linemap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.linemap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.name "Link to this definition"){.headerlink}

:   Name identifier of this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    Names are automatically assigned to each mapping. The nature of the
    name depends on the type of data used to create the mapping. If your
    data has only one dependent variable, the default is to use the zone
    name for the mapping. If your data has multiple dependent variables,
    then the default is to use the dependent variable name for the
    mapping. In either case each mapping is assigned a special name
    ([`&ZN&`{.docutils .literal .notranslate}]{.pre} or
    [`&DN&`{.docutils .literal .notranslate}]{.pre}) that is replaced
    with the zone or variable name when the name is displayed.

    Selecting variables in a 3D finite element zone may require
    significant time, since the variable must be loaded over the entire
    zone. XY and Polar line plots are best used with linear or ordered
    data, or with two-dimensional finite element data.

    Certain placeholder text will be replaced with values based on
    elements within the plot. By combining static text with these
    placeholders, you can construct a name in any format you like:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(2).name = 'Zone: &ZN&'
    :::
    ::::

    The placeholders available are:

    Zone name ([`&ZN&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the zone assigned
        to that mapping.

    Zone number ([`&Z#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the zone
        assigned to the mapping.

    Independent variable name ([`&IV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the independent
        variable assigned to that mapping.

    Independent variable number ([`&I#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the independent
        variable assigned to the mapping.

    Dependent variable name ([`&DV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the dependent
        variable assigned to that mapping.

    Dependent variable number ([`&D#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the dependent
        variable assigned to the mapping.

    Map number ([`&M#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the mapping.

    X-Axis number ([`&X#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the X-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Y-Axis number ([`&Y#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the Y-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.show "Link to this definition"){.headerlink}

:   Display this linemap on the plot.

    Example usage for turning on all linemaps:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> for lmap in plot.linemaps():
        ...     lmap.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[show_in_legend]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.show_in_legend "Link to this definition"){.headerlink}

:   Show this [[Linemaps]{.std .std-ref}](#linemap){.reference
    .internal} in the legend.

    Possible values:

    [[`LegendShow.Always`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Always "tecplot.constant.LegendShow.Always"){.reference .internal}

    :   The mapping appears in the legend even if the mapping is turned
        off (deactivated) or its entry in the table looks exactly like
        another mapping's entry.

    [[`LegendShow.Never`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Never "tecplot.constant.LegendShow.Never"){.reference .internal}

    :   The mapping never appears in the legend.

    [[`LegendShow.Auto`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Auto "tecplot.constant.LegendShow.Auto"){.reference .internal} (default)

    :   The mapping appears in the legend only when the mapping is
        turned on. If two mappings would result in the same entry in the
        legend, only one entry is shown.

    Type[:]{.colon}

    :   [[`LegendShow`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow "tecplot.constant.LegendShow"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[sort_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.sort_mode "Link to this definition"){.headerlink}

:   Control which [[`Variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to use when sorting lines.

    Possible values: [[`LineMapSort.BySpecificVar`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}, [[`LineMapSort.ByIndependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByIndependentVar "tecplot.constant.LineMapSort.ByIndependentVar"){.reference
    .internal}, [[`LineMapSort.ByDependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByDependentVar "tecplot.constant.LineMapSort.ByDependentVar"){.reference
    .internal} or [[`LineMapSort.None_`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.None_ "tecplot.constant.LineMapSort.None_"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_mode = LineMapSort.ByDependentVar
    :::
    ::::

    Type[:]{.colon}

    :   [[`LineMapSort`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort "tecplot.constant.LineMapSort"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[sort_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.sort_variable "Link to this definition"){.headerlink}

:   Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used when listing lines.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[sort_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.sort_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the specific [[`Variable`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for sorting.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[symbols]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.symbols "Link to this definition"){.headerlink}

:   Style for markers at points along the lines.

    Type[:]{.colon}

    :   [[`LinemapSymbols`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols "tecplot.plot.LinemapSymbols"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[x_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.x_axis "Link to this definition"){.headerlink}

:   The X-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_axis = plot.axes.x_axis(2)
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[x_axis_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.x_axis_index "Link to this definition"){.headerlink}

:   Zero-based index of the x-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_axis_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[x_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.x_variable "Link to this definition"){.headerlink}

:   [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for x-positions of this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[x_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.x_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for x-positions.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_variable_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[y_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.y_axis "Link to this definition"){.headerlink}

:   Y-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_axis = plot.axes.y_axis(2)
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[y_axis_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.y_axis_index "Link to this definition"){.headerlink}

:   Zero-based index of the y-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).y_axis_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[y_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.y_variable "Link to this definition"){.headerlink}

:   [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for y-positions of this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).y_variable = dataset.variable('Q')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[y_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.y_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for y-positions.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).y_variable_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[zone]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.zone "Link to this definition"){.headerlink}

:   Data source ([[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}) for
    this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).zone = dataset.zone('Zone 1')
    :::
    ::::

<!-- -->

[[XYLinemap.]{.pre}]{.sig-prename .descclassname}[[zone_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemap.zone_index "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Zero-based index of the [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} this
    [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will
    draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).zone_index = 2
    :::
    ::::
:::

::: {#xylinemapcollection .section}
### [XYLinemapCollection](#id67){.toc-backref role="doc-backlink"}[¶](#xylinemapcollection "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[XYLinemapCollection]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*, *[[\*]{.pre}]{.o}[[indices]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#XYLinemapCollection){.reference .internal}[¶](#tecplot.plot.XYLinemapCollection "Link to this definition"){.headerlink}

:   Data mapping and style control for one or more line plots.

    This class behaves like [[`XYLinemap`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
    .internal} except that setting any underlying style will do so for
    all of the represented linemaps. The style properties are then
    always returned as a [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external} of properties, one for each linemap, ordered by index
    number. This means there is an asymmetry between setting and getting
    any property under this object, illustrated by the following
    example:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> lmaps = plot.linemaps(0, 1, 2)
        >>> lmaps.show = True
        >>> print(lmaps.show)
        (True, True, True)
    :::
    ::::

    This is the preferred way to control the style of many linemaps as
    it is much faster to execute. All examples that set style on a
    single linemap like the following:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).line.color = Color.Blue
    :::
    ::::

    may be converted to setting the same style on all linemaps like so:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemaps().line.color = Color.Blue
    :::
    ::::

    ::: versionadded
    [New in version 1.1: ]{.versionmodified .added}Linemap collection
    objects.
    :::

    The Linemap layer controls how ordered or connected data is
    represented. This may be either a set of line segments connecting
    all the data points, or a curve fitted to the original data. This
    object represents one or more linemaps and can conveniently control
    the style for each one.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, LinePattern, AxisTitleMode

        # load data from examples directory
        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        # get handle to the active frame and set plot type to XY Line
        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()

        # We will set the name, color and a few other properties
        # for the first three linemaps in the dataset.
        names = ['Seattle', 'Dallas', 'Miami']
        colors = [Color.Blue, Color.DeepRed, Color.Khaki]

        lmaps = plot.linemaps()

        # set common style for all linemaps in the collection
        lmaps.show = True
        lmaps.line.line_thickness = 1
        lmaps.line.line_pattern = LinePattern.LongDash
        lmaps.line.pattern_length = 2

        # loop over the linemaps, setting name and color for each
        for lmap, name, color in zip(lmaps, names, colors):
            lmap.name = name
            lmap.line.color = color

        # Set the y-axis label
        plot.axes.y_axis(0).title.title_mode = AxisTitleMode.UseText
        plot.axes.y_axis(0).title.text = 'Rainfall'

        # Turn on legend
        plot.legend.show = True

        # Adjust the axes limits to show all the data
        plot.view.fit()

        # save image to file
        tp.export.save_png('linemap.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap.png"
    class="reference internal image-reference"><img
    src="../_images/linemap.png" style="width: 300px;"
    alt="../_images/linemap.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`bars`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.bars "tecplot.plot.XYLinemapCollection.bars"){.reference .internal}                                                [[`LinemapBars`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars "tecplot.plot.LinemapBars"){.reference .internal} style for bar charts.
      [[`curve`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.curve "tecplot.plot.XYLinemapCollection.curve"){.reference .internal}                                             Style and fitting-method control for lines.
      [[`error_bars`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.error_bars "tecplot.plot.XYLinemapCollection.error_bars"){.reference .internal}                              [[`LinemapErrorBars`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars "tecplot.plot.LinemapErrorBars"){.reference .internal} style for error bars.
      [[`function_dependency`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.function_dependency "tecplot.plot.XYLinemapCollection.function_dependency"){.reference .internal}   The independent variable for function evalulation.
      [[`indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.indices "tecplot.plot.XYLinemapCollection.indices"){.reference .internal}                                       Object controlling which lines are shown.
      [[`line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.line "tecplot.plot.XYLinemapCollection.line"){.reference .internal}                                                Style for lines to be drawn.
      [[`linemap_indices`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.linemap_indices "tecplot.plot.XYLinemapCollection.linemap_indices"){.reference .internal}               Read-only, sorted [[`list`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference .external} of zero-based fieldmap indices.
      [[`name`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.name "tecplot.plot.XYLinemapCollection.name"){.reference .internal}                                                Name identifier of this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.show "tecplot.plot.XYLinemapCollection.show"){.reference .internal}                                                Display this linemap on the plot.
      [[`show_in_legend`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.show_in_legend "tecplot.plot.XYLinemapCollection.show_in_legend"){.reference .internal}                  Show this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} in the legend.
      [[`sort_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.sort_mode "tecplot.plot.XYLinemapCollection.sort_mode"){.reference .internal}                                 Control which [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to use when sorting lines.
      [[`sort_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.sort_variable "tecplot.plot.XYLinemapCollection.sort_variable"){.reference .internal}                     Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used when listing lines.
      [[`sort_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.sort_variable_index "tecplot.plot.XYLinemapCollection.sort_variable_index"){.reference .internal}   Zero-based index of the specific [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for sorting.
      [[`symbols`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.symbols "tecplot.plot.XYLinemapCollection.symbols"){.reference .internal}                                       Style for markers at points along the lines.
      [[`x_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.x_axis "tecplot.plot.XYLinemapCollection.x_axis"){.reference .internal}                                          The X-axis used by this linemap.
      [[`x_axis_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.x_axis_index "tecplot.plot.XYLinemapCollection.x_axis_index"){.reference .internal}                        Zero-based index of the x-axis used by this linemap.
      [[`x_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.x_variable "tecplot.plot.XYLinemapCollection.x_variable"){.reference .internal}                              [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for x-positions of this linemap.
      [[`x_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.x_variable_index "tecplot.plot.XYLinemapCollection.x_variable_index"){.reference .internal}            Zero-based index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for x-positions.
      [[`y_axis`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.y_axis "tecplot.plot.XYLinemapCollection.y_axis"){.reference .internal}                                          Y-axis used by this linemap.
      [[`y_axis_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.y_axis_index "tecplot.plot.XYLinemapCollection.y_axis_index"){.reference .internal}                        Zero-based index of the y-axis used by this linemap.
      [[`y_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.y_variable "tecplot.plot.XYLinemapCollection.y_variable"){.reference .internal}                              [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for y-positions of this linemap.
      [[`y_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.y_variable_index "tecplot.plot.XYLinemapCollection.y_variable_index"){.reference .internal}            Zero-based index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} used for y-positions.
      [[`zone`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.zone "tecplot.plot.XYLinemapCollection.zone"){.reference .internal}                                                [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} of this linemap collection.
      [[`zone_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.XYLinemapCollection.zone_index "tecplot.plot.XYLinemapCollection.zone_index"){.reference .internal}                              [[`int`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference .external}: Zero-based index of the [[Zone]{.std .std-ref}](tecplot.data.html#data-access){.reference .internal} this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will draw.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[bars]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.bars "Link to this definition"){.headerlink}

:   [[`LinemapBars`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapBars "tecplot.plot.LinemapBars"){.reference
    .internal} style for bar charts.

    Type[:]{.colon}

    :   [[`LinemapBars`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapBars "tecplot.plot.LinemapBars"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[curve]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.curve "Link to this definition"){.headerlink}

:   Style and fitting-method control for lines.

    Type[:]{.colon}

    :   [[`LinemapCurve`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapCurve "tecplot.plot.LinemapCurve"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[error_bars]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.error_bars "Link to this definition"){.headerlink}

:   [[`LinemapErrorBars`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars "tecplot.plot.LinemapErrorBars"){.reference
    .internal} style for error bars.

    Type[:]{.colon}

    :   [[`LinemapErrorBars`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars "tecplot.plot.LinemapErrorBars"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[function_dependency]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.function_dependency "Link to this definition"){.headerlink}

:   The independent variable for function evalulation.

    Possible values: [[`XIndependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency.XIndependent "tecplot.constant.FunctionDependency.XIndependent"){.reference
    .internal}, [[`YIndependent`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency.YIndependent "tecplot.constant.FunctionDependency.YIndependent"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import FunctionDependency
        >>> lmap = plot.linemap(0)
        >>> lmap.function_dependency = FunctionDependency.YIndependent
    :::
    ::::

    Type[:]{.colon}

    :   [[`FunctionDependency`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FunctionDependency "tecplot.constant.FunctionDependency"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.indices "Link to this definition"){.headerlink}

:   Object controlling which lines are shown.

    Type[:]{.colon}

    :   [[`LinemapIndices`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapIndices "tecplot.plot.LinemapIndices"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.line "Link to this definition"){.headerlink}

:   Style for lines to be drawn.

    Type[:]{.colon}

    :   [[`LinemapLine`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapLine "tecplot.plot.LinemapLine"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[linemap_indices]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.linemap_indices "Link to this definition"){.headerlink}

:   Read-only, sorted [[`list`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
    .external} of zero-based fieldmap indices.

    Type[:]{.colon}

    :   [[`list`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[name]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.name "Link to this definition"){.headerlink}

:   Name identifier of this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    Names are automatically assigned to each mapping. The nature of the
    name depends on the type of data used to create the mapping. If your
    data has only one dependent variable, the default is to use the zone
    name for the mapping. If your data has multiple dependent variables,
    then the default is to use the dependent variable name for the
    mapping. In either case each mapping is assigned a special name
    ([`&ZN&`{.docutils .literal .notranslate}]{.pre} or
    [`&DN&`{.docutils .literal .notranslate}]{.pre}) that is replaced
    with the zone or variable name when the name is displayed.

    Selecting variables in a 3D finite element zone may require
    significant time, since the variable must be loaded over the entire
    zone. XY and Polar line plots are best used with linear or ordered
    data, or with two-dimensional finite element data.

    Certain placeholder text will be replaced with values based on
    elements within the plot. By combining static text with these
    placeholders, you can construct a name in any format you like:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(2).name = 'Zone: &ZN&'
    :::
    ::::

    The placeholders available are:

    Zone name ([`&ZN&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the zone assigned
        to that mapping.

    Zone number ([`&Z#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the zone
        assigned to the mapping.

    Independent variable name ([`&IV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the independent
        variable assigned to that mapping.

    Independent variable number ([`&I#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the independent
        variable assigned to the mapping.

    Dependent variable name ([`&DV&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual name of the dependent
        variable assigned to that mapping.

    Dependent variable number ([`&D#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the dependent
        variable assigned to the mapping.

    Map number ([`&M#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the mapping.

    X-Axis number ([`&X#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the X-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Y-Axis number ([`&Y#&`{.docutils .literal .notranslate}]{.pre})

    :   This will be replaced with the actual number of the Y-axis
        assigned to that mapping for XY Line plots. This option is not
        available for Polar Line plots.

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.show "Link to this definition"){.headerlink}

:   Display this linemap on the plot.

    Example usage for turning on all linemaps:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemaps().show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[show_in_legend]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.show_in_legend "Link to this definition"){.headerlink}

:   Show this [[Linemaps]{.std .std-ref}](#linemap){.reference
    .internal} in the legend.

    Possible values:

    [[`LegendShow.Always`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Always "tecplot.constant.LegendShow.Always"){.reference .internal}

    :   The mapping appears in the legend even if the mapping is turned
        off (deactivated) or its entry in the table looks exactly like
        another mapping's entry.

    [[`LegendShow.Never`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Never "tecplot.constant.LegendShow.Never"){.reference .internal}

    :   The mapping never appears in the legend.

    [[`LegendShow.Auto`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow.Auto "tecplot.constant.LegendShow.Auto"){.reference .internal} (default)

    :   The mapping appears in the legend only when the mapping is
        turned on. If two mappings would result in the same entry in the
        legend, only one entry is shown.

    Type[:]{.colon}

    :   [[`LegendShow`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LegendShow "tecplot.constant.LegendShow"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[sort_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.sort_mode "Link to this definition"){.headerlink}

:   Control which [[`Variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to use when sorting lines.

    Possible values: [[`LineMapSort.BySpecificVar`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}, [[`LineMapSort.ByIndependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByIndependentVar "tecplot.constant.LineMapSort.ByIndependentVar"){.reference
    .internal}, [[`LineMapSort.ByDependentVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.ByDependentVar "tecplot.constant.LineMapSort.ByDependentVar"){.reference
    .internal} or [[`LineMapSort.None_`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.None_ "tecplot.constant.LineMapSort.None_"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_mode = LineMapSort.ByDependentVar
    :::
    ::::

    Type[:]{.colon}

    :   [[`LineMapSort`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort "tecplot.constant.LineMapSort"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[sort_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.sort_variable "Link to this definition"){.headerlink}

:   Specific [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used when listing lines.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[sort_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.sort_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the specific [[`Variable`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for sorting.

    The [`sort_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`LineMapSort.BySpecificVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LineMapSort.BySpecificVar "tecplot.constant.LineMapSort.BySpecificVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LineMapSort
        >>> plot.linemap(0).sort_by = LineMapSort.BySpecificVar
        >>> plot.linemap(0).sort_variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[symbols]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.symbols "Link to this definition"){.headerlink}

:   Style for markers at points along the lines.

    Type[:]{.colon}

    :   [[`LinemapSymbols`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols "tecplot.plot.LinemapSymbols"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[x_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.x_axis "Link to this definition"){.headerlink}

:   The X-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_axis = plot.axes.x_axis(2)
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[x_axis_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.x_axis_index "Link to this definition"){.headerlink}

:   Zero-based index of the x-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_axis_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[x_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.x_variable "Link to this definition"){.headerlink}

:   [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for x-positions of this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[x_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.x_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for x-positions.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_variable_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[y_axis]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.y_axis "Link to this definition"){.headerlink}

:   Y-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).x_axis = plot.axes.y_axis(2)
    :::
    ::::

    Type[:]{.colon}

    :   [[`XYLineAxis`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.axes.html#tecplot.plot.XYLineAxis "tecplot.plot.XYLineAxis"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[y_axis_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.y_axis_index "Link to this definition"){.headerlink}

:   Zero-based index of the y-axis used by this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).y_axis_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[y_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.y_variable "Link to this definition"){.headerlink}

:   [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for y-positions of this linemap.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).y_variable = dataset.variable('Q')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[y_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.y_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} used for y-positions.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).y_variable_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[zone]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.zone "Link to this definition"){.headerlink}

:   [[Zones]{.std .std-ref}](tecplot.data.html#data-access){.reference
    .internal} of this linemap collection.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print([z.name for z in plot.linemaps().zone])
        ['Zone 1', 'Zone 2']
    :::
    ::::

    ::: versionadded
    [New in version 1.6: ]{.versionmodified .added}Linemap collection
    *zone* property.
    :::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[Zones]{.std
        .std-ref}](tecplot.data.html#data-access){.reference .internal}

<!-- -->

[[XYLinemapCollection.]{.pre}]{.sig-prename .descclassname}[[zone_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.XYLinemapCollection.zone_index "Link to this definition"){.headerlink}

:   [[`int`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
    .external}: Zero-based index of the [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal} this
    [[Linemaps]{.std .std-ref}](#linemap){.reference .internal} will
    draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).zone_index = 2
    :::
    ::::
:::

::: {#linemapline .section}
### [LinemapLine](#id68){.toc-backref role="doc-backlink"}[¶](#linemapline "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[LinemapLine]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[linemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapLine){.reference .internal}[¶](#tecplot.plot.LinemapLine "Link to this definition"){.headerlink}

:   Style control for the line to be drawn.

    This controls the style of the lines plotted for a given
    [[`XYLinemap`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, LinePattern

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()

        lmap = plot.linemap(0)

        line = lmap.line
        line.color = Color.Blue
        line.line_thickness = 1
        line.line_pattern = LinePattern.LongDash
        line.pattern_length = 2

        tp.export.save_png('linemap_line.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_line.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_line.png" style="width: 300px;"
    alt="../_images/linemap_line.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapLine.color "tecplot.plot.LinemapLine.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the line to be drawn.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapLine.line_pattern "tecplot.plot.LinemapLine.line_pattern"){.reference .internal}         Pattern style of the line to be drawn.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapLine.line_thickness "tecplot.plot.LinemapLine.line_thickness"){.reference .internal}   Width of the line to be drawn.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapLine.pattern_length "tecplot.plot.LinemapLine.pattern_length"){.reference .internal}   Segment length of the repeated line pattern.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapLine.show "tecplot.plot.LinemapLine.show"){.reference .internal}                                 Display this point-to-point line on the plot.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[LinemapLine.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapLine.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the line to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.linemap(0).line.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[LinemapLine.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapLine.line_pattern "Link to this definition"){.headerlink}

:   Pattern style of the line to be drawn.

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
        >>> lmap = plot.linemap(0)
        >>> lmap.line.line_pattern = LinePattern.LongDash
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[LinemapLine.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapLine.line_thickness "Link to this definition"){.headerlink}

:   Width of the line to be drawn.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).line.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapLine.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapLine.pattern_length "Link to this definition"){.headerlink}

:   Segment length of the repeated line pattern.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> lmap = plot.linemap(0)
        >>> lmap.line.line_pattern = LinePattern.LongDash
        >>> lmap.line.pattern_length = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapLine.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapLine.show "Link to this definition"){.headerlink}

:   Display this point-to-point line on the plot.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).line.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::

::: {#linemapcurve .section}
### [LinemapCurve](#id69){.toc-backref role="doc-backlink"}[¶](#linemapcurve "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[LinemapCurve]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[linemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapCurve){.reference .internal}[¶](#tecplot.plot.LinemapCurve "Link to this definition"){.headerlink}

:   Curve-fitting of the line.

    This class controls how the line is to be drawn between data points.
    By default, the [[`CurveType.LineSeg`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.LineSeg "tecplot.constant.CurveType.LineSeg"){.reference
    .internal} option is used and straight lines are used. Setting
    [[`curve_type`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.curve_type "tecplot.plot.LinemapCurve.curve_type"){.reference
    .internal} to a fit type or spline type will replace the line
    segments with a smooth curve:

    :::: {.highlight-python .notranslate}
    ::: highlight
        import numpy as np
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, CurveType

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)
        dataset.add_variable('Weight')

        # convert error to weighting to be used for fitting below
        # This converts the error to  (1 / error)
        # and normalizes to the range [1,100]
        zone = dataset.zone('ZONE 1')
        err1 = zone.values('Error 1')
        wvar = zone.values('Weight')
        err = err1.as_numpy_array()
        sigma = 1. / err
        dsigma = sigma.max() - sigma.min()
        sigma = (99 * (sigma - sigma.min()) / dsigma) + 1
        wvar[:] = sigma

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()

        lmaps = plot.linemaps()

        lmaps.show = True
        lmaps.x_variable = dataset.variable(0)

        for lmap, var in zip(lmaps, list(dataset.variables())[1:4]):
            lmap.y_variable = var

        curves = [lmap.curve for lmap in plot.linemaps()]

        curves[0].curve_type = CurveType.PolynomialFit
        curves[0].num_points = 1000
        curves[0].polynomial_order = 10

        curves[1].curve_type = CurveType.PowerFit
        curves[1].use_fit_range = True
        curves[1].fit_range = 4,8
        curves[1].weight_variable = dataset.variable('Weight')
        curves[1].use_weight_variable = True

        curves[2].curve_type = CurveType.Spline
        curves[2].clamp_spline = True
        curves[2].spline_derivative_at_ends = 0,0

        tp.export.save_png('linemap_curve.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_curve.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_curve.png" style="width: 300px;"
    alt="../_images/linemap_curve.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------
      [[`clamp_spline`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.clamp_spline "tecplot.plot.LinemapCurve.clamp_spline"){.reference .internal}                                          Enable derivative clamping for spline fits.
      [[`curve_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.curve_type "tecplot.plot.LinemapCurve.curve_type"){.reference .internal}                                                Type of curve to draw or fit.
      [[`fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.fit_range "tecplot.plot.LinemapCurve.fit_range"){.reference .internal}                                                   The range to fit and display a fitted curve.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.num_points "tecplot.plot.LinemapCurve.num_points"){.reference .internal}                                                Number of points to use when drawing a fitted curve.
      [[`polynomial_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.polynomial_order "tecplot.plot.LinemapCurve.polynomial_order"){.reference .internal}                              Order of the fit when set to polynomial.
      [[`spline_derivative_at_ends`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.spline_derivative_at_ends "tecplot.plot.LinemapCurve.spline_derivative_at_ends"){.reference .internal}   Clamp the derivative of the spline fit at the edges of the range.
      [[`use_fit_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.use_fit_range "tecplot.plot.LinemapCurve.use_fit_range"){.reference .internal}                                       Limit the fit to the [`fit_range`{.docutils .literal .notranslate}]{.pre} specified.
      [[`use_weight_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.use_weight_variable "tecplot.plot.LinemapCurve.use_weight_variable"){.reference .internal}                     Use the specified variable for curve-fit weighting.
      [[`weight_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.weight_variable "tecplot.plot.LinemapCurve.weight_variable"){.reference .internal}                                 Variable to use for curve-fit weighting.
      [[`weight_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.weight_variable_index "tecplot.plot.LinemapCurve.weight_variable_index"){.reference .internal}               Zero-based index of the variable to use for curve-fit weighting.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[clamp_spline]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.clamp_spline "Link to this definition"){.headerlink}

:   Enable derivative clamping for spline fits.

    Example showing how to set the derivative at the limits of a spline
    curve to zero:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.Spline
        >>> curve.clamp_spline = True
        >>> curve.spline_derivative_at_ends = 0, 0
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[curve_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.curve_type "Link to this definition"){.headerlink}

:   Type of curve to draw or fit.

    Possible values: [[`LineSeg`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.LineSeg "tecplot.constant.CurveType.LineSeg"){.reference
    .internal}, [[`PolynomialFit`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.PolynomialFit "tecplot.constant.CurveType.PolynomialFit"){.reference
    .internal}, [[`EToRFit`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.EToRFit "tecplot.constant.CurveType.EToRFit"){.reference
    .internal}, [[`PowerFit`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.PowerFit "tecplot.constant.CurveType.PowerFit"){.reference
    .internal}, [[`Spline`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.Spline "tecplot.constant.CurveType.Spline"){.reference
    .internal}, [[`ParaSpline`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.ParaSpline "tecplot.constant.CurveType.ParaSpline"){.reference
    .internal}.

    [[`CurveType.LineSeg`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.LineSeg "tecplot.constant.CurveType.LineSeg"){.reference .internal} (line segment, no curve-fit)

    :   A series of linear segments connect adjacent data points. In XY
        Line plots, these will be line segments.

    [[`CurveType.PolynomialFit`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.PolynomialFit "tecplot.constant.CurveType.PolynomialFit"){.reference .internal}

    :   A polynomial of order [[`LinemapCurve.polynomial_order`{.xref
        .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapCurve.polynomial_order "tecplot.plot.LinemapCurve.polynomial_order"){.reference
        .internal} is fit to the data points where [\\(1 \<= N \<=
        10\\)]{.math .notranslate .nohighlight}. [\\(N = 1\\)]{.math
        .notranslate .nohighlight} is a straight-line fit.

    [[`CurveType.EToRFit`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.EToRFit "tecplot.constant.CurveType.EToRFit"){.reference .internal} (exponential curve-fit)

    :   An exponential curve-fit that finds the best curve of the form
        [\\(Y = e\^{b\\cdot X+c}\\)]{.math .notranslate .nohighlight}
        which is equivalent to [\\(Y = a\\cdot e\^{b\\cdot X}\\)]{.math
        .notranslate .nohighlight}, where [\\(a = e\^c\\)]{.math
        .notranslate .nohighlight}. To use this curve type, *Y*-values
        for this variable must be all positive or all negative. If the
        function dependency is set to [\\(X = f(Y)\\)]{.math
        .notranslate .nohighlight} all *X*-values must be all positive
        or all negative.

    [[`CurveType.PowerFit`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.PowerFit "tecplot.constant.CurveType.PowerFit"){.reference .internal}

    :   A power curve fit that finds the best curve of the form [\\(Y =
        e\^{b \\cdot \\ln X + c}\\)]{.math .notranslate .nohighlight}
        which is equivalent to [\\(Y = a\\cdot X\^b\\)]{.math
        .notranslate .nohighlight} , where [\\(a = e\^c\\)]{.math
        .notranslate .nohighlight}. To use this curve type, *Y*-values
        for this variable must be all positive or all negative;
        *X*-values must be all positive. If the function dependency is
        set to [\\(X = f(Y)\\)]{.math .notranslate .nohighlight},
        *X*-values must be all positive or all negative, and the
        *Y*-values must all be positive.

    [[`CurveType.Spline`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.Spline "tecplot.constant.CurveType.Spline"){.reference .internal}

    :   A smooth curve is generated that goes through every point. The
        spline is drawn through the data points after sorting the points
        into increasing values of the independent variable, resulting in
        a single-valued function of the independent variable. The spline
        may be clamped or free. With a clamped spline, you supply the
        derivative of the function at each end point; with a non-clamped
        (natural or free) spline, these derivatives are determined for
        you. In xy-line plots, specifying the derivative gives you
        control over the initial and final slopes of the curve.

    [[`CurveType.ParaSpline`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.ParaSpline "tecplot.constant.CurveType.ParaSpline"){.reference .internal} (parametric spline)

    :   Creates a smooth curve as with a spline, except the assumption
        is that both variables are functions of the index of the data
        points. For example in xy-line plot, [[`ParaSpline`{.xref .any
        .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType.ParaSpline "tecplot.constant.CurveType.ParaSpline"){.reference
        .internal} fits [\\(x = f(i)\\)]{.math .notranslate
        .nohighlight} and [\\(y=g(i)\\)]{.math .notranslate
        .nohighlight} where [\\(f()\\)]{.math .notranslate .nohighlight}
        and [\\(g()\\)]{.math .notranslate .nohighlight} are both
        smooth. No additional sorting of the points is performed. This
        spline may result in a multi-valued function of either or both
        axis variables.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> plot.linemap(0).curve.curve_type = CurveType.PolynomialFit
    :::
    ::::

    Type[:]{.colon}

    :   [[`CurveType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CurveType "tecplot.constant.CurveType"){.reference
        .internal}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[fit_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.fit_range "Link to this definition"){.headerlink}

:   The range to fit and display a fitted curve.

    Example showing how to set the limits of a polynomial fit to
    \[5,10\]. The [`use_fit_range`{.docutils .literal
    .notranslate}]{.pre} attribute must be set to [[`True`{.xref .any
    .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.use_fit_range = True
        >>> curve.fit_range = 5, 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.num_points "Link to this definition"){.headerlink}

:   Number of points to use when drawing a fitted curve.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.num_points = 100
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[polynomial_order]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.polynomial_order "Link to this definition"){.headerlink}

:   Order of the fit when set to polynomial.

    A value of 1 will fit the data to a straight line. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.polynomial_order = 4
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (1 to 10)

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[spline_derivative_at_ends]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.spline_derivative_at_ends "Link to this definition"){.headerlink}

:   Clamp the derivative of the spline fit at the edges of the range.

    Example showing how to set the derivative at the limits of a spline
    curve to zero. Notice the [`clamp_spline`{.docutils .literal
    .notranslate}]{.pre} attribute must be set to [[`True`{.xref .any
    .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.Spline
        >>> curve.clamp_spline = True
        >>> curve.spline_derivative_at_ends = 0, 0
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[use_fit_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.use_fit_range "Link to this definition"){.headerlink}

:   Limit the fit to the [`fit_range`{.docutils .literal
    .notranslate}]{.pre} specified.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.use_fit_range = True
        >>> curve.fit_range = 5, 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[use_weight_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.use_weight_variable "Link to this definition"){.headerlink}

:   Use the specified variable for curve-fit weighting.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.use_weight_variable = True
        >>> curve.weight_variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[weight_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.weight_variable "Link to this definition"){.headerlink}

:   Variable to use for curve-fit weighting.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.use_weight_variable = True
        >>> curve.weight_variable = dataset.variable('P')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[LinemapCurve.]{.pre}]{.sig-prename .descclassname}[[weight_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapCurve.weight_variable_index "Link to this definition"){.headerlink}

:   Zero-based index of the variable to use for curve-fit weighting.

    The [`use_weight_variable`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CurveType
        >>> curve = plot.linemap(0).curve
        >>> curve.curve_type = CurveType.PolynomialFit
        >>> curve.use_weight_variable = True
        >>> curve.weight_variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}
:::

::: {#linemapbars .section}
### [LinemapBars](#id70){.toc-backref role="doc-backlink"}[¶](#linemapbars "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[LinemapBars]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[linemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapBars){.reference .internal}[¶](#tecplot.plot.LinemapBars "Link to this definition"){.headerlink}

:   Bar chart style control.

    A bar chart is an XY Line plot that uses vertical or horizontal bars
    placed along an axis to represent data points. Changing the function
    dependency of the linemap with
    [[`XYLinemap.function_dependency`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemap.function_dependency "tecplot.plot.XYLinemap.function_dependency"){.reference
    .internal} controls the direction of the bars. By default, all
    mappings use [\\(y = f(x)\\)]{.math .notranslate .nohighlight} and
    appear as vertical bar charts. Setting *y* to be the independent
    variable will cause the bars to be horizontal:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()
        plot.show_bars = True

        lmap = plot.linemap(0)

        bars = lmap.bars
        bars.show = True
        bars.size = 0.6*(100 / dataset.zone(0).num_points)
        bars.fill_color = Color.Red
        bars.line_color = Color.Red
        bars.line_thickness = 0.01

        tp.export.save_png('linemap_bars.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_bars.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_bars.png" style="width: 300px;"
    alt="../_images/linemap_bars.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars.fill_color "tecplot.plot.LinemapBars.fill_color"){.reference .internal}               Fill color of the bars.
      [[`fill_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars.fill_mode "tecplot.plot.LinemapBars.fill_mode"){.reference .internal}                  fill mode for the bars.
      [[`line_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars.line_color "tecplot.plot.LinemapBars.line_color"){.reference .internal}               Edge line color of the bars.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars.line_thickness "tecplot.plot.LinemapBars.line_thickness"){.reference .internal}   Edge line thickness of the bars.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars.show "tecplot.plot.LinemapBars.show"){.reference .internal}                                 Display bars on the plot for this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapBars.size "tecplot.plot.LinemapBars.size"){.reference .internal}                                 Width of the bars.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------

<!-- -->

[[LinemapBars.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapBars.fill_color "Link to this definition"){.headerlink}

:   Fill color of the bars.

    The [`fill_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`FillMode.UseSpecificColor`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseSpecificColor "tecplot.constant.FillMode.UseSpecificColor"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, FillMode
        >>> bars = plot.linemap(0).bars
        >>> bars.fill_mode = FillMode.UseSpecificColor
        >>> bars.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal} or [[`ContourGroup`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.plot_style.html#tecplot.plot.ContourGroup "tecplot.plot.ContourGroup"){.reference
        .internal}.

<!-- -->

[[LinemapBars.]{.pre}]{.sig-prename .descclassname}[[fill_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapBars.fill_mode "Link to this definition"){.headerlink}

:   fill mode for the bars.

    Possible values: [[`FillMode.UseSpecificColor`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseSpecificColor "tecplot.constant.FillMode.UseSpecificColor"){.reference .internal}, [[`FillMode.UseLineColor`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseLineColor "tecplot.constant.FillMode.UseLineColor"){.reference .internal},

    :   [[`FillMode.UseBackgroundColor`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseBackgroundColor "tecplot.constant.FillMode.UseBackgroundColor"){.reference
        .internal} or [[`FillMode.None_`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.None_ "tecplot.constant.FillMode.None_"){.reference
        .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import FillMode
        >>> bars = plot.linemap(0).bars
        >>> bars.fill_mode = FillMode.UseBackgroundColor
    :::
    ::::

    Type[:]{.colon}

    :   [[`FillMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode "tecplot.constant.FillMode"){.reference
        .internal}

<!-- -->

[[LinemapBars.]{.pre}]{.sig-prename .descclassname}[[line_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapBars.line_color "Link to this definition"){.headerlink}

:   Edge line color of the bars.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.linemap(0).bars.line_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[LinemapBars.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapBars.line_thickness "Link to this definition"){.headerlink}

:   Edge line thickness of the bars.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).bars.line_thickness = 0.1
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapBars.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapBars.show "Link to this definition"){.headerlink}

:   Display bars on the plot for this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    The parent plot object must have bars enabled as well:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_bars = True
        >>> plot.linemap(0).bars.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapBars.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapBars.size "Link to this definition"){.headerlink}

:   Width of the bars.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).bars.size = 0.10
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (percentange of [[`Frame`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
        .internal} width)
:::

::: {#linemaperrorbars .section}
### [LinemapErrorBars](#id71){.toc-backref role="doc-backlink"}[¶](#linemaperrorbars "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[LinemapErrorBars]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[linemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapErrorBars){.reference .internal}[¶](#tecplot.plot.LinemapErrorBars "Link to this definition"){.headerlink}

:   Error bar style and variable assignment control.

    A single [[`XYLinemap`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.XYLinemap "tecplot.plot.XYLinemap"){.reference
    .internal} holds a single [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} assignment for error bars. Therefore, if you wish to have
    separate error bars for *x* and *y*, two linemaps are required:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from math import sqrt
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, ErrorBar

        # setup dataset
        frame = tp.active_frame()
        ds = frame.create_dataset('Dataset')
        for v in ['x', 'y', 'xerr', 'yerr']:
            ds.add_variable(v)
        zone = ds.add_ordered_zone('Zone', 5)

        # create some data (x, y)
        zone.values('x')[:] = [0,1,2,3,4]
        zone.values('y')[:] = [1,2,4,8,10]

        # error in x is a constant
        zone.values('xerr')[:] = [0.2]*5

        # error in y is the square-root of the value
        zone.values('yerr')[:] = [sqrt(y) for y in zone.values('y')[:]]

        frame.plot_type = PlotType.XYLine
        plot = frame.plot()

        plot.delete_linemaps()
        xerr_lmap = plot.add_linemap('xerr', zone, ds.variable('x'),
                                     ds.variable('y'))
        yerr_lmap = plot.add_linemap('yerr', zone, ds.variable('x'),
                                     ds.variable('y'))

        xerr_lmap.error_bars.variable = ds.variable('xerr')
        xerr_lmap.error_bars.bar_type = ErrorBar.Horz
        xerr_lmap.error_bars.color = Color.Blue
        xerr_lmap.error_bars.line_thickness = 0.8
        xerr_lmap.error_bars.show = True

        yerr_lmap.error_bars.variable = ds.variable('yerr')
        yerr_lmap.error_bars.bar_type = ErrorBar.Vert
        yerr_lmap.error_bars.color = Color.Blue
        yerr_lmap.error_bars.line_thickness = 0.8
        yerr_lmap.error_bars.show = True

        plot.show_lines = False
        plot.show_error_bars = True

        plot.view.fit()

        tp.export.save_png('linemap_error_bars.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_error_bars.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_error_bars.png" style="width: 300px;"
    alt="../_images/linemap_error_bars.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`bar_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.bar_type "tecplot.plot.LinemapErrorBars.bar_type"){.reference .internal}                     Style of the error bar to draw.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.color "tecplot.plot.LinemapErrorBars.color"){.reference .internal}                              [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the error bars.
      [[`endcap_size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.endcap_size "tecplot.plot.LinemapErrorBars.endcap_size"){.reference .internal}            Length of the endcaps of the error bars.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.line_thickness "tecplot.plot.LinemapErrorBars.line_thickness"){.reference .internal}   Width of the error bar lines.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.show "tecplot.plot.LinemapErrorBars.show"){.reference .internal}                                 Display error bars on the plot for this [[Linemaps]{.std .std-ref}](#linemap){.reference .internal}.
      [[`step`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.step "tecplot.plot.LinemapErrorBars.step"){.reference .internal}                                 Space between points to show error bars.
      [[`step_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.step_mode "tecplot.plot.LinemapErrorBars.step_mode"){.reference .internal}                  Space the error bars by index or frame height.
      [[`variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.variable "tecplot.plot.LinemapErrorBars.variable"){.reference .internal}                     [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to use for error bar sizes.
      [[`variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.variable_index "tecplot.plot.LinemapErrorBars.variable_index"){.reference .internal}   Zero-based variable index to use for error bar sizes.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[bar_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.bar_type "Link to this definition"){.headerlink}

:   Style of the error bar to draw.

    Possible values: [[`Up`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Up "tecplot.constant.ErrorBar.Up"){.reference
    .internal}, [[`Down`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Down "tecplot.constant.ErrorBar.Down"){.reference
    .internal}, [[`Left`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Left "tecplot.constant.ErrorBar.Left"){.reference
    .internal}, [[`Right`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Right "tecplot.constant.ErrorBar.Right"){.reference
    .internal}, [[`Horz`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Horz "tecplot.constant.ErrorBar.Horz"){.reference
    .internal}, [[`Vert`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Vert "tecplot.constant.ErrorBar.Vert"){.reference
    .internal}, [[`Cross`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar.Cross "tecplot.constant.ErrorBar.Cross"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ErrorBar
        >>> plot.linemap(0).error_bars.bar_type = ErrorBar.Cross
    :::
    ::::

    Type[:]{.colon}

    :   [[`ErrorBar`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ErrorBar "tecplot.constant.ErrorBar"){.reference
        .internal}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the error bars.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.linemap(0).error_bars.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[endcap_size]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.endcap_size "Link to this definition"){.headerlink}

:   Length of the endcaps of the error bars.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bars.endcap_size = 2.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.line_thickness "Link to this definition"){.headerlink}

:   Width of the error bar lines.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bars.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.show "Link to this definition"){.headerlink}

:   Display error bars on the plot for this [[Linemaps]{.std
    .std-ref}](#linemap){.reference .internal}.

    The parent plot object must have error bars enables as well which
    will require a variable to be set:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bars.variable = dataset.variable('E')
        >>> plot.show_error_bars = True
        >>> plot.linemap(0).error_bars.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[step]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.step "Link to this definition"){.headerlink}

:   Space between points to show error bars.

    The step is specified either as a percentage of the frame height or
    as a number of indices to skip depending on the value of
    [[`LinemapErrorBars.step_mode`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapErrorBars.step_mode "tecplot.plot.LinemapErrorBars.step_mode"){.reference
    .internal}. This example will add error bars to every third point:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bars.step = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[step_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.step_mode "Link to this definition"){.headerlink}

:   Space the error bars by index or frame height.

    This example will make sure all error bars are no closer than 10% of
    the frame height to each other:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import StepMode
        >>> ebars = plot.linemap(0).error_bars
        >>> ebars.step_mode = StepMode.ByFrameUnits
        >>> ebars.step = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`StepMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.StepMode "tecplot.constant.StepMode"){.reference
        .internal}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.variable "Link to this definition"){.headerlink}

:   [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to use for error bar sizes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> ebars = plot.linemap(0).error_bars
        >>> ebars.variable = dataset.variable('Err')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[LinemapErrorBars.]{.pre}]{.sig-prename .descclassname}[[variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapErrorBars.variable_index "Link to this definition"){.headerlink}

:   Zero-based variable index to use for error bar sizes.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).error_bars.variable_index = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}
:::

::: {#linemapindices .section}
### [LinemapIndices](#id72){.toc-backref role="doc-backlink"}[¶](#linemapindices "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[LinemapIndices]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[linemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapIndices){.reference .internal}[¶](#tecplot.plot.LinemapIndices "Link to this definition"){.headerlink}

:   Ordering and spacing of points to be drawn.

    Each mapping can show either *I*, *J*, or *K*-varying families of
    lines. By default, the *I*-varying family of lines are displayed.
    You can also choose which members of the family are drawn (and using
    which data points), by specifying index ranges for each of *I*, *J*,
    and *K*. The index range for the varying index says which points to
    include in each line, and the index ranges for the other indices
    determine which lines in the family to include:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, IJKLines

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()

        lmaps = plot.linemaps(0, 1, 2)
        lmaps.show = True
        lmaps.indices.varying_index = IJKLines.I
        lmaps.indices.i_range = 0,0,3

        # save image to file
        tp.export.save_png('linemap_indices.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_indices.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_indices.png" style="width: 300px;"
    alt="../_images/linemap_indices.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`i_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapIndices.i_range "tecplot.plot.LinemapIndices.i_range"){.reference .internal}                     [[`IndexRange`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference .internal} for the *I* dimension of ordered data.
      [[`j_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapIndices.j_range "tecplot.plot.LinemapIndices.j_range"){.reference .internal}                     [[`IndexRange`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference .internal} for the *J* dimension of ordered data.
      [[`k_range`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapIndices.k_range "tecplot.plot.LinemapIndices.k_range"){.reference .internal}                     [[`IndexRange`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference .internal} for the *K* dimension of ordered data.
      [[`varying_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapIndices.varying_index "tecplot.plot.LinemapIndices.varying_index"){.reference .internal}   Family of lines to be drawn.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[LinemapIndices.]{.pre}]{.sig-prename .descclassname}[[i_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapIndices.i_range "Link to this definition"){.headerlink}

:   [[`IndexRange`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference
    .internal} for the *I* dimension of ordered data.

    This example shows [`I`{.docutils .literal
    .notranslate}]{.pre}-lines at [`i`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`=`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`[0,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`2,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`4,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`6,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`8,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`10]`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).indices.i_range = 0, 10, 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (min, max, step)

<!-- -->

[[LinemapIndices.]{.pre}]{.sig-prename .descclassname}[[j_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapIndices.j_range "Link to this definition"){.headerlink}

:   [[`IndexRange`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference
    .internal} for the *J* dimension of ordered data.

    This example shows all [`J`{.docutils .literal
    .notranslate}]{.pre}-lines starting with [`j`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`=`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`10`{.docutils .literal .notranslate}]{.pre} up to the
    maximum [`J`{.docutils .literal .notranslate}]{.pre}-line of the
    associated [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).indices.j_range = 10, None, 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (min, max, step)

<!-- -->

[[LinemapIndices.]{.pre}]{.sig-prename .descclassname}[[k_range]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapIndices.k_range "Link to this definition"){.headerlink}

:   [[`IndexRange`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.session.html#tecplot.session.IndexRange "tecplot.session.IndexRange"){.reference
    .internal} for the *K* dimension of ordered data.

    This example shows all [`K`{.docutils .literal
    .notranslate}]{.pre}-lines starting with the first up to 5 from the
    last [`K`{.docutils .literal .notranslate}]{.pre}-line of the
    associated [[Zone]{.std
    .std-ref}](tecplot.data.html#data-access){.reference .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).indices.k_range = None, -5
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external} of [[`integers`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external} (min, max, step)

<!-- -->

[[LinemapIndices.]{.pre}]{.sig-prename .descclassname}[[varying_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapIndices.varying_index "Link to this definition"){.headerlink}

:   Family of lines to be drawn.

    This is the order which varies along the lines drawn. *K*-varying is
    only available if the mapping is using an *IJK*-ordered zone:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import IJKLines
        >>> plot.linemap(0).indices.varying_index = IJKLines.J
    :::
    ::::

    Type[:]{.colon}

    :   [[`IJKLines`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.IJKLines "tecplot.constant.IJKLines"){.reference
        .internal}
:::

::: {#linemapsymbols .section}
### [LinemapSymbols](#id73){.toc-backref role="doc-backlink"}[¶](#linemapsymbols "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[LinemapSymbols]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[linemap]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapSymbols){.reference .internal}[¶](#tecplot.plot.LinemapSymbols "Link to this definition"){.headerlink}

:   Style control for markers placed along lines.

    This class allows the user to set the style of the symbols to be
    shown including setting a geometric shape, text character, line and
    fill colors and spacing. The plot-level [`show_symbols`{.docutils
    .literal .notranslate}]{.pre} attribute must be enabled to show
    symbols in any specific linemap within the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, FillMode, GeomShape

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()
        plot.show_symbols = True

        lmaps = plot.linemaps(0, 1, 2)

        lmaps.symbols.show = True
        lmaps.symbols.symbol().shape = GeomShape.Square
        lmaps.symbols.size = 2.5
        lmaps.symbols.color = Color.Blue
        lmaps.symbols.line_thickness = 0.4
        lmaps.symbols.fill_mode = FillMode.UseSpecificColor
        lmaps.symbols.fill_color = Color.Azure

        # save image to file
        tp.export.save_png('linemap_symbols.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_symbols.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_symbols.png" style="width: 300px;"
    alt="../_images/linemap_symbols.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.color "tecplot.plot.LinemapSymbols.color"){.reference .internal}                              Edge or text [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the drawn symbols.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.fill_color "tecplot.plot.LinemapSymbols.fill_color"){.reference .internal}               The fill or background color.
      [[`fill_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.fill_mode "tecplot.plot.LinemapSymbols.fill_mode"){.reference .internal}                  The fill mode for the background.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.line_thickness "tecplot.plot.LinemapSymbols.line_thickness"){.reference .internal}   Width of the lines when drawing geometry symbols.
      [[`show`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.show "tecplot.plot.LinemapSymbols.show"){.reference .internal}                                 Display symbols along the lines to be drawn.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.size "tecplot.plot.LinemapSymbols.size"){.reference .internal}                                 Size of the symbols to draw.
      [[`step`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.step "tecplot.plot.LinemapSymbols.step"){.reference .internal}                                 Space between symbols to be shown.
      [[`step_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.step_mode "tecplot.plot.LinemapSymbols.step_mode"){.reference .internal}                  Space the symbols by index or frame height.
      [[`symbol_type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.symbol_type "tecplot.plot.LinemapSymbols.symbol_type"){.reference .internal}            The [[`SymbolType`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference .internal} to use for this linemap.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------
      [[`symbol`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.symbol "tecplot.plot.LinemapSymbols.symbol"){.reference .internal}(\[symbol_type\])   Returns a linemap symbol style object.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.color "Link to this definition"){.headerlink}

:   Edge or text [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the drawn symbols.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.linemap(1).symbols.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.fill_color "Link to this definition"){.headerlink}

:   The fill or background color.

    The [`fill_mode`{.docutils .literal .notranslate}]{.pre} attribute
    must be set to [[`FillMode.UseSpecificColor`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseSpecificColor "tecplot.constant.FillMode.UseSpecificColor"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, FillMode
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.fill_mode = FillMode.UseSpecificColor
        >>> symbols.fill_color = Color.Yellow
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[fill_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.fill_mode "Link to this definition"){.headerlink}

:   The fill mode for the background.

    Possible values: [[`FillMode.UseSpecificColor`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseSpecificColor "tecplot.constant.FillMode.UseSpecificColor"){.reference .internal}, [[`FillMode.UseLineColor`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseLineColor "tecplot.constant.FillMode.UseLineColor"){.reference .internal},

    :   [[`FillMode.UseBackgroundColor`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.UseBackgroundColor "tecplot.constant.FillMode.UseBackgroundColor"){.reference
        .internal} or [[`FillMode.None_`{.xref .any .py .py-attr
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode.None_ "tecplot.constant.FillMode.None_"){.reference
        .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, FillMode
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.fill_mode = FillMode.UseBackgroundColor
    :::
    ::::

    Type[:]{.colon}

    :   [[`FillMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.FillMode "tecplot.constant.FillMode"){.reference
        .internal}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.line_thickness "Link to this definition"){.headerlink}

:   Width of the lines when drawing geometry symbols.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.symbol_type = SymbolType.Geometry
        >>> symbols.line_thickness = 0.8
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[show]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.show "Link to this definition"){.headerlink}

:   Display symbols along the lines to be drawn.

    The parent plot object must have symbols enabled as well:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.show_symbols = True
        >>> plot.linemap(0).symbols.show = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.size "Link to this definition"){.headerlink}

:   Size of the symbols to draw.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).symbols.size = 3.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[step]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.step "Link to this definition"){.headerlink}

:   Space between symbols to be shown.

    The step is specified either as a percentage of the frame height or
    as a number of indices to skip depending on the value of
    [[`LinemapSymbols.step_mode`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.step_mode "tecplot.plot.LinemapSymbols.step_mode"){.reference
    .internal}. This example will add symbols to every third point:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.linemap(0).symbols.step = 3
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[step_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.step_mode "Link to this definition"){.headerlink}

:   Space the symbols by index or frame height.

    This example will make sure all symbols are no closer than 10% of
    the frame height to each other:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import StepMode
        >>> sym = plot.linemap(0).symbols
        >>> sym.step_mode = StepMode.ByFrameUnits
        >>> sym.step = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`StepMode`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.StepMode "tecplot.constant.StepMode"){.reference
        .internal}

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[symbol]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[symbol_type]{.pre}]{.n}[[=]{.pre}]{.o}[[None]{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/linemap.html#LinemapSymbols.symbol){.reference .internal}[¶](#tecplot.plot.LinemapSymbols.symbol "Link to this definition"){.headerlink}

:   Returns a linemap symbol style object.

    Parameters[:]{.colon}

    :   **symbol_type** ([[`SymbolType`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference
        .internal}, optional) -- The type of symbol to return. By
        default, this will return the active symbol type which is
        obtained from [[`LinemapSymbols.symbol_type`{.xref .any .py
        .py-attr .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.LinemapSymbols.symbol_type "tecplot.plot.LinemapSymbols.symbol_type"){.reference
        .internal}.

    Returns: [[`TextSymbol`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.TextSymbol "tecplot.plot.TextSymbol"){.reference
    .internal} or [[`GeometrySymbol`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.GeometrySymbol "tecplot.plot.GeometrySymbol"){.reference
    .internal}

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> plot.linemap(0).symbols.symbol_type = SymbolType.Text
        >>> symbol = plot.linemap(0).symbols.symbol()
        >>> symbol.text = 'a'
    :::
    ::::

<!-- -->

[[LinemapSymbols.]{.pre}]{.sig-prename .descclassname}[[symbol_type]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.LinemapSymbols.symbol_type "Link to this definition"){.headerlink}

:   The [[`SymbolType`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference
    .internal} to use for this linemap.

    Possible values are: [[`SymbolType.Geometry`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType.Geometry "tecplot.constant.SymbolType.Geometry"){.reference
    .internal}, [[`SymbolType.Text`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType.Text "tecplot.constant.SymbolType.Text"){.reference
    .internal}.

    This sets the active symbol type. Use LinemapSymbols.symbol\` to
    access the symbol:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> linemap = plot.linemap(0)
        >>> linemap.symbols.symbol_type = SymbolType.Text
        >>> symbol = linemap.symbols.symbol(SymbolType.Text)
        >>> symbol.text = 'a'
    :::
    ::::

    Type[:]{.colon}

    :   [[`SymbolType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.SymbolType "tecplot.constant.SymbolType"){.reference
        .internal}
:::

::: {#geometrysymbol .section}
### [GeometrySymbol](#id74){.toc-backref role="doc-backlink"}[¶](#geometrysymbol "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[GeometrySymbol]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[parent]{.pre}]{.n}*, *[[svarg]{.pre}]{.n}[[=]{.pre}]{.o}[[\'SYMBOLSHAPE\']{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/symbol.html#GeometrySymbol){.reference .internal}[¶](#tecplot.plot.GeometrySymbol "Link to this definition"){.headerlink}

:   Geometric shape for linemap symbols.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import (PlotType, Color, GeomShape, SymbolType,
                                      FillMode)

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()
        plot.show_symbols = True

        cols = [Color.DeepRed, Color.Blue, Color.Fern]
        shapes = [GeomShape.Square, GeomShape.Circle, GeomShape.Del]

        lmaps = plot.linemaps()

        lmaps.show = True
        lmaps.symbols.show = True
        lmaps.symbols.size = 4.5
        lmaps.symbols.fill_mode = FillMode.UseSpecificColor
        lmaps.symbols.symbol_type = SymbolType.Geometry

        for lmap, color, shape in zip(lmaps, cols, shapes):
            lmap.line.color = color
            lmap.symbols.color = color
            lmap.symbols.fill_color = color
            lmap.symbols.symbol().shape = shape

        plot.view.fit()

        # save image to file
        tp.export.save_png('linemap_symbols_geometry.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_symbols_geometry.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_symbols_geometry.png" style="width: 300px;"
    alt="../_images/linemap_symbols_geometry.png" /></a>
    </figure>

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------
      [[`shape`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.GeometrySymbol.shape "tecplot.plot.GeometrySymbol.shape"){.reference .internal}   Geometric shape to use when plotting linemap symbols.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------

<!-- -->

[[GeometrySymbol.]{.pre}]{.sig-prename .descclassname}[[shape]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.GeometrySymbol.shape "Link to this definition"){.headerlink}

:   Geometric shape to use when plotting linemap symbols.

    Possible values: [[`Square`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Square "tecplot.constant.GeomShape.Square"){.reference
    .internal}, [[`Del`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Del "tecplot.constant.GeomShape.Del"){.reference
    .internal}, [[`Grad`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Grad "tecplot.constant.GeomShape.Grad"){.reference
    .internal}, [[`RTri`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.RTri "tecplot.constant.GeomShape.RTri"){.reference
    .internal}, [[`LTri`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.LTri "tecplot.constant.GeomShape.LTri"){.reference
    .internal}, [[`Diamond`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Diamond "tecplot.constant.GeomShape.Diamond"){.reference
    .internal}, [[`Circle`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Circle "tecplot.constant.GeomShape.Circle"){.reference
    .internal}, [[`Cube`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Cube "tecplot.constant.GeomShape.Cube"){.reference
    .internal}, [[`Sphere`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Sphere "tecplot.constant.GeomShape.Sphere"){.reference
    .internal}, [[`Octahedron`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Octahedron "tecplot.constant.GeomShape.Octahedron"){.reference
    .internal}, [[`Point`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape.Point "tecplot.constant.GeomShape.Point"){.reference
    .internal}.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType, GeomShape
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.symbol_type = SymbolType.Geometry
        >>> symbols.symbol().shape = GeomShape.Diamond
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomShape`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomShape "tecplot.constant.GeomShape"){.reference
        .internal}
:::

::: {#textsymbol .section}
### [TextSymbol](#id75){.toc-backref role="doc-backlink"}[¶](#textsymbol "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[TextSymbol]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[parent]{.pre}]{.n}*, *[[svarg]{.pre}]{.n}[[=]{.pre}]{.o}[[\'SYMBOLSHAPE\']{.pre}]{.default_value}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/symbol.html#TextSymbol){.reference .internal}[¶](#tecplot.plot.TextSymbol "Link to this definition"){.headerlink}

:   Text character for linemap symbols.

    Only a single character can be used.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import PlotType, Color, SymbolType, FillMode

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Rainfall.dat')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        frame.plot_type = PlotType.XYLine
        plot = frame.plot()
        plot.show_symbols = True

        cols = [Color.DeepRed, Color.Blue, Color.Fern]
        chars = ['S','D','M']

        lmaps = plot.linemaps()
        lmaps.show = True
        lmaps.symbols.show = True
        lmaps.symbols.size = 2.5
        lmaps.symbols.color = Color.White
        lmaps.symbols.fill_mode = FillMode.UseSpecificColor
        lmaps.symbols.symbol_type = SymbolType.Text

        for lmap, color, character in zip(lmaps, cols, chars):
            lmap.line.color = color
            lmap.symbols.fill_color = color
            lmap.symbols.symbol().text = character

        plot.view.fit()

        # save image to file
        tp.export.save_png('linemap_symbols_text.png', 600, supersample=3)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/linemap_symbols_text.png"
    class="reference internal image-reference"><img
    src="../_images/linemap_symbols_text.png" style="width: 300px;"
    alt="../_images/linemap_symbols_text.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------
      [[`font_override`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TextSymbol.font_override "tecplot.plot.TextSymbol.font_override"){.reference .internal}   Typeface to use when rendering text-based symbols.
      [[`text`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TextSymbol.text "tecplot.plot.TextSymbol.text"){.reference .internal}                              The ASCII character to use as the symbol to show
      [[`use_base_font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.TextSymbol.use_base_font "tecplot.plot.TextSymbol.use_base_font"){.reference .internal}   Use the base typeface when rendering text-based symbols.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------

<!-- -->

[[TextSymbol.]{.pre}]{.sig-prename .descclassname}[[font_override]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TextSymbol.font_override "Link to this definition"){.headerlink}

:   Typeface to use when rendering text-based symbols.

    Possible values: [[`constant.Font.Greek`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font.Greek "tecplot.constant.Font.Greek"){.reference
    .internal}, [[`constant.Font.Math`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font.Math "tecplot.constant.Font.Math"){.reference
    .internal} or [[`constant.Font.UserDefined`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font.UserDefined "tecplot.constant.Font.UserDefined"){.reference
    .internal}.

    The [`use_base_font`{.docutils .literal .notranslate}]{.pre}
    attribute must be set to [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType, Font
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.symbol_type = SymbolType.Text
        >>> symbols.symbol().use_base_font = False
        >>> symbols.symbol().font_override = Font.Greek
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Font`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Font "tecplot.constant.Font"){.reference
        .internal}

<!-- -->

[[TextSymbol.]{.pre}]{.sig-prename .descclassname}[[text]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TextSymbol.text "Link to this definition"){.headerlink}

:   The ASCII character to use as the symbol to show

    ::: {.admonition .note}
    Note

    This is limited to a single character.
    :::

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.symbol_type = SymbolType.Text
        >>> symbols.symbol().text = 'X'
    :::
    ::::

<!-- -->

[[TextSymbol.]{.pre}]{.sig-prename .descclassname}[[use_base_font]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.TextSymbol.use_base_font "Link to this definition"){.headerlink}

:   Use the base typeface when rendering text-based symbols.

    When [[`False`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#False "(in Python v3.13)"){.reference
    .external}, the [`font_override`{.docutils .literal
    .notranslate}]{.pre} attribute takes effect:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import SymbolType, Font
        >>> symbols = plot.linemap(0).symbols
        >>> symbols.symbol_type = SymbolType.Text
        >>> symbols.symbol().use_base_font = False
        >>> symbols.symbol().font_override = Font.Greek
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}
:::
:::::::::::::::
::::::::::::::::::::::::::::::::::::::::

::: clearer
:::
::::::::::::::::::::::::::::::::::::::::::
