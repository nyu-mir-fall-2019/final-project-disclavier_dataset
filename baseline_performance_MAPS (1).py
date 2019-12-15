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


# In[397]:


# AkPnBcht tracks 

ISOL_TRACKS = [
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
    'RAND/M21-108/I32-96/P2/MAPS_RAND_P2_M21-108_I32-96_S1_n50_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n2_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n3_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n4_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n6_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n10_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n11_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n12_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S0_n14_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n1_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n5_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n7_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n8_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n9_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n13_AkPnBcht',
    'UCHO/I32-96/C0-24/MAPS_UCHO_C0-24_I32-96_S1_n15_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n1_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n4_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n5_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n7_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n8_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n9_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n10_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n11_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n12_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S0_n13_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S1_n2_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S1_n3_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S1_n6_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S1_n14_AkPnBcht',
    'UCHO/I32-96/C0-4-8/MAPS_UCHO_C0-4-8_I32-96_S1_n15_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M21_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M22_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M25_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M27_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M28_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M32_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M34_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M41_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M42_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M44_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M45_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M47_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M49_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M50_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M51_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M52_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M53_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M54_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M55_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M57_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M60_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M61_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M65_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M66_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M69_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M73_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M74_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M75_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M79_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M81_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M83_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M84_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M85_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M86_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M89_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M90_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M91_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M92_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M94_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M97_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M98_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M99_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M101_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M102_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M105_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M106_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S0_M107_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M23_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M24_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M26_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M30_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M37_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M38_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M43_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M46_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M48_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M56_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M58_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M59_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M62_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M63_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M64_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M67_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M68_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M70_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M71_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M72_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M76_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M77_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M78_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M80_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M82_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M87_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M88_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M93_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M95_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M96_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M100_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M103_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M104_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_F_S1_M108_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M21_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M22_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M25_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M28_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M30_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M32_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M34_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M38_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M41_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M45_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M47_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M49_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M52_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M54_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M55_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M58_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M59_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M60_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M61_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M62_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M63_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M64_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M66_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M67_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M68_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M69_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M71_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M72_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M79_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M80_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M83_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M93_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M97_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M101_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M102_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M105_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M106_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M107_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S0_M108_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M23_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M24_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M26_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M27_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M37_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M42_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M43_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M44_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M46_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M48_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M50_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M51_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M53_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M56_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M57_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M65_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M70_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M73_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M74_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M75_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M76_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M77_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M78_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M81_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M82_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M84_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M85_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M86_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M87_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M88_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M89_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M90_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M91_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M92_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M94_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M95_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M96_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M98_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M99_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M100_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M103_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_M_S1_M104_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M23_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M26_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M30_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M32_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M34_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M37_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M38_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M41_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M42_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M45_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M47_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M48_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M50_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M53_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M54_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M55_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M56_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M59_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M61_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M62_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M67_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M68_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M72_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M73_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M74_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M75_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M77_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M78_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M79_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M80_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M82_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M84_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M85_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M89_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M92_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M98_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M99_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M100_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M101_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M104_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M105_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S0_M107_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M21_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M22_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M24_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M25_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M27_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M28_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M31_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M29_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M33_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M35_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M36_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M39_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M40_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M43_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M44_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M46_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M49_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M51_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M52_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M57_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M58_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M60_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M63_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M64_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M65_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M66_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M69_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M70_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M71_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M76_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M81_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M83_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M86_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M87_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M88_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M90_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M91_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M93_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M94_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M95_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M96_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M97_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M102_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M103_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M106_AkPnBcht',
    'ISOL/ST/MAPS_ISOL_ST_P_S1_M108_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M35_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M37_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M47_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M53_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M59_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M66_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M67_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M83_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M87_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S0_M90_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M29_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M36_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M40_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M55_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M57_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M72_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M84_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M97_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M98_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M99_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M100_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_F_S1_M106_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M23_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M40_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M42_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M43_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M46_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M59_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M70_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M78_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S0_M99_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M26_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M27_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M35_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M45_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M48_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M51_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M65_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M68_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M85_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M92_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M96_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M105_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_M_S1_M107_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M21_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M23_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M25_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M27_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M33_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M41_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M48_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M54_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M58_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M65_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M78_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M84_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M94_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S0_M100_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M36_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M44_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M47_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M50_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M57_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M60_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M61_AkPnBcht',
    'ISOL/TR1/MAPS_ISOL_TR1_P_S1_M99_AkPnBcht'

    
]


# # Create dictionary with file paths for each folder (txt, wav and midi)

# In[398]:


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


# In[414]:


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
    sonified_audio = sonify_annotation(intervals, pitches, sonification_fs=sr)
    
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


# In[415]:


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


# In[416]:


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


# In[417]:


# run this code to test your function:
test_estimate_intervals, test_estimate_pitches = estimate_notes('/Volumes/amelia_gdrive/MAPS/AkPnBcht/ISOL/NO/MAPS_ISOL_NO_M_S0_M44_AkPnBcht.wav')

audio = sonify_annotation(test_estimate_intervals, test_estimate_pitches)
IPython.display.Audio(audio, rate=8000)


# # Evaluate Transcription

# In[418]:


import mir_eval
import pandas as pd
from tqdm import tqdm


# In[419]:


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


# In[420]:


#print (transcription_scores)


# # Plot Results 

# In[421]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import librosa.display


# In[422]:


precision = []
recall = []
f_measure = []
avg_overlap_ratio = []
track_names = []

for track_id in transcription_scores:
    
    p = transcription_scores[track_id]['precision']
    r = transcription_scores[track_id]['recall']
    f = transcription_scores[track_id]['f_measure']
    a = transcription_scores[track_id]['avg_overlap_ratio']
    
    precision.append(p)
    recall.append(r)
    f_measure.append(f)
    avg_overlap_ratio.append(a)
    track_names.append(track_id)

data = [precision, recall, f_measure, avg_overlap_ratio]    
fig, ax = plt.subplots()
ax.boxplot(data, labels=['precision','recall','f-measure','avg_overlap_ratio'])
plt.xlabel('Metrics')
plt.ylabel('Score')
plt.title('Metrics Across Tracks')
plt.show()


# # Plot and Sonify Results 

# In[423]:


import mir_eval.display


# ### Best & Worst F-Measure

# In[432]:


# get indexes of best and worst f-measure
best_track = np.argmax(f_measure)
worst_track = np.argmin(f_measure)


# In[433]:


# track 1: best f-measure 
track_id = track_names[best_track] 

track_paths = ISOL_DICT.get(track_id)
audio_path = track_paths['wav']
midi_path = track_paths['midi']

est_intervals, est_pitches = estimate_notes(audio_path)
ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)

fig = plt.figure()
plt.subplot(211, xlabel='time',ylabel='midi notes', title='annotations')
mir_eval.display.piano_roll(intervals=ref_intervals, pitches=ref_pitches)
plt.subplot(212, xlabel='time',ylabel='midi notes', title='notes')
mir_eval.display.piano_roll(intervals=est_intervals, pitches=est_pitches)

plt.tight_layout()

# sonify
y, fs = sonify_notes(audio_path, est_intervals, est_pitches)
IPython.display.Audio(y, rate=fs)


# In[434]:


# track 2: worst f-measure 
track_id = track_names[worst_track] 


track_paths = ISOL_DICT.get(track_id)
audio_path = track_paths['wav']
midi_path = track_paths['midi']

est_intervals, est_pitches = estimate_notes(audio_path)
ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)

fig = plt.figure()
plt.subplot(211, xlabel='time',ylabel='midi notes', title='annotations')
mir_eval.display.piano_roll(intervals=ref_intervals, pitches=ref_pitches)
plt.subplot(212, xlabel='time',ylabel='midi notes', title='notes')
mir_eval.display.piano_roll(intervals=est_intervals, pitches=est_pitches)

plt.tight_layout()

# sonify
y, fs = sonify_notes(audio_path, est_intervals, est_pitches)
IPython.display.Audio(y, rate=fs)


# ### Best & Worst Precision 

# In[436]:


# get indexes of best and worst precision
best_pre = np.argmax(precision)
worst_pre = np.argmin(precision)


# In[437]:


# track 3: best precision
track_id = track_names[best_pre] 


track_paths = ISOL_DICT.get(track_id)
audio_path = track_paths['wav']
midi_path = track_paths['midi']

est_intervals, est_pitches = estimate_notes(audio_path)
ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)

fig = plt.figure()
plt.subplot(211, xlabel='time',ylabel='midi notes', title='annotations')
mir_eval.display.piano_roll(intervals=ref_intervals, pitches=ref_pitches)
plt.subplot(212, xlabel='time',ylabel='midi notes', title='notes')
mir_eval.display.piano_roll(intervals=est_intervals, pitches=est_pitches)

plt.tight_layout()

# sonify
y, fs = sonify_notes(audio_path, est_intervals, est_pitches)
IPython.display.Audio(y, rate=fs)


# In[438]:


# track 4: worst precision 
track_id = track_names[worst_pre] 


track_paths = ISOL_DICT.get(track_id)
audio_path = track_paths['wav']
midi_path = track_paths['midi']

est_intervals, est_pitches = estimate_notes(audio_path)
ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)

fig = plt.figure()
plt.subplot(211, xlabel='time',ylabel='midi notes', title='annotations')
mir_eval.display.piano_roll(intervals=ref_intervals, pitches=ref_pitches)
plt.subplot(212, xlabel='time',ylabel='midi notes', title='notes')
mir_eval.display.piano_roll(intervals=est_intervals, pitches=est_pitches)

plt.tight_layout()

# sonify
y, fs = sonify_notes(audio_path, est_intervals, est_pitches)
IPython.display.Audio(y, rate=fs)


# ### Best & Worst Recall

# In[439]:


# get indexes of best and worst recall

best_rec = np.argmax(recall)
worst_rec = np.argmin(recall)


# In[440]:


# track 5: best recall
track_id = track_names[best_rec] 


track_paths = ISOL_DICT.get(track_id)
audio_path = track_paths['wav']
midi_path = track_paths['midi']

est_intervals, est_pitches = estimate_notes(audio_path)
ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)

fig = plt.figure()
plt.subplot(211, xlabel='time',ylabel='midi notes', title='annotations')
mir_eval.display.piano_roll(intervals=ref_intervals, pitches=ref_pitches)
plt.subplot(212, xlabel='time',ylabel='midi notes', title='notes')
mir_eval.display.piano_roll(intervals=est_intervals, pitches=est_pitches)

plt.tight_layout()

# sonify
y, fs = sonify_notes(audio_path, est_intervals, est_pitches)
IPython.display.Audio(y, rate=fs)


# In[441]:


# track 6: worst recall
track_id = track_names[worst_rec] 


track_paths = ISOL_DICT.get(track_id)
audio_path = track_paths['wav']
midi_path = track_paths['midi']

est_intervals, est_pitches = estimate_notes(audio_path)
ref_intervals, ref_pitches = load_labrosa_apt_midi(midi_path)

fig = plt.figure()
plt.subplot(211, xlabel='time',ylabel='midi notes', title='annotations')
mir_eval.display.piano_roll(intervals=ref_intervals, pitches=ref_pitches)
plt.subplot(212, xlabel='time',ylabel='midi notes', title='notes')
mir_eval.display.piano_roll(intervals=est_intervals, pitches=est_pitches)

plt.tight_layout()

# sonify
y, fs = sonify_notes(audio_path, est_intervals, est_pitches)
IPython.display.Audio(y, rate=fs)


# #                
# 
# 
# 

# # Extra Stuff
# 

# In[ ]:





# In[24]:





# In[ ]:





# In[ ]:




