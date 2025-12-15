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
    def apply_zone_style(self, zone):
        """
        Apply this style configuration to a zone's fieldmap layer.

        Args:
            zone: The tecplot Zone object to apply styling to.
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

    def apply_zone_style(self, zone):
        """Apply scatter styling to a zone."""
        try:
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

            fieldmap = plot.fieldmap(zone)
            scatter = fieldmap.scatter

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
            print(f"Error applying scatter style to zone {zone.name}: {e}")


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

    def apply_zone_style(self, zone):
        """Apply mesh styling to a zone."""
        try:
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

            fieldmap = plot.fieldmap(zone)
            mesh = fieldmap.mesh

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
            print(f"Error applying mesh style to zone {zone.name}: {e}")


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

    def apply_zone_style(self, zone):
        """Apply contour styling to a zone."""
        try:
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

            fieldmap = plot.fieldmap(zone)
            contour = fieldmap.contour

            contour.show = self.show

            # Handle translucency if specified
            if self.translucency is not None:
                effects = fieldmap.effects
                effects.use_translucency = True
                # Convert 0.0-1.0 to 0-100 if needed
                translucency_percent = int(self.translucency * 100) if self.translucency <= 1.0 else int(self.translucency)
                effects.surface_translucency = translucency_percent
        except Exception as e:
            print(f"Error applying contour style to zone {zone.name}: {e}")


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

    def apply_zone_style(self, zone):
        """Apply shade styling to a zone."""
        try:
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

            fieldmap = plot.fieldmap(zone)
            shade = fieldmap.shade

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
            print(f"Error applying shade style to zone {zone.name}: {e}")


class VectorConfig(StyleConfig):
    """Configuration for vector layer styling."""

    def __init__(self, show: bool = False):
        """
        Initialize vector layer configuration.

        Args:
            show: Whether to show the vector layer
        """
        self.show = show

    def apply_zone_style(self, zone):
        """Apply vector styling to a zone."""
        try:
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

            fieldmap = plot.fieldmap(zone)
            vector = fieldmap.vector

            vector.show = self.show
        except Exception as e:
            print(f"Error applying vector style to zone {zone.name}: {e}")


class EdgeConfig(StyleConfig):
    """Configuration for edge layer styling."""

    def __init__(self, show: bool = False):
        """
        Initialize edge layer configuration.

        Args:
            show: Whether to show the edge layer
        """
        self.show = show

    def apply_zone_style(self, zone):
        """Apply edge styling to a zone."""
        try:
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

            fieldmap = plot.fieldmap(zone)
            edge = fieldmap.edge

            edge.show = self.show
        except Exception as e:
            print(f"Error applying edge style to zone {zone.name}: {e}")


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

    def apply_zone_style(self, zone):
        """
        Apply all style configurations to a zone.

        Args:
            zone: The tecplot Zone object to apply styling to.
        """
        try:
            # Apply each layer configuration
            self.scatter_config.apply_zone_style(zone)
            self.mesh_config.apply_zone_style(zone)
            self.contour_config.apply_zone_style(zone)
            self.shade_config.apply_zone_style(zone)
            self.vector_config.apply_zone_style(zone)
            self.edge_config.apply_zone_style(zone)

            # Set zone visibility by controlling fieldmap active status
            frame = tecplot.active_frame()
            if frame is None:
                return

            plot = frame.plot()
            if plot is None:
                return

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
            print(f"Error applying zone style to zone {zone.name}: {e}")
