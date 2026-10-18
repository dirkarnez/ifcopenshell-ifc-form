# -*- coding: utf-8 -*-
from typing import Any, List
import numpy as np
import ifcopenshell

def main():
  schema = ifcopenshell.schema_by_name("IFC4")


  [
    "IfcAirTerminal",
    "IfcAirTerminalBox",
    "IfcAirTerminalBoxType",
    "IfcAirTerminalType",
    "IfcAirToAirHeatRecovery",
    "IfcAirToAirHeatRecoveryType",
    "IfcBoiler",
    "IfcBoilerType",
    "IfcBurner",
    "IfcBurnerType",
    "IfcChiller",
    "IfcChillerType",
    "IfcCoil",
    "IfcCoilType",
    "IfcCompressor",
    "IfcCompressorType",
    "IfcCondenser",
    "IfcCondenserType",
    "IfcCooledBeam",
    "IfcCooledBeamType",
    "IfcCoolingTower",
    "IfcCoolingTowerType",
    "IfcDamper",
    "IfcDamperType",
    "IfcDuctFitting",
    "IfcDuctFittingType",
    "IfcDuctSegment",
    "IfcDuctSegmentType",
    "IfcDuctSilencer",
    "IfcDuctSilencerType",
    "IfcEngine",
    "IfcEngineType",
    "IfcEvaporativeCooler",
    "IfcEvaporativeCoolerType",
    "IfcEvaporator",
    "IfcEvaporatorType",
    "IfcFan",
    "IfcFanType",
    "IfcFilter",
    "IfcFilterType",
    "IfcFlowMeter",
    "IfcFlowMeterType",
    "IfcHeatExchanger",
    "IfcHeatExchangerType",
    "IfcHumidifier",
    "IfcHumidifierType",
    "IfcMedicalDevice",
    "IfcMedicalDeviceType",
    "IfcPipeFitting",
    "IfcPipeFittingType",
    "IfcPipeSegment",
    "IfcPipeSegmentType",
    "IfcPump",
    "IfcPumpType",
    "IfcSpaceHeater",
    "IfcSpaceHeaterType",
    "IfcTank",
    "IfcTankType",
    "IfcTubeBundle",
    "IfcTubeBundleType",
    "IfcUnitaryEquipment",
    "IfcUnitaryEquipmentType",
    "IfcValve",
    "IfcValveType",
    "IfcVibrationIsolator",
    "IfcVibrationIsolatorType"
  ]

  # 2. Grab the anchor defined in the IfcSharedBldgServiceElements layer
  # This is the supertype that the IfcHvacDomain schema relies on to function.
  d = schema.declaration_by_name("IfcVibrationIsolator")
  print(d.as_type_declaration())
  print(d.subtypes())
  print(d._is)
  print(d.as_entity())
  print(d.as_enumeration_type())
  print(d.as_select_type())
  print(d.name())
        
              
          

  # def traverse_domain_extensions(declaration):
  #     """Recursively walks down the schema tree to discover all specialized domain items."""
  #     discovered_classes = []
  #     for subtype in declaration.subtypes():
  #         print(f"subtype = {subtype}")
  #         discovered_classes.append(subtype)
  #         discovered_classes.extend(traverse_domain_extensions(subtype))
  #     return discovered_classes

  # # 3. Dynamically discover all elements expanding into the Domain layer
  # all_hvac_extensions = traverse_domain_extensions(shared_base)

  # # Filter out abstract placeholders so we have a clean list of runnable elements
  # instantiable_hvac_classes = [
  #     decl.name() for decl in all_hvac_extensions if not decl.is_abstract()
  # ]

  # print(f"Discovered {len(instantiable_hvac_classes)} concrete classes extending IfcSharedBldgServiceElements:")
  # print(instantiable_hvac_classes)


  # # 2. Grab the abstract anchor for the entire flow/HVAC domain layer
  # hvac_base_decl = schema.declaration_by_name("IfcDistributionFlowElement")

  # def get_all_descendants(declaration):
  #     """Recursively walks down the schema declaration tree to find child classes."""
  #     descendants = []
  #     for subtype in declaration.subtypes():
  #         descendants.append(subtype)
  #         descendants.extend(get_all_descendants(subtype))
  #     return descendants

  # # 3. Compile the exact runtime list of classes from the schema topology
  # all_hvac_classes = get_all_descendants(hvac_base_decl)

  # # 4. Filter for instantiable (non-abstract) classes to get a precise runtime list
  # instantiable_hvac_classes = [
  #     decl.name() for decl in all_hvac_classes if not decl.is_abstract()
  # ]

  # print(f"--- Dynamically discovered {instantiable_hvac_classes} classes from the schema architecture ---")
if __name__ == "__main__":
  main()
