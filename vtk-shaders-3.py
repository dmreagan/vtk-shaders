# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:35 2018

@author: Ashutosh
"""
import vtk

case = 3
#### Case 1 for normal rendering of a line WITHOUT any Geometric Shader
#### Case 2 for using SetRenderLinesAsTubes to render with the help of WideLineGS
#### Case 3 for manually injecting Geometry Shader (NOT WORKING)


lineSource = vtk.vtkLineSource()
lineSource.SetPoint1([1.0, 0.0, 0.0])
lineSource.SetPoint2([0.0, 1.0, 0.0])

mapper = vtk.vtkOpenGLPolyDataMapper()
mapper.SetInputConnection(lineSource.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetLineWidth(11)
if case == 2:
    actor.GetProperty().SetRenderLinesAsTubes(1)
if case == 3:
    mapper.SetGeometryShaderCode(
        "//VTK::System::Dec\n"
        "//VTK::PositionVC::Dec\n"
        "//VTK::PrimID::Dec\n"
        "//VTK::Color::Dec\n"
        "//VTK::Normal::Dec\n"
        "//VTK::Light::Dec\n"
        "//VTK::TCoord::Dec\n"
        "//VTK::Picking::Dec\n"
        "//VTK::DepthPeeling::Dec\n"
        "//VTK::Clip::Dec\n"
        "//VTK::Output::Dec\n"
        "uniform vec2 lineWidthNVC;\n"
        "layout(lines) in;\n"
        "layout(triangle_strip, max_vertices = 4) out;\n"
        "void main() {\n"
        "   vec2 normal = normalize(\n"
        "       gl_in[1].gl_Position.xy/gl_in[1].gl_Position.w - gl_in[0].gl_Position.xy/gl_in[0].gl_Position.w);\n"
        "   normal = vec2(-1.0*normal.y,normal.x);\n"
        "   for (int j = 0; j < 4; j++){\n"
        "       int i = j/2;\n"
        "       //VTK::PrimID::Impl\n"
        "       //VTK::Clip::Impl\n"
        "       //VTK::Color::Impl\n"
        "       //VTK::Normal::Impl\n"
        "       //VTK::Light::Impl\n"
        "       //VTK::TCoord::Impl\n"
        "       //VTK::DepthPeeling::Impl\n"
        "       //VTK::Picking::Impl\n"
        "       //VTK::PositionVC::Impl\n"
        "       gl_Position = vec4(\n"
        "           gl_in[i].gl_Position.xy + (lineWidthNVC*normal)*((j+1)%2 - 0.5)*gl_in[i].gl_Position.w, gl_in[i].gl_Position.z, gl_in[i].gl_Position.w);\n"
        "       EmitVertex();\n"
        "   }\n"
        "   EndPrimitive();\n"
        "}\n"
        )

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor)

renderWindow.Render()
renderWindowInteractor.Start()