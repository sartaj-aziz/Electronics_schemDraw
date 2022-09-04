# SchemDraw is a drawing package of python. version 7.01 is used to draw this circuits schematic diagram.
# We didn't use the latest version of SchemDraw for a bug, which creates problem to save the drawing.

import SchemDraw
import SchemDraw.elements as elm

d = SchemDraw.Drawing()

r1=d.add(elm.Resistor(label='10k$\Omega$',color='red'))
opamp=d.add(elm.Opamp(anchor='in1',color='blue',rgtlabel='LM741'))

m=d.add(elm.Line(d='right',at=opamp.out))
d.add(elm.Line(d='up'))
d.add(elm.Line(d='left'))
d.add(elm.Resistor(d='left',label='20k$\Omega$',color='red'))
d.add(elm.Line(d='down',l=d.unit/1.28))
d.add(elm.Line(d='left',at=(opamp,'in2')))
g=d.add(elm.Line(d='down'))
d.add(elm.Dot(xy=r1.start))
d.add(elm.LineDot(d='left',label='Vin '))
d.add(elm.LineDot(xy=m.end,d='right',label='Vo'))
d.add(elm.Ground(xy=g.end,color='blue'))
d.add(elm.Line(xy=opamp.vd,d='up',l=d.unit/2.5,rgtlabel='Vd'))
d.add(elm.Line(d='left',l=d.unit*1))
d.add(elm.Line(d='down',l=d.unit*1.17))
d.add(elm.Line(xy=opamp.vs,l=d.unit/1.57,label='Vs'))
a=d.add(elm.Line(d='left'))
d.add(elm.Line(xy=a.end,d='up',l=d.unit/12))
d.add(elm.SourceV(d='up',color='green',l=d.unit/5,rotate=True,botlabel='+15/-15'))

d.draw()





