from Util import materialType


class MaterialManager:

    def __init__(self, params: list):
        self.params = params
        # other configurations

<<<<<<< HEAD
  def changeMaterial(self, material) -> bool:
=======
        def changeMaterial(self, material) -> bool:
>>>>>>> bruce-alloyX
        returnText = ""

        match material:
            case materialType.Titanium:
                self.carManager.setMaterial(materialType.Titanium)
                returnText = "Material is changed to Titanium."

            case materialType.Carbon:
                self.carManager.setMaterial(materialType.Carbon)
                returnText = "Material is changed to Carbon."

<<<<<<< HEAD
            case materialType.Vibranium:
                self.carManager.setMaterial(materialType.Vibranium)
                returnText = "Material is changed to Vibranium."
=======
            case materialType.AlloyX:
                self.carManager.setMaterial(materialType.AlloyX)
                returnText = "Material is changed to AlloyX."
>>>>>>> bruce-alloyX

            case _:
                returnText = "Material selection is invalid."

        return self._announceMaterial(returnText)


   def _announceMaterial(self, text: str) -> bool:
   returnValue = False
   try:
       returnValue = self.announcer(text)
   except:
       print("Announcement of material type is failed.")
       returnValue = False
   finally:
       return returnValue


