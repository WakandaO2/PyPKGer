# **PyPKGer**


## Introduction
"Scene" Wallpapers used in Wallpaper Engine are saved in proprietary PKG format.  
With this tool you can extract PKG files or convert them to known archive formats.  

## Features
- Convert PKG files to/from other archive formats.
- Extract PKG files.

## Usage
- Convert "package.pkg" to ZIP archive:
```bash
python3 ./pypkger.py -ot zip "package.pkg" 
```

- Create a PKG file from the directory "dir":
```bash
python3 ./pypkger.py -ot pkg "dir/"
```

- Extract "package.pkg":
```bash
python3 ./pypkger.py "package.pkg"
```

## Planned Features
- TEX files support. (TEX is another format used by Wallpaper Engine.)

---
### Further Notes
* This tool was created for educational purposes only.
* PKG files might contain copyrighted materials.
