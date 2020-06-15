# Test Case 1

This test case includes heat diffusing from the LHS of the image to the RHS. This folder includes the original image of a simple star surrounded by a white background, the FE mesh required to run the simulation and the simulation results. The Python log is also included in this folder, which can be edited for each simulation and run using the OOF2. In the Python log, the materials can be defined, pixels are assigned material IDs, the FE mesh can be generated (an Abaqus version) and fields and boundary conditions can be defined.

As there is a difference in thermal expansions of the two materials present in the image, there will be some displacement. The next test case will look at including displacements into the FE simulation as well as focusing on an actual microstructural grain.
