from fipy import Variable, CellVariable, Grid2D, TransientTerm, DiffusionTerm, ImplicitSourceTerm, Viewer, Matplotlib2DGridViewer
from fipy.tools import numerix


dx = dy = 0.025
if __name__ == '__main__':
        nx = ny = 500
else:
        nx = ny = 20
mesh = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)

dt = 5e-4

phase = CellVariable(name=r'$\phi$', mesh=mesh, hasOld=True)

dT = CellVariable(name=r'$\Delta T$', mesh=mesh, hasOld=True)

DT = 2.25
heatEq = (TransientTerm() == DiffusionTerm(DT)+ (phase - phase.old) / dt)

alpha = 0.015
c = 0.02
N = 6.
theta = numerix.pi / 8.
psi = theta + numerix.arctan2(phase.faceGrad[1],phase.faceGrad[0])
Phi = numerix.tan(N * psi / 2)
PhiSq = Phi**2
beta = (1. - PhiSq) / (1. + PhiSq)
DbetaDpsi = -N * 2 * Phi / (1 + PhiSq)
Ddia = (1.+ c * beta)
Doff = c * DbetaDpsi
I0 = Variable(value=((1, 0), (0, 1)))
I1 = Variable(value=((0, -1), (1, 0)))
D = alpha**2 * (1.+ c * beta) * (Ddia * I0 + Doff * I1)

tau = 3e-4
kappa1 = 0.9
kappa2 = 20.
phaseEq = (TransientTerm(tau) == DiffusionTerm(D)+ ImplicitSourceTerm((phase - 0.5 - kappa1 / numerix.pi * numerix.arctan(kappa2 * dT))* (1 - phase)))

radius = dx * 5.
C = (nx * dx / 2, ny * dy / 2)
x, y = mesh.cellCenters
phase.setValue(1., where=((x - C[0])**2 + (y - C[1])**2) < radius**2)

dT.setValue(-0.5)

if __name__ == "__main__":
        try:
                import pylab
                class DendriteViewer(Matplotlib2DGridViewer):
                        def __init__(self, phase, dT, title=None, limits={}, **kwlimits):
                                self.phase = phase
                                self.contour = None
                                Matplotlib2DGridViewer.__init__(self, vars=(dT,), title=title,cmap=pylab.cm.hot,limits=limits, **kwlimits)

                        def _plot(self):
                                Matplotlib2DGridViewer._plot(self)

                                if self.contour is not None:
                                        for c in self.contour.collections:
                                                c.remove()

                                mesh = self.phase.mesh
                                shape = mesh.shape
                                x, y = mesh.cellCenters
                                z = self.phase.value
                                x, y, z = [a.reshape(shape, order="FORTRAN") for a in (x, y, z)]

                                self.contour = self.axes.contour(x, y, z, (0.5,))
                viewer = DendriteViewer(phase=phase, dT=dT,title=r"%s & %s" % (phase.name, dT.name),datamin=-0.1, datamax=0.05)
        except ImportError:
                viewer = MultiViewer(viewers=(Viewer(vars=phase),Viewer(vars=dT,datamin=-0.5,datamax=0.5)))
