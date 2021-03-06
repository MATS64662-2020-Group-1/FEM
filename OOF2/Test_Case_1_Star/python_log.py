OOF.Microstructure.Create_From_ImageFile(filename='/home/nanohub/srehman6/data/results/1646090/Screenshot 2020-06-08 at 23.58.43.png', microstructure_name='Screenshot 2020-06-08 at 23.58.43.png', height=automatic, width=automatic)
OOF.Windows.Graphics.New()
OOF.Graphics_1.Toolbox.Pixel_Select.Color(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', range=DeltaRGB(delta_red=0,delta_green=0,delta_blue=0), points=[Point(352.9,301.14)], shift=0, ctrl=0)
OOF.Graphics_1.Toolbox.Pixel_Select.Color(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', range=DeltaRGB(delta_red=0,delta_green=0,delta_blue=0), points=[Point(214.3,433.58)], shift=0, ctrl=0)
OOF.Graphics_1.Toolbox.Pixel_Select.Color(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', range=DeltaRGB(delta_red=0,delta_green=0,delta_blue=0), points=[Point(205.06,279.58)], shift=0, ctrl=0)
OOF.Graphics_1.Toolbox.Pixel_Select.Burn(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', local_flammability=0.1, global_flammability=0.2, color_space_norm='L1', next_nearest=False, points=[Point(365.22,353.5)], shift=0, ctrl=0)
OOF.PixelGroup.New(name='star', microstructure='Screenshot 2020-06-08 at 23.58.43.png')
OOF.PixelGroup.AddSelection(microstructure='Screenshot 2020-06-08 at 23.58.43.png', group='star')
OOF.Graphics_1.Toolbox.Pixel_Select.Burn(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', local_flammability=0.1, global_flammability=0.2, color_space_norm='L1', next_nearest=False, points=[Point(226.62,479.78)], shift=0, ctrl=0)
OOF.PixelGroup.New(name='background', microstructure='Screenshot 2020-06-08 at 23.58.43.png')
OOF.Material.New(name='star_material', material_type='bulk')
OOF.Material.New(name='background_material', material_type='bulk')
OOF.Property.Copy(property='Mechanical:Elasticity:Isotropic', new_name='youngs_star')
OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.youngs_star(cijkl=IsotropicRank4TensorEnu(young=300000000000.0,poisson=0.3333333333333333))
OOF.Material.Add_property(name='star_material', property='Mechanical:Elasticity:Isotropic:youngs_star')
OOF.Property.Copy(property='Thermal:Conductivity:Isotropic', new_name='k_star')
OOF.Property.Parametrize.Thermal.Conductivity.Isotropic.k_star(kappa=1000)
OOF.Material.Add_property(name='star_material', property='Thermal:Conductivity:Isotropic:k_star')
OOF.Property.Copy(property='Couplings:ThermalExpansion:Isotropic', new_name='a_star')
OOF.Property.Parametrize.Couplings.ThermalExpansion.Isotropic.a_star(alpha=5e-06, T0=0.0)
OOF.Material.Add_property(name='star_material', property='Couplings:ThermalExpansion:Isotropic:a_star')
OOF.Property.Copy(property='Color', new_name='colour_star')
OOF.Property.Parametrize.Color.colour_star(color=Gray(value=0.0))
OOF.Material.Add_property(name='star_material', property='Color:colour_star')
OOF.Material.Assign(material='star_material', microstructure='Screenshot 2020-06-08 at 23.58.43.png', pixels='star')
OOF.Property.Copy(property='Mechanical:Elasticity:Isotropic', new_name='youngs_background')
OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.youngs_background(cijkl=IsotropicRank4TensorEnu(young=10000000000.0,poisson=0.27))
OOF.Material.Add_property(name='background_material', property='Mechanical:Elasticity:Isotropic:youngs_background')
OOF.Property.Copy(property='Thermal:Conductivity:Isotropic', new_name='k_background')
OOF.Property.Parametrize.Thermal.Conductivity.Isotropic.k_background(kappa=1.0)
OOF.Material.Add_property(name='background_material', property='Thermal:Conductivity:Isotropic:k_background')
OOF.Property.Copy(property='Couplings:ThermalExpansion:Isotropic', new_name='a_background')
OOF.Property.Parametrize.Couplings.ThermalExpansion.Isotropic.a_background(alpha=1.0, T0=0.0)
OOF.Material.Add_property(name='background_material', property='Couplings:ThermalExpansion:Isotropic:a_background')
OOF.Property.Copy(property='Color', new_name='colour_background')
OOF.Property.Parametrize.Color.colour_background(color=Gray(value=1.0))
OOF.Material.Add_property(name='background_material', property='Color:colour_background')
OOF.Material.Assign(material='background_material', microstructure='Screenshot 2020-06-08 at 23.58.43.png', pixels='background')
OOF.Skeleton.New(name='skeleton', microstructure='Screenshot 2020-06-08 at 23.58.43.png', x_elements=40, y_elements=40, skeleton_geometry=QuadSkeleton(left_right_periodicity=False,top_bottom_periodicity=False))
OOF.Skeleton.Modify(skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', modifier=Anneal(targets=AllNodes(),criterion=AverageEnergy(alpha=0.8),T=0.0,delta=1.0,iteration=FixedIteration(iterations=100)))
OOF.Skeleton.Modify(skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', modifier=SwapEdges(targets=AllElements(),criterion=AverageEnergy(alpha=0.8)))
OOF.Skeleton.Modify(skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', modifier=Smooth(targets=AllNodes(),criterion=AverageEnergy(alpha=0.8),T=0.0,iteration=FixedIteration(iterations=50)))
OOF.Mesh.New(name='mesh', skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', element_types=['D2_2', 'T3_3', 'Q4_4'])
OOF.Subproblem.Field.Define(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', field=Temperature)
OOF.Subproblem.Field.Activate(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', field=Temperature)
OOF.Mesh.Field.In_Plane(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', field=Temperature)
OOF.Subproblem.Equation.Activate(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', equation=Heat_Eqn)
OOF.Mesh.Boundary_Conditions.New(name='bc', mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', condition=DirichletBC(field=Temperature,field_component='',equation=Heat_Eqn,eqn_component='',profile=ConstantProfile(value=0.0),boundary='left'))
OOF.Mesh.Boundary_Conditions.New(name='bc<2>', mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', condition=DirichletBC(field=Temperature,field_component='',equation=Heat_Eqn,eqn_component='',profile=ConstantProfile(value=1000),boundary='right'))
OOF.Subproblem.Set_Solver(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', solver_mode=BasicSolverMode(time_stepper=BasicStaticDriver(),matrix_method=BasicIterative(tolerance=1e-13,max_iterations=1000)))
OOF.Mesh.Set_Field_Initializer(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', field=Temperature, initializer=ConstScalarFieldInit(value=0.0))
OOF.Mesh.Solve(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', endtime=0.0)
OOF.Graphics_1.Toolbox.Pixel_Select.Burn(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', local_flammability=0.1, global_flammability=0.2, color_space_norm='L1', next_nearest=False, points=[Point(312.86,20.86)], shift=0, ctrl=0)
OOF.Graphics_1.Layer.Hide(n=4)
OOF.Graphics_1.Layer.Select(n=4)
OOF.Graphics_1.Layer.Hide(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.Layer.Select(n=5)
OOF.LayerEditor.LayerSet.Edit(window='Graphics_1', layer_number=5)
OOF.LayerEditor.LayerSet.Add_Method(method=FilledContourDisplay(when=latest,what=getOutput('Field:Component',component='',field=Temperature),where=getOutput('original'),min=automatic,max=automatic,levels=11,nbins=5,colormap=ThermalMap()))
OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
OOF.Graphics_1.Layer.Freeze(n=5)
OOF.Graphics_1.Layer.Select(n=5)
OOF.Graphics_1.Layer.Show(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.Layer.Unfreeze(n=5)
OOF.Graphics_1.Layer.Select(n=5)
OOF.Graphics_1.Layer.Show(n=5)
OOF.Graphics_1.Layer.Hide(n=6)
OOF.Graphics_1.Layer.Select(n=6)
OOF.Graphics_1.Layer.Show(n=6)
OOF.Graphics_1.Layer.Hide(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.Layer.Hide_Contour_Map(n=1)
OOF.Graphics_1.Layer.Select(n=1)
OOF.Graphics_1.Layer.Show_Contour_Map(n=1)
OOF.Graphics_1.Layer.Hide(n=1)
OOF.Graphics_1.Layer.Show(n=1)
OOF.Graphics_1.Layer.Hide(n=5)
OOF.Graphics_1.Layer.Select(n=5)
OOF.Graphics_1.Layer.Show(n=5)
OOF.Graphics_1.Layer.Hide(n=6)
OOF.Graphics_1.Layer.Select(n=6)
OOF.Graphics_1.Layer.Hide(n=1)
OOF.Graphics_1.Layer.Select(n=1)
OOF.Graphics_1.Layer.Show(n=6)
OOF.Graphics_1.Layer.Select(n=6)
OOF.Graphics_1.Layer.Hide(n=5)
OOF.Graphics_1.Layer.Select(n=5)
OOF.Graphics_1.File.Close()
OOF.Mesh.Delete(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh')
OOF.Mesh.New(name='mesh', skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', element_types=['D2_2', 'T3_3', 'Q4_4'])
OOF.Windows.Graphics.New()
OOF.Graphics_1.Layer.Hide(n=4)
OOF.Graphics_1.Layer.Select(n=4)
OOF.Graphics_1.Layer.Hide(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.File.Close()
OOF.Mesh.Delete(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh')
OOF.Mesh.New(name='mesh', skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', element_types=['D2_2', 'T3_3', 'Q4_4'])
OOF.Windows.Graphics.New()
OOF.Graphics_1.Toolbox.Pixel_Select.Burn(source='Screenshot 2020-06-08 at 23.58.43.png:Screenshot 2020-06-08 at 23.58.43.png', local_flammability=0.1, global_flammability=0.2, color_space_norm='L1', next_nearest=False, points=[Point(54.14,224.14)], shift=0, ctrl=0)
OOF.PixelGroup.AddSelection(microstructure='Screenshot 2020-06-08 at 23.58.43.png', group='background')
OOF.Mesh.Delete(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh')
OOF.Mesh.New(name='mesh', skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', element_types=['D2_2', 'T3_3', 'Q4_4'])
OOF.Graphics_1.Layer.Hide(n=4)
OOF.Graphics_1.Layer.Select(n=4)
OOF.Graphics_1.Layer.Show(n=4)
OOF.Graphics_1.File.Close()
OOF.Material.Assign(material='background_material', microstructure='Screenshot 2020-06-08 at 23.58.43.png', pixels='background')
OOF.Mesh.Delete(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh')
OOF.Mesh.New(name='mesh', skeleton='Screenshot 2020-06-08 at 23.58.43.png:skeleton', element_types=['D2_2', 'T3_3', 'Q4_4'])
OOF.Subproblem.Field.Define(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', field=Temperature)
OOF.Subproblem.Field.Activate(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', field=Temperature)
OOF.Mesh.Field.In_Plane(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', field=Temperature)
OOF.Subproblem.Equation.Activate(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', equation=Heat_Eqn)
OOF.Mesh.Boundary_Conditions.New(name='bc', mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', condition=DirichletBC(field=Temperature,field_component='',equation=Heat_Eqn,eqn_component='',profile=ConstantProfile(value=1000.0),boundary='right'))
OOF.Mesh.Boundary_Conditions.New(name='bc<2>', mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', condition=DirichletBC(field=Temperature,field_component='',equation=Heat_Eqn,eqn_component='',profile=ConstantProfile(value=0),boundary='left'))
OOF.Windows.Graphics.New()
OOF.Graphics_1.Layer.Hide(n=4)
OOF.Graphics_1.Layer.Select(n=4)
OOF.Graphics_1.Layer.Hide(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.File.Close()
OOF.Subproblem.Set_Solver(subproblem='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh:default', solver_mode=BasicSolverMode(time_stepper=BasicStaticDriver(),matrix_method=BasicIterative(tolerance=1e-13,max_iterations=1000)))
OOF.Mesh.Set_Field_Initializer(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', field=Temperature, initializer=ConstScalarFieldInit(value=0.0))
OOF.Mesh.Solve(mesh='Screenshot 2020-06-08 at 23.58.43.png:skeleton:mesh', endtime=0.0)
OOF.Windows.Graphics.New()
OOF.Graphics_1.Layer.Hide(n=4)
OOF.Graphics_1.Layer.Select(n=4)
OOF.Graphics_1.Layer.Hide(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.Layer.Select(n=5)
OOF.LayerEditor.LayerSet.Edit(window='Graphics_1', layer_number=5)
OOF.LayerEditor.LayerSet.Add_Method(method=FilledContourDisplay(when=latest,what=getOutput('Field:Component',component='',field=Temperature),where=getOutput('original'),min=automatic,max=automatic,levels=11,nbins=5,colormap=ThermalMap()))
OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
OOF.Graphics_1.File.Save_Contourmap(filename='/home/nanohub/srehman6/data/results/1646090/contour_map', overwrite=False)
OOF.Graphics_1.File.Save_Image(filename='/home/nanohub/srehman6/data/results/1646090/image', overwrite=False)
