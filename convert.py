import os
import pathlib
from PIL import Image

# Zdrojová složka
SOURCE_PATH = 'source/'

# Cílová složka
DESTINATION_PATH = 'dest/'

# Načtení souborů
FILES = os.listdir( SOURCE_PATH )

# Povolené typy souborů
ALLOWED_EXT = [ '.jpg', '.png' ]

# Cílový formát
FORMATE = 'webp'

# Počet provedených konverzí
conv_count = 0


for file in FILES:
    extension = pathlib.Path( file ).suffix

    if extension in ALLOWED_EXT:

        conv_count += 1
        conv = Image.open( SOURCE_PATH + file ).convert( 'RGB' )
        conv.save( DESTINATION_PATH + file.replace( extension, '.' + FORMATE ), FORMATE )

print( f'Provedeno {conv_count} konverzí obrázků!' )