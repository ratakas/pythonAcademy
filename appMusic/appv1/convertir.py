import re
texto='Afaz Natural - "Quizás" LETRA  (Video Lyric)'
removeSpecialChars = texto.translate ({ord(c): "" for c in "!@#$%^&*()\"[]{};:,./<>?\|`~-=_+"})

print(removeSpecialChars)