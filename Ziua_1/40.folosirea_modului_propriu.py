### Versiunea 1 - import modulul 
import modul_meu
print(modul_meu.inlocuieste_diacritice('până la început'))


### Versiunea 2 - import modulul + alias la modul
import modul_meu as mdl
print(mdl.inlocuieste_diacritice('până la început'))


### Versiunea 3 - import de functie (specific)
from modul_meu import inlocuieste_diacritice
print(inlocuieste_diacritice('până la început'))


