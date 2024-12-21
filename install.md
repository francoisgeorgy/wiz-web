    francois@m2:~/dev/projects/wiz-web $ sudo python3 setup.py install
    running install
    /opt/homebrew/lib/python3.13/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
    !!
    
            ********************************************************************************
            Please avoid running ``setup.py`` directly.
            Instead, use pypa/build, pypa/installer or other
            standards-based tools.
    
            See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
            ********************************************************************************
    
    !!
      self.initialize_options()
    /opt/homebrew/lib/python3.13/site-packages/setuptools/_distutils/cmd.py:66: EasyInstallDeprecationWarning: easy_install command is deprecated.
      self.initialize_options()
    running bdist_egg
    running egg_info
    creating wiz.egg-info
    writing wiz.egg-info/PKG-INFO
    writing dependency_links to wiz.egg-info/dependency_links.txt
    writing entry points to wiz.egg-info/entry_points.txt
    writing top-level names to wiz.egg-info/top_level.txt
    writing manifest file 'wiz.egg-info/SOURCES.txt'
    reading manifest file 'wiz.egg-info/SOURCES.txt'
    writing manifest file 'wiz.egg-info/SOURCES.txt'
    installing library code to build/bdist.macosx-13.0-arm64/egg
    running install_lib
    running build_py
    creating build/lib
    copying wiz.py -> build/lib
    creating build/bdist.macosx-13.0-arm64/egg
    copying build/lib/wiz.py -> build/bdist.macosx-13.0-arm64/egg
    byte-compiling build/bdist.macosx-13.0-arm64/egg/wiz.py to wiz.cpython-313.pyc
    creating build/bdist.macosx-13.0-arm64/egg/EGG-INFO
    copying wiz.egg-info/PKG-INFO -> build/bdist.macosx-13.0-arm64/egg/EGG-INFO
    copying wiz.egg-info/SOURCES.txt -> build/bdist.macosx-13.0-arm64/egg/EGG-INFO
    copying wiz.egg-info/dependency_links.txt -> build/bdist.macosx-13.0-arm64/egg/EGG-INFO
    copying wiz.egg-info/entry_points.txt -> build/bdist.macosx-13.0-arm64/egg/EGG-INFO
    copying wiz.egg-info/top_level.txt -> build/bdist.macosx-13.0-arm64/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating dist
    creating 'dist/wiz-1.0.0-py3.13.egg' and adding 'build/bdist.macosx-13.0-arm64/egg' to it
    removing 'build/bdist.macosx-13.0-arm64/egg' (and everything under it)
    Processing wiz-1.0.0-py3.13.egg
    Copying wiz-1.0.0-py3.13.egg to /opt/homebrew/lib/python3.13/site-packages
    Adding wiz 1.0.0 to easy-install.pth file
    Installing wiz script to /opt/homebrew/bin
    
    Installed /opt/homebrew/lib/python3.13/site-packages/wiz-1.0.0-py3.13.egg
    Processing dependencies for wiz==1.0.0
    Finished processing dependencies for wiz==1.0.0


    
    $ which wiz
    /opt/homebrew/bin/wiz