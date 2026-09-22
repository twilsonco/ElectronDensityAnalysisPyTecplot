"""
Zone styling configuration classes.

This module defines an abstract configuration system for applying styles to zones
based on their ZoneType auxiliary data. The system is composed of per-layer config
classes (Scatter, Mesh, Contour, Shade, Vector, Edge) and a main ZoneStyleConfig
class that orchestrates the application of all styles.
"""

from abc import ABC, abstractmethod
from typing import Optional, Any
import tecplot
from tecplot.constant import SymbolType, GeomShape, Color, FillMode


class StyleConfig(ABC):
    """
    Abstract base class for all style configuration classes.

    Each subclass represents a specific layer type and must implement
    the apply_zone_style method to apply its styling to a zone's fieldmap.
    """

    @abstractmethod
    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """
        Apply this style configuration to a zone's fieldmap layer.

        Args:
            zone: The tecplot Zone object to apply styling to.
            fieldmap_index: Optional pre-computed fieldmap index to avoid lookup overhead.
                           If provided, uses plot.fieldmap(fieldmap_index) instead of plot.fieldmap(zone).
            frame: Optional pre-computed frame object to avoid active_frame() lookup.
            plot: Optional pre-computed plot object to avoid frame.plot() lookup.
            fieldmap: Optional pre-resolved fieldmap object. Each plot.fieldmap()
                      call constructs a new object with RPC overhead in connected
                      mode, so callers styling multiple layers should resolve the
                      fieldmap once and pass it here.
            assume_layers_off: If True, skip writing show=False (the caller has
                      already disabled all layers in bulk). Each redundant
                      write is an RPC round-trip in connected mode.
        """
        pass


class ScatterConfig(StyleConfig):
    """Configuration for scatter plot layer styling."""

    def __init__(
        self,
        show: bool = False,
        symbol_shape: Optional[GeomShape] = None,
        color: Optional[Color] = None,
        fill_color: Optional[Color] = None,
        fill_mode: Optional[FillMode] = None,
        line_thickness: Optional[float] = None,
        size: Optional[float] = None,
        size_function=None,
        color_function=None,
    ):
        """
        Initialize scatter layer configuration.

        Args:
            show: Whether to show the scatter layer
            symbol_shape: Scatter symbol shape (e.g., GeomShape.Sphere, GeomShape.Octahedron)
            color: Scatter outline color (Color enum, e.g., Color.Red)
            fill_color: Scatter fill color (Color enum, e.g., Color.Blue)
            fill_mode: Fill mode for scatter symbols (FillMode enum, e.g., FillMode.UseSpecificColor)
            line_thickness: Outline line thickness
            size: Scatter symbol size (constant)
            size_function: Callable that takes a zone and returns size. If provided, overrides size.
            color_function: Callable that takes a zone and returns Color enum. If provided, overrides color.
        """
        self.show = show
        self.symbol_shape = symbol_shape
        self.color = color
        self.fill_color = fill_color
        self.fill_mode = fill_mode
        self.line_thickness = line_thickness
        self.size = size
        self.size_function = size_function
        self.color_function = color_function

    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """Apply scatter styling to a zone."""
        try:
            if fieldmap is None:
                # Use provided frame/plot or look them up (frame/plot cached for performance)
                if frame is None:
                    frame = tecplot.active_frame()
                if frame is None:
                    return

                if plot is None:
                    plot = frame.plot()
                if plot is None:
                    return

                # Use cached fieldmap index if provided, otherwise look up by zone
                if fieldmap_index is not None:
                    fieldmap = plot.fieldmap(fieldmap_index)
                else:
                    fieldmap = plot.fieldmap(zone)
            scatter = fieldmap.scatter

            # Skip redundant show=False writes when the caller already
            # disabled all layers in bulk (each write is an RPC round-trip)
            if self.show or not assume_layers_off:
                scatter.show = self.show

            if self.symbol_shape is not None:
                scatter.symbol_type = SymbolType.Geometry
                scatter.symbol().shape = self.symbol_shape

            # Color can be constant or computed via function
            if self.color_function is not None:
                computed_color = self.color_function(zone)
                if computed_color is not None:
                    scatter.color = computed_color
            elif self.color is not None:
                scatter.color = self.color

            if self.fill_color is not None:
                scatter.fill_color = self.fill_color

            if self.fill_mode is not None:
                scatter.fill_mode = self.fill_mode

            if self.line_thickness is not None:
                scatter.line_thickness = self.line_thickness

            # Size can be constant or computed via function
            if self.size_function is not None:
                computed_size = self.size_function(zone)
                if computed_size is not None:
                    scatter.size = computed_size
            elif self.size is not None:
                scatter.size = self.size
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def resolve_for_zone(self, zone):
        """Return an equivalent config with computed color/size evaluated for this zone.

        Used to bucket zones with identical resolved styles so they can be
        styled together with bulk fieldmap operations.
        """
        color = self.color
        if self.color_function is not None:
            color = self.color_function(zone)
        size = self.size
        if self.size_function is not None:
            size = self.size_function(zone)
        return ScatterConfig(
            show=self.show,
            symbol_shape=self.symbol_shape,
            color=color,
            fill_color=self.fill_color,
            fill_mode=self.fill_mode,
            line_thickness=self.line_thickness,
            size=size,
        )

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing)."""
        return (
            "scatter", self.show, self.symbol_shape, self.color,
            self.fill_color, self.fill_mode, self.line_thickness, self.size,
        )


class MeshConfig(StyleConfig):
    """Configuration for mesh layer styling."""

    def __init__(
        self,
        show: bool = False,
        color: Optional[Color] = None,
        line_thickness: Optional[float] = None,
        mesh_type: Optional[Any] = None,
        line_pattern: Optional[Any] = None,
        pattern_length: Optional[float] = None,
        color_function=None,
    ):
        """
        Initialize mesh layer configuration.

        Args:
            show: Whether to show the mesh layer
            color: Mesh line color (Color enum, e.g., Color.Black)
            line_thickness: Mesh line thickness
            mesh_type: Mesh type (e.g., MeshType enum)
            line_pattern: Line pattern (e.g., LinePattern enum)
            pattern_length: Pattern length for mesh lines
            color_function: Callable that takes a zone and returns Color enum. If provided, overrides color.
        """
        self.show = show
        self.color = color
        self.line_thickness = line_thickness
        self.mesh_type = mesh_type
        self.line_pattern = line_pattern
        self.pattern_length = pattern_length
        self.color_function = color_function

    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """Apply mesh styling to a zone."""
        try:
            if fieldmap is None:
                # Use provided frame/plot or look them up (frame/plot cached for performance)
                if frame is None:
                    frame = tecplot.active_frame()
                if frame is None:
                    return

                if plot is None:
                    plot = frame.plot()
                if plot is None:
                    return

                # Use cached fieldmap index if provided, otherwise look up by zone
                if fieldmap_index is not None:
                    fieldmap = plot.fieldmap(fieldmap_index)
                else:
                    fieldmap = plot.fieldmap(zone)
            mesh = fieldmap.mesh

            # Skip redundant show=False writes when the caller already
            # disabled all layers in bulk (each write is an RPC round-trip)
            if self.show or not assume_layers_off:
                mesh.show = self.show

            # Color can be constant or computed via function
            if self.color_function is not None:
                computed_color = self.color_function(zone)
                if computed_color is not None:
                    mesh.color = computed_color
            elif self.color is not None:
                mesh.color = self.color

            if self.line_thickness is not None:
                mesh.line_thickness = self.line_thickness

            if self.mesh_type is not None:
                mesh.mesh_type = self.mesh_type

            if self.line_pattern is not None:
                mesh.line_pattern = self.line_pattern

            if self.pattern_length is not None:
                mesh.pattern_length = self.pattern_length
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def resolve_for_zone(self, zone):
        """Return an equivalent config with the computed color evaluated for this zone."""
        color = self.color
        if self.color_function is not None:
            color = self.color_function(zone)
        return MeshConfig(
            show=self.show,
            color=color,
            line_thickness=self.line_thickness,
            mesh_type=self.mesh_type,
            line_pattern=self.line_pattern,
            pattern_length=self.pattern_length,
        )

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing)."""
        return (
            "mesh", self.show, self.color, self.line_thickness,
            self.mesh_type, self.line_pattern, self.pattern_length,
        )


class ContourConfig(StyleConfig):
    """Configuration for contour layer styling."""

    def __init__(self, show: bool = False, translucency: Optional[float] = None):
        """
        Initialize contour layer configuration.

        Args:
            show: Whether to show the contour layer
            translucency: Translucency value (0.0-1.0 or 0-100). If provided, enables effects and surface translucency.
        """
        self.show = show
        self.translucency = translucency

    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """Apply contour styling to a zone."""
        try:
            if fieldmap is None:
                # Use provided frame/plot or look them up (frame/plot cached for performance)
                if frame is None:
                    frame = tecplot.active_frame()
                if frame is None:
                    return

                if plot is None:
                    plot = frame.plot()
                if plot is None:
                    return

                # Use cached fieldmap index if provided, otherwise look up by zone
                if fieldmap_index is not None:
                    fieldmap = plot.fieldmap(fieldmap_index)
                else:
                    fieldmap = plot.fieldmap(zone)
            contour = fieldmap.contour

            # Skip redundant show=False writes when the caller already
            # disabled all layers in bulk (each write is an RPC round-trip)
            if self.show or not assume_layers_off:
                contour.show = self.show

            # Handle translucency if specified
            if self.translucency is not None:
                effects = fieldmap.effects
                effects.use_translucency = True
                # Convert 0.0-1.0 to 0-100 if needed
                translucency_percent = int(self.translucency * 100) if self.translucency <= 1.0 else int(self.translucency)
                effects.surface_translucency = translucency_percent
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def resolve_for_zone(self, zone):
        """Return this config (contour styling has no computed values)."""
        return self

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing)."""
        return ("contour", self.show, self.translucency)


class ShadeConfig(StyleConfig):
    """Configuration for shade layer styling."""

    def __init__(
        self, show: bool = False, color: Optional[Color] = None, color_function=None, translucency: Optional[float] = None
    ):
        """
        Initialize shade layer configuration.

        Args:
            show: Whether to show the shade layer
            color: Shade color (Color enum, e.g., Color.White)
            color_function: Callable that takes a zone and returns Color enum. If provided, overrides color.
            translucency: Translucency value (0.0-1.0 or 0-100). If provided, enables effects and surface translucency.
        """
        self.show = show
        self.color = color
        self.color_function = color_function
        self.translucency = translucency

    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """Apply shade styling to a zone."""
        try:
            if fieldmap is None:
                # Use provided frame/plot or look them up (frame/plot cached for performance)
                if frame is None:
                    frame = tecplot.active_frame()
                if frame is None:
                    return

                if plot is None:
                    plot = frame.plot()
                if plot is None:
                    return

                # Use cached fieldmap index if provided, otherwise look up by zone
                if fieldmap_index is not None:
                    fieldmap = plot.fieldmap(fieldmap_index)
                else:
                    fieldmap = plot.fieldmap(zone)
            shade = fieldmap.shade

            # Skip redundant show=False writes when the caller already
            # disabled all layers in bulk (each write is an RPC round-trip)
            if self.show or not assume_layers_off:
                shade.show = self.show

            # Color can be constant or computed via function
            if self.color_function is not None:
                computed_color = self.color_function(zone)
                if computed_color is not None:
                    shade.color = computed_color
            elif self.color is not None:
                shade.color = self.color

            # Handle translucency if specified
            if self.translucency is not None:
                effects = fieldmap.effects
                effects.use_translucency = True
                # Convert 0.0-1.0 to 0-100 if needed
                translucency_percent = int(self.translucency * 100) if self.translucency <= 1.0 else int(self.translucency)
                effects.surface_translucency = translucency_percent
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def resolve_for_zone(self, zone):
        """Return an equivalent config with the computed color evaluated for this zone."""
        color = self.color
        if self.color_function is not None:
            color = self.color_function(zone)
        return ShadeConfig(show=self.show, color=color, translucency=self.translucency)

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing)."""
        return ("shade", self.show, self.color, self.translucency)


class VectorConfig(StyleConfig):
    """Configuration for vector layer styling."""

    def __init__(self, show: bool = False):
        """
        Initialize vector layer configuration.

        Args:
            show: Whether to show the vector layer
        """
        self.show = show

    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """Apply vector styling to a zone."""
        try:
            if fieldmap is None:
                # Use provided frame/plot or look them up (frame/plot cached for performance)
                if frame is None:
                    frame = tecplot.active_frame()
                if frame is None:
                    return

                if plot is None:
                    plot = frame.plot()
                if plot is None:
                    return

                # Use cached fieldmap index if provided, otherwise look up by zone
                if fieldmap_index is not None:
                    fieldmap = plot.fieldmap(fieldmap_index)
                else:
                    fieldmap = plot.fieldmap(zone)
            vector = fieldmap.vector

            # Skip redundant show=False writes when the caller already
            # disabled all layers in bulk (each write is an RPC round-trip)
            if self.show or not assume_layers_off:
                vector.show = self.show
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def resolve_for_zone(self, zone):
        """Return this config (vector styling has no computed values)."""
        return self

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing)."""
        return ("vector", self.show)


class EdgeConfig(StyleConfig):
    """Configuration for edge layer styling."""

    def __init__(self, show: bool = False):
        """
        Initialize edge layer configuration.

        Args:
            show: Whether to show the edge layer
        """
        self.show = show

    def apply_zone_style(self, zone, fieldmap_index=None, frame=None, plot=None,
                         fieldmap=None, assume_layers_off=False):
        """Apply edge styling to a zone."""
        try:
            if fieldmap is None:
                # Use provided frame/plot or look them up (frame/plot cached for performance)
                if frame is None:
                    frame = tecplot.active_frame()
                if frame is None:
                    return

                if plot is None:
                    plot = frame.plot()
                if plot is None:
                    return

                # Use cached fieldmap index if provided, otherwise look up by zone
                if fieldmap_index is not None:
                    fieldmap = plot.fieldmap(fieldmap_index)
                else:
                    fieldmap = plot.fieldmap(zone)
            edge = fieldmap.edge

            # Skip redundant show=False writes when the caller already
            # disabled all layers in bulk (each write is an RPC round-trip)
            if self.show or not assume_layers_off:
                edge.show = self.show
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def resolve_for_zone(self, zone):
        """Return this config (edge styling has no computed values)."""
        return self

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing)."""
        return ("edge", self.show)


class ZoneStyleConfig:
    """
    Main zone style configuration class.

    Composes all per-layer config objects and general zone settings.
    Orchestrates the application of all styles to a zone.
    """

    def __init__(
        self,
        zone_enabled: bool = False,
        scatter_config: Optional[ScatterConfig] = None,
        mesh_config: Optional[MeshConfig] = None,
        contour_config: Optional[ContourConfig] = None,
        shade_config: Optional[ShadeConfig] = None,
        vector_config: Optional[VectorConfig] = None,
        edge_config: Optional[EdgeConfig] = None,
    ):
        """
        Initialize main zone style configuration.

        By default, all layers are disabled and the zone is disabled.
        Pass specific layer configs to override defaults.

        Args:
            zone_enabled: Whether the zone should be enabled (visible)
            scatter_config: Scatter layer configuration
            mesh_config: Mesh layer configuration
            contour_config: Contour layer configuration
            shade_config: Shade layer configuration
            vector_config: Vector layer configuration
            edge_config: Edge layer configuration
        """
        self.zone_enabled = zone_enabled
        self.scatter_config = scatter_config or ScatterConfig()
        self.mesh_config = mesh_config or MeshConfig()
        self.contour_config = contour_config or ContourConfig()
        self.shade_config = shade_config or ShadeConfig()
        self.vector_config = vector_config or VectorConfig()
        self.edge_config = edge_config or EdgeConfig()
    def resolve_for_zone(self, zone):
        """Return an equivalent config with all computed values evaluated for this zone.

        The returned config has no color_function/size_function, so zones that
        resolve to the same style_key can be styled together with a single bulk
        fieldmap operation (computed values like atom colors repeat heavily,
        e.g., all atoms of the same element share color and size).
        """
        return ZoneStyleConfig(
            zone_enabled=self.zone_enabled,
            scatter_config=self.scatter_config.resolve_for_zone(zone),
            mesh_config=self.mesh_config.resolve_for_zone(zone),
            contour_config=self.contour_config.resolve_for_zone(zone),
            shade_config=self.shade_config.resolve_for_zone(zone),
            vector_config=self.vector_config.resolve_for_zone(zone),
            edge_config=self.edge_config.resolve_for_zone(zone),
        )

    def style_key(self):
        """Hashable key identifying this config's constant style values (for bucketing).

        Only valid on configs returned by resolve_for_zone() (or configs that
        never had computed properties). Two configs with the same key apply
        identical styling and can share one bulk operation.
        """
        return (
            self.scatter_config.style_key(),
            self.mesh_config.style_key(),
            self.contour_config.style_key(),
            self.shade_config.style_key(),
            self.vector_config.style_key(),
            self.edge_config.style_key(),
        )
    def apply_zone_style(self, zone, skip_visibility=False, fieldmap_index=None, frame=None, plot=None,
                         assume_layers_off=False):
        """
        Apply all style configurations to a zone.

        Args:
            zone: The tecplot Zone object to apply styling to.
            skip_visibility: If True, skip zone visibility update (use when bulk-updating separately).
            fieldmap_index: Optional pre-computed fieldmap index to pass to layer configs.
                           Avoids redundant fieldmap lookups in each layer.
            frame: Optional pre-computed frame object to avoid active_frame() lookup.
            plot: Optional pre-computed plot object to avoid frame.plot() lookup.
            assume_layers_off: If True, layer configs skip writing show=False
                           (caller already disabled all layers in bulk).
        """
        try:
            # Use provided frame/plot or look them up once (avoids redundant lookups in each layer)
            if frame is None:
                frame = tecplot.active_frame()
            if plot is None and frame is not None:
                plot = frame.plot()

            # Resolve the fieldmap object ONCE per zone and share it across all
            # layer configs. Each plot.fieldmap() call constructs a new object
            # with RPC overhead in connected mode (6x per zone otherwise).
            fieldmap = None
            if plot is not None:
                try:
                    if fieldmap_index is not None:
                        fieldmap = plot.fieldmap(fieldmap_index)
                    else:
                        fieldmap = plot.fieldmap(zone)
                        fieldmap_index = fieldmap.index
                except Exception:
                    fieldmap = None

            # Apply each layer configuration with the shared fieldmap object to eliminate lookups
            self.scatter_config.apply_zone_style(zone, fieldmap_index=fieldmap_index, frame=frame, plot=plot,
                                                 fieldmap=fieldmap, assume_layers_off=assume_layers_off)
            self.mesh_config.apply_zone_style(zone, fieldmap_index=fieldmap_index, frame=frame, plot=plot,
                                              fieldmap=fieldmap, assume_layers_off=assume_layers_off)
            self.contour_config.apply_zone_style(zone, fieldmap_index=fieldmap_index, frame=frame, plot=plot,
                                                 fieldmap=fieldmap, assume_layers_off=assume_layers_off)
            self.shade_config.apply_zone_style(zone, fieldmap_index=fieldmap_index, frame=frame, plot=plot,
                                               fieldmap=fieldmap, assume_layers_off=assume_layers_off)
            self.vector_config.apply_zone_style(zone, fieldmap_index=fieldmap_index, frame=frame, plot=plot,
                                                fieldmap=fieldmap, assume_layers_off=assume_layers_off)
            self.edge_config.apply_zone_style(zone, fieldmap_index=fieldmap_index, frame=frame, plot=plot,
                                              fieldmap=fieldmap, assume_layers_off=assume_layers_off)

            # Set zone visibility by controlling fieldmap active status
            # (skip if bulk-updating visibility separately)
            if not skip_visibility and plot is not None:
                try:
                    fieldmap_index = plot.fieldmap_index(zone)
                    current_active = set(plot.active_fieldmap_indices)

                    if self.zone_enabled:
                        # Add this zone's fieldmap to active set
                        current_active.add(fieldmap_index)
                    else:
                        # Remove this zone's fieldmap from active set
                        current_active.discard(fieldmap_index)

                    plot.active_fieldmap_indices = list(current_active)
                except Exception:
                    # If fieldmap_index fails, skip zone visibility control
                    pass
        except Exception as e:
            pass  # Silently skip on error (fieldmap may not exist for all zones)

    def apply_zone_style_bulk(self, fieldmap_indices, plot=None, assume_layers_off=False):
        """
        Apply style configuration to multiple fieldmaps at once using bulk operations.

        This method applies the configuration to a collection of fieldmaps, which is
        more efficient than applying to individual fieldmaps when multiple zones share
        the same configuration. No visibility changes are made (assumed to be handled
        separately via plot.active_fieldmap_indices).

        Args:
            fieldmap_indices: Iterable of fieldmap indices to apply styling to.
                            Should be non-empty; no-op if empty.
            plot: Optional pre-computed plot object to avoid frame.plot() lookup.
            assume_layers_off: If True, skip writing show=False (caller already
                            disabled all layers in bulk; each write is an RPC).
        """
        if not fieldmap_indices:
            return

        try:
            # Use provided plot or look it up (plot cached for performance)
            if plot is None:
                frame = tecplot.active_frame()
                if frame is None:
                    return
                plot = frame.plot()
            
            if plot is None:
                return

            # Get fieldmap collection for the provided indices
            fieldmap_collection = plot.fieldmaps(*fieldmap_indices)

            # Apply each layer configuration to the entire collection
            # For bulk operations, properties are set on the collection directly
            try:
                if self.scatter_config.show or not assume_layers_off:
                    fieldmap_collection.scatter.show = self.scatter_config.show
                if self.scatter_config.symbol_shape is not None:
                    fieldmap_collection.scatter.symbol_type = SymbolType.Geometry
                    fieldmap_collection.scatter.symbol().shape = self.scatter_config.symbol_shape
                if self.scatter_config.color is not None:
                    fieldmap_collection.scatter.color = self.scatter_config.color
                if self.scatter_config.fill_color is not None:
                    fieldmap_collection.scatter.fill_color = self.scatter_config.fill_color
                if self.scatter_config.fill_mode is not None:
                    fieldmap_collection.scatter.fill_mode = self.scatter_config.fill_mode
                if self.scatter_config.line_thickness is not None:
                    fieldmap_collection.scatter.line_thickness = self.scatter_config.line_thickness
                if self.scatter_config.size is not None:
                    fieldmap_collection.scatter.size = self.scatter_config.size
            except Exception as e:
                print(f"Warning: Could not apply scatter settings to fieldmap collection: {e}")

            try:
                if self.mesh_config.show or not assume_layers_off:
                    fieldmap_collection.mesh.show = self.mesh_config.show
                if self.mesh_config.color is not None:
                    fieldmap_collection.mesh.color = self.mesh_config.color
                if self.mesh_config.line_thickness is not None:
                    fieldmap_collection.mesh.line_thickness = self.mesh_config.line_thickness
                if self.mesh_config.mesh_type is not None:
                    fieldmap_collection.mesh.mesh_type = self.mesh_config.mesh_type
                if self.mesh_config.line_pattern is not None:
                    fieldmap_collection.mesh.line_pattern = self.mesh_config.line_pattern
                if self.mesh_config.pattern_length is not None:
                    fieldmap_collection.mesh.pattern_length = self.mesh_config.pattern_length
            except Exception as e:
                print(f"Warning: Could not apply mesh settings to fieldmap collection: {e}")

            try:
                if self.contour_config.show or not assume_layers_off:
                    fieldmap_collection.contour.show = self.contour_config.show
                if self.contour_config.translucency is not None:
                    try:
                        fieldmap_collection.effects.use_translucency = True
                        translucency_percent = int(self.contour_config.translucency * 100) if self.contour_config.translucency <= 1.0 else int(self.contour_config.translucency)
                        fieldmap_collection.effects.surface_translucency = translucency_percent
                    except:
                        pass  # Silently skip if translucency assignment fails
            except Exception as e:
                print(f"Warning: Could not apply contour settings to fieldmap collection: {e}")

            try:
                if self.shade_config.show or not assume_layers_off:
                    fieldmap_collection.shade.show = self.shade_config.show
                if self.shade_config.color is not None:
                    fieldmap_collection.shade.color = self.shade_config.color
                if self.shade_config.translucency is not None:
                    try:
                        fieldmap_collection.effects.use_translucency = True
                        translucency_percent = int(self.shade_config.translucency * 100) if self.shade_config.translucency <= 1.0 else int(self.shade_config.translucency)
                        fieldmap_collection.effects.surface_translucency = translucency_percent
                    except:
                        pass  # Silently skip if translucency assignment fails
            except Exception as e:
                print(f"Warning: Could not apply shade settings to fieldmap collection: {e}")

            try:
                if self.vector_config.show or not assume_layers_off:
                    fieldmap_collection.vector.show = self.vector_config.show
            except Exception as e:
                print(f"Warning: Could not apply vector settings to fieldmap collection: {e}")

            try:
                if self.edge_config.show or not assume_layers_off:
                    fieldmap_collection.edge.show = self.edge_config.show
            except Exception as e:
                print(f"Warning: Could not apply edge settings to fieldmap collection: {e}")

        except Exception as e:
            print(f"Error applying zone style bulk to fieldmap collection: {e}")
