### Konvertor obrázků na formát .webp

Postup:
1. ```virtualenv venv && source venv/bin/activate && pip install Pillow```
2. Nahrej obrázky do složky "source"
3. ```python3 convert.py```
4. Přeformátované obrázky se uloží pod stejným názvem do složky dest

##### Změna výchozí složky
SOURCE_PATH = 'source/'

##### Změna cílové složky
DESTINATION_PATH = 'dest/'

##### Změna cílového formátu
FORMATE = 'webp'

##### Povolené formáty pro konverzi
[ '.jpg', '.png' ]
