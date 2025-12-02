"""
Apply zone styling based on ZoneType aux data.

This script iterates over all zones in the active dataset and applies
styling configurations based on each zone's ZoneType aux data value.
"""

import math
import tecplot
from collections import defaultdict
from tecplot.constant import Color, GeomShape, FillMode
from zone_style_config import (
    ZoneStyleConfig,
    ScatterConfig,
    MeshConfig,
    ContourConfig,
    ShadeConfig,
)

# Constant for atom sphere minimum size
ATOM_MIN_SPHERE_SIZE = 2.5

# Predefined colors with their RGB values for color matching
PREDEFINED_COLORS = {
    # Primary colors
    Color.Black: (0, 0, 0),
    Color.Red: (1, 0, 0),
    Color.Green: (0, 1, 0),
    Color.Blue: (0, 0, 1),
    Color.White: (1, 1, 1),
    Color.Yellow: (1, 1, 0),
    Color.Cyan: (0, 1, 1),
    Color.Magenta: (1, 0, 1),
    
    # Greys and neutrals
    Color.Grey: (0.5, 0.5, 0.5),
    Color.LightGrey: (0.75, 0.75, 0.75),
    
    # Reds and warm colors
    Color.Orange: (1, 0.65, 0),
    Color.Coral: (1, 0.5, 0.31),
    Color.DeepRed: (0.55, 0, 0),
    Color.Mahogany: (0.75, 0.25, 0),
    Color.RedOrange: (1, 0.27, 0),
    Color.HotPink: (1, 0.41, 0.71),
    Color.Raspberry: (0.9, 0.04, 0.52),
    Color.BrightPink: (1, 0.08, 0.58),
    
    # Purples and violets
    Color.Purple: (0.5, 0, 0.5),
    Color.Violet: (0.93, 0.51, 0.93),
    Color.Lilac: (0.78, 0.64, 0.78),
    Color.Indigo: (0.29, 0, 0.51),
    Color.BluePurple: (0.54, 0.17, 0.89),
    Color.DeepViolet: (0.25, 0, 0.4),
    Color.MediumPurple: (0.58, 0.44, 0.86),
    Color.LightPurple: (0.87, 0.63, 0.87),
    
    # Blues and cyans
    Color.Azure: (0, 0.5, 1),
    Color.BrightBlue: (0, 0.75, 1),
    Color.LightBlue: (0.68, 0.85, 0.9),
    Color.DarkBlue: (0, 0, 0.55),
    Color.RoyalBlue: (0.25, 0.41, 0.88),
    Color.SkyBlue: (0.53, 0.81, 0.92),
    Color.OceanBlue: (0, 0.47, 0.75),
    Color.BrightCyan: (0, 1, 1),
    Color.LightCyan: (0.88, 1, 1),
    Color.Turquoise: (0.25, 0.88, 0.82),
    Color.DarkTurquoise: (0, 0.81, 0.82),
    Color.GreyTeal: (0.3, 0.5, 0.5),
    Color.WarmBlue: (0.26, 0.57, 0.78),
    Color.DuskyBlue: (0.24, 0.44, 0.59),
    
    # Greens
    Color.LimeGreen: (0.2, 0.8, 0.2),
    Color.LightGreen: (0.56, 0.93, 0.56),
    Color.AquaGreen: (0.5, 1, 0.5),
    Color.Forest: (0.13, 0.55, 0.13),
    Color.Emerald: (0.31, 0.78, 0.47),
    Color.SeaGreen: (0.56, 0.74, 0.56),
    Color.Spearmint: (0.5, 1, 0.5),
    Color.LeafGreen: (0.4, 0.8, 0.2),
    Color.MustardGreen: (0.71, 0.79, 0.34),
    Color.LemonGreen: (0.5, 1, 0),
    Color.Fern: (0.6, 0.8, 0.2),
    Color.Chartreuse: (0.5, 1, 0),
    Color.YellowGreen: (0.6, 0.8, 0.2),
    Color.LightMintGreen: (0.7, 1, 0.8),
    Color.Olive: (0.5, 0.5, 0),
    
    # Yellows and oranges
    Color.Lemon: (1, 0.97, 0.28),
    Color.Khaki: (0.94, 0.9, 0.55),
    Color.Creme: (1, 0.97, 0.8),
    Color.LightOrange: (1, 0.75, 0.4),
    Color.LightSalmon: (1, 0.63, 0.48),
    Color.Cinnamon: (0.82, 0.41, 0.12),
    
    # Pinks and warm pastels
    Color.BubbleGum: (1, 0.76, 0.81),
    Color.LightMagenta: (1, 0.5, 1),
    
    # Maroons and dark colors
    Color.LightMaroon: (0.65, 0.2, 0.2),
}




def get_closest_color_for_hex(hex_color_str):
    """
    Find the closest predefined Color enum for a hex color string.
    
    Uses Euclidean distance in RGB space to find the nearest match.

    Args:
        hex_color_str: Hex color string (e.g., "#ffffff")

    Returns:
        tecplot.constant.Color enum value, or Color.White if not found
    """
    if not hex_color_str or not hex_color_str.startswith("#"):
        return Color.White
    
    try:
        hex_color = hex_color_str.lstrip("#")
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0
        target_rgb = (r, g, b)
    except (ValueError, IndexError):
        return Color.White
    
    # Find closest color using Euclidean distance
    min_distance = float('inf')
    closest_color = Color.White
    
    for color, rgb in PREDEFINED_COLORS.items():
        distance = math.sqrt(
            (target_rgb[0] - rgb[0])**2 +
            (target_rgb[1] - rgb[1])**2 +
            (target_rgb[2] - rgb[2])**2
        )
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    
    return closest_color


def get_atom_color_from_aux_data(zone):
    """
    Extract and map color from zone's AtomColor aux data to closest Color enum.
    
    Parses hex color strings (e.g., "#ffffff") and maps to the nearest
    predefined Tecplot Color enum value using Euclidean distance in RGB space.

    Args:
        zone: The tecplot Zone object

    Returns:
        tecplot.constant.Color enum value, or None if not found
    """
    try:
        color_hex = zone.aux_data["AtomColor"].strip()
        return get_closest_color_for_hex(color_hex)
    except (KeyError, AttributeError):
        return None
def get_atom_size_from_aux_data(zone):
    """
    Calculate scatter size based on AtomElementNumber aux data.

    Formula: ATOM_MIN_SPHERE_SIZE + log(AtomElementNumber + 1)

    Args:
        zone: The tecplot Zone object

    Returns:
        float: Calculated size, or None if AtomElementNumber not found
    """
    try:
        atom_num = float(zone.aux_data["AtomElementNumber"])
        size = ATOM_MIN_SPHERE_SIZE + math.log(atom_num + 1)
        return size
    except (ValueError, KeyError, AttributeError):
        return None


# Connect to Tecplot 360 session
tecplot.session.connect()

frame = tecplot.active_frame()
dataset = frame.dataset if frame is not None else None

if dataset is None:
    print("No dataset loaded in the active frame.")
else:
    # Create defaultdict with zone type style configurations
    zone_styles = defaultdict(lambda: ZoneStyleConfig())

    # Define specific zone type configurations
    # No ZoneType: all layers disabled, zone disabled (default)
    # (uses default ZoneStyleConfig())

    # FullVolumeZone: all layers disabled, zone ENABLED
    zone_styles["FullVolumeZone"] = ZoneStyleConfig(zone_enabled=True)

    # Atoms: scatter only, sphere, size from log formula, color from hex mapping
    zone_styles["Atoms"] = ZoneStyleConfig(
        zone_enabled=True,
        scatter_config=ScatterConfig(
            show=True,
            symbol_shape=GeomShape.Sphere,
            size_function=get_atom_size_from_aux_data,
            color_function=get_atom_color_from_aux_data,
            fill_mode=FillMode.UseSpecificColor,
        ),
    )

    # CriticalPoints: scatter only, sphere, size 1, zone DISABLED
    zone_styles["CriticalPoints"] = ZoneStyleConfig(
        zone_enabled=False,
        scatter_config=ScatterConfig(
            show=True,
            symbol_shape=GeomShape.Sphere,
            size=1.0,
        ),
    )

    # CriticalPoints Nuclear: scatter only, sphere, white, size 4, zone ENABLED
    zone_styles["CriticalPoints Nuclear"] = ZoneStyleConfig(
        zone_enabled=True,
        scatter_config=ScatterConfig(
            show=True,
            symbol_shape=GeomShape.Sphere,
            color=Color.White,
            size=4.0,
        ),
    )

    # CriticalPoints Bond: scatter only, sphere, red, size 2.5, zone ENABLED
    zone_styles["CriticalPoints Bond"] = ZoneStyleConfig(
        zone_enabled=True,
        scatter_config=ScatterConfig(
            show=True,
            symbol_shape=GeomShape.Sphere,
            color=Color.Red,
            size=1.8,
        ),
    )

    # CriticalPoints Ring: scatter only, sphere, green, size 1, zone ENABLED
    zone_styles["CriticalPoints Ring"] = ZoneStyleConfig(
        zone_enabled=True,
        scatter_config=ScatterConfig(
            show=True,
            symbol_shape=GeomShape.Sphere,
            color=Color.Green,
            size=1.0,
        ),
    )

    # CriticalPoints Cage: scatter only, octahedron, cyan, size 1, zone ENABLED
    zone_styles["CriticalPoints Cage"] = ZoneStyleConfig(
        zone_enabled=True,
        scatter_config=ScatterConfig(
            show=True,
            symbol_shape=GeomShape.Octahedron,
            color=Color.Cyan,
            size=1.0,
        ),
    )

    # AtomSphereData: contour + shade with color from atom data
    zone_styles["AtomSphereData"] = ZoneStyleConfig(
        zone_enabled=True,
        contour_config=ContourConfig(show=True),
        shade_config=ShadeConfig(
            show=True,
            color_function=get_atom_color_from_aux_data,
        ),
    )

    # GradientPath: mesh only, size 0.2
    zone_styles["GradientPath"] = ZoneStyleConfig(
        zone_enabled=True,
        mesh_config=MeshConfig(show=True, line_thickness=0.2),
    )

    # BondPath: mesh only, black, size 0.4
    zone_styles["BondPath"] = ZoneStyleConfig(
        zone_enabled=True,
        mesh_config=MeshConfig(show=True, color=Color.Black, line_thickness=0.4),
    )

    # Get all zones
    zones = list(dataset.zones())
    print(f"Processing {len(zones)} zones...")

    # Apply styles to each zone
    for zone in zones:
        try:
            zone_type = zone.aux_data["ZoneType"] if zone.aux_data else None
        except (KeyError, AttributeError):
            zone_type = None

        print(f"Zone: {zone.name}, ZoneType: {zone_type}")

        # Get and apply the style config for this zone type
        zone_styles[zone_type].apply_zone_style(zone)

    # Activate layers that are in use by any enabled zone
    frame = tecplot.active_frame()
    if frame is not None:
        plot = frame.plot()
        if plot is not None:
            # Check which layers are in use by enabled zones
            layers_in_use = {"scatter": False, "mesh": False, "contour": False, 
                           "shade": False, "vector": False, "edge": False}
            
            for zone_type, config in zone_styles.items():
                if config.zone_enabled:
                    if config.scatter_config.show:
                        layers_in_use["scatter"] = True
                    if config.mesh_config.show:
                        layers_in_use["mesh"] = True
                    if config.contour_config.show:
                        layers_in_use["contour"] = True
                    if config.shade_config.show:
                        layers_in_use["shade"] = True
                    if config.vector_config.show:
                        layers_in_use["vector"] = True
                    if config.edge_config.show:
                        layers_in_use["edge"] = True
            
            # Activate plot-level layers that are in use
            if layers_in_use["scatter"]:
                plot.show_scatter = True
            if layers_in_use["mesh"]:
                plot.show_mesh = True
            if layers_in_use["contour"]:
                plot.show_contour = True
            if layers_in_use["shade"]:
                plot.show_shade = True
            if layers_in_use["vector"]:
                plot.show_vector = True
            if layers_in_use["edge"]:
                plot.show_edge = True
            
            print(f"Layers activated: {[k for k,v in layers_in_use.items() if v]}")

    print("Zone styling complete.")
