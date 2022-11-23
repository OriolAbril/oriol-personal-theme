"""A thin sphinx theme to customize and adapt pydata-sphinx-theme for my website."""

__version__ = "0.1"

from pathlib import Path


# For more details, see:
# https://www.sphinx-doc.org/en/master/development/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    theme_path = Path(__file__).parent.resolve()
    app.add_html_theme("oriol_personal_theme", str(theme_path))
    app.config.templates_path.append(str(theme_path / "components"))
    return {"version": __version__, "parallel_read_safe": True}
