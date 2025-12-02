:::::::::::::::::::::: {.body role="main"}
:::::::::::::::::::: {#annotations .section}
[]{#annotation}

# Annotations[¶](#annotations "Link to this heading"){.headerlink}

- [Text](#text){#id3 .reference .internal}

  - [Text](#id2){#id4 .reference .internal}

  - [TextBox](#textbox){#id5 .reference .internal}

  - [TextFont](#textfont){#id6 .reference .internal}

- [Geometric Shapes](#geometric-shapes){#id7 .reference .internal}

  - [Circle](#circle){#id8 .reference .internal}

  - [Ellipse](#ellipse){#id9 .reference .internal}

  - [Rectangle](#rectangle){#id10 .reference .internal}

  - [Square](#square){#id11 .reference .internal}

  - [Polyline2D](#polyline2d){#id12 .reference .internal}

  - [Polyline3D](#polyline3d){#id13 .reference .internal}

  - [MultiPolyline2D](#multipolyline2d){#id14 .reference .internal}

  - [MultiPolyline3D](#multipolyline3d){#id15 .reference .internal}

  - [Arrowhead](#arrowhead){#id16 .reference .internal}

- [Images](#images){#id17 .reference .internal}

  - [Image](#image){#id18 .reference .internal}

  - [GeoreferencedImage](#georeferencedimage){#id19 .reference
    .internal}

:::::: {#text .section}
## [Text](#id3){.toc-backref role="doc-backlink"}[¶](#text "Link to this heading"){.headerlink}

- [Text](#id2){#id20 .reference .internal}

- [TextBox](#textbox){#id21 .reference .internal}

- [TextFont](#textfont){#id22 .reference .internal}

::: {#id2 .section}
### [Text](#id20){.toc-backref role="doc-backlink"}[¶](#id2 "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Text]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/text.html#Text){.reference .internal}[¶](#tecplot.annotation.Text "Link to this definition"){.headerlink}

:   Text annotation.

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`anchor`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.anchor "tecplot.annotation.Text.anchor"){.reference .internal}                                                               Anchor location of this [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`angle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.angle "tecplot.annotation.Text.angle"){.reference .internal}                                                                  Angle of the text box in degrees.
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.attached_map_index "tecplot.annotation.Text.attached_map_index"){.reference .internal}                           Index of the attached fieldmap or linemap.
      [[`box`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.box "tecplot.annotation.Text.box"){.reference .internal}                                                                        The frame and area around this [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.clipping "tecplot.annotation.Text.clipping"){.reference .internal}                                                         [[`Clipping`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference .internal} properties of the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal}
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.color "tecplot.annotation.Text.color"){.reference .internal}                                                                  [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal} of the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`font`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.font "tecplot.annotation.Text.font"){.reference .internal}                                                                     Typeface properties for a [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`line_spacing`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.line_spacing "tecplot.annotation.Text.line_spacing"){.reference .internal}                                             Spacing between lines in the text box.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.position "tecplot.annotation.Text.position"){.reference .internal}                                                         Anchor position of the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.position_coordinate_system "tecplot.annotation.Text.position_coordinate_system"){.reference .internal}   Position coordinate system of the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.scope "tecplot.annotation.Text.scope"){.reference .internal}                                                                  The [[`Scope`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference .internal} (local or global) of the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal}.
      [[`text_string`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.text_string "tecplot.annotation.Text.text_string"){.reference .internal}                                                The text to be displayed in a text box.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text.type "tecplot.annotation.Text.type"){.reference .internal}                                                                     Normal or LaTeX text type setting.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[anchor]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.anchor "Link to this definition"){.headerlink}

:   Anchor location of this [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    Specify the anchor point, or fixed point, for the text object. As
    the text object grows or shrinks, the anchor location is fixed,
    while the rest of the box adjusts to accommodate the new size.
    (default = [[`TextAnchor.Left`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor.Left "tecplot.constant.TextAnchor.Left"){.reference
    .internal})

    There are nine possible anchor position points, corresponding to the
    left, right, and center positions on the headline, midline, and
    baseline of the text box.

    Example showing how to set the anchor of a [[`Text`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.anchor = tecplot.constant.TextAnchor.Center
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Text.position`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text.position "tecplot.annotation.Text.position"){.reference
    .internal}
    :::

    Type[:]{.colon}

    :   [[`TextAnchor`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextAnchor "tecplot.constant.TextAnchor"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[angle]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.angle "Link to this definition"){.headerlink}

:   Angle of the text box in degrees.

    The text angle is the orientation of the text relative to the axis.
    The angle is measured in degrees counter-clockwise from horizontal.
    Horizontal text is at zero degrees; vertical text is at 90 degrees.

    Example showing how to set the angle of a [[`Text`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.angle = 45
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (degrees counter-clockwise)

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.attached_map_index "Link to this definition"){.headerlink}

:   Index of the attached fieldmap or linemap.

    Example showing how to set the attached object [[`Index`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
    .internal} of a [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.attached_map_index = 1
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[box]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.box "Link to this definition"){.headerlink}

:   The frame and area around this [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    > <div>
    >
    > The text box is a rectangular frame drawn around the text. Note
    > that in order to show the text box, you must set TextBox.type to a
    > value other than [[`constant.TextBox.None_`{.xref .any .py
    > .py-attr .docutils .literal
    > .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox.None_ "tecplot.constant.TextBox.None_"){.reference
    > .internal}.
    >
    > </div>

    Example showing how to enable the text box for a [[`Text`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.box.type = tecplot.constant.TextBox.Filled
    :::
    ::::

    Type[:]{.colon}

    :   [[`annotation.TextBox`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.clipping "Link to this definition"){.headerlink}

:   [[`Clipping`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
    .internal} properties of the [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal}

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified your text position in the Frame coordinate system, the
    [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    Example showing how to set the clipping of a [[`Text`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.clipping = tecplot.constant.Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.color "Link to this definition"){.headerlink}

:   [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of the [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    Default: [[`Color.Black`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color.Black "tecplot.constant.Color.Black"){.reference
    .internal}. Example showing how to set the [[`Color`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} of a [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.color = tecplot.constant.Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[font]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.font "Link to this definition"){.headerlink}

:   Typeface properties for a [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`TextFont`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.annotation.TextFont "tecplot.annotation.TextFont"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[line_spacing]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.line_spacing "Link to this definition"){.headerlink}

:   Spacing between lines in the text box.

    Line spacing is dependent on the height of the text and the size
    unit system in which it is drawn. This example shows how to set the
    line spacing of a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.line_spacing = 4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external} (default = 1.0)

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.position "Link to this definition"){.headerlink}

:   Anchor position of the [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal}.

    This is the position of the [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} on the [[`Frame`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} and will be [\\((x,y)\\)]{.math .notranslate
    .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type (Cartesian or polar). This
    example shows how to set the anchor position of a [[`Text`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.position = (1.0, 2.0)
    :::
    ::::

    ::: {.admonition .seealso}
    See also

    [[`Text.anchor`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text.anchor "tecplot.annotation.Text.anchor"){.reference
    .internal}
    :::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system of the [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    The text object may be positioned using either the grid coordinate
    system or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}

    If the position_coordinate_system is [[`CoordSys.Frame`{.xref .any
    .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal}, then the size_units property must be
    [[`Units.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Frame "tecplot.constant.Units.Frame"){.reference
    .internal} or [[`Units.Point`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
    .internal}.

    The text object's position and text height are adjusted so that it
    remains identical to its visual appearance in the original
    coordinate and unit system.

    If the size units are [[`Units.Grid`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Grid "tecplot.constant.Units.Grid"){.reference
    .internal} and the position coordinate system is changed to
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal}, then the size units will be changed to
    [[`Units.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Frame "tecplot.constant.Units.Frame"){.reference
    .internal}. (default = CoordSys.Frame)

    Example showing how to set the position coordinate system for a
    [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> text = frame.add_text("abc")
        >>> text.position_coordinate_system = CoordSys.Grid
    :::
    ::::

    Example showing side effect if size units are
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal} and the coordinate system is changed to
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, Units
        >>> text = frame.add_text("abc")
        >>> text.font.size_units = Units.Grid
        >>> text.position_coordinate_system = CoordSys.Frame
        >>> text.position_coordinate_system
        CoordSys.Frame
        >>> text.font.size_units
        Units.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.scope "Link to this definition"){.headerlink}

:   The [[`Scope`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
    .internal} (local or global) of the [[`Text`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal}.

    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    with local scope are displayed only in the [[`frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If the [[annotation]{.std
    .std-ref}](#annotation){.reference .internal} is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the [[annotation]{.std .std-ref}](#annotation){.reference
    .internal} was created. (default: [[`Scope.Local`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example showing how to set the scope of a [[`Text`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.scope = tecplot.constant.Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[text_string]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.text_string "Link to this definition"){.headerlink}

:   The text to be displayed in a text box.

    You can embed Greek, Math, and User-defined characters into
    English-font strings by enclosing them with text formatting tags,
    together with the keyboard characters.

    The text formatting tags and their effects are as follows. Format
    tags are not case sensitive and may be either upper or lower case:

    > <div>
    >
    > - \<b\>...\</b\> - Boldface
    >
    > - \<i\>...\</i\> - Italic
    >
    > - \<verbatim\>...\</verbatim\> - Verbatim
    >
    > - \<sub\>...\</sub\> - Subscripts
    >
    > - \<sup\>...\</sup\> - Superscripts
    >
    > - \<greek\>...\</greek\> - Greek font.
    >
    > - \<math\>...\</math\> - Math font.
    >
    > - \<userdef\>...\</userdef\> - User-defined font.
    >
    > - \<helvetica\>...\</helvetica\> - Helvetica font.
    >
    > - \<times\>...\</times\> - Times font.
    >
    > - \<courier\>...\</courier\> - Courier font.
    >
    > </div>

    Not all fonts have Bold and/or Italic variants. For fonts that do
    not have these styles, the \<b\> and/or \<i\> tags may have no
    effect.

    Embedding and escaping special characters work only in English-font
    text; they have no effect in text created in Greek, Math, or
    User-defined character sets.

    You can produce subscripts or superscripts by enclosing any
    characters with \<sub\>...\</sub\> or \<sup\>...\</sup\>,
    respectively. [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} has only one level of superscripts and subscripts.
    Expressions requiring additional levels must be created by hand
    using multiple text objects. If you alternate subscripts and
    superscripts, [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} positions the superscript directly above the subscript.
    To produce consecutive superscripts, enclose all superscript
    characters in a single pair of tags.

    To insert a tag into text literally, precede the first angle bracket
    with a backslash (""). To insert a backslash in the text, just type
    two backslashes ("\"). This example shows how to set the text string
    of a [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.text_string
        'abc'
        >>> text.text_string ='def'
        >>> text.text_string
        'def'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Text.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Text.type "Link to this definition"){.headerlink}

:   Normal or LaTeX text type setting.

    Possible values are [[`TextType.Regular`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType.Regular "tecplot.constant.TextType.Regular"){.reference
    .internal} or [[`TextType.LaTeX`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType.LaTeX "tecplot.constant.TextType.LaTeX"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text(r'\alpha')
        >>> text.type = TextType.LaTeX
    :::
    ::::

    Type[:]{.colon}

    :   [[`TextType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextType "tecplot.constant.TextType"){.reference
        .internal}
:::

::: {#textbox .section}
### [TextBox](#id21){.toc-backref role="doc-backlink"}[¶](#textbox "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[TextBox]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[text]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/text.html#TextBox){.reference .internal}[¶](#tecplot.annotation.TextBox "Link to this definition"){.headerlink}

:   The box surrounding a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox.color "tecplot.annotation.TextBox.color"){.reference .internal}                                    Border line color of the text box.
      [[`corner_locations`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox.corner_locations "tecplot.annotation.TextBox.corner_locations"){.reference .internal}   [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Position of the four corners of the [[`text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}` `{.xref .any .py .py-class .docutils .literal .notranslate}[`box`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference .internal}.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox.fill_color "tecplot.annotation.TextBox.fill_color"){.reference .internal}                     Background fill color of the text box.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox.line_thickness "tecplot.annotation.TextBox.line_thickness"){.reference .internal}         Border line thickness.
      [[`margin`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox.margin "tecplot.annotation.TextBox.margin"){.reference .internal}                                 Margin between the text and the surrounding border.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextBox.type "tecplot.annotation.TextBox.type"){.reference .internal}                                       Style of the text box fill area and border.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[TextBox.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextBox.color "Link to this definition"){.headerlink}

:   Border line color of the text box.

    Default: [[`Color.Black`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color.Black "tecplot.constant.Color.Black"){.reference
    .internal}. Example showing how to set the outline color of the
    [[`text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}` `{.xref .any .py .py-class .docutils .literal
    .notranslate}[`box`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal} for a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, TextBox
        >>> text = frame.add_text("abc")
        >>> text.box.type = TextBox.Filled
        >>> text.box.color = Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[TextBox.]{.pre}]{.sig-prename .descclassname}[[corner_locations]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextBox.corner_locations "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Position of the four corners of the [[`text`{.xref .any
    .py .py-class .docutils .literal .notranslate}]{.pre}` `{.xref .any
    .py .py-class .docutils .literal .notranslate}[`box`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal}.

    **Note:** This property is read-only.

    The tuple consists of 8 [[`floats`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
    .external}:

    > <div>
    >
    > - x1: X-Coordinate for bottom left corner
    >
    > - y1: Y-Coordinate for bottom left corner
    >
    > - x2: X-Coordinate for bottom right corner
    >
    > - y2: Y-Coordinate for bottom right corner
    >
    > - x3: X-Coordinate for upper right corner
    >
    > - y3: Y-Coordinate for upper right corner
    >
    > - x4: X-Coordinate for upper left corner
    >
    > - y4: Y-Coordinate for upper left corner
    >
    > </div>

    There is no default, position will vary with text box properties.
    Example showing how to query position of the [[`text`{.xref .any .py
    .py-class .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
    .py-class .docutils .literal .notranslate}[`box`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal} for a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object. The values [`x1,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`...,`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`` y4` ``{.docutils .literal .notranslate}]{.pre}
    contain the corners of the text box:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.box.type = tecplot.constant.TextBox.Filled
        >>> x1,y1,x2,y2,x3,y3,x4,y4 = text.box.corner_locations
    :::
    ::::

<!-- -->

[[TextBox.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextBox.fill_color "Link to this definition"){.headerlink}

:   Background fill color of the text box.

    Example showing how to set the fill color of the [[`text`{.xref .any
    .py .py-class .docutils .literal .notranslate}]{.pre}` `{.xref .any
    .py .py-class .docutils .literal .notranslate}[`box`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal} for a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.box.type = TextBox.Filled
        >>> text.box.fill_color = tecplot.constant.Color.Blue
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[TextBox.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextBox.line_thickness "Link to this definition"){.headerlink}

:   Border line thickness.

    Must be greater than 0, default: [`0.1`{.docutils .literal
    .notranslate}]{.pre}. Example showing how to set the line thickness
    of the [[`text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}` `{.xref .any .py .py-class .docutils .literal
    .notranslate}[`box`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.box.line_thickness = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TextBox.]{.pre}]{.sig-prename .descclassname}[[margin]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextBox.margin "Link to this definition"){.headerlink}

:   Margin between the text and the surrounding border.

    Specify the margin as a percentage of the text character height.
    Margin must be greater than or equal to 0.0, and may be greater
    than 100. (default = 20.0)

    Example showing how to set the margin of the [[`text`{.xref .any .py
    .py-class .docutils .literal .notranslate}]{.pre}` `{.xref .any .py
    .py-class .docutils .literal .notranslate}[`box`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal} for a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.box.type = tecplot.constant.TextBox.Filled
        >>> text.box.margin = 0.5
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TextBox.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextBox.type "Link to this definition"){.headerlink}

:   Style of the text box fill area and border.

    The text box type can be set to the following:

    > <div>
    >
    > - [`None_`{.docutils .literal .notranslate}]{.pre} - (default) No
    >   box is drawn around the text.
    >
    > - 
    >
    >   Filled - A filled box around the text which is opaque. if you
    >
    >   :   place it over another [Tecplot
    >       360](https://www.tecplot.com/products/tecplot-360){.reference
    >       .external} object, the underlying object cannot be seen.
    >
    > - Hollow - A plain box around the text.
    >
    > </div>

    Example showing how to set the type of the text box for a
    [[`TextBox`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.TextBox "tecplot.annotation.TextBox"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text("abc")
        >>> text.box.type = tecplot.constant.TextBox.Filled
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.TextBox`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.TextBox "tecplot.constant.TextBox"){.reference
        .internal}
:::

::: {#textfont .section}
### [TextFont](#id22){.toc-backref role="doc-backlink"}[¶](#textfont "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[TextFont]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[text]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/text.html#TextFont){.reference .internal}[¶](#tecplot.annotation.TextFont "Link to this definition"){.headerlink}

:   Typeface and font settings for a [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`bold`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextFont.bold "tecplot.annotation.TextFont.bold"){.reference .internal}                     Use bold typeface in the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`italic`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextFont.italic "tecplot.annotation.TextFont.italic"){.reference .internal}               Use italic typeface of the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextFont.size "tecplot.annotation.TextFont.size"){.reference .internal}                     The text size in the currently defined text size units.
      [[`size_units`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextFont.size_units "tecplot.annotation.TextFont.size_units"){.reference .internal}   Units of the text character height.
      [[`typeface`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.TextFont.typeface "tecplot.annotation.TextFont.typeface"){.reference .internal}         The font family used by the [[`Text`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference .internal} object.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[TextFont.]{.pre}]{.sig-prename .descclassname}[[bold]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextFont.bold "Link to this definition"){.headerlink}

:   Use bold typeface in the [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    Example showing how to set the bold property of a [[`Text`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.font.bold = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TextFont.]{.pre}]{.sig-prename .descclassname}[[italic]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextFont.italic "Link to this definition"){.headerlink}

:   Use italic typeface of the [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    Example showing how to set the italic property of a [[`Text`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.font.italic = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TextFont.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextFont.size "Link to this definition"){.headerlink}

:   The text size in the currently defined text size units.

    Example showing how to set the text size of a [[`Text`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.font.size_units = tecplot.constant.Units.Point
        >>> text.font.size = 14
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[TextFont.]{.pre}]{.sig-prename .descclassname}[[size_units]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextFont.size_units "Link to this definition"){.headerlink}

:   Units of the text character height.

    [[`Units`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units "tecplot.constant.Units"){.reference
    .internal} may be one of the following:

    > <div>
    >
    > - [[`Units.Point`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
    >   .internal}: Specify character height in points.
    >
    > - 
    >
    >   [[`Units.Frame`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Frame "tecplot.constant.Units.Frame"){.reference .internal}: Specify character height as a percentage of frame
    >
    >   :   height
    >
    > - [[`Units.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Grid "tecplot.constant.Units.Grid"){.reference
    >   .internal}: Specify character height in grid units.
    >
    > </div>

    (default = [[`Units.Point`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Point "tecplot.constant.Units.Point"){.reference
    .internal})

    ::: {.admonition .note}
    Note

    - One point is 1/72nd of an inch.

    - 

      [[`Units.Grid`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Grid "tecplot.constant.Units.Grid"){.reference .internal} is available only if position_coordinate_system is

      :   [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
          .internal}

    - 

      The position coordinate system will be changed to [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference .internal}

      :   if size units is set to [[`Units.Grid`{.xref .any .py .py-attr
          .docutils .literal
          .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units.Grid "tecplot.constant.Units.Grid"){.reference
          .internal}
    :::

    Example showing how to set the units of the character height for a
    [[`Text`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> text = frame.add_text("abc")
        >>> text.position_coordinate_system = CoordSys.Grid
        >>> text.font.size_units = Units.Point
    :::
    ::::

    Type[:]{.colon}

    :   [[`Units`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Units "tecplot.constant.Units"){.reference
        .internal}

<!-- -->

[[TextFont.]{.pre}]{.sig-prename .descclassname}[[typeface]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.TextFont.typeface "Link to this definition"){.headerlink}

:   The font family used by the [[`Text`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object.

    For consistency across various platforms, [Tecplot
    360](https://www.tecplot.com/products/tecplot-360){.reference
    .external} guarantees that the following standard typeface names are
    available:

    > <div>
    >
    > - "Helvetica"
    >
    > - "Times"
    >
    > - "Courier"
    >
    > - "Greek"
    >
    > - "Math"
    >
    > - "User Defined"
    >
    > </div>

    Other typefaces may or may not be available depending on the
    TrueType fonts available. If the typeface or style is not available,
    a suitable replacement will be selected. This example shows how to
    set the typeface of a [[`Text`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Text "tecplot.annotation.Text"){.reference
    .internal} object to 'Times':

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> text = frame.add_text('abc')
        >>> text.font.typeface = 'Times'
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}
:::
::::::

:::::::::::: {#geometric-shapes .section}
[]{#geometry}

## [Geometric Shapes](#id7){.toc-backref role="doc-backlink"}[¶](#geometric-shapes "Link to this heading"){.headerlink}

::: {#circle .section}
### [Circle](#id8){.toc-backref role="doc-backlink"}[¶](#circle "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Circle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/geometry.html#Circle){.reference .internal}[¶](#tecplot.annotation.Circle "Link to this definition"){.headerlink}

:   A circle annotation attached to a [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_circle()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_circle "tecplot.layout.Frame.add_circle"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        frame = tp.active_frame()

        circle0 = frame.add_circle((40, 50), 12, CoordSys.Frame)
        circle1 = frame.add_circle((50, 50), 12, CoordSys.Frame)
        circle2 = frame.add_circle((60, 50), 12, CoordSys.Frame)

        circle0.fill_color = Color.Magenta
        circle1.fill_color = Color.Yellow
        circle2.fill_color = Color.Cyan

        tp.export.save_png('circle.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/circle.png"
    class="reference internal image-reference"><img
    src="../_images/circle.png" style="width: 300px;"
    alt="../_images/circle.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.attached_map_index "tecplot.annotation.Circle.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.clipping "tecplot.annotation.Circle.clipping"){.reference .internal}                                                         Clip geometry to the axes or frame for 2D plots.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.color "tecplot.annotation.Circle.color"){.reference .internal}                                                                  Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.draw_order "tecplot.annotation.Circle.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.fill_color "tecplot.annotation.Circle.fill_color"){.reference .internal}                                                   Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.line_pattern "tecplot.annotation.Circle.line_pattern"){.reference .internal}                                             Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.line_thickness "tecplot.annotation.Circle.line_thickness"){.reference .internal}                                       Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.macro_function "tecplot.annotation.Circle.macro_function"){.reference .internal}                                       An associated macro function.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.num_points "tecplot.annotation.Circle.num_points"){.reference .internal}                                                   Number of points to use when creating the curved shape.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.pattern_length "tecplot.annotation.Circle.pattern_length"){.reference .internal}                                       Length of the line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.position "tecplot.annotation.Circle.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.position_coordinate_system "tecplot.annotation.Circle.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`radius`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.radius "tecplot.annotation.Circle.radius"){.reference .internal}                                                               Length of the radius.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.scope "tecplot.annotation.Circle.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Circle.type "tecplot.annotation.Circle.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.clipping "Link to this definition"){.headerlink}

:   Clip geometry to the axes or frame for 2D plots.

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified the position in the Frame coordinate system, the
    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[Annotations]{.std .std-ref}](#annotation){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    ::: {.admonition .warning}
    Warning

    For 3D and line plots the viewport is the same as the frame and so
    clipping to the viewport or the frame will have no apparent affect.
    In cartesian 2D plots, clipping to the axes
    ([[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}) is only available when the position coordinate system is
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}.
    :::

    Example of clipping a circle to the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Clipping, CoordSys
        >>> geom = frame.add_circle((0.5, 0.5), 0.55, CoordSys.Grid)
        >>> geom.clipping = Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.num_points "Link to this definition"){.headerlink}

:   Number of points to use when creating the curved shape.

    This is the number of segments along the edge plus one. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.num_points = 300
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[radius]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.radius "Link to this definition"){.headerlink}

:   Length of the radius.

    This will be in the coordinate system specified by
    [[`Circle.position_coordinate_system`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Circle.position_coordinate_system "tecplot.annotation.Circle.position_coordinate_system"){.reference
    .internal}. This example creates a circle of radius 5 and then
    doubles it to 10 later:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((20, 30), 5, CoordSys.Frame)
        >>> geom.radius = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Circle.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Circle.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#ellipse .section}
### [Ellipse](#id9){.toc-backref role="doc-backlink"}[¶](#ellipse "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Ellipse]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/geometry.html#Ellipse){.reference .internal}[¶](#tecplot.annotation.Ellipse "Link to this definition"){.headerlink}

:   An ellipse annotation attached to a [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_ellipse()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_ellipse "tecplot.layout.Frame.add_ellipse"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        frame = tp.active_frame()

        ellipse0 = frame.add_ellipse((40, 45), (10, 12), CoordSys.Frame)
        ellipse1 = frame.add_ellipse((50, 50), (10, 16), CoordSys.Frame)
        ellipse2 = frame.add_ellipse((60, 55), (10, 20), CoordSys.Frame)

        ellipse0.fill_color = Color.Magenta
        ellipse1.fill_color = Color.Yellow
        ellipse2.fill_color = Color.Cyan

        tp.export.save_png('ellipse.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/ellipse.png"
    class="reference internal image-reference"><img
    src="../_images/ellipse.png" style="width: 300px;"
    alt="../_images/ellipse.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.attached_map_index "tecplot.annotation.Ellipse.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.clipping "tecplot.annotation.Ellipse.clipping"){.reference .internal}                                                         Clip geometry to the axes or frame for 2D plots.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.color "tecplot.annotation.Ellipse.color"){.reference .internal}                                                                  Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.draw_order "tecplot.annotation.Ellipse.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.fill_color "tecplot.annotation.Ellipse.fill_color"){.reference .internal}                                                   Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.line_pattern "tecplot.annotation.Ellipse.line_pattern"){.reference .internal}                                             Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.line_thickness "tecplot.annotation.Ellipse.line_thickness"){.reference .internal}                                       Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.macro_function "tecplot.annotation.Ellipse.macro_function"){.reference .internal}                                       An associated macro function.
      [[`num_points`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.num_points "tecplot.annotation.Ellipse.num_points"){.reference .internal}                                                   Number of points to use when creating the curved shape.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.pattern_length "tecplot.annotation.Ellipse.pattern_length"){.reference .internal}                                       Length of the line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.position "tecplot.annotation.Ellipse.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.position_coordinate_system "tecplot.annotation.Ellipse.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.scope "tecplot.annotation.Ellipse.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.size "tecplot.annotation.Ellipse.size"){.reference .internal}                                                                     Size [\\((h\_{axis}, v\_{axis})\\)]{.math .notranslate .nohighlight} of the ellipse.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Ellipse.type "tecplot.annotation.Ellipse.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.clipping "Link to this definition"){.headerlink}

:   Clip geometry to the axes or frame for 2D plots.

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified the position in the Frame coordinate system, the
    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[Annotations]{.std .std-ref}](#annotation){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    ::: {.admonition .warning}
    Warning

    For 3D and line plots the viewport is the same as the frame and so
    clipping to the viewport or the frame will have no apparent affect.
    In cartesian 2D plots, clipping to the axes
    ([[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}) is only available when the position coordinate system is
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}.
    :::

    Example of clipping a circle to the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Clipping, CoordSys
        >>> geom = frame.add_circle((0.5, 0.5), 0.55, CoordSys.Grid)
        >>> geom.clipping = Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[num_points]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.num_points "Link to this definition"){.headerlink}

:   Number of points to use when creating the curved shape.

    This is the number of segments along the edge plus one. Example
    usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.num_points = 300
    :::
    ::::

    Type[:]{.colon}

    :   [[`int`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.size "Link to this definition"){.headerlink}

:   Size [\\((h\_{axis}, v\_{axis})\\)]{.math .notranslate .nohighlight}
    of the ellipse.

    This is the horizontal and vertical axis lengths of the ellipse and
    will be in the coordinate system specified by
    [[`Ellipse.position_coordinate_system`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Ellipse.position_coordinate_system "tecplot.annotation.Ellipse.position_coordinate_system"){.reference
    .internal}. This example creates an ellipse with [\\((h\_{axis},
    v\_{axis})\\)]{.math .notranslate .nohighlight} of [\\((5,
    10)\\)]{.math .notranslate .nohighlight} and changes it to [\\((10,
    20)\\)]{.math .notranslate .nohighlight} later:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_ellipse((50, 50), (5, 10), CoordSys.Frame)
        >>> geom.size = (10, 20)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Ellipse.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Ellipse.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#rectangle .section}
### [Rectangle](#id10){.toc-backref role="doc-backlink"}[¶](#rectangle "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Rectangle]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/geometry.html#Rectangle){.reference .internal}[¶](#tecplot.annotation.Rectangle "Link to this definition"){.headerlink}

:   A rectangle annotation attached to a [[`Frame`{.xref .any .py
    .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_rectangle()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_rectangle "tecplot.layout.Frame.add_rectangle"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        frame = tp.active_frame()

        rectangle0 = frame.add_rectangle((40, 45), (20, 12), CoordSys.Frame)
        rectangle1 = frame.add_rectangle((50, 50), (20, 16), CoordSys.Frame)
        rectangle2 = frame.add_rectangle((60, 55), (20, 20), CoordSys.Frame)

        rectangle0.fill_color = Color.Magenta
        rectangle1.fill_color = Color.Yellow
        rectangle2.fill_color = Color.Cyan

        tp.export.save_png('rectangle.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/rectangle.png"
    class="reference internal image-reference"><img
    src="../_images/rectangle.png" style="width: 300px;"
    alt="../_images/rectangle.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.attached_map_index "tecplot.annotation.Rectangle.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.clipping "tecplot.annotation.Rectangle.clipping"){.reference .internal}                                                         Clip geometry to the axes or frame for 2D plots.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.color "tecplot.annotation.Rectangle.color"){.reference .internal}                                                                  Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.draw_order "tecplot.annotation.Rectangle.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.fill_color "tecplot.annotation.Rectangle.fill_color"){.reference .internal}                                                   Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.line_pattern "tecplot.annotation.Rectangle.line_pattern"){.reference .internal}                                             Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.line_thickness "tecplot.annotation.Rectangle.line_thickness"){.reference .internal}                                       Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.macro_function "tecplot.annotation.Rectangle.macro_function"){.reference .internal}                                       An associated macro function.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.pattern_length "tecplot.annotation.Rectangle.pattern_length"){.reference .internal}                                       Length of the line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.position "tecplot.annotation.Rectangle.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.position_coordinate_system "tecplot.annotation.Rectangle.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.scope "tecplot.annotation.Rectangle.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.size "tecplot.annotation.Rectangle.size"){.reference .internal}                                                                     Size [\\((width, height)\\)]{.math .notranslate .nohighlight} of the rectangle.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Rectangle.type "tecplot.annotation.Rectangle.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.clipping "Link to this definition"){.headerlink}

:   Clip geometry to the axes or frame for 2D plots.

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified the position in the Frame coordinate system, the
    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[Annotations]{.std .std-ref}](#annotation){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    ::: {.admonition .warning}
    Warning

    For 3D and line plots the viewport is the same as the frame and so
    clipping to the viewport or the frame will have no apparent affect.
    In cartesian 2D plots, clipping to the axes
    ([[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}) is only available when the position coordinate system is
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}.
    :::

    Example of clipping a circle to the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Clipping, CoordSys
        >>> geom = frame.add_circle((0.5, 0.5), 0.55, CoordSys.Grid)
        >>> geom.clipping = Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.size "Link to this definition"){.headerlink}

:   Size [\\((width, height)\\)]{.math .notranslate .nohighlight} of the
    rectangle.

    This is the width and height of the rectangle and will be in the
    coordinate system specified by
    [[`Rectangle.position_coordinate_system`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Rectangle.position_coordinate_system "tecplot.annotation.Rectangle.position_coordinate_system"){.reference
    .internal}. This example creates a rectangle with [\\((width,
    height)\\)]{.math .notranslate .nohighlight} of [\\((5,
    10)\\)]{.math .notranslate .nohighlight} and changes it to [\\((10,
    20)\\)]{.math .notranslate .nohighlight} later:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_rectangle((50, 50), (5, 10), CoordSys.Frame)
        >>> geom.size = (10, 20)
    :::
    ::::

    Type[:]{.colon}

    :   [[`tuple`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Rectangle.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Rectangle.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#square .section}
### [Square](#id11){.toc-backref role="doc-backlink"}[¶](#square "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Square]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/geometry.html#Square){.reference .internal}[¶](#tecplot.annotation.Square "Link to this definition"){.headerlink}

:   A square annotation attached to a [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_square()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_square "tecplot.layout.Frame.add_square"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        frame = tp.active_frame()

        square0 = frame.add_square((40, 40), 15, CoordSys.Frame)
        square1 = frame.add_square((50, 50), 15, CoordSys.Frame)
        square2 = frame.add_square((60, 60), 15, CoordSys.Frame)

        square0.fill_color = Color.Magenta
        square1.fill_color = Color.Yellow
        square2.fill_color = Color.Cyan

        tp.export.save_png('square.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/square.png"
    class="reference internal image-reference"><img
    src="../_images/square.png" style="width: 300px;"
    alt="../_images/square.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.attached_map_index "tecplot.annotation.Square.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.clipping "tecplot.annotation.Square.clipping"){.reference .internal}                                                         Clip geometry to the axes or frame for 2D plots.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.color "tecplot.annotation.Square.color"){.reference .internal}                                                                  Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.draw_order "tecplot.annotation.Square.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.fill_color "tecplot.annotation.Square.fill_color"){.reference .internal}                                                   Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.line_pattern "tecplot.annotation.Square.line_pattern"){.reference .internal}                                             Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.line_thickness "tecplot.annotation.Square.line_thickness"){.reference .internal}                                       Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.macro_function "tecplot.annotation.Square.macro_function"){.reference .internal}                                       An associated macro function.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.pattern_length "tecplot.annotation.Square.pattern_length"){.reference .internal}                                       Length of the line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.position "tecplot.annotation.Square.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.position_coordinate_system "tecplot.annotation.Square.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.scope "tecplot.annotation.Square.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.size "tecplot.annotation.Square.size"){.reference .internal}                                                                     Length of one side of the square.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Square.type "tecplot.annotation.Square.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.clipping "Link to this definition"){.headerlink}

:   Clip geometry to the axes or frame for 2D plots.

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified the position in the Frame coordinate system, the
    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[Annotations]{.std .std-ref}](#annotation){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    ::: {.admonition .warning}
    Warning

    For 3D and line plots the viewport is the same as the frame and so
    clipping to the viewport or the frame will have no apparent affect.
    In cartesian 2D plots, clipping to the axes
    ([[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}) is only available when the position coordinate system is
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}.
    :::

    Example of clipping a circle to the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Clipping, CoordSys
        >>> geom = frame.add_circle((0.5, 0.5), 0.55, CoordSys.Grid)
        >>> geom.clipping = Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.size "Link to this definition"){.headerlink}

:   Length of one side of the square.

    This will be in the coordinate system specified by
    [[`Square.position_coordinate_system`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Square.position_coordinate_system "tecplot.annotation.Square.position_coordinate_system"){.reference
    .internal}. This example creates a square of side-length 5 and then
    doubles it to 10 later:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_square((50, 50), 5, CoordSys.Frame)
        >>> geom.radius = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Square.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Square.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#polyline2d .section}
### [Polyline2D](#id12){.toc-backref role="doc-backlink"}[¶](#polyline2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Polyline2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*, *[[mpolyline]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/polyline.html#Polyline2D){.reference .internal}[¶](#tecplot.annotation.Polyline2D "Link to this definition"){.headerlink}

:   A series of connected points in 2D.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_polyline()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import math

        import tecplot as tp
        from tecplot.constant import *

        # create sine-wave in frame % coordinates
        xx = list(range(10, 90))
        yy = [10 * math.sin(x / 5) + 50 for x in xx]
        points = [(x, y) for x, y in zip(xx, yy)]

        frame = tp.active_frame()

        line = frame.add_polyline(points, coord_sys=CoordSys.Frame)
        line.line_thickness = 2
        line.color = Color.Blue

        tp.export.save_png('polyline2d.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/polyline2d.png"
    class="reference internal image-reference"><img
    src="../_images/polyline2d.png" style="width: 300px;"
    alt="../_images/polyline2d.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`arrowhead`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.arrowhead "tecplot.annotation.Polyline2D.arrowhead"){.reference .internal}                                                      Style control for arrowheads.
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.attached_map_index "tecplot.annotation.Polyline2D.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.clipping "tecplot.annotation.Polyline2D.clipping"){.reference .internal}                                                         Clip geometry to the axes or frame for 2D plots.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.color "tecplot.annotation.Polyline2D.color"){.reference .internal}                                                                  Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.draw_order "tecplot.annotation.Polyline2D.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.fill_color "tecplot.annotation.Polyline2D.fill_color"){.reference .internal}                                                   Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.line_pattern "tecplot.annotation.Polyline2D.line_pattern"){.reference .internal}                                             Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.line_thickness "tecplot.annotation.Polyline2D.line_thickness"){.reference .internal}                                       Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.macro_function "tecplot.annotation.Polyline2D.macro_function"){.reference .internal}                                       An associated macro function.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.pattern_length "tecplot.annotation.Polyline2D.pattern_length"){.reference .internal}                                       Length of the line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.position "tecplot.annotation.Polyline2D.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.position_coordinate_system "tecplot.annotation.Polyline2D.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.scope "tecplot.annotation.Polyline2D.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.type "tecplot.annotation.Polyline2D.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[arrowhead]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.arrowhead "Link to this definition"){.headerlink}

:   Style control for arrowheads.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadAttachment, ArrowheadStyle
        >>> polyline.arrowhead.attachment = ArrowheadAttachment.AtEnd
        >>> polyline.arrowhead.style = ArrowheadStyle.Filled
    :::
    ::::

    Type[:]{.colon}

    :   [[`Arrowhead`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.annotation.Arrowhead "tecplot.annotation.Arrowhead"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.clipping "Link to this definition"){.headerlink}

:   Clip geometry to the axes or frame for 2D plots.

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified the position in the Frame coordinate system, the
    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[Annotations]{.std .std-ref}](#annotation){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    ::: {.admonition .warning}
    Warning

    For 3D and line plots the viewport is the same as the frame and so
    clipping to the viewport or the frame will have no apparent affect.
    In cartesian 2D plots, clipping to the axes
    ([[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}) is only available when the position coordinate system is
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}.
    :::

    Example of clipping a circle to the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Clipping, CoordSys
        >>> geom = frame.add_circle((0.5, 0.5), 0.55, CoordSys.Grid)
        >>> geom.clipping = Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Polyline2D.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline2D.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#polyline3d .section}
### [Polyline3D](#id13){.toc-backref role="doc-backlink"}[¶](#polyline3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Polyline3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[index]{.pre}]{.n}*, *[[mpolyline]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/polyline.html#Polyline3D){.reference .internal}[¶](#tecplot.annotation.Polyline3D "Link to this definition"){.headerlink}

:   A series of connected points in 3D.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_polyline()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import math

        import tecplot as tp
        from tecplot.constant import *

        # create helix polyline in data coordinates
        zz = [z / 2000 for z in range(1000)]
        xx = [0.5 * math.cos(z * 50) for z in zz]
        yy = [0.5 * math.sin(z * 50) for z in zz]
        points = [(x, y, z) for x, y, z in zip(xx, yy, zz)]

        frame = tp.active_frame()
        dataset = frame.create_dataset('Dataset Name', ['x', 'y', 'z'])
        dataset.add_ordered_zone('Zone Name', (10, 10, 10))
        plot = frame.plot(PlotType.Cartesian3D)
        plot.activate()

        line = frame.add_polyline(points)
        line.line_thickness = 2
        line.color = Color.Chartreuse

        tp.export.save_png('polyline3d.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/polyline3d.png"
    class="reference internal image-reference"><img
    src="../_images/polyline3d.png" style="width: 300px;"
    alt="../_images/polyline3d.png" /></a>
    </figure>

    **Attributes**

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.attached_map_index "tecplot.annotation.Polyline3D.attached_map_index"){.reference .internal}   Index to the associated fieldmap or linemap.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.color "tecplot.annotation.Polyline3D.color"){.reference .internal}                                          Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.fill_color "tecplot.annotation.Polyline3D.fill_color"){.reference .internal}                           Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.line_pattern "tecplot.annotation.Polyline3D.line_pattern"){.reference .internal}                     Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.line_thickness "tecplot.annotation.Polyline3D.line_thickness"){.reference .internal}               Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.macro_function "tecplot.annotation.Polyline3D.macro_function"){.reference .internal}               An associated macro function.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.pattern_length "tecplot.annotation.Polyline3D.pattern_length"){.reference .internal}               Length of the line pattern.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.scope "tecplot.annotation.Polyline3D.scope"){.reference .internal}                                          Display annotation in all frames with the same data.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Polyline3D.type "tecplot.annotation.Polyline3D.type"){.reference .internal}                                             The type of this annotation (read-only).
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Polyline3D.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Polyline3D.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#multipolyline2d .section}
### [MultiPolyline2D](#id14){.toc-backref role="doc-backlink"}[¶](#multipolyline2d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[MultiPolyline2D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/polyline.html#MultiPolyline2D){.reference .internal}[¶](#tecplot.annotation.MultiPolyline2D "Link to this definition"){.headerlink}

:   A collection of [[`Polyline2D`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Polyline2D "tecplot.annotation.Polyline2D"){.reference
    .internal} objects.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_polyline()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import math

        import tecplot as tp
        from tecplot.constant import *

        # create sine-wave in frame % coordinates
        xx = list(range(10, 90))
        yy = [10 * math.sin(x / 5) + 50 for x in xx]
        points = [(x, y) for x, y in zip(xx, yy)]

        # create new line with points shifted up and to the left
        shifted_points = [(x + 5, y + 5) for x, y in points]

        frame = tp.active_frame()

        multi_line = frame.add_polyline(points, shifted_points, coord_sys=CoordSys.Frame)
        multi_line.line_thickness = 2
        multi_line.color = Color.Blue

        tp.export.save_png('multipolyline2d.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/multipolyline2d.png"
    class="reference internal image-reference"><img
    src="../_images/multipolyline2d.png" style="width: 300px;"
    alt="../_images/multipolyline2d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`arrowhead`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.arrowhead "tecplot.annotation.MultiPolyline2D.arrowhead"){.reference .internal}                                                      Style control for arrowheads.
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.attached_map_index "tecplot.annotation.MultiPolyline2D.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`clipping`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.clipping "tecplot.annotation.MultiPolyline2D.clipping"){.reference .internal}                                                         Clip geometry to the axes or frame for 2D plots.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.color "tecplot.annotation.MultiPolyline2D.color"){.reference .internal}                                                                  Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.draw_order "tecplot.annotation.MultiPolyline2D.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.fill_color "tecplot.annotation.MultiPolyline2D.fill_color"){.reference .internal}                                                   Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.line_pattern "tecplot.annotation.MultiPolyline2D.line_pattern"){.reference .internal}                                             Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.line_thickness "tecplot.annotation.MultiPolyline2D.line_thickness"){.reference .internal}                                       Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.macro_function "tecplot.annotation.MultiPolyline2D.macro_function"){.reference .internal}                                       An associated macro function.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.pattern_length "tecplot.annotation.MultiPolyline2D.pattern_length"){.reference .internal}                                       Length of the line pattern.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.position "tecplot.annotation.MultiPolyline2D.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.position_coordinate_system "tecplot.annotation.MultiPolyline2D.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.scope "tecplot.annotation.MultiPolyline2D.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline2D.type "tecplot.annotation.MultiPolyline2D.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[arrowhead]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.arrowhead "Link to this definition"){.headerlink}

:   Style control for arrowheads.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadAttachment, ArrowheadStyle
        >>> multi_polyline.arrowhead.attachment = ArrowheadAttachment.AtEnd
        >>> multi_polyline.arrowhead.style = ArrowheadStyle.Filled
    :::
    ::::

    Type[:]{.colon}

    :   [[`Arrowhead`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](#tecplot.annotation.Arrowhead "tecplot.annotation.Arrowhead"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[clipping]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.clipping "Link to this definition"){.headerlink}

:   Clip geometry to the axes or frame for 2D plots.

    Clipping refers to displaying only that portion of an object that
    falls within a specified clipping region of the plot. If you have
    specified the position in the Frame coordinate system, the
    [[Annotations]{.std .std-ref}](#annotation){.reference .internal}
    will be clipped to the frame. Default:
    [[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}.

    If you have specified the Grid coordinate system, you can choose to
    clip your [[Annotations]{.std .std-ref}](#annotation){.reference
    .internal} to the frame or the viewport. The size of the viewport
    depends on the plot type as follows:

    > <div>
    >
    > - 
    >
    >   3D Cartesian - The viewport is the same as the frame, so viewport
    >
    >   :   clipping is the same as frame clipping.
    >
    > - 
    >
    >   2D Cartesian/XY Line - The viewport is defined by the extents of
    >
    >   :   the X and Y axes.
    >
    > - 
    >
    >   Polar Line/Sketch - By default, the viewport is the same as the
    >
    >   :   frame.
    >
    > </div>

    ::: {.admonition .warning}
    Warning

    For 3D and line plots the viewport is the same as the frame and so
    clipping to the viewport or the frame will have no apparent affect.
    In cartesian 2D plots, clipping to the axes
    ([[`Clipping.ClipToViewport`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping.ClipToViewport "tecplot.constant.Clipping.ClipToViewport"){.reference
    .internal}) is only available when the position coordinate system is
    [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}.
    :::

    Example of clipping a circle to the frame:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Clipping, CoordSys
        >>> geom = frame.add_circle((0.5, 0.5), 0.55, CoordSys.Grid)
        >>> geom.clipping = Clipping.ClipToFrame
    :::
    ::::

    Type[:]{.colon}

    :   [[`Clipping`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Clipping "tecplot.constant.Clipping"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[MultiPolyline2D.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline2D.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#multipolyline3d .section}
### [MultiPolyline3D](#id15){.toc-backref role="doc-backlink"}[¶](#multipolyline3d "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[MultiPolyline3D]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/polyline.html#MultiPolyline3D){.reference .internal}[¶](#tecplot.annotation.MultiPolyline3D "Link to this definition"){.headerlink}

:   A collection of [[`Polyline3D`{.xref .any .py .py-class .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Polyline3D "tecplot.annotation.Polyline3D"){.reference
    .internal} objects.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_polyline()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import math

        import tecplot as tp
        from tecplot.constant import *

        # create double-helix multi-polyline in data coordinates
        zz = [z / 2000 for z in range(1000)]
        xx = [0.5 * math.cos(z * 50) for z in zz]
        yy = [0.5 * math.sin(z * 50) for z in zz]
        points = [(x, y, z) for x, y, z in zip(xx, yy, zz)]
        points_shifted = [(x, y, z + 0.02) for x, y, z in zip(xx, yy, zz)]

        frame = tp.active_frame()
        dataset = frame.create_dataset('Dataset Name', ['x', 'y', 'z'])
        dataset.add_ordered_zone('Zone Name', (10, 10, 10))
        plot = frame.plot(PlotType.Cartesian3D)
        plot.activate()

        line = frame.add_polyline(points, points_shifted)
        line.line_thickness = 2
        line.color = Color.Turquoise

        tp.export.save_png('multipolyline3d.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/multipolyline3d.png"
    class="reference internal image-reference"><img
    src="../_images/multipolyline3d.png" style="width: 300px;"
    alt="../_images/multipolyline3d.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.attached_map_index "tecplot.annotation.MultiPolyline3D.attached_map_index"){.reference .internal}   Index to the associated fieldmap or linemap.
      [[`color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.color "tecplot.annotation.MultiPolyline3D.color"){.reference .internal}                                          Line [[`Color`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference .internal}.
      [[`fill_color`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.fill_color "tecplot.annotation.MultiPolyline3D.fill_color"){.reference .internal}                           Background fill color.
      [[`line_pattern`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.line_pattern "tecplot.annotation.MultiPolyline3D.line_pattern"){.reference .internal}                     Pattern used for drawing lines or edges.
      [[`line_thickness`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.line_thickness "tecplot.annotation.MultiPolyline3D.line_thickness"){.reference .internal}               Thickness of lines or edges.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.macro_function "tecplot.annotation.MultiPolyline3D.macro_function"){.reference .internal}               An associated macro function.
      [[`pattern_length`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.pattern_length "tecplot.annotation.MultiPolyline3D.pattern_length"){.reference .internal}               Length of the line pattern.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.scope "tecplot.annotation.MultiPolyline3D.scope"){.reference .internal}                                          Display annotation in all frames with the same data.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.MultiPolyline3D.type "tecplot.annotation.MultiPolyline3D.type"){.reference .internal}                                             The type of this annotation (read-only).
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.color "Link to this definition"){.headerlink}

:   Line [[`Color`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal}.

    This example shows how to change the edge or line [[`Color`{.xref
    .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[fill_color]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.fill_color "Link to this definition"){.headerlink}

:   Background fill color.

    This example shows how to change the area fill [[`Color`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
    .internal} to red. To turn off filling the geometry, set this
    attribute to [[`None`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
    .external}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Color, CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.fill_color = Color.Red
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.Color`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Color "tecplot.constant.Color"){.reference
        .internal}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[line_pattern]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.line_pattern "Link to this definition"){.headerlink}

:   Pattern used for drawing lines or edges.

    This example shows how to change the line pattern:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys, LinePattern
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_pattern = LinePattern.DashDot
    :::
    ::::

    Type[:]{.colon}

    :   [[`LinePattern`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LinePattern "tecplot.constant.LinePattern"){.reference
        .internal}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[line_thickness]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.line_thickness "Link to this definition"){.headerlink}

:   Thickness of lines or edges.

    This example shows how to change the line thickness:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.line_thickness = 4.0
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[pattern_length]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.pattern_length "Link to this definition"){.headerlink}

:   Length of the line pattern.

    This example shows how to change the pattern length:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> geom = frame.add_circle((50, 50), 10, CoordSys.Frame)
        >>> geom.pattern_length = 1.2
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[MultiPolyline3D.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.MultiPolyline3D.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}
:::

::: {#arrowhead .section}
### [Arrowhead](#id16){.toc-backref role="doc-backlink"}[¶](#arrowhead "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Arrowhead]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[polyline]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/polyline.html#Arrowhead){.reference .internal}[¶](#tecplot.annotation.Arrowhead "Link to this definition"){.headerlink}

:   Polyline arrowhead properties.

    ::: {.admonition .seealso}
    See also

    [[`Frame.add_polyline()`{.xref .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_polyline "tecplot.layout.Frame.add_polyline"){.reference
    .internal}
    :::

    :::: {.highlight-python .notranslate}
    ::: highlight
        import tecplot as tp
        from tecplot.constant import *

        frame = tp.active_frame()

        line0 = frame.add_polyline([[30,30], [50,60]], coord_sys=CoordSys.Frame)
        line1 = frame.add_polyline([[35,30], [55,60]], coord_sys=CoordSys.Frame)
        line2 = frame.add_polyline([[40,30], [60,60]], coord_sys=CoordSys.Frame)

        line0.arrowhead.attachment = ArrowheadAttachment.AtEnd
        line1.arrowhead.attachment = ArrowheadAttachment.AtEnd
        line2.arrowhead.attachment = ArrowheadAttachment.AtEnd

        line0.line_thickness = 2
        line1.line_thickness = 2
        line2.line_thickness = 2

        tp.export.save_png('arrowhead.png', 600)
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/arrowhead.png"
    class="reference internal image-reference"><img
    src="../_images/arrowhead.png" style="width: 300px;"
    alt="../_images/arrowhead.png" /></a>
    </figure>

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------
      [[`angle`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Arrowhead.angle "tecplot.annotation.Arrowhead.angle"){.reference .internal}                  The angle of the arrow lines in degrees.
      [[`attachment`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Arrowhead.attachment "tecplot.annotation.Arrowhead.attachment"){.reference .internal}   Location of arrowhead on the polyline.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Arrowhead.size "tecplot.annotation.Arrowhead.size"){.reference .internal}                     Size of the arrowhead on the polyline.
      [[`style`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Arrowhead.style "tecplot.annotation.Arrowhead.style"){.reference .internal}                  The style of the arrowhead on the polyline.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------

<!-- -->

[[Arrowhead.]{.pre}]{.sig-prename .descclassname}[[angle]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Arrowhead.angle "Link to this definition"){.headerlink}

:   The angle of the arrow lines in degrees.

    This is the angle that one side of the arrowhead makes with the
    vector, i.e. the apex angle is twice the arrowhead angle:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadAttachment
        >>> polyline.arrowhead.attachment = ArrowheadAttachment.AtEnd
        >>> polyline.arrowhead.angle = 45
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Arrowhead.]{.pre}]{.sig-prename .descclassname}[[attachment]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Arrowhead.attachment "Link to this definition"){.headerlink}

:   Location of arrowhead on the polyline.

    Possible values are [[`ArrowheadAttachment.None_`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadAttachment.None_ "tecplot.constant.ArrowheadAttachment.None_"){.reference
    .internal}, [[`ArrowheadAttachment.AtBeginning`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadAttachment.AtBeginning "tecplot.constant.ArrowheadAttachment.AtBeginning"){.reference
    .internal}, [[`ArrowheadAttachment.AtEnd`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadAttachment.AtEnd "tecplot.constant.ArrowheadAttachment.AtEnd"){.reference
    .internal} and [[`ArrowheadAttachment.AtBothEnds`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadAttachment.AtBothEnds "tecplot.constant.ArrowheadAttachment.AtBothEnds"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadAttachment
        >>> polyline.arrowhead.attachment = ArrowheadAttachment.AtEnd
    :::
    ::::

    Type[:]{.colon}

    :   [[`ArrowheadAttachment`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadAttachment "tecplot.constant.ArrowheadAttachment"){.reference
        .internal}

<!-- -->

[[Arrowhead.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Arrowhead.size "Link to this definition"){.headerlink}

:   Size of the arrowhead on the polyline.

    This is in the coordinate system specified by the
    [[`position_coordinate_system`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Polyline2D.position_coordinate_system "tecplot.annotation.Polyline2D.position_coordinate_system"){.reference
    .internal} attribute of the polyline:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadAttachment
        >>> polyline.arrowhead.attachment = ArrowheadAttachment.AtEnd
        >>> polyline.arrowhead.size = 10
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Arrowhead.]{.pre}]{.sig-prename .descclassname}[[style]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Arrowhead.style "Link to this definition"){.headerlink}

:   The style of the arrowhead on the polyline.

    Possible values are [[`ArrowheadStyle.Plain`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle.Plain "tecplot.constant.ArrowheadStyle.Plain"){.reference
    .internal}, [[`ArrowheadStyle.Hollow`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle.Hollow "tecplot.constant.ArrowheadStyle.Hollow"){.reference
    .internal} and [[`ArrowheadStyle.Filled`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle.Filled "tecplot.constant.ArrowheadStyle.Filled"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ArrowheadAttachment, ArrowheadStyle
        >>> polyline.arrowhead.attachment = ArrowheadAttachment.AtEnd
        >>> polyline.arrowhead.style = ArrowheadStyle.Filled
    :::
    ::::

    Type[:]{.colon}

    :   [[`ArrowheadStyle`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ArrowheadStyle "tecplot.constant.ArrowheadStyle"){.reference
        .internal}
:::
::::::::::::

::::: {#images .section}
## [Images](#id17){.toc-backref role="doc-backlink"}[¶](#images "Link to this heading"){.headerlink}

::: {#image .section}
### [Image](#id18){.toc-backref role="doc-backlink"}[¶](#image "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[Image]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/image.html#Image){.reference .internal}[¶](#tecplot.annotation.Image "Link to this definition"){.headerlink}

:   Image annotation.

    This example shows creating an image from a 2D plot and overlaying
    it on the 3D plot of the same data.

    :::: {.highlight-python .notranslate}
    ::: highlight
        import os

        import tecplot as tp
        from tecplot.constant import PlotType

        examples_dir = tp.session.tecplot_examples_directory()
        datafile = os.path.join(examples_dir, 'SimpleData', 'F18.plt')
        dataset = tp.data.load_tecplot(datafile)

        frame = tp.active_frame()

        plot2d = frame.plot(PlotType.Cartesian2D)
        plot2d.activate()
        plot2d.show_contour = True
        plot2d.contour(0).colormap_name = 'Sequential - Blue'
        plot2d.contour(0).variable = dataset.variable('S')
        tp.export.save_png('embedded_image.png')

        plot3d = frame.plot(PlotType.Cartesian3D)
        plot3d.activate()
        plot3d.show_contour = True
        frame.add_image('embedded_image.png', (5, 55), 40)

        tp.export.save_png('image.png')
    :::
    ::::

    <figure class="align-default" style="width: 300px">
    <a href="../_images/image.png"
    class="reference internal image-reference"><img
    src="../_images/image.png" style="width: 300px;"
    alt="../_images/image.png" /></a>
    </figure>

    **Attributes**

      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.attached_map_index "tecplot.annotation.Image.attached_map_index"){.reference .internal}                           Index to the associated fieldmap or linemap.
      [[`draw_order`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.draw_order "tecplot.annotation.Image.draw_order"){.reference .internal}                                                   Draw before or after the data.
      [[`filename`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.filename "tecplot.annotation.Image.filename"){.reference .internal}                                                         Source file (read-only).
      [[`height`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.height "tecplot.annotation.Image.height"){.reference .internal}                                                               Displayed image height in the coordinate system specified.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.macro_function "tecplot.annotation.Image.macro_function"){.reference .internal}                                       An associated macro function.
      [[`maintain_aspect_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.maintain_aspect_ratio "tecplot.annotation.Image.maintain_aspect_ratio"){.reference .internal}                  Keep aspect ratio on width or height change.
      [[`position`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.position "tecplot.annotation.Image.position"){.reference .internal}                                                         [[`tuple`{.xref .any .docutils .literal .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference .external}: Location on the [[`Frame`{.xref .any .py .py-class .docutils .literal .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference .internal}.
      [[`position_coordinate_system`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.position_coordinate_system "tecplot.annotation.Image.position_coordinate_system"){.reference .internal}   Position coordinate system.
      [[`raw_size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.raw_size "tecplot.annotation.Image.raw_size"){.reference .internal}                                                         Original image size in pixels (read-only).
      [[`resize_filter`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.resize_filter "tecplot.annotation.Image.resize_filter"){.reference .internal}                                          Smoothing filter.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.scope "tecplot.annotation.Image.scope"){.reference .internal}                                                                  Display annotation in all frames with the same data.
      [[`size`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.size "tecplot.annotation.Image.size"){.reference .internal}                                                                     Displayed image size.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.type "tecplot.annotation.Image.type"){.reference .internal}                                                                     The type of this annotation (read-only).
      [[`width`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.width "tecplot.annotation.Image.width"){.reference .internal}                                                                  Displayed image width in the coordinate system specified.
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    **Methods**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------
      [[`reset_aspect_ratio`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.Image.reset_aspect_ratio "tecplot.annotation.Image.reset_aspect_ratio"){.reference .internal}()   Restore the aspect ratio to that of the original image.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[draw_order]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.draw_order "Link to this definition"){.headerlink}

:   Draw before or after the data.

    Annotations can be drawn either before or after the data. If a
    geometry or image is drawn before the data, the plot layers, such as
    mesh, contour lines, etc. will be drawn on top of the geometry.
    Otherwise, the annotation will be drawn last, potentially obscuring
    the data.

    ::: {.admonition .note}
    Note

    Tecplot 360 draws all geometries and images first, in the order they
    were added, then all text.
    :::

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import DrawOrder
        >>> anno.draw_order = DrawOrder.BeforeData
    :::
    ::::

    Type[:]{.colon}

    :   [[`constant.DrawOrder`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.DrawOrder "tecplot.constant.DrawOrder"){.reference
        .internal}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[filename]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.filename "Link to this definition"){.headerlink}

:   Source file (read-only).

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> image = frame.add_imge('my_image.png', (20, 20), 40)
        >>> print(image.filename)
        my_image.png
    :::
    ::::

    Type[:]{.colon}

    :   [[`pathlib.Path`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[height]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.height "Link to this definition"){.headerlink}

:   Displayed image height in the coordinate system specified.

    The units for height are determined by the
    [[`position_coordinate_system`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Image.position_coordinate_system "tecplot.annotation.Image.position_coordinate_system"){.reference
    .internal} of the image. This example sets the height to 40% of the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> image.position_coordinate_system = CoordSys.Frame
        >>> image.height = 40
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[maintain_aspect_ratio]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.maintain_aspect_ratio "Link to this definition"){.headerlink}

:   Keep aspect ratio on width or height change.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> image.maintain_aspect_ratio = True
    :::
    ::::

    Type[:]{.colon}

    :   [[`bool`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[position]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.position "Link to this definition"){.headerlink}

:   [[`tuple`{.xref .any .docutils .literal
    .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)"){.reference
    .external}: Location on the [[`Frame`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}.

    This is the origin of the annotation and will be [\\((x,y)\\)]{.math
    .notranslate .nohighlight} or [\\((\\theta,r)\\)]{.math .notranslate
    .nohighlight} depending on the plot type. Example usage assuming an
    annotation variable [`anno`{.docutils .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.position = (3, 4)
    :::
    ::::

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[position_coordinate_system]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.position_coordinate_system "Link to this definition"){.headerlink}

:   Position coordinate system.

    The object may be positioned using either the grid coordinate system
    or the frame coordinate system and must be one of
    [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    .internal} or [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    .internal}:

    > <div>
    >
    > - [[`CoordSys.Frame`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Frame "tecplot.constant.CoordSys.Frame"){.reference
    >   .internal}: The geometry is always displayed at constant size
    >   and position when you zoom in or out of the plot.
    >
    > - [[`CoordSys.Grid`{.xref .any .py .py-attr .docutils .literal
    >   .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys.Grid "tecplot.constant.CoordSys.Grid"){.reference
    >   .internal}: The geometry resizes and moves with the data grid.
    >   However, the geometry remains fixed when you rotate the plot.
    >   Changing the center of rotation may cause the geometry to move.
    >
    > </div>

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> anno.position_coordinate_system = CoordSys.Frame
    :::
    ::::

    Type[:]{.colon}

    :   [[`CoordSys`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.CoordSys "tecplot.constant.CoordSys"){.reference
        .internal}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[raw_size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.raw_size "Link to this definition"){.headerlink}

:   Original image size in pixels (read-only).

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> print(image.raw_size)
        (600, 400)
    :::
    ::::

    Type[:]{.colon}

    :   [\\((width, height)\\)]{.math .notranslate .nohighlight}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[reset_aspect_ratio]{.pre}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/image.html#Image.reset_aspect_ratio){.reference .internal}[¶](#tecplot.annotation.Image.reset_aspect_ratio "Link to this definition"){.headerlink}

:   Restore the aspect ratio to that of the original image.

    Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> image.reset_aspect_ratio()
    :::
    ::::

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[resize_filter]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.resize_filter "Link to this definition"){.headerlink}

:   Smoothing filter.

    Possible values are [[`ImageResizeFilter.Texture`{.xref .any .py
    .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Texture "tecplot.constant.ImageResizeFilter.Texture"){.reference
    .internal}, [[`ImageResizeFilter.Box`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Box "tecplot.constant.ImageResizeFilter.Box"){.reference
    .internal}, [[`ImageResizeFilter.Lanczos2`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Lanczos2 "tecplot.constant.ImageResizeFilter.Lanczos2"){.reference
    .internal}, [[`ImageResizeFilter.Lanczos3`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Lanczos3 "tecplot.constant.ImageResizeFilter.Lanczos3"){.reference
    .internal}, [[`ImageResizeFilter.Triangle`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Triangle "tecplot.constant.ImageResizeFilter.Triangle"){.reference
    .internal}, [[`ImageResizeFilter.Bell`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Bell "tecplot.constant.ImageResizeFilter.Bell"){.reference
    .internal}, [[`ImageResizeFilter.BSpline`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.BSpline "tecplot.constant.ImageResizeFilter.BSpline"){.reference
    .internal}, [[`ImageResizeFilter.Cubic`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Cubic "tecplot.constant.ImageResizeFilter.Cubic"){.reference
    .internal}, [[`ImageResizeFilter.Mitchell`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Mitchell "tecplot.constant.ImageResizeFilter.Mitchell"){.reference
    .internal}, [[`ImageResizeFilter.Gaussian`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter.Gaussian "tecplot.constant.ImageResizeFilter.Gaussian"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import ImageResizeFilter
        >>> image.resize_filter = ImageResizeFilter.BSpline
    :::
    ::::

    Type[:]{.colon}

    :   [[`ImageResizeFilter`{.xref .any .py .py-class .docutils
        .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.ImageResizeFilter "tecplot.constant.ImageResizeFilter"){.reference
        .internal}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[size]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.size "Link to this definition"){.headerlink}

:   Displayed image size.

    This will be in the coordinates specified by
    [[`Image.position_coordinate_system`{.xref .any .py .py-attr
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.Image.position_coordinate_system "tecplot.annotation.Image.position_coordinate_system"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> image.size = (40, 20)
    :::
    ::::

    Type[:]{.colon}

    :   [\\((width, height)\\)]{.math .notranslate .nohighlight}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}

<!-- -->

[[Image.]{.pre}]{.sig-prename .descclassname}[[width]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.Image.width "Link to this definition"){.headerlink}

:   Displayed image width in the coordinate system specified.

    The units for width are determined by the
    [[`position_coordinate_system`{.xref .any .py .py-attr .docutils
    .literal
    .notranslate}]{.pre}](#tecplot.annotation.Image.position_coordinate_system "tecplot.annotation.Image.position_coordinate_system"){.reference
    .internal} of the image. This example sets the width to 40% of the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import CoordSys
        >>> image.position_coordinate_system = CoordSys.Frame
        >>> image.width = 0.4
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::

::: {#georeferencedimage .section}
### [GeoreferencedImage](#id19){.toc-backref role="doc-backlink"}[¶](#georeferencedimage "Link to this heading"){.headerlink}

*[class]{.pre}[ ]{.w}*[[tecplot.annotation.]{.pre}]{.sig-prename .descclassname}[[GeoreferencedImage]{.pre}]{.sig-name .descname}[(]{.sig-paren}*[[uid]{.pre}]{.n}*, *[[frame]{.pre}]{.n}*[)]{.sig-paren}[[[\[source\]]{.pre}]{.viewcode-link}](../_modules/tecplot/annotation/georeference.html#GeoreferencedImage){.reference .internal}[¶](#tecplot.annotation.GeoreferencedImage "Link to this definition"){.headerlink}

:   A Geographic reference image.

    A georeferenced can be added to a plot with a call to
    [[`Frame.add_georeferenced_image()`{.xref .any .py .py-meth
    .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.add_georeferenced_image "tecplot.layout.Frame.add_georeferenced_image"){.reference
    .internal}. Placement of the image is controlled by the [\\((x,
    y)\\)]{.math .notranslate .nohighlight} variables of the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} and the [[`GeoreferencedImage`{.xref .any .py .py-class
    .docutils .literal
    .notranslate}]{.pre}](#tecplot.annotation.GeoreferencedImage "tecplot.annotation.GeoreferencedImage"){.reference
    .internal} object's [\\(z\\)]{.math .notranslate .nohighlight}
    parameter.

    **Attributes**

      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------
      [[`attached_map_index`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.GeoreferencedImage.attached_map_index "tecplot.annotation.GeoreferencedImage.attached_map_index"){.reference .internal}   Index to the associated fieldmap or linemap.
      [[`macro_function`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.GeoreferencedImage.macro_function "tecplot.annotation.GeoreferencedImage.macro_function"){.reference .internal}               An associated macro function.
      [[`scope`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.GeoreferencedImage.scope "tecplot.annotation.GeoreferencedImage.scope"){.reference .internal}                                          Display annotation in all frames with the same data.
      [[`type`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.GeoreferencedImage.type "tecplot.annotation.GeoreferencedImage.type"){.reference .internal}                                             The type of this annotation (read-only).
      [[`z`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](#tecplot.annotation.GeoreferencedImage.z "tecplot.annotation.GeoreferencedImage.z"){.reference .internal}                                                      [\\(z\\)]{.math .notranslate .nohighlight}-position of the georeferenced image.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------

<!-- -->

[[GeoreferencedImage.]{.pre}]{.sig-prename .descclassname}[[attached_map_index]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.GeoreferencedImage.attached_map_index "Link to this definition"){.headerlink}

:   Index to the associated fieldmap or linemap.

    This property allows an annotation to follow the same
    active/inactive state as another plot object so their visibility can
    be changed together. Attach this annotation to a fieldmap or linemap
    using the object's index property. Geometries and images that are
    attached to an inactive or non-existent zone are not displayed.
    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.attached_map_index = plot.fieldmap(2).index
    :::
    ::::

    Type[:]{.colon}

    :   [[`Index`{.xref .any .py .py-attr .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.LabelType.Index "tecplot.constant.LabelType.Index"){.reference
        .internal} or [[`None`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GeoreferencedImage.]{.pre}]{.sig-prename .descclassname}[[macro_function]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.GeoreferencedImage.macro_function "Link to this definition"){.headerlink}

:   An associated macro function.

    All geometry or image annotations may be linked to a macro function.
    This macro function is called when you hold down the Control key
    (Command key on Mac OS X) and click the right mouse button on the
    text, geometry or image in the frame.

    In order to be attached to a text or geometry object, the macro
    function must be a "retained" macro function. A macro function is
    "retained" via either of the following scenarios:

    - running a macro file that contains the required macro functions

    - including it in your tecplot.mcr file (which is run at start up,
      making it a special case of the preceding scenario)

    In both cases, the macro function is defined using the
    \$!MACROFUNCTION macro command. Refer to
    "\$!MACROFUNCTION...\$!ENDMACROFUNCTION" on page 157 in the [Tecplot
    Macro Scripting
    Guide](https://download.tecplot.com/360/current/360_scripting_guide.pdf){.reference
    .external} for additional information.

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> anno.macro_function = 'MYMACROFUNCTION'
    :::
    ::::

    To run this function from PyTecplot it is neccessary to pass the
    function to a call to [[`macro.execute_function()`{.xref .any .py
    .py-func .docutils .literal
    .notranslate}]{.pre}](tecplot.macros.html#tecplot.macro.execute_function "tecplot.macro.execute_function"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> tecplot.macro.execute_function(anno.macro_function)
    :::
    ::::

    Type[:]{.colon}

    :   [[`str`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"){.reference
        .external}

<!-- -->

[[GeoreferencedImage.]{.pre}]{.sig-prename .descclassname}[[scope]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.GeoreferencedImage.scope "Link to this definition"){.headerlink}

:   Display annotation in all frames with the same data.

    Annotations with local scope are displayed only in the
    [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal} in which they are created. If it is defined as having
    [[`global`{.xref .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Global "tecplot.constant.Scope.Global"){.reference
    .internal} scope, it will appear in all "like" [[`frames`{.xref .any
    .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. That is, those frames using the same data set as the one
    in which the annotation was created. (default: [[`Scope.Local`{.xref
    .any .py .py-attr .docutils .literal
    .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope.Local "tecplot.constant.Scope.Local"){.reference
    .internal})

    Example usage assuming an annotation variable [`anno`{.docutils
    .literal .notranslate}]{.pre}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> from tecplot.constant import Scope
        >>> anno.scope = Scope.Global
    :::
    ::::

    Type[:]{.colon}

    :   [[`Scope`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.Scope "tecplot.constant.Scope"){.reference
        .internal}

<!-- -->

[[GeoreferencedImage.]{.pre}]{.sig-prename .descclassname}[[type]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.GeoreferencedImage.type "Link to this definition"){.headerlink}

:   The type of this annotation (read-only).

    This is the generic type information for geometry and image
    annotations. This is a read-only parameter and is used, in
    combination with *position_coordinate_system* to determine the
    actual return types of the iterators [[`Frame.geometries()`{.xref
    .any .py .py-meth .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.geometries "tecplot.layout.Frame.geometries"){.reference
    .internal} and [[`Frame.images()`{.xref .any .py .py-meth .docutils
    .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame.images "tecplot.layout.Frame.images"){.reference
    .internal}:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> frame.add_image('image.png', (1, 1), 5)
        >>> frame.add_circle((0,0), 1, CoordSys.Grid)
        >>> frame.add_square((0,0), 1, CoordSys.Grid)
        >>> for anno in frame.images():
        ...     print(anno.type)
        ...
        GeomType.Image
        >>> for anno in frame.geometries():
        ...     print(anno.type)
        ...
        GeomType.Circle
        GeomType.Square
    :::
    ::::

    Type[:]{.colon}

    :   [[`GeomType`{.xref .any .py .py-class .docutils .literal
        .notranslate}]{.pre}](tecplot.constants.html#tecplot.constant.GeomType "tecplot.constant.GeomType"){.reference
        .internal}

<!-- -->

[[GeoreferencedImage.]{.pre}]{.sig-prename .descclassname}[[z]{.pre}]{.sig-name .descname}[¶](#tecplot.annotation.GeoreferencedImage.z "Link to this definition"){.headerlink}

:   [\\(z\\)]{.math .notranslate .nohighlight}-position of the
    georeferenced image.

    This is the [\\(z\\)]{.math .notranslate .nohighlight} position
    (typically elevation) of the georeferenced image with respect to the
    [\\((x, y, z)\\)]{.math .notranslate .nohighlight} variables set in
    the [[`Frame`{.xref .any .py .py-class .docutils .literal
    .notranslate}]{.pre}](tecplot.layout.html#tecplot.layout.Frame "tecplot.layout.Frame"){.reference
    .internal}. Example usage:

    :::: {.highlight-python .notranslate}
    ::: highlight
        >>> georefimg.z = 100
    :::
    ::::

    Type[:]{.colon}

    :   [[`float`{.xref .any .docutils .literal
        .notranslate}]{.pre}](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"){.reference
        .external}
:::
:::::
::::::::::::::::::::

::: clearer
:::
::::::::::::::::::::::
