# vtk-shaders

A simple example of applying custom shader code to a VTK object. Requires VTK >=7.0

## Installing VTK 7 on Windows
VTK 7 is not yet available on Anaconda or the like, so to install it on your system, download the standalone Python interface (installer) from [the VTK website](http://www.vtk.org/download/). This will install a version of Python with VTK built in in C:\Program Files\VTK 7.1.0. 

## Running this example on Windows
Once vtkpython is installed on your system, clone this repository and navigate to it. From the repo directory, you can run the example code with:

```
"C:\Program Files\VTK 7.1.0\bin\vtkpython.exe" vtk-shaders.py
```

The example code demonstrates two methods of customizing shaders with the `vtkOpenGLPolyDataMapper`. The default method modifies the existing shader using `AddShaderReplacement`.

The second method injects a custom shader using `SetVertexShaderCode` and `SetFragmentShaderCode`. To switch to method #2, comment out the block of code under where it says METHOD #1 and uncomment the block of code under where it says METHOD #2.

## Resources
This example borrows from:
* http://www.vtk.org/Wiki/VTK/Examples/Python/Cylinder
* http://www.vtk.org/Wiki/Shader_In_VTK
* https://gitlab.kitware.com/vtk/vtk/blob/v7.0.0.rc2/Rendering/OpenGL2/Testing/Cxx/TestUserShader.cxx
