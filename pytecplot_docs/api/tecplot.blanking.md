::::::::::: {.body role="main"}
::::::::: {#blanking .section}
# Blanking[¶](#blanking "Link to this heading"){.headerlink}

- [Value Blanking](#value-blanking){#id2 .reference .internal}

  - [ValueBlanking](#valueblanking){#id3 .reference .internal}

  - [ValueBlankingCartesian2D](#valueblankingcartesian2d){#id4
    .reference .internal}

  - [ValueBlankingCartesian3D](#valueblankingcartesian3d){#id5
    .reference .internal}

  - [ValueBlankingConstraint](#valueblankingconstraint){#id6 .reference
    .internal}

  - [ValueBlankingConstraintCartesian2D](#valueblankingconstraintcartesian2d){#id7
    .reference .internal}

:::::::: {#value-blanking .section}
## [Value Blanking](#id2){.toc-backref role="doc-backlink"}[¶](#value-blanking "Link to this heading"){.headerlink}

- [ValueBlanking](#valueblanking){#id8 .reference .internal}

- [ValueBlankingCartesian2D](#valueblankingcartesian2d){#id9 .reference
  .internal}

- [ValueBlankingCartesian3D](#valueblankingcartesian3d){#id10 .reference
  .internal}

- [ValueBlankingConstraint](#valueblankingconstraint){#id11 .reference
  .internal}

- [ValueBlankingConstraintCartesian2D](#valueblankingconstraintcartesian2d){#id12
  .reference .internal}

::: {#valueblanking .section}
### [ValueBlanking](#id8){.toc-backref role="doc-backlink"}[¶](#valueblanking "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[ValueBlanking]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlanking){.reference .internal}[¶](#tecplot.plot.ValueBlanking "Link to this definition"){.headerlink}

:   Value blanking for line plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import *

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

        plot.value_blanking.active = True
        constraint = plot.value_blanking.constraint(0)
        constraint.active = True
        constraint.compare_by = ConstraintOp2Mode.UseConstant
        constraint.comparison_operator = RelOp.LessThanOrEqual
        constraint.comparison_value = 6
        constraint.variable = dataset.variable('Month')

        tp.export.save_png('value_blanking_line.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/value_blanking_line.png"
    class="reference internal image-reference"><img
    src="../_images/value_blanking_line.png" style="width: 300px;"
    alt="../_images/value_blanking_line.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlanking.active "tecplot.plot.ValueBlanking.active"){.reference .internal}   Include value blanking.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------

    **Methods**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------
      [[`constraint`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlanking.constraint "tecplot.plot.ValueBlanking.constraint"){.reference .internal}(index)   One of the eight availble value-blanking constraints.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------

<!-- -->

[[ValueBlanking.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlanking.active "Link to this definition"){.headerlink}

:   Include value blanking.

    Set to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external} to include value blanking. The individual constraints
    must be activated as well:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.active = True
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlanking.]{.pre}]{.sig-prename .descclassname}[[constraint]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlanking.constraint){.reference .internal}[¶](#tecplot.plot.ValueBlanking.constraint "Link to this definition"){.headerlink}

:   One of the eight availble value-blanking constraints.

    Parameters[:]{.colon}

    :   **index** ([[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}) -- Integer from 0 to 7 inclusive for the eight
        possible value-blanking constraints.

    Returns[:]{.colon}

    :   [[`ValueBlankingConstraint`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint "tecplot.plot.ValueBlankingConstraint"){.reference
        .internal}

    There are total of eight value blanking constraints that can be
    independendly activated and adjusted. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(4).active = True
    :::
    ::::
:::

::: {#valueblankingcartesian2d .section}
### [ValueBlankingCartesian2D](#id9){.toc-backref role="doc-backlink"}[¶](#valueblankingcartesian2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[ValueBlankingCartesian2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlankingCartesian2D){.reference .internal}[¶](#tecplot.plot.ValueBlankingCartesian2D "Link to this definition"){.headerlink}

:   Value blanking for cartesian 2D plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import *

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'HeatExchanger.plt')
        dataset = tp.data.load_tecplot(infile)

        frame = tp.active_frame()
        plot = frame.plot(PlotType.Cartesian2D)

        plot.show_contour = True

        plot.value_blanking.active = True
        plot.value_blanking.cell_mode = ValueBlankCellMode.AnyCorner
        constraint = plot.value_blanking.constraint(0)
        constraint.active = True
        constraint.compare_by = ConstraintOp2Mode.UseConstant
        constraint.comparison_operator = RelOp.LessThanOrEqual
        constraint.comparison_value = 5
        constraint.variable = dataset.variable('X(M)')

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('value_blanking_2d.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/value_blanking_2d.png"
    class="reference internal image-reference"><img
    src="../_images/value_blanking_2d.png" style="width: 300px;"
    alt="../_images/value_blanking_2d.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian2D.active "tecplot.plot.ValueBlankingCartesian2D.active"){.reference .internal}            Include value blanking.
      [[`cell_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian2D.cell_mode "tecplot.plot.ValueBlankingCartesian2D.cell_mode"){.reference .internal}   Determine which cells to blank.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

    **Methods**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------
      [[`constraint`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian2D.constraint "tecplot.plot.ValueBlankingCartesian2D.constraint"){.reference .internal}(index)   One of the eight availble value-blanking constraints.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------

<!-- -->

[[ValueBlankingCartesian2D.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingCartesian2D.active "Link to this definition"){.headerlink}

:   Include value blanking.

    Set to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external} to include value blanking. The individual constraints
    must be activated as well:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.active = True
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingCartesian2D.]{.pre}]{.sig-prename .descclassname}[[cell_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingCartesian2D.cell_mode "Link to this definition"){.headerlink}

:   Determine which cells to blank.

    This property controls which value is used when determining if a
    cell should be blanked. It also allows for trimming cells precisely.
    Possible values are: [[`ValueBlankCellMode.AllCorners`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.AllCorners "tecplot.constant.ValueBlankCellMode.AllCorners"){.reference
    .internal}, [[`ValueBlankCellMode.AnyCorner`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.AnyCorner "tecplot.constant.ValueBlankCellMode.AnyCorner"){.reference
    .internal}, [[`ValueBlankCellMode.PrimaryValue`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.PrimaryValue "tecplot.constant.ValueBlankCellMode.PrimaryValue"){.reference
    .internal} and [[`ValueBlankCellMode.TrimCells`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.TrimCells "tecplot.constant.ValueBlankCellMode.TrimCells"){.reference
    .internal}. This affects all value-blanking constraints on the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ValueBlankCellMode
        >>> plot.value_blanking.cell_mode = ValueBlankCellMode.TrimCells
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueBlankCellMode`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode "tecplot.constant.ValueBlankCellMode"){.reference
        .internal}

<!-- -->

[[ValueBlankingCartesian2D.]{.pre}]{.sig-prename .descclassname}[[constraint]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlankingCartesian2D.constraint){.reference .internal}[¶](#tecplot.plot.ValueBlankingCartesian2D.constraint "Link to this definition"){.headerlink}

:   One of the eight availble value-blanking constraints.

    Parameters[:]{.colon}

    :   **index** ([[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}) -- Integer from 0 to 7 inclusive for the eight
        possible value-blanking constraints.

    Returns[:]{.colon}

    :   [[`ValueBlankingConstraintCartesian2D`{.xref .any .py .py-class
        .docutils .literal
        .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D "tecplot.plot.ValueBlankingConstraintCartesian2D"){.reference
        .internal}

    There are total of eight value blanking constraints that can be
    independendly activated and adjusted. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(4).active = True
    :::
    ::::
:::

::: {#valueblankingcartesian3d .section}
### [ValueBlankingCartesian3D](#id10){.toc-backref role="doc-backlink"}[¶](#valueblankingcartesian3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[ValueBlankingCartesian3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[plot]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlankingCartesian3D){.reference .internal}[¶](#tecplot.plot.ValueBlankingCartesian3D "Link to this definition"){.headerlink}

:   Value blanking for cartesian 3D plots.

    :::: {.highlight-python .notranslate}
    ::: highlight
        from os import path
        import tecplot as tp
        from tecplot.constant import *

        examples_dir = tp.session.tecplot_examples_directory()
        infile = path.join(examples_dir, 'SimpleData', 'Sphere.lpk')
        tp.load_layout(infile)

        frame = tp.active_frame()
        plot = frame.plot()

        plot.value_blanking.active = True
        plot.value_blanking.cell_mode = ValueBlankCellMode.AnyCorner
        constraint = plot.value_blanking.constraint(0)
        constraint.active = True
        constraint.compare_by = ConstraintOp2Mode.UseConstant
        constraint.comparison_operator = RelOp.GreaterThan
        constraint.comparison_value = 0
        constraint.variable = frame.dataset.variable('X')

        # ensure consistent output between interactive (connected) and batch
        plot.contour(0).levels.reset_to_nice()

        tp.export.save_png('value_blanking_3d.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/value_blanking_3d.png"
    class="reference internal image-reference"><img
    src="../_images/value_blanking_3d.png" style="width: 300px;"
    alt="../_images/value_blanking_3d.png" /></a>
    </figure>

    **Attributes**

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian3D.active "tecplot.plot.ValueBlankingCartesian3D.active"){.reference .internal}            Include value blanking.
      [[`cell_mode`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian3D.cell_mode "tecplot.plot.ValueBlankingCartesian3D.cell_mode"){.reference .internal}   Determine which cells to blank.
      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------

    **Methods**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------
      [[`constraint`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian3D.constraint "tecplot.plot.ValueBlankingCartesian3D.constraint"){.reference .internal}(index)   One of the eight availble value-blanking constraints.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------

<!-- -->

[[ValueBlankingCartesian3D.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingCartesian3D.active "Link to this definition"){.headerlink}

:   Include value blanking.

    Set to [[`True`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#True "(in Python v3.13)"){.reference
    .external} to include value blanking. The individual constraints
    must be activated as well:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.active = True
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingCartesian3D.]{.pre}]{.sig-prename .descclassname}[[cell_mode]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingCartesian3D.cell_mode "Link to this definition"){.headerlink}

:   Determine which cells to blank.

    This property controls which value is used when determining if a
    cell should be blanked. Possible values are:
    [[`ValueBlankCellMode.AllCorners`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.AllCorners "tecplot.constant.ValueBlankCellMode.AllCorners"){.reference
    .internal}, [[`ValueBlankCellMode.AnyCorner`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.AnyCorner "tecplot.constant.ValueBlankCellMode.AnyCorner"){.reference
    .internal} and [[`ValueBlankCellMode.PrimaryValue`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode.PrimaryValue "tecplot.constant.ValueBlankCellMode.PrimaryValue"){.reference
    .internal}. This affects all value-blanking constraints on the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ValueBlankCellMode
        >>> plot.value_blanking.cell_mode = ValueBlankCellMode.AnyCorner
    :::
    ::::

    Type[:]{.colon}

    :   [[`ValueBlankCellMode`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ValueBlankCellMode "tecplot.constant.ValueBlankCellMode"){.reference
        .internal}

<!-- -->

[[ValueBlankingCartesian3D.]{.pre}]{.sig-prename .descclassname}[[constraint]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*[)]{.sig-paren}[¶](#tecplot.plot.ValueBlankingCartesian3D.constraint "Link to this definition"){.headerlink}

:   One of the eight availble value-blanking constraints.

    Parameters[:]{.colon}

    :   **index** ([[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}) -- Integer from 0 to 7 inclusive for the eight
        possible value-blanking constraints.

    Returns[:]{.colon}

    :   [[`ValueBlankingConstraint`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint "tecplot.plot.ValueBlankingConstraint"){.reference
        .internal}

    There are total of eight value blanking constraints that can be
    independendly activated and adjusted. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(4).active = True
    :::
    ::::
:::

::: {#valueblankingconstraint .section}
### [ValueBlankingConstraint](#id11){.toc-backref role="doc-backlink"}[¶](#valueblankingconstraint "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[ValueBlankingConstraint]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[blanking]{.pre}]{.n}*, *[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlankingConstraint){.reference .internal}[¶](#tecplot.plot.ValueBlankingConstraint "Link to this definition"){.headerlink}

:   Value blanking constraint for cartesian 3D and line plots.

    ::: {.admonition .seealso}
    See also

    [[`ValueBlankingCartesian3D`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian3D "tecplot.plot.ValueBlankingCartesian3D"){.reference
    .internal}
    :::

    **Attributes**

      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.active "tecplot.plot.ValueBlankingConstraint.active"){.reference .internal}                                                            Include value blanking.
      [[`compare_by`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.compare_by "tecplot.plot.ValueBlankingConstraint.compare_by"){.reference .internal}                                                Compare against a constant or [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal}.
      [[`comparison_operator`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_operator "tecplot.plot.ValueBlankingConstraint.comparison_operator"){.reference .internal}                     The relationship to use to determine blanking.
      [[`comparison_value`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_value "tecplot.plot.ValueBlankingConstraint.comparison_value"){.reference .internal}                              Constant value for blanking.
      [[`comparison_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_variable "tecplot.plot.ValueBlankingConstraint.comparison_variable"){.reference .internal}                     The [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to determine when to blank.
      [[`comparison_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_variable_index "tecplot.plot.ValueBlankingConstraint.comparison_variable_index"){.reference .internal}   [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal} of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to determine when to blank.
      [[`variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.variable "tecplot.plot.ValueBlankingConstraint.variable"){.reference .internal}                                                      The [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to be blanked.
      [[`variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.variable_index "tecplot.plot.ValueBlankingConstraint.variable_index"){.reference .internal}                                    Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to be blanked.
      -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.active "Link to this definition"){.headerlink}

:   Include value blanking.

    Toggle-on to include this constraint for value blanking on the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[compare_by]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.compare_by "Link to this definition"){.headerlink}

:   Compare against a constant or [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal}.

    This controls what is used in the comparison for blanking. Possible
    values are: [[`ConstraintOp2Mode.UseConstant`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseConstant "tecplot.constant.ConstraintOp2Mode.UseConstant"){.reference
    .internal} and [[`ConstraintOp2Mode.UseVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseVar "tecplot.constant.ConstraintOp2Mode.UseVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseConstant
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_value = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`ConstraintOp2Mode`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode "tecplot.constant.ConstraintOp2Mode"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[comparison_operator]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.comparison_operator "Link to this definition"){.headerlink}

:   The relationship to use to determine blanking.

    This controls what comparison relation is used for blanking.
    Possible values are [[`RelOp.LessThanOrEqual`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.LessThanOrEqual "tecplot.constant.RelOp.LessThanOrEqual"){.reference
    .internal}, [[`RelOp.GreaterThanOrEqual`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.GreaterThanOrEqual "tecplot.constant.RelOp.GreaterThanOrEqual"){.reference
    .internal}, [[`RelOp.LessThan`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.LessThan "tecplot.constant.RelOp.LessThan"){.reference
    .internal}, [[`RelOp.GreaterThan`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.GreaterThan "tecplot.constant.RelOp.GreaterThan"){.reference
    .internal}, [[`RelOp.EqualTo`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.EqualTo "tecplot.constant.RelOp.EqualTo"){.reference
    .internal} and [[`RelOp.NotEqualTo`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.NotEqualTo "tecplot.constant.RelOp.NotEqualTo"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseConstant
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_value = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`RelOp`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp "tecplot.constant.RelOp"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[comparison_value]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.comparison_value "Link to this definition"){.headerlink}

:   Constant value for blanking.

    The variable will be blanked according to this constant value, using
    the [[`comparison_operator`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_operator "tecplot.plot.ValueBlankingConstraint.comparison_operator"){.reference
    .internal} for this constraint, when the [[`compare_by`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.compare_by "tecplot.plot.ValueBlankingConstraint.compare_by"){.reference
    .internal} attribute is set to
    [[`ConstraintOp2Mode.UseConstant`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseConstant "tecplot.constant.ConstraintOp2Mode.UseConstant"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseConstant
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_value = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[comparison_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.comparison_variable "Link to this definition"){.headerlink}

:   The [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to determine when to blank.

    The variable will be blanked according to values in this
    "comparison" variable, using the [[`comparison_operator`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_operator "tecplot.plot.ValueBlankingConstraint.comparison_operator"){.reference
    .internal} for this constraint, when the [[`compare_by`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.compare_by "tecplot.plot.ValueBlankingConstraint.compare_by"){.reference
    .internal} attribute is set to [[`ConstraintOp2Mode.UseVar`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseVar "tecplot.constant.ConstraintOp2Mode.UseVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_variable = dataset.variable('s')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[comparison_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.comparison_variable_index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal} of the [[`Variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to determine when to blank.

    The variable will be blanked according to values in this
    "comparison" variable, using the [[`comparison_operator`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.comparison_operator "tecplot.plot.ValueBlankingConstraint.comparison_operator"){.reference
    .internal} for this constraint, when the [[`compare_by`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraint.compare_by "tecplot.plot.ValueBlankingConstraint.compare_by"){.reference
    .internal} attribute is set to [[`ConstraintOp2Mode.UseVar`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseVar "tecplot.constant.ConstraintOp2Mode.UseVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_variable_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.variable "Link to this definition"){.headerlink}

:   The [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to be blanked.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.variable = dataset.variable('s')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraint.]{.pre}]{.sig-prename .descclassname}[[variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraint.variable_index "Link to this definition"){.headerlink}

:   Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to be blanked.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.variable_index = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}
:::

::: {#valueblankingconstraintcartesian2d .section}
### [ValueBlankingConstraintCartesian2D](#id12){.toc-backref role="doc-backlink"}[¶](#valueblankingconstraintcartesian2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.plot.]{.pre}]{.sig-prename .descclassname}[[ValueBlankingConstraintCartesian2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[blanking]{.pre}]{.n}*, *[[index]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/plot/blanking.html#ValueBlankingConstraintCartesian2D){.reference .internal}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D "Link to this definition"){.headerlink}

:   Value blanking constraint for cartesian 2D plots.

    ::: {.admonition .seealso}
    See also

    [[`ValueBlankingCartesian2D`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingCartesian2D "tecplot.plot.ValueBlankingCartesian2D"){.reference
    .internal}
    :::

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`active`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.active "tecplot.plot.ValueBlankingConstraintCartesian2D.active"){.reference .internal}                                                            Include value blanking.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.color "tecplot.plot.ValueBlankingConstraintCartesian2D.color"){.reference .internal}                                                               [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the constraint boundary line.
      [[`compare_by`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by "tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by"){.reference .internal}                                                Compare against a constant or [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal}.
      [[`comparison_operator`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator"){.reference .internal}                     The relationship to use to determine blanking.
      [[`comparison_value`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_value "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_value"){.reference .internal}                              Constant value for blanking.
      [[`comparison_variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_variable "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_variable"){.reference .internal}                     The [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to determine when to blank.
      [[`comparison_variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_variable_index "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_variable_index"){.reference .internal}   [[`Index`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference .internal} of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to determine when to blank.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.line_pattern "tecplot.plot.ValueBlankingConstraintCartesian2D.line_pattern"){.reference .internal}                                          Dash pattern of the constraint boundary line.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.line_thickness "tecplot.plot.ValueBlankingConstraintCartesian2D.line_thickness"){.reference .internal}                                    Width of the constraint boundary line.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.pattern_length "tecplot.plot.ValueBlankingConstraintCartesian2D.pattern_length"){.reference .internal}                                    Length of the dash pattern for the boundary line. Example usage::.
      [[`show_line`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.show_line "tecplot.plot.ValueBlankingConstraintCartesian2D.show_line"){.reference .internal}                                                   Show constraint boundary.
      [[`variable`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.variable "tecplot.plot.ValueBlankingConstraintCartesian2D.variable"){.reference .internal}                                                      The [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to be blanked.
      [[`variable_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.variable_index "tecplot.plot.ValueBlankingConstraintCartesian2D.variable_index"){.reference .internal}                                    Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference .internal} to be blanked.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[active]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.active "Link to this definition"){.headerlink}

:   Include value blanking.

    Toggle-on to include this constraint for value blanking on the plot:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).active = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the constraint boundary line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color
        >>> plot.value_blanking.constraint(0).show_line = True
        >>> plot.value_blanking.constraint(0).color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[compare_by]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by "Link to this definition"){.headerlink}

:   Compare against a constant or [[`Variable`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal}.

    This controls what is used in the comparison for blanking. Possible
    values are: [[`ConstraintOp2Mode.UseConstant`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseConstant "tecplot.constant.ConstraintOp2Mode.UseConstant"){.reference
    .internal} and [[`ConstraintOp2Mode.UseVar`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseVar "tecplot.constant.ConstraintOp2Mode.UseVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseConstant
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_value = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`ConstraintOp2Mode`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode "tecplot.constant.ConstraintOp2Mode"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[comparison_operator]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator "Link to this definition"){.headerlink}

:   The relationship to use to determine blanking.

    This controls what comparison relation is used for blanking.
    Possible values are [[`RelOp.LessThanOrEqual`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.LessThanOrEqual "tecplot.constant.RelOp.LessThanOrEqual"){.reference
    .internal}, [[`RelOp.GreaterThanOrEqual`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.GreaterThanOrEqual "tecplot.constant.RelOp.GreaterThanOrEqual"){.reference
    .internal}, [[`RelOp.LessThan`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.LessThan "tecplot.constant.RelOp.LessThan"){.reference
    .internal}, [[`RelOp.GreaterThan`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.GreaterThan "tecplot.constant.RelOp.GreaterThan"){.reference
    .internal}, [[`RelOp.EqualTo`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.EqualTo "tecplot.constant.RelOp.EqualTo"){.reference
    .internal} and [[`RelOp.NotEqualTo`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp.NotEqualTo "tecplot.constant.RelOp.NotEqualTo"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseConstant
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_value = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`RelOp`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.RelOp "tecplot.constant.RelOp"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[comparison_value]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_value "Link to this definition"){.headerlink}

:   Constant value for blanking.

    The variable will be blanked according to this constant value, using
    the [[`comparison_operator`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator"){.reference
    .internal} for this constraint, when the [[`compare_by`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by "tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by"){.reference
    .internal} attribute is set to
    [[`ConstraintOp2Mode.UseConstant`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseConstant "tecplot.constant.ConstraintOp2Mode.UseConstant"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseConstant
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_value = 3.14
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[comparison_variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_variable "Link to this definition"){.headerlink}

:   The [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to determine when to blank.

    The variable will be blanked according to values in this
    "comparison" variable, using the [[`comparison_operator`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator"){.reference
    .internal} for this constraint, when the [[`compare_by`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by "tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by"){.reference
    .internal} attribute is set to [[`ConstraintOp2Mode.UseVar`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseVar "tecplot.constant.ConstraintOp2Mode.UseVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_variable = dataset.variable('s')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[comparison_variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_variable_index "Link to this definition"){.headerlink}

:   [[`Index`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal} of the [[`Variable`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to determine when to blank.

    The variable will be blanked according to values in this
    "comparison" variable, using the [[`comparison_operator`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator "tecplot.plot.ValueBlankingConstraintCartesian2D.comparison_operator"){.reference
    .internal} for this constraint, when the [[`compare_by`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by "tecplot.plot.ValueBlankingConstraintCartesian2D.compare_by"){.reference
    .internal} attribute is set to [[`ConstraintOp2Mode.UseVar`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ConstraintOp2Mode.UseVar "tecplot.constant.ConstraintOp2Mode.UseVar"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode, RelOp
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.active = True
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.comparison_operator = RelOp.LessThanOrEqual
        >>> constraint.comparison_variable_index = 2
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.line_pattern "Link to this definition"){.headerlink}

:   Dash pattern of the constraint boundary line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.show_line = True
        >>> constraint.line_pattern = LinePattern.Dashed
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.line_thickness "Link to this definition"){.headerlink}

:   Width of the constraint boundary line.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).show_line = True
        >>> plot.value_blanking.constraint(0).line_thickness = 1.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.pattern_length "Link to this definition"){.headerlink}

:   Length of the dash pattern for the boundary line. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import LinePattern
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.show_line = True
        >>> constraint.line_pattern = LinePattern.Dashed
        >>> constraint.pattern_length = 1.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[show_line]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.show_line "Link to this definition"){.headerlink}

:   Show constraint boundary.

    Toggle-on to display a line that separates the region of your data
    that is blanked from the region which is not blanked:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> plot.value_blanking.constraint(0).show_line = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[variable]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.variable "Link to this definition"){.headerlink}

:   The [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to be blanked.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.variable = dataset.variable('s')
    :::
    ::::

    Type[:]{.colon}

    :   [[`Variable`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
        .internal}

<!-- -->

[[ValueBlankingConstraintCartesian2D.]{.pre}]{.sig-prename .descclassname}[[variable_index]{.pre}]{.sig-name .descname}[¶](#tecplot.plot.ValueBlankingConstraintCartesian2D.variable_index "Link to this definition"){.headerlink}

:   Index of the [[`Variable`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.AuxDataObjectType.Variable "tecplot.constant.AuxDataObjectType.Variable"){.reference
    .internal} to be blanked.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ConstraintOp2Mode
        >>> constraint = plot.value_blanking.constraint(0)
        >>> constraint.compare_by = ConstraintOp2Mode.UseVar
        >>> constraint.variable_index = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal}
:::
::::::::
:::::::::

::: clearer
:::
:::::::::::
