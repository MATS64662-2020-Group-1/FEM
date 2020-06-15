OOF.Microstructure.Create_From_ImageFile(filename='/home/nanohub/srehman6/data/results/1646633/grain_2.png', microstructure_name='grain_2.png', height=automatic, width=automatic)
OOF.Windows.Graphics.New()
OOF.Graphics_1.Toolbox.Pixel_Select.Color(source='grain_2.png:grain_2.png', range=DeltaRGB(delta_red=0,delta_green=0,delta_blue=0), points=[Point(12.2306666667,28.2171111111)], shift=0, ctrl=0)
OOF.PixelGroup.New(name='alpha_phase', microstructure='grain_2.png')
OOF.PixelGroup.AddSelection(microstructure='grain_2.png', group='alpha_phase')
OOF.PixelGroup.New(name='beta_phase', microstructure='grain_2.png')
OOF.Graphics_1.Toolbox.Pixel_Select.Color(source='grain_2.png:grain_2.png', range=DeltaRGB(delta_red=0,delta_green=0,delta_blue=0), points=[Point(2.80977777778,37.2371111111)], shift=0, ctrl=0)
OOF.PixelGroup.AddSelection(microstructure='grain_2.png', group='beta_phase')
OOF.Material.New(name='alpha_mat', material_type='bulk')
OOF.Material.New(name='beta_mat', material_type='bulk')
OOF.Property.Copy(property='Color', new_name='colour_alpha')
OOF.Property.Parametrize.Color.colour_alpha(color=Gray(value=1.0))
OOF.Material.Add_property(name='alpha_mat', property='Color:colour_alpha')
OOF.Property.Copy(property='Mechanical:Elasticity:Isotropic', new_name='youngs_alpha')
OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.youngs_alpha(cijkl=IsotropicRank4TensorEnu(young=117000000000.0,poisson=0.3333333333333333))
OOF.Material.Add_property(name='alpha_mat', property='Mechanical:Elasticity:Isotropic:youngs_alpha')
OOF.Property.Copy(property='Thermal:Conductivity:Isotropic', new_name='k_alpha')
OOF.Property.Parametrize.Thermal.Conductivity.Isotropic.k_alpha(kappa=7)
OOF.Material.Add_property(name='alpha_mat', property='Thermal:Conductivity:Isotropic:k_alpha')
OOF.Property.Copy(property='Couplings:ThermalExpansion:Isotropic', new_name='a_alpha')
OOF.Property.Parametrize.Couplings.ThermalExpansion.Isotropic.a_alpha(alpha=8e-06, T0=0.0)
OOF.Material.Add_property(name='alpha_mat', property='Couplings:ThermalExpansion:Isotropic:a_alpha')
OOF.Material.Assign(material='alpha_mat', microstructure='grain_2.png', pixels='alpha_phase')
OOF.Property.Copy(property='Color', new_name='colour_beta')
OOF.Property.Parametrize.Color.colour_beta(color=Gray(value=0.0))
OOF.Material.Add_property(name='beta_mat', property='Color:colour_beta')
OOF.Property.Copy(property='Mechanical:Elasticity:Isotropic', new_name='youngs_beta')
OOF.Property.Parametrize.Mechanical.Elasticity.Isotropic.youngs_beta(cijkl=IsotropicRank4TensorEnu(young=30000000000.0,poisson=0.3333333333333333))
OOF.Material.Add_property(name='beta_mat', property='Mechanical:Elasticity:Isotropic:youngs_beta')
OOF.Property.Copy(property='Thermal:Conductivity:Isotropic', new_name='k_beta')
OOF.Property.Parametrize.Thermal.Conductivity.Isotropic.k_beta(kappa=15)
OOF.Property.Parametrize.Thermal.Conductivity.Isotropic.k_beta(kappa=15.0)
OOF.Material.Add_property(name='beta_mat', property='Thermal:Conductivity:Isotropic:k_beta')
OOF.Property.Copy(property='Couplings:ThermalExpansion:Isotropic', new_name='a_beta')
OOF.Property.Parametrize.Couplings.ThermalExpansion.Isotropic.a_beta(alpha=0.001, T0=0.0)
OOF.Material.Add_property(name='beta_mat', property='Couplings:ThermalExpansion:Isotropic:a_beta')
OOF.Material.Assign(material='beta_mat', microstructure='grain_2.png', pixels='beta_phase')
OOF.Skeleton.New(name='skeleton', microstructure='grain_2.png', x_elements=40, y_elements=40, skeleton_geometry=QuadSkeleton(left_right_periodicity=False,top_bottom_periodicity=False))
OOF.Skeleton.Modify(skeleton='grain_2.png:skeleton', modifier=Anneal(targets=AllNodes(),criterion=AverageEnergy(alpha=0.8),T=0.0,delta=1.0,iteration=FixedIteration(iterations=100)))
OOF.Skeleton.Modify(skeleton='grain_2.png:skeleton', modifier=SwapEdges(targets=AllElements(),criterion=AverageEnergy(alpha=0.8)))
OOF.Mesh.New(name='mesh', skeleton='grain_2.png:skeleton', element_types=['D2_2', 'T3_3', 'Q4_4'])
OOF.Subproblem.Field.Define(subproblem='grain_2.png:skeleton:mesh:default', field=Temperature)
OOF.Subproblem.Field.Define(subproblem='grain_2.png:skeleton:mesh:default', field=Displacement)
OOF.Subproblem.Field.Activate(subproblem='grain_2.png:skeleton:mesh:default', field=Displacement)
OOF.Subproblem.Field.Activate(subproblem='grain_2.png:skeleton:mesh:default', field=Temperature)
OOF.Mesh.Field.In_Plane(mesh='grain_2.png:skeleton:mesh', field=Displacement)
OOF.Mesh.Field.In_Plane(mesh='grain_2.png:skeleton:mesh', field=Temperature)
OOF.Subproblem.Equation.Activate(subproblem='grain_2.png:skeleton:mesh:default', equation=Heat_Eqn)
OOF.Subproblem.Equation.Activate(subproblem='grain_2.png:skeleton:mesh:default', equation=Force_Balance)
OOF.Mesh.Boundary_Conditions.New(name='bc', mesh='grain_2.png:skeleton:mesh', condition=DirichletBC(field=Temperature,field_component='',equation=Heat_Eqn,eqn_component='',profile=ConstantProfile(value=0.0),boundary='left'))
OOF.Mesh.Boundary_Conditions.New(name='bc<2>', mesh='grain_2.png:skeleton:mesh', condition=DirichletBC(field=Temperature,field_component='',equation=Heat_Eqn,eqn_component='',profile=ConstantProfile(value=1000.0),boundary='right'))
OOF.Mesh.Boundary_Conditions.New(name='bc<3>', mesh='grain_2.png:skeleton:mesh', condition=DirichletBC(field=Displacement,field_component='x',equation=Force_Balance,eqn_component='x',profile=ConstantProfile(value=0),boundary='right'))
OOF.Mesh.Boundary_Conditions.New(name='bc<4>', mesh='grain_2.png:skeleton:mesh', condition=DirichletBC(field=Displacement,field_component='y',equation=Force_Balance,eqn_component='y',profile=ConstantProfile(value=0.0),boundary='right'))
OOF.Subproblem.Set_Solver(subproblem='grain_2.png:skeleton:mesh:default', solver_mode=BasicSolverMode(time_stepper=BasicStaticDriver(),matrix_method=BasicIterative(tolerance=1e-13,max_iterations=1000)))
OOF.Mesh.Set_Field_Initializer(mesh='grain_2.png:skeleton:mesh', field=Temperature, initializer=ConstScalarFieldInit(value=0.0))
OOF.Mesh.Set_Field_Initializer(mesh='grain_2.png:skeleton:mesh', field=Displacement, initializer=ConstTwoVectorFieldInit(cx=0.0,cy=0.0))
OOF.Mesh.Solve(mesh='grain_2.png:skeleton:mesh', endtime=0.0)
OOF.Graphics_1.Settings.Scroll.Vertical(position=0.0)
OOF.Graphics_1.Layer.Hide(n=0)
OOF.Graphics_1.Layer.Select(n=0)
OOF.Graphics_1.Layer.Hide(n=4)
OOF.Graphics_1.Layer.Select(n=4)
OOF.Graphics_1.Layer.Select(n=5)
OOF.LayerEditor.LayerSet.Edit(window='Graphics_1', layer_number=5)
OOF.LayerEditor.LayerSet.Add_Method(method=FilledContourDisplay(when=latest,what=getOutput('Field:Component',component='',field=Temperature),where=getOutput('original'),min=automatic,max=automatic,levels=11,nbins=5,colormap=ThermalMap()))
OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
OOF.LayerEditor.LayerSet.Add_Method(method=FilledContourDisplay(when=latest,what=getOutput('Field:Component',component='x',field=Displacement),where=getOutput('original'),min=automatic,max=automatic,levels=11,nbins=5,colormap=SpectralMap(saturation=1,value=1)))
OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
OOF.LayerEditor.LayerSet.Add_Method(method=FilledContourDisplay(when=latest,what=getOutput('Field:Component',component='y',field=Displacement),where=getOutput('original'),min=automatic,max=automatic,levels=11,nbins=5,colormap=SpectralMap(saturation=1,value=1)))
OOF.LayerEditor.LayerSet.Send(window='Graphics_1')
OOF.Graphics_1.Layer.Hide(n=8)
OOF.Graphics_1.Layer.Show(n=7)
OOF.Graphics_1.Layer.Select(n=7)
OOF.Graphics_1.File.Save_Image(filename='/home/nanohub/srehman6/data/results/1646633/disp_y', overwrite=False)
OOF.Graphics_1.Layer.Hide(n=3)
OOF.Graphics_1.Layer.Select(n=3)
OOF.Graphics_1.File.Save_Image(filename='/home/nanohub/srehman6/data/results/1646633/disp_x', overwrite=False)
OOF.Graphics_1.Layer.Hide(n=2)
OOF.Graphics_1.Layer.Select(n=2)
OOF.Graphics_1.File.Save_Image(filename='/home/nanohub/srehman6/data/results/1646633/temp', overwrite=False)
OOF.Graphics_1.Layer.Hide(n=1)
OOF.Graphics_1.Layer.Select(n=1)
OOF.Graphics_1.File.Save_Image(filename='/home/nanohub/srehman6/data/results/1646633/mesh', overwrite=False)
OOF.Graphics_1.Layer.Hide(n=7)
OOF.Graphics_1.Layer.Select(n=7)
OOF.Graphics_1.Layer.Show(n=8)
OOF.Graphics_1.Layer.Select(n=8)
OOF.Graphics_1.File.Save_Image(filename='/home/nanohub/srehman6/data/results/1646633/mesh_after_sim', overwrite=False)