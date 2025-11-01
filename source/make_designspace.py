import os
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, RuleDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Wasabe"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 900
a1.minimum = 100
a1.default = 100
a1.name = "weight"
a1.tag = "wght"
a1.map = [(100, 100), (200, 200), (310, 300), (420, 400), (530, 500), (640, 600), (750, 700), (900, 900)]
doc.addAxis(a1)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "Wasabe-Thin.ufo"
s0.familyName = familyName
s0.styleName = "Thin"
s0.location = dict(weight=100,slant=0)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "Wasabe-Black.ufo"
s1.familyName = familyName
s1.styleName = "Black"
s1.location = dict(weight=900,slant=0)
doc.addSource(s1)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'Wasabe-Thin'
i0.familyName = familyName
i0.styleName = "Thin"
i0.path = os.path.join(root, "instances", "Wasabe-Thin.ufo")
i0.location = dict(weight=100,slant=0)
i0.kerning = True
i0.info = True
i0.styleMapFamilyName = "Wasabe Thin"
i0.styleMapStyleName = "regular"
doc.addInstance(i0)

i1 = InstanceDescriptor()
i1.name = 'Wasabe-ExtraLight'
i1.familyName = familyName
i1.styleName = "ExtraLight"
i1.path = os.path.join(root, "instances", "Wasabe-ExtraLight.ufo")
i1.location = dict(weight=200,slant=0)
i1.kerning = True
i1.info = True
i1.styleMapFamilyName = "Wasabe ExtraLight"
i1.styleMapStyleName = "regular"
doc.addInstance(i1)

i2 = InstanceDescriptor()
i2.name = 'Wasabe-Light'
i2.familyName = familyName
i2.styleName = "Light"
i2.path = os.path.join(root, "instances", "Wasabe-Light.ufo")
i2.location = dict(weight=300,slant=0)
i2.kerning = True
i2.info = True
i2.styleMapFamilyName = "Wasabe Light"
i2.styleMapStyleName = "regular"
doc.addInstance(i2)

i3 = InstanceDescriptor()
i3.name = 'Wasabe-Regular'
i3.familyName = familyName
i3.styleName = "Regular"
i3.path = os.path.join(root, "instances", "Wasabe-Regular.ufo")
i3.location = dict(weight=400,slant=0)
i3.kerning = True
i3.info = True
i3.styleMapFamilyName = "Wasabe"
i3.styleMapStyleName = "regular"
doc.addInstance(i3)

i4 = InstanceDescriptor()
i4.name = 'Wasabe-Medium'
i4.familyName = familyName
i4.styleName = "Medium"
i4.path = os.path.join(root, "instances", "Wasabe-Medium.ufo")
i4.location = dict(weight=500,slant=0)
i4.kerning = True
i4.info = True
i4.styleMapFamilyName = "Wasabe Medium"
i4.styleMapStyleName = "regular"
doc.addInstance(i4)

i5 = InstanceDescriptor()
i5.name = 'Wasabe-SemiBold'
i5.familyName = familyName
i5.styleName = "SemiBold"
i5.path = os.path.join(root, "instances", "Wasabe-SemiBold.ufo")
i5.location = dict(weight=600,slant=0)
i5.kerning = True
i5.info = True
i5.styleMapFamilyName = "Wasabe SemiBold"
i5.styleMapStyleName = "regular"
doc.addInstance(i5)

i6 = InstanceDescriptor()
i6.name = 'Wasabe-Bold'
i6.familyName = familyName
i6.styleName = "Bold"
i6.path = os.path.join(root, "instances", "Wasabe-Bold.ufo")
i6.location = dict(weight=700,slant=0)
i6.kerning = True
i6.info = True
i6.styleMapFamilyName = "Wasabe"
i6.styleMapStyleName = "regular"
doc.addInstance(i6)

i7 = InstanceDescriptor()
i7.name = 'Wasabe-Black'
i7.familyName = familyName
i7.styleName = "Black"
i7.path = os.path.join(root, "instances", "Wasabe-Black.ufo")
i7.location = dict(weight=900,slant=0)
i7.kerning = True
i7.info = True
i7.styleMapFamilyName = "Wasabe Black"
i7.styleMapStyleName = "regular"
doc.addInstance(i7)

#--------
# saving
#--------

path = "Wasabe.designspace"
doc.write(path)
