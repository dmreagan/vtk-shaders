# vtk-shaders

Two simple examples of applying custom shader code to a VTK object. These examples demonstrate two methods of customizing shaders with the `vtkOpenGLPolyDataMapper`. The first method modifies the existing shader using `AddShaderReplacement`. The second method injects a custom shader using `SetVertexShaderCode` and `SetFragmentShaderCode`. Requires VTK >=7.0.

## Resources

This example borrows from:

* http://www.vtk.org/Wiki/VTK/Examples/Python/Cylinder
* http://www.vtk.org/Wiki/Shader_In_VTK
* https://gitlab.kitware.com/vtk/vtk/blob/v7.0.0.rc2/Rendering/OpenGL2/Testing/Cxx/TestUserShader.cxx

See also:

* https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/OpenGL2/vtkOpenGLPolyDataMapper.cxx
* https://gitlab.kitware.com/vtk/vtk/tree/master/Rendering/OpenGL2/glsl
* http://noeskasmit.com/shaders-vtk-cel-shaded-skull-example-100-lines-python-code/
