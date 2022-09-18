# SchemDraw is a drawing package of python. version 7.01 is used to draw this circuits schematic diagram.
# This version should be installed in system.
# We didn't use the latest version of SchemDraw for a bug, which creates problem to save the drawing.

import SchemDraw
import SchemDraw.elements as elm

d=SchemDraw.Drawing()

opamp=d.add(elm.Opamp(d='right'))
l=d.add(elm.Line(d='right',at=opamp.out))
d1=d.add(elm.Diode(d='up',label='ideal',l=d.unit/1.09))
d.add(elm.Line(d='left',label='V-',at=opamp.in1))
r1=d.add(elm.Resistor(d='up',l=d.unit/1.4,botlabel='100k$\Omega$'))
d.add(elm.Capacitor(d='left',label='1uF'))
d.add(elm.Line(d='down',l=d.unit/2.2))
d.add(elm.SourceSin(d='down',label='Vin'))
d.add(elm.Ground)
d.add(elm.Line(d='right',xy=r1.end))
r2=d.add(elm.Line(d='right'))
l1=d.add(elm.Line(d='right',at=r2.end,to=d1.end))
d.add(elm.Line(d='left',label='V+',at=opamp.in2))
d.add(elm.Line(d='down',l=d.unit/4))
d.add(elm.Ground)
l2=d.add(elm.Line(d='right',at=l1.end,l=d.unit/2))
d.add(elm.Line(d='down',l=d.unit/4))
d.add(elm.Resistor(d='down',label='Rl'))
d.add(elm.Line(d='down',l=d.unit/4))
d.add(elm.Ground)
d.add(elm.Line(d='right',at=l2.end,label='Vout'))
d.add((elm.Dot))

d.draw()
