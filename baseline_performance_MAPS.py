#!/usr/bin/env python
# coding: utf-8

# ### Load In MSMD Dataset

# In[23]:


import xml.etree.ElementTree as ET
import xmltodict
import json
from mido import MidiFile
import mir_eval
from mido import Message, MidiFile, MidiTrack
import pandas as pd
import numpy as np
import os


# In[371]:


# AkPnBcht tracks 

ISOL_TRACKS = [
    #'MUS/MAPS_MUS-alb_se3_AkPnBcht',
#     'MUS/MAPS_MUS-bach_846_AkPnBcht',
#     'MUS/MAPS_MUS-bach_847_AkPnBcht',
#     'MUS/MAPS_MUS-bk_xmas5_AkPnBcht',
#     'MUS/MAPS_MUS-chp_op31_AkPnBcht',
#     'MUS/MAPS_MUS-chpn_op25_e2_AkPnBcht',
#     'MUS/MAPS_MUS-chpn_op66_AkPnBcht',
#     'MUS/MAPS_MUS-chpn-p1_AkPnBcht',
#     'MUS/MAPS_MUS-chpn-p3_AkPnBcht',
#     'MUS/MAPS_MUS-chpn-p4_AkPnBcht',
#     'MUS/MAPS_MUS-chpn-p8_AkPnBcht',
#     'MUS/MAPS_MUS-chpn-p12_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M102_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.1_F_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.1_M_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.1_P_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.3_F_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.3_M_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.3_P_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.05_F_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.05_M_AkPnBcht',
    'ISOL/CH/MAPS_ISOL_CH0.05_P_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M31_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M37_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M44_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M59_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M67_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M83_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M84_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M95_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M101_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S0_M105_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M33_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M38_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M47_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M49_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M50_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M53_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M65_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M66_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M70_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M96_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_F_S1_M97_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M24_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M31_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M56_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M57_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M66_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M70_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M80_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M101_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M108_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M33_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M41_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M49_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M63_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M69_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M72_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M76_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M84_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M86_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M91_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M94_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S1_M104_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M23_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M31_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M38_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M39_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M40_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M44_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M53_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M62_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M66_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M68_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M70_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M83_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M84_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M95_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S0_M98_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M30_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M36_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M61_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M65_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M79_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M89_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_P_S1_M107_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M103_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M106_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M108_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M104_AkPnBcht',
    #'ISOL/NO/MAPS_ISOL_RE_F_S0_M28_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M23_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M28_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M29_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M30_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M31_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M32_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M33_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M36_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M37_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M38_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M42_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M43_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M44_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M45_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M49_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M55_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M56_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M57_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M59_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M62_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M66_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M67_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M69_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M70_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M72_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M73_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M76_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M77_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M78_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M81_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M82_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M86_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M87_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M88_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M94_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M96_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M98_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M100_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M105_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M106_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S0_M108_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M21_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M22_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M24_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M25_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M26_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M27_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M34_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M35_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M39_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M40_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M41_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M46_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M47_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M48_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M50_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M51_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M52_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M53_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M54_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M58_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M60_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M61_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M63_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M64_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M65_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M68_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M71_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M74_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M75_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M79_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M80_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M83_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M84_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M85_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M89_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M90_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M91_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M92_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M93_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M95_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M97_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M99_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M101_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M102_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_F_S1_M107_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M22_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M24_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M27_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M28_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M30_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M32_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M33_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M36_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M38_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M43_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M44_AkPnBcht',
    'ISOL/NO/MAPS_ISOL_NO_M_S0_M46_AkPnBcht',
    'ISOL/RE/MAPS_ISOL_RE_M_S0_M102_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n3_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n5_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n6_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n7_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n8_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n10_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n11_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n15_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n16_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n17_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n18_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n20_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n21_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n22_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n23_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n24_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n25_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n26_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n29_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n33_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n35_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n36_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n37_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n38_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n41_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n42_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n44_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n45_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S0_n49_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n1_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n2_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n4_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n9_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n12_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n13_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n14_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n19_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n27_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n28_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n30_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n31_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n32_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n34_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n39_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n40_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n43_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n46_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n47_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n48_AkPnBcht',
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n50_AkPnBcht'
]


# # Create dictionary with file paths for each folder (txt, wav and midi)

# In[372]:


ISOL_DICT = {}

filename = 'ISOL/RE/MAPS_ISOL_RE_P_S1_M107_AkPnBcht'
base_path = "/Volumes/amelia_gdrive/MAPS/AkPnBcht/"

for track_id in ISOL_TRACKS: 
    txt_path = os.path.join(base_path + track_id + '.txt')
    wav_path = os.path.join(base_path + track_id + '.wav')
    midi_path = os.path.join(base_path + track_id + '.mid')

    ISOL_DICT[track_id] = { 'txt' : txt_path, 
                            'wav' : wav_path, 
                            'midi' : midi_path }



# # Functions from homework 9 to sonify notes

# In[115]:


import pretty_midi
import librosa
import numpy as np
import IPython.display


# In[356]:


def load_labrosa_apt_midi(midi_path):
    """Load a midi file from the dataset.
    Removes all notes later than 60 seconds (audio clips are cut to 60 seconds)
    
    Parameters
    ----------
    midi_path: str
        Path to midi file from this datasett
    
    Returns
    -------
    intervals: np.ndarray shape=(n, 2)
        Array of note start and end times in seconds
    pitches: np.ndarray shape=(n)
        Array of note pitches in Hz

    """
    midi_data = pretty_midi.PrettyMIDI(midi_path)
    piano_notes = midi_data.instruments[0].notes
    intervals = np.array([(note.start, note.end) for note in piano_notes if note.end < 60.0])
    pitches = librosa.midi_to_hz([note.pitch for note in piano_notes if note.end < 60.0])
    return intervals, pitches


# In[357]:


def sonify_annotation(intervals, pitches, sonification_fs=8000):
    """Sonify a note annotation.
    
    Parameters
    ----------
    intervals: np.ndarray shape=(n, 2)
        Array of note start and end times in seconds
    pitches: np.ndarray shape=(n,)
        Array of note pitches in Hz
    sonification_fs: float
        Sample rate of sonified audio.
        
    Returns
    -------
    y_sonify: np.ndarray shape=(m,)
        Mono audio signal of sonified notes
    
    """
    pm = pretty_midi.PrettyMIDI()
    inst = pretty_midi.Instrument(program=0, is_drum=False, name='piano')
    pm.instruments.append(inst)
    velocity = 100
    for interval, pitch in zip(intervals, pitches):
        inst.notes.append(pretty_midi.Note(
            velocity, librosa.hz_to_midi(pitch), interval[0], interval[1]))
            
    return pm.synthesize(fs=sonification_fs)


# In[358]:


def sonify_notes(audio_path, intervals, pitches):
    """Sonify a note annotation along side its corresponding audio file.
    The original piano audio should be in one channel and the sonified notes in the other.
    
    Parameters
    ----------
    audio_path: str
        Path to audio file
    intervals: np.ndarray shape=(n, 2)
        Array of note start and end times in seconds
    pitches: np.ndarray shape=(n,)
        Array of note pitches in Hz

    Returns
    -------
    y_sonify: np.ndarray shape=(2, m)
        Mono audio signal of sonified notes
    fs_sonify: float
        Sample rate of sonified audio

    """
    # hint: if one channel is consistently louder than the other, turn it down :)
    
    y, sr = librosa.load(audio_path, sr=None)
    sonified_audio = sonify_annotation(intervals, pitches)
    
    if len(sonified_audio) > len(y):
        diff = len(sonified_audio) - len(y)
        zeros = np.zeros((diff))
        y_pad = np.append(y, zeros)  
        stack = np.vstack((y_pad, sonified_audio))
        
    elif len(y) > len(sonified_audio):
        diff = len(y) - len(sonified_audio)
        zeros = np.zeros((diff))
        son_pad = np.append(sonified_audio, zeros)  
        stack = np.vstack((y, son_pad))
    
    else: 
        stack = np.vstack((y, sonified_audio))
        
    audio1 = IPython.display.Audio(stack, rate=sr)

    return stack, sr


# In[359]:


# test the code
test_track_id = 'ISOL/CH/MAPS_ISOL_CH0.1_F_AkPnBcht'
test_midi_path = '/Volumes/amelia_gdrive/MAPS/AkPnBcht/ISOL/CH/MAPS_ISOL_CH0.1_F_AkPnBcht.mid'
test_audio_path = '/Volumes/amelia_gdrive/MAPS/AkPnBcht/ISOL/CH/MAPS_ISOL_CH0.1_F_AkPnBcht.wav'

test_intervals, test_pitches = load_labrosa_apt_midi(test_midi_path)

test_y_sonify, test_fs_sonify = sonify_notes(test_audio_path, test_intervals, test_pitches)
IPython.display.Audio(test_y_sonify, rate=test_fs_sonify)


# In[ ]:





# # decode the text file

# In[360]:


def get_txt(txt_path):

    text = np.genfromtxt(fname = txt_path, dtype='str')

    return text


# In[361]:


track_key = 'ISOL/CH/MAPS_ISOL_CH0.1_F_AkPnBcht'
track = ISOL_DICT.get(test_track_id)
txt_path = track['txt']
track_txt = get_txt(txt_path)


# # Transcribe recordings

# In[362]:


import madmom
import mir_eval


# In[386]:


def estimate_notes(audio_path, frames_per_second=100, note_length=0.1):
    """Transcribe the given piano recording using madmom's piano transcription algorithm.
    Returns the notes in the format expected by mir_eval.
    
    Parameters
    ----------
    audio_path : str
        Path to input audio file
    frames_per_second : float, default=100
        Number of frames per second madmom should use internally to transcribe
    note_length : float
        The fixed length duration in seconds of all estimated notes

    Returns
    -------
    intervals: np.ndarray shape=(n, 2)
        Array of note start and end times in seconds
    pitches: np.ndarray shape=(n)
        Array of note pitches in Hz

    """
    ## To run madmom's algorithm ##
    # proc = madmom.features.notes.NotePeakPickingProcessor(fps=frames_per_second)
    # act = madmom.features.notes.RNNPianoNoteProcessor()(audio_path)
    # notes = proc(act)
    
    proc = madmom.features.notes.NotePeakPickingProcessor(fps=frames_per_second, threshold = 0.35)
    act = madmom.features.notes.RNNPianoNoteProcessor()(audio_path)
    intervals = proc(act)
    if len(intervals) > 0:
        pitches_raw = intervals
        pitches_midi = np.delete(pitches_raw, 0, 1)
        pitches_hz = mir_eval.util.midi_to_hz(pitches_midi)
        x = len(pitches_hz)
        pitches = np.reshape(pitches_hz, x)

        for i in range(0, len(pitches)):
             intervals[i][1] = intervals[i][0] + note_length

    else:
        intervals = [1,1]
        pitches = [1]
    
    return intervals, pitches


# In[387]:


# run this code to test your function:
test_estimate_intervals, test_estimate_pitches = estimate_notes('/Volumes/amelia_gdrive/MAPS/AkPnBcht/ISOL/NO/MAPS_ISOL_NO_M_S0_M44_AkPnBcht.wav')

audio = sonify_annotation(test_estimate_intervals, test_estimate_pitches)
IPython.display.Audio(audio, rate=8000)


# # Evaluate Transcription

# In[388]:


import mir_eval
import pandas as pd
from tqdm import tqdm


# In[390]:


# the keys should be track_id, values should be a dictionary with each of the four metrics.
# track id : precision, recall, f_measure, avg_overlap_ratio

transcription_scores = {}

for track in ISOL_DICT:
    #print (track)
    track_paths = ISOL_DICT.get(track)
    audio_path = track_paths['wav']
    midi_path = track_paths['midi']
    est_intervals, est_pitches = estimate_notes(audio_path)
    if est_pitches[0] == 1:
        #print ('^bad')
        pass
    else: 
        ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)
        precision, recall, f_measure, avg_overlap_ratio =  mir_eval.transcription.precision_recall_f1_overlap(ref_intervals, ref_pitches, est_intervals, est_pitches, offset_ratio=None)
        transcription_scores[track] = {'precision' : precision, 
                                          'recall' : recall, 
                                          'f_measure' : f_measure, 
                                          'avg_overlap_ratio' : avg_overlap_ratio}


# In[391]:


#print (transcription_scores)


# # Plot Results 

# In[302]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import librosa.display


# In[392]:


precision = []
recall = []
f_measure = []
avg_overlap_ratio = []

for track_id in transcription_scores:
    
    p = transcription_scores[track_id]['precision']
    r = transcription_scores[track_id]['recall']
    f = transcription_scores[track_id]['f_measure']
    a = transcription_scores[track_id]['avg_overlap_ratio']
    
    precision.append(p)
    recall.append(r)
    f_measure.append(f)
    avg_overlap_ratio.append(a)

data = [precision, recall, f_measure, avg_overlap_ratio]    
fig, ax = plt.subplots()
ax.boxplot(data, labels=['precision','recall','f-measure','avg_overlap_ratio'])
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('Metrics Across Tracks')
plt.show()


# In[ ]:





# #                
# 
# 
# 

# # Extra Stuff
# 

# In[40]:


filepath = '/Volumes/amelia_gdrive/mir_final_project/midi_warm_ups/a_scale1.mid'


mid = MidiFile(filepath)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

for msg in MidiFile(filepath):
    time.sleep(msg.time)
    if not msg.is_meta:
        port.send(msg)
#seconds = mido.tick2second(mid, mid.ticks_per_beat ,120)
#mir_eval.util.boundaries_to_intervals()


# In[24]:


"""
# original dataset folder name: msmd_aug_v1-1_no-audio
# changed to: msmd_aug_v1

#amelia_gdrive/msmd_aug_v1/AdamA__giselle__giselle/scores/mung/'01.xml'
xml_filepath = '/Volumes/amelia_gdrive/msmd_aug_v1/AdamA__giselle__giselle/scores/AdamA__giselle__giselle_ly/mung/01.xml'

tree = ET.parse(xml_filepath)
xml_data = tree.getroot()

xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')


data_dict = dict(xmltodict.parse(xmlstr))

print(data_dict)

with open('new_data_2.json', 'w+') as json_file:
    json.dump(data_dict, json_file, indent=4, sort_keys=True)
"""


# In[ ]:


#fd = open(path_to_file , 'r')

