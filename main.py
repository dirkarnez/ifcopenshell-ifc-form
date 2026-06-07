# -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import ifcopenshell

def main():
  ifc4 = ifcopenshell.schema_by_name("IFC4")
  
  
  for declaration in ifc4.declarations():
      print(declaration.name()) # 'IfcAbsorbedDoseMeasure', 'IfcAccelerationMeasure', 'IfcActionRequest', ...
  
  ifcwall = ifc4.declaration_by_name("IfcWall")

if __name__ == "__main__":
  main()
