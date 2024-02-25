from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = "20240222"
except PackageNotFoundError:
    # package is not installed, return default
    __version__ = "20240222"

if __name__ == "__main__":
    print(__version__)
