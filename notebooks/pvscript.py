
import argparse
import json
from pathlib import Path
from paraview import simple as pvs

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('path')

arg_parser.add_argument('--particles_var')
arg_parser.add_argument('--particles_unit')
arg_parser.add_argument('--particles_color_range')
arg_parser.add_argument('--particles_var_multiplier', default=1)
arg_parser.add_argument('--particles_logscale', default=False)

arg_parser.add_argument('--surface_var')
arg_parser.add_argument('--surface_color_range')
arg_parser.add_argument('--surface_unit')

arg_parser.add_argument('--save_frame_pdfs', action=argparse.BooleanOptionalAction)
arg_parser.add_argument('--anim_path_suffix', default='')

args = arg_parser.parse_args()

# load data
reader_prod = pvs.OpenDataFile(f"{args.path}/output/sd_products.pvd")
reader_attr = pvs.OpenDataFile(f"{args.path}/output/sd_attributes.pvd")

# prepare view settings
view = pvs.GetRenderView()
view.ViewSize = [2000, 800]
view.Background = [1, 1, 1]
view.CenterAxesVisibility = False
view.OrientationAxesVisibility = False
axesGrid = view.AxesGrid
axesGrid.Visibility = True
axesGrid.XTitle = 'Z [$m$]'
axesGrid.YTitle = 'X [$m$]'

axesGrid.XAxisUseCustomLabels = True
axesGrid.XAxisLabels = [0, 125, 375, 500]
axesGrid.YAxisUseCustomLabels = True
axesGrid.YAxisLabels = [300, 600, 900, 1200]

axesGrid.XTitleFontSize = 30
axesGrid.XLabelFontSize = 30
axesGrid.YTitleFontSize = 30
axesGrid.YLabelFontSize = 30

axesGrid.XTitleColor = [0, 0, 0]
axesGrid.XLabelColor = [0, 0, 0]
axesGrid.YTitleColor = [0, 0, 0]
axesGrid.YLabelColor = [0, 0, 0]
axesGrid.GridColor = [0.1, 0.1, 0.1]

# render particles
if args.particles_var is not None:
    palette = 'Cold and Hot'
    palette_invert = True
    title = args.particles_var + r' [$' + args.particles_unit + '$]'
    
    calculator = pvs.Calculator(reader_attr)
    calculator.Function = f'{args.particles_var}*{args.particles_var_multiplier}'
    display_attr = pvs.Show(calculator, view)
    
    display_attr.SetRepresentationType('Point Gaussian')
    display_attr.ShaderPreset = 'Sphere'
    display_attr.GaussianRadius = 3
    display_attr.MapScalars = 1
    
    display_attr.Ambient = .25
    pvs.ColorBy(display_attr, ('POINTS', 'Result'))
    color_scale_attr = pvs.GetColorTransferFunction('Result')
    color_scale_attr.ApplyPreset(palette, True)
    if palette_invert:
        color_scale_attr.InvertTransferFunction()
    if args.particles_color_range is None:
        display_attr.RescaleTransferFunctionToDataRange(True)
    else:
        color_scale_attr.RescaleTransferFunction(json.loads(args.particles_color_range))
    if args.particles_logscale:
        color_scale_attr.MapControlPointsToLogSpace()
        color_scale_attr.UseLogScale = 1
    colorbar_attr = pvs.GetScalarBar(color_scale_attr, view)
    colorbar_attr.TitleColor = [0, 0, 0]
    colorbar_attr.LabelColor = [0, 0, 0]
    colorbar_attr.Title = title
    colorbar_attr.ComponentTitle = ''
    colorbar_attr.TitleFontSize = 30
    colorbar_attr.LabelFontSize = 30
    colorbar_attr.Visibility = True
    colorbar_attr.WindowLocation = 'Any Location'
    colorbar_attr.Position = [.025, .333]
    colorbar_attr.RangeLabelFormat = '%g'
    
# render product
if args.surface_var is not None:
    palette = 'X Ray'
    palette_invert = True
    color_range = [0, 300]
    logscale = False
    title = '$' + args.surface_var + '$' + ' [$' + args.surface_unit + '$ STP]'
    
    display_prod = pvs.Show(reader_prod)
    display_prod.SetRepresentationType('Surface')
    display_prod.Ambient = .25
    pvs.ColorBy(display_prod, ('CELLS', args.surface_var))
    color_scale_prod = pvs.GetColorTransferFunction(args.surface_var)
    if args.surface_color_range is None:
        display_prod.RescaleTransferFunctionToDataRange(True)
    else:
        color_scale_prod.RescaleTransferFunction(json.loads(args.surface_color_range))
    color_scale_prod.ApplyPreset(palette, True)
    if palette_invert:
        color_scale_prod.InvertTransferFunction()
    colorbar_prod = pvs.GetScalarBar(color_scale_prod, view)
    colorbar_prod.TitleColor = [0, 0, 0]
    colorbar_prod.LabelColor = [0, 0, 0]
    colorbar_prod.Title = title
    colorbar_prod.ComponentTitle = ''
    colorbar_prod.TitleFontSize = 30
    colorbar_prod.LabelFontSize = 30
    colorbar_prod.Visibility = True
    colorbar_prod.Position = [.925, .333]
    colorbar_prod.WindowLocation = 'Any Location'
    colorbar_prod.RangeLabelFormat = '%g'

# time annotation
time = pvs.AnnotateTimeFilter(guiName = "AnnotateTimeFilter1", Format = 'Time: %gs')
repr = pvs.Show(time, view)
repr.Color = [0.0, 0.0, 0.0]
repr.FontSize = 20
view.Update()

# compose the scene
scene = pvs.GetAnimationScene()
scene.UpdateAnimationUsingDataTimeSteps()
pvs.Render(view)
cam = pvs.GetActiveCamera()
cam.SetViewUp(1, 0, 0)
pos = list(cam.GetPosition())
pos[-1] = -pos[-1]
cam.SetPosition(pos)
cam.Dolly(1.85)

# save animation to an Ogg Vorbis file
anim_file = f'{args.path}/anim{args.anim_path_suffix}.ogv'
print(anim_file)
pvs.SaveAnimation(anim_file, view, FrameRate=5, Quality=0)

# save animation frame as pdfs
if args.save_frame_pdfs is not None:
    for t in reader_prod.TimestepValues:
        view.ViewTime = t
        for reader in (reader_prod, reader_attr):
            reader.UpdatePipeline(t)
        pvs.ExportView(
            filename=f'{args.path}/anim_frame_{t}{args.anim_path_suffix}.pdf',
            view=view,
            Rasterize3Dgeometry= False,
            GL2PSdepthsortmethod= 'BSP sorting (slow, best)',
        )
