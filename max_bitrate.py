# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db 
# n0_j bw_hz
# Implement the calculation for maximum achievable bitrate.
# Parameters:
# Parameters:
#  tx_w: Transmitter power in watts
#  tx_gain_db: Transmitter gain in dB
#  freq_hz: Frequency of the transmission in Hz
#  dist_km: Distance between the transmitter and receiver in km
#  rx_gain_db: Receiver gain in dB
#  n0_j: Noise power density in W/Hz
#  bw_hz: Bandwidth of the channel in Hz
# Output:
#  Print r_max (maximum achievable bitrate)
#
# Written by Mandar Ajgaonkar
# Other contributors: None
#
# See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
c = 2.99792458e8; # speed of light (m/s)

# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv) == 8:
     tx_w = float(sys.argv[1])
     tx_gain_db = float(sys.argv[2])
     freq_hz = float(sys.argv[3])
     dist_km = float(sys.argv[4])
     rx_gain_db = float(sys.argv[5])
     n0_j = float(sys.argv[6])
     bw_hz = float(sys.argv[7])

else:
   print(\
    'Usage: '\
    'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
   )
   exit()

# write script below this line

# calculate wavelength 
lam = c/freq_hz 

# assumptions for loss factors
L_a_dB = 0; # atmospheric loss (dB)
L_a = 10**(L_a_dB/10); 
L_l_dB = -1; # transmitter to antenna line loss (dB)
L_l = 10**(L_l_dB/10); 

# gains 
G_t = 10**(tx_gain_db/10)
G_r = 10**(rx_gain_db/10)

# calculate received signal power
C = tx_w*L_l*G_t*(lam/(4*math.pi*(dist_km*1000)))**2*L_a*G_r

# calculate received noise power and maximum achievable bitrate
N = n0_j*bw_hz
r_max = bw_hz*math.log2(1 + C/N)

# print result 
print(math.floor(r_max)) # bps (bits per second)


        

