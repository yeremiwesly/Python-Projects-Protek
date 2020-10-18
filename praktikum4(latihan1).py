#Created by Yeremi Wesly Sinaga K3520080 PTIK 2020

"""

╱╭━━┳━┳━┳╮      Alat 
━┫╱┓┣┳━━━╯      Hitung
╱╱╱┃┃╯                 Sewa
━┫╱╰┛╯                 Rental
╱╰━━━╯                 Mobil

"""
#program hitung tarif rental

tarif1 = 200000
tarif2 = 10000
JamMulai = 6
MenitMulai = 0
JamSelesai = 23
MenitSelesai = 50

JamSewa = JamSelesai - JamMulai
MenitSewa = MenitSelesai - MenitMulai

LamaSewa = int(JamSewa + MenitSewa / 60)

TotalBiayaSewa = int(tarif1 + tarif2 * (LamaSewa - 12))

print("Total tarif rental mobil yang harus dibayarkan adalah ",TotalBiayaSewa)
"""

░░░░░░░░░░░░░░░░░░░░       ░░░░░RENTAL  MOBIL░░░░░
░░░░░░░░░░░░░░░░░░░░


"""