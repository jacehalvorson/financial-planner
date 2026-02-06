from pywire import PyWire

# Create application instance
app = PyWire(
    pages_dir="src/pages",
    enable_pjax=True,
    debug=True,
)