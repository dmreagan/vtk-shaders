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
    mapper.SetGeometryShaderCode("""
        //VTK::System::Dec
        //VTK::PositionVC::Dec
        //VTK::PrimID::Dec
        //VTK::Color::Dec
        //VTK::Normal::Dec
        //VTK::Light::Dec
        //VTK::TCoord::Dec
        //VTK::Picking::Dec
        //VTK::DepthPeeling::Dec
        //VTK::Clip::Dec
        //VTK::Output::Dec
        uniform vec2 lineWidthNVC;
        layout(lines) in;
        layout(triangle_strip, max_vertices = 4) out;
        void main() {
            int lineWidth = 10;
            vec2 lineWidthNVC2 = vec2(2.0*lineWidth/500, 2.0*lineWidth/500);
            vec2 normal = normalize(
                gl_in[1].gl_Position.xy/gl_in[1].gl_Position.w - gl_in[0].gl_Position.xy/gl_in[0].gl_Position.w);
            normal = vec2(-1.0*normal.y,normal.x);
            for (int j = 0; j < 4; j++){
                int i = j/2;
                //VTK::PrimID::Impl
                //VTK::Clip::Impl
                //VTK::Color::Impl
                //VTK::Normal::Impl
                //VTK::Light::Impl
                //VTK::TCoord::Impl
                //VTK::DepthPeeling::Impl
                //VTK::Picking::Impl
                //VTK::PositionVC::Impl
                gl_Position = vec4(
                    //gl_in[i].gl_Position.xy + (lineWidthNVC*normal)*((j+1)%2 - 0.5)*gl_in[i].gl_Position.w, gl_in[i].gl_Position.z, gl_in[i].gl_Position.w);
                    //gl_in[i].gl_Position.xy + (vec2(0.01, 0.01)*normal)*((j+1)%2 - 0.5)*gl_in[i].gl_Position.w, gl_in[i].gl_Position.z, gl_in[i].gl_Position.w);
                    gl_in[i].gl_Position.xy + (lineWidthNVC2*normal)*((j+1)%2 - 0.5)*gl_in[i].gl_Position.w, gl_in[i].gl_Position.z, gl_in[i].gl_Position.w);
                EmitVertex();
            }
            EndPrimitive();
        }
    """)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor)

renderWindow.Render()
renderWindowInteractor.Start()