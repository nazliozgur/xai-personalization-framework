"""
XAE-FRAME: PUBLICATION-QUALITY VISUALIZATION TEMPLATE
IEEE/ACM/Springer Conference & Journal Standards

This template ensures all figures meet:
- IEEE Transactions style guide
- ACM SIGCHI formatting
- Springer LNCS requirements
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# PUBLICATION SETTINGS (MUST USE IN EVERY NOTEBOOK)

# Color-blind friendly palette (Wong 2011, Nature Methods)
CB_COLORS = {
    'blue': '#0173B2',      # Primary
    'orange': '#DE8F05',    # Secondary
    'green': '#029E73',     # Success
    'purple': '#CC78BC',    # Accent 1
    'brown': '#CA9161',     # Accent 2
    'pink': '#ECE133',      # Highlight
    'red': '#D55E00',       # Danger
    'black': '#000000',
    'gray': '#949494'
}

CB_PALETTE = [CB_COLORS['blue'], CB_COLORS['orange'], CB_COLORS['green'], 
              CB_COLORS['purple'], CB_COLORS['brown']]

# Set global matplotlib parameters (IEEE standard)
plt.rcParams.update({
    # Figure size (column width for IEEE is ~3.5 inches)
    'figure.figsize': (7, 5),           # Single column
    'figure.dpi': 100,                  # Screen preview
    'savefig.dpi': 300,                 # Publication quality
    'savefig.format': 'png',            # Default format
    'savefig.bbox': 'tight',            # No cropping
    
    # Fonts (IEEE prefers Times, ACM prefers Arial/Helvetica)
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,                    # Base font size
    
    # Axes
    'axes.labelsize': 11,               # Axis label font size
    'axes.titlesize': 12,               # Title font size
    'axes.titleweight': 'bold',         # Bold titles
    'axes.linewidth': 1.0,              # Axis line width
    'axes.grid': True,                  # Enable grid by default
    'axes.axisbelow': True,             # Grid behind data
    
    # Ticks
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'xtick.direction': 'in',            # Ticks inside
    'ytick.direction': 'in',
    
    # Legend
    'legend.fontsize': 9,
    'legend.framealpha': 0.9,
    'legend.edgecolor': 'black',
    'legend.fancybox': False,           # Square legend box
    
    # Grid
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    
    # Lines
    'lines.linewidth': 1.5,
    'lines.markersize': 6,
})

# Seaborn theme
sns.set_theme(style='whitegrid', palette=CB_PALETTE)

# FIGURE CREATION TEMPLATES

def create_publication_figure(nrows=1, ncols=1, figsize=None, 
                              sharex=False, sharey=False):
    """
    Create a publication-ready figure with IEEE/ACM standards.
    
    Args:
        nrows: Number of subplot rows
        ncols: Number of subplot columns
        figsize: Tuple (width, height) in inches
                 - Single column: (3.5, 2.5)
                 - Double column: (7.0, 5.0)
                 - Full page: (7.0, 9.0)
        sharex/sharey: Share axes between subplots
    
    Returns:
        fig, axes: Matplotlib figure and axes objects
    """
    if figsize is None:
        # Auto-calculate based on layout
        if ncols == 1:
            figsize = (3.5, 2.5 * nrows)  # Single column
        elif ncols == 2:
            figsize = (7.0, 2.5 * nrows)  # Double column
        else:
            figsize = (7.0, 5.0)  # Default
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize,
                             sharex=sharex, sharey=sharey,
                             constrained_layout=True)
    
    return fig, axes


def save_publication_figure(fig, filename, formats=['png', 'svg'], **kwargs):
    """
    Save figure in multiple formats for publication.
    
    Args:
        fig: Matplotlib figure object
        filename: Base filename (without extension)
        formats: List of formats ['png', 'svg', 'pdf']
        **kwargs: Additional savefig arguments
    """
    import os
    
    # Ensure output directory exists
    output_dir = '../docs/figures'
    os.makedirs(output_dir, exist_ok=True)
    
    # Default save parameters
    save_params = {
        'dpi': 300,
        'bbox_inches': 'tight',
        'facecolor': 'white',
        'edgecolor': 'none'
    }
    save_params.update(kwargs)
    
    # Save in each format
    for fmt in formats:
        filepath = os.path.join(output_dir, f"{filename}.{fmt}")
        
        # Adjust DPI for vector formats
        if fmt in ['svg', 'pdf']:
            save_params_copy = save_params.copy()
            save_params_copy.pop('dpi', None)  # Not needed for vector
            fig.savefig(filepath, format=fmt, **save_params_copy)
        else:
            fig.savefig(filepath, format=fmt, **save_params)
        
        print(f"✓ Saved: {filepath}")


def add_figure_caption(fig, caption, figure_number=None):
    """
    Add IEEE-style caption below figure.
    
    Args:
        fig: Matplotlib figure object
        caption: Caption text
        figure_number: Figure number (e.g., 1, 2, 3)
    """
    if figure_number is not None:
        caption = f"Figure {figure_number}. {caption}"
    
    fig.text(0.5, -0.02, caption,
             ha='center', va='top',
             fontsize=9, style='italic',
             wrap=True)


def add_panel_labels(axes, labels=None, loc='upper left', 
                     fontsize=12, fontweight='bold'):
    """
    Add panel labels (A, B, C, D) to multi-panel figures.
    
    Args:
        axes: Array of axes objects
        labels: List of labels (default: A, B, C, ...)
        loc: Label location
        fontsize: Label font size
        fontweight: Label font weight
    """
    if labels is None:
        import string
        labels = list(string.ascii_uppercase)
    
    # Flatten axes if needed
    if hasattr(axes, 'flatten'):
        axes_flat = axes.flatten()
    else:
        axes_flat = [axes]
    
    for ax, label in zip(axes_flat, labels):
        ax.text(0.02, 0.98, f'({label})',
                transform=ax.transAxes,
                fontsize=fontsize, fontweight=fontweight,
                va='top', ha='left',
                bbox=dict(boxstyle='round', facecolor='white', 
                         alpha=0.8, edgecolor='none'))


# EXAMPLE USAGE

def example_publication_figure():
    """Example: Create a publication-ready figure."""
    
    # Generate sample data
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
    y2 = np.cos(x) + np.random.normal(0, 0.1, 100)
    
    # Create figure
    fig, axes = create_publication_figure(nrows=1, ncols=2, figsize=(7, 3))
    
    # Panel A: Line plot
    axes[0].plot(x, y1, label='sin(x)', color=CB_COLORS['blue'], linewidth=2)
    axes[0].plot(x, y2, label='cos(x)', color=CB_COLORS['orange'], linewidth=2)
    axes[0].set_xlabel('X-axis (units)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Y-axis (units)', fontsize=11, fontweight='bold')
    axes[0].set_title('Time Series Analysis', fontsize=12, fontweight='bold')
    axes[0].legend(loc='best', frameon=True)
    axes[0].grid(alpha=0.3)
    
    # Panel B: Scatter plot
    scatter = axes[1].scatter(y1, y2, c=x, cmap='viridis', 
                              s=30, alpha=0.6, edgecolors='black', linewidth=0.5)
    axes[1].set_xlabel('sin(x)', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('cos(x)', fontsize=11, fontweight='bold')
    axes[1].set_title('Correlation Analysis', fontsize=12, fontweight='bold')
    axes[1].grid(alpha=0.3)
    cbar = plt.colorbar(scatter, ax=axes[1])
    cbar.set_label('Time', fontsize=10)
    
    # Add panel labels
    add_panel_labels(axes, labels=['A', 'B'])
    
    # Add caption
    add_figure_caption(fig, 
                       "Example publication-quality figure. (A) Time series of sine and cosine functions with added noise. (B) Correlation plot showing relationship between the two signals. N=100 samples.",
                       figure_number=1)
    
    # Save in multiple formats
    save_publication_figure(fig, 'example_publication_figure', 
                           formats=['png', 'svg', 'pdf'])
    
    plt.show()


# COMMON PLOT TYPES

def plot_bar_chart(data, labels, xlabel, ylabel, title, 
                   colors=None, filename=None):
    """Create publication-quality bar chart."""
    
    fig, ax = create_publication_figure(figsize=(5, 4))
    
    if colors is None:
        colors = CB_PALETTE[:len(data)]
    
    bars = ax.bar(range(len(data)), data, color=colors, 
                  edgecolor='black', linewidth=1, alpha=0.8)
    
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_xlabel(xlabel, fontsize=11, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=9)
    
    if filename:
        save_publication_figure(fig, filename)
    
    return fig, ax


def plot_time_series(dates, values, xlabel, ylabel, title, 
                     confidence_band=None, filename=None):
    """Create publication-quality time series plot."""
    
    fig, ax = create_publication_figure(figsize=(6, 4))
    
    ax.plot(dates, values, color=CB_COLORS['blue'], 
            linewidth=2, marker='o', markersize=4)
    
    if confidence_band is not None:
        lower, upper = confidence_band
        ax.fill_between(dates, lower, upper, 
                        alpha=0.2, color=CB_COLORS['blue'],
                        label='95% CI')
    
    ax.set_xlabel(xlabel, fontsize=11, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3)
    ax.tick_params(axis='x', rotation=45)
    
    if confidence_band is not None:
        ax.legend(loc='best')
    
    if filename:
        save_publication_figure(fig, filename)
    
    return fig, ax


def plot_heatmap(data, xticklabels, yticklabels, title, 
                 cmap='RdYlGn', filename=None):
    """Create publication-quality heatmap."""
    
    fig, ax = create_publication_figure(figsize=(6, 5))
    
    im = ax.imshow(data, cmap=cmap, aspect='auto')
    
    ax.set_xticks(range(len(xticklabels)))
    ax.set_yticks(range(len(yticklabels)))
    ax.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax.set_yticklabels(yticklabels)
    
    ax.set_title(title, fontsize=12, fontweight='bold', pad=15)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.ax.tick_params(labelsize=9)
    
    # Add values in cells
    for i in range(len(yticklabels)):
        for j in range(len(xticklabels)):
            text = ax.text(j, i, f'{data[i, j]:.2f}',
                          ha="center", va="center", 
                          color="black", fontsize=8)
    
    if filename:
        save_publication_figure(fig, filename)
    
    return fig, ax


# QUALITY CHECK FUNCTION

def check_figure_quality(fig):
    """
    Check if figure meets publication standards.
    
    Returns dict with quality metrics.
    """
    checks = {
        'dpi': fig.dpi >= 300,
        'font_size': plt.rcParams['font.size'] >= 9,
        'title_present': any(ax.get_title() for ax in fig.axes),
        'labels_present': all(ax.get_xlabel() and ax.get_ylabel() 
                             for ax in fig.axes),
        'grid_enabled': all(ax.xaxis._gridOnMajor or ax.yaxis._gridOnMajor 
                           for ax in fig.axes)
    }
    
    all_passed = all(checks.values())
    
    return {
        'passed': all_passed,
        'checks': checks,
        'score': sum(checks.values()) / len(checks) * 100
    }


# USAGE NOTES

"""
BEST PRACTICES FOR IEEE/ACM/SPRINGER PUBLICATIONS:

1. ALWAYS use this template at the start of your notebook:
   
   from publication_viz_template import *
   
2. Create figures with:
   
   fig, ax = create_publication_figure(figsize=(7, 5))
   
3. Save in BOTH PNG and SVG:
   
   save_publication_figure(fig, 'my_figure', formats=['png', 'svg'])
   
4. Add captions for papers:
   
   add_figure_caption(fig, "Description here", figure_number=1)
   
5. Use panel labels for multi-panel figures:
   
   add_panel_labels(axes, labels=['A', 'B', 'C'])
   
6. Check quality before submission:
   
   quality = check_figure_quality(fig)
   print(f"Quality score: {quality['score']:.0f}%")

7. Color-blind friendly colors:
   
   Always use CB_COLORS dictionary!

8. Font sizes:
   
   Title: 12pt (bold)
   Labels: 11pt (bold)
   Ticks: 9pt
   Legend: 9pt
   Caption: 9pt (italic)

9. Figure sizes (IEEE column width = 3.5 inches):
   
   Single column: (3.5, 2.5)
   Double column: (7.0, 5.0)
   Full page: (7.0, 9.0)

10. File formats:
    
    - PNG (300 DPI) for web/preview
    - SVG/PDF for print (vector graphics)
"""

print(" Publication-quality visualization template loaded!")
print("  Use: from publication_viz_template import *")
print("  Docs: See docstrings for each function")
