#!/usr/bin/env python
 
# This simple example shows how to do basic rendering and pipeline
# creation.
 
import vtk
# The colors module defines various useful colors.
from vtk.util.colors import tomato
 
# This creates a polygonal cylinder model with eight circumferential
# facets.
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(8)
 
# The mapper is responsible for pushing the geometry into the graphics
# library. It may also do color mapping, if scalars or other
# attributes are defined.
cylinderMapper = vtk.vtkOpenGLPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())




# METHOD #2
# Use our own hardcoded shader code. Generally this is a bad idea in a
# general purpose program as there are so many things VTK supports that
# hardcoded shaders will not handle depth peeling, picking, etc, but if you
# know what your data will be like it can be very useful. The mapper will set
# a bunch of uniforms regardless of if you are using them. But feel free to
# use them :-)
cylinderMapper.SetVertexShaderCode(
"//VTK::System::Dec\n"  # always start with this line
"attribute vec4 vertexMC;\n"
# use the default normal decl as the mapper
# will then provide the normalMatrix uniform
# which we use later on
"//VTK::Normal::Dec\n"
"uniform mat4 MCDCMatrix;\n"
"void main () {\n"
"  normalVCVSOutput = normalMatrix * normalMC;\n"
# do something weird with the vertex positions
# this will mess up your head if you keep
# rotating and looking at it, very trippy
"  vec4 tmpPos = MCDCMatrix * vertexMC;\n"
"  gl_Position = tmpPos*vec4(0.2+0.8*abs(tmpPos.x),0.2+0.8*abs(tmpPos.y),1.0,1.0);\n"
"}\n"
)

cylinderMapper.SetFragmentShaderCode(
"//VTK::System::Dec\n"  # always start with this line
"//VTK::Output::Dec\n"  # always have this line in your FS
"varying vec3 normalVCVSOutput;\n"
"uniform vec3 diffuseColorUniform;\n"
"void main () {\n"
"  float df = max(0.0, normalVCVSOutput.z);\n"
"  float sf = pow(df, 20.0);\n"
"  vec3 diffuse = df * diffuseColorUniform;\n"
"  vec3 specular = sf * vec3(0.4,0.4,0.4);\n"
"  gl_FragData[0] = vec4(0.3*abs(normalVCVSOutput) + 0.7*diffuse + specular, 1.0);\n"
"}\n"
)




 
# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it -22.5 degrees.
cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(tomato)
cylinderActor.RotateX(30.0)
cylinderActor.RotateY(-45.0)
 
# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 
# Add the actors to the renderer, set the background and size
ren.AddActor(cylinderActor)
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200, 200)
 
# This allows the interactor to initalize itself. It has to be
# called before an event loop.
iren.Initialize()
 
# We'll zoom in a little by accessing the camera and invoking a "Zoom"
# method on it.
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()
 
# Start the event loop.
iren.Start()