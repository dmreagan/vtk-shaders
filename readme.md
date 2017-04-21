# vtk-shaders

Two simple examples of applying custom shader code to a VTK object. These examples demonstrate two methods of customizing shaders with the `vtkOpenGLPolyDataMapper`. The first method modifies the existing shader using `AddShaderReplacement`. The second method injects a custom shader using `SetVertexShaderCode` and `SetFragmentShaderCode`. Requires VTK >=7.0. 

## Installing VTK 7 on Windows
VTK 7 is not yet available on Anaconda or the like, so to install it on your system, download the standalone Python interface (installer) from [the VTK website](http://www.vtk.org/download/). This will install a version of Python with VTK built in in C:\Program Files\VTK 7.1.0. 

## Running these examples on Windows
Once vtkpython is installed on your system, clone this repository and navigate to it. From the repo directory, you can run the first example with:

```
"C:\Program Files\VTK 7.1.0\bin\vtkpython.exe" vtk-shaders-1.py
```

You can run the second example with: 

```
"C:\Program Files\VTK 7.1.0\bin\vtkpython.exe" vtk-shaders-2.py
```

## Resources
This example borrows from:
* http://www.vtk.org/Wiki/VTK/Examples/Python/Cylinder
* http://www.vtk.org/Wiki/Shader_In_VTK
* https://gitlab.kitware.com/vtk/vtk/blob/v7.0.0.rc2/Rendering/OpenGL2/Testing/Cxx/TestUserShader.cxx

See also:
* https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/OpenGL2/vtkOpenGLPolyDataMapper.cxx
* https://gitlab.kitware.com/vtk/vtk/tree/master/Rendering/OpenGL2/glsl
* http://noeskasmit.com/shaders-vtk-cel-shaded-skull-example-100-lines-python-code/
