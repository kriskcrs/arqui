from bluedot.btcomm import BluetoothServer
import board
import neopixel


pixel_pin = board.D21

num_pixels = 210

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

# Mapeo de colores
color_dict = {
    '1': (255, 0, 0),
    '2': (0, 255, 0),
    '3': (0, 0, 255),
    '4': (244, 255, 82),
    '5': (250, 120, 5),
    '6': (153, 5, 250),
    '7': (253, 235, 208),
    '8': (133, 193, 233),
    '9': (255, 255, 255)
}

def pintar_color(dataT):
    return color_dict.get(dataT, (0, 0, 0))

def left():
    pixels[0]=(0,0,0)
    pixels[1]=(0,0,0)
    pixels[2]=(0,0,0)
    pixels[3]=(0,0,0)
    pixels[4]=(0,0,0)
    pixels[5]=(0,0,0)
    pixels[6]=(0,0,0)
    pixels[7]=(0,0,0)
    pixels[8]=(0,0,0)
    pixels[9]=(0,0,0)
    pixels[10]=(0,0,0)
    pixels[11]=(0,0,0)
    pixels[12]=(0,0,0)
    pixels[13]=(0,0,0)

    pixels[27]=(0,0,0)
    pixels[26]=(0,0,0)
    pixels[25]=(0,0,0)
    pixels[24]=(0,0,0)
    pixels[23]=(0,0,0)
    pixels[22]=(0,0,0)
    pixels[21]=(0,0,0)
    pixels[20]=(0,0,0)
    pixels[19]=(0,0,0)
    pixels[18]=(0,0,0)
    pixels[17]=(0,0,0)
    pixels[16]=(0,0,0)
    pixels[15]=(0,0,0)
    pixels[14]=(0,0,0)

    pixels[28]=(0,0,0)
    pixels[29]=(0,0,0)
    pixels[30]=(0,0,0)
    pixels[31]=(0,0,0)
    pixels[32]=(0,0,0)
    pixels[33]=(244,255,82)
    pixels[34]=(244,255,82)
    pixels[35]=(0,0,0)
    pixels[36]=(0,0,0)
    pixels[37]=(0,0,0)
    pixels[38]=(0,0,0)
    pixels[39]=(0,0,0)
    pixels[40]=(0,0,0)
    pixels[41]=(0,0,0)

    pixels[55]=(0,0,0)
    pixels[54]=(0,0,0)
    pixels[53]=(0,0,0)
    pixels[52]=(0,0,0)
    pixels[51]=(244,255,82)
    pixels[50]=(244,255,82)
    pixels[49]=(244,255,82)
    pixels[48]=(0,0,0)
    pixels[47]=(0,0,0)
    pixels[46]=(0,0,0)
    pixels[45]=(0,0,0)
    pixels[44]=(0,0,0)
    pixels[43]=(0,0,0)
    pixels[42]=(0,0,0)

    pixels[56]=(0,0,0)
    pixels[57]=(0,0,0)
    pixels[58]=(0,0,0)
    pixels[59]=(244,255,82)
    pixels[60]=(244,255,82)
    pixels[61]=(244,255,82)
    pixels[62]=(244,255,82)
    pixels[63]=(0,0,0)
    pixels[64]=(0,0,0)
    pixels[65]=(0,0,0)
    pixels[66]=(0,0,0)
    pixels[67]=(0,0,0)
    pixels[68]=(0,0,0)
    pixels[69]=(0,0,0)

    pixels[83]=(0,0,0)
    pixels[82]=(0,0,0)
    pixels[81]=(244,255,82)
    pixels[80]=(244,255,82)
    pixels[79]=(244,255,82)
    pixels[78]=(244,255,82)
    pixels[77]=(244,255,82)
    pixels[76]=(0,0,0)
    pixels[75]=(0,0,0)
    pixels[74]=(0,0,0)
    pixels[73]=(0,0,0)
    pixels[72]=(0,0,0)
    pixels[71]=(0,0,0)
    pixels[70]=(0,0,0)

    pixels[84]=(0,0,0)
    pixels[85]=(244,255,82)
    pixels[86]=(244,255,82)
    pixels[87]=(244,255,82)
    pixels[88]=(244,255,82)
    pixels[89]=(244,255,82)
    pixels[90]=(244,255,82)
    pixels[91]=(244,255,82)
    pixels[92]=(244,255,82)
    pixels[93]=(244,255,82)
    pixels[94]=(244,255,82)
    pixels[95]=(244,255,82)
    pixels[96]=(244,255,82)
    pixels[97]=(244,255,82)

    pixels[111]=(244,255,82)
    pixels[110]=(244,255,82)
    pixels[109]=(244,255,82)
    pixels[108]=(244,255,82)
    pixels[107]=(244,255,82)
    pixels[106]=(244,255,82)
    pixels[105]=(244,255,82)
    pixels[104]=(244,255,82)
    pixels[103]=(244,255,82)
    pixels[102]=(244,255,82)
    pixels[101]=(244,255,82)
    pixels[100]=(244,255,82)
    pixels[99]=(244,255,82)
    pixels[98]=(244,255,82)

    pixels[112]=(0,0,0)
    pixels[113]=(244,255,82)
    pixels[114]=(244,255,82)
    pixels[115]=(244,255,82)
    pixels[116]=(244,255,82)
    pixels[117]=(244,255,82)
    pixels[118]=(244,255,82)
    pixels[119]=(244,255,82)
    pixels[120]=(244,255,82)
    pixels[121]=(244,255,82)
    pixels[122]=(244,255,82)
    pixels[123]=(244,255,82)
    pixels[124]=(244,255,82)
    pixels[125]=(244,255,82)

    pixels[139]=(0,0,0)
    pixels[138]=(0,0,0)
    pixels[137]=(244,255,82)
    pixels[136]=(244,255,82)
    pixels[135]=(244,255,82)
    pixels[134]=(244,255,82)
    pixels[133]=(244,255,82)
    pixels[132]=(0,0,0)
    pixels[131]=(0,0,0)
    pixels[130]=(0,0,0)
    pixels[129]=(0,0,0)
    pixels[128]=(0,0,0)
    pixels[127]=(0,0,0)
    pixels[126]=(0,0,0)

    pixels[140]=(0,0,0)
    pixels[141]=(0,0,0)
    pixels[142]=(0,0,0)
    pixels[143]=(244,255,82)
    pixels[144]=(244,255,82)
    pixels[145]=(244,255,82)
    pixels[146]=(244,255,82)
    pixels[147]=(0,0,0)
    pixels[148]=(0,0,0)
    pixels[149]=(0,0,0)
    pixels[150]=(0,0,0)
    pixels[151]=(0,0,0)
    pixels[152]=(0,0,0)
    pixels[153]=(0,0,0)

    pixels[167]=(0,0,0)
    pixels[166]=(0,0,0)
    pixels[165]=(0,0,0)
    pixels[164]=(0,0,0)
    pixels[163]=(244,255,82)
    pixels[162]=(244,255,82)
    pixels[161]=(244,255,82)
    pixels[160]=(0,0,0)
    pixels[159]=(0,0,0)
    pixels[158]=(0,0,0)
    pixels[157]=(0,0,0)
    pixels[156]=(0,0,0)
    pixels[155]=(0,0,0)
    pixels[154]=(0,0,0)

    pixels[168]=(0,0,0)
    pixels[169]=(0,0,0)
    pixels[170]=(0,0,0)
    pixels[171]=(0,0,0)
    pixels[172]=(0,0,0)
    pixels[173]=(244,255,82)
    pixels[174]=(244,255,82)
    pixels[175]=(0,0,0)
    pixels[176]=(0,0,0)
    pixels[177]=(0,0,0)
    pixels[178]=(0,0,0)
    pixels[179]=(0,0,0)
    pixels[180]=(0,0,0)
    pixels[181]=(0,0,0)

    pixels[195]=(0,0,0)
    pixels[194]=(0,0,0)
    pixels[193]=(0,0,0)
    pixels[192]=(0,0,0)
    pixels[191]=(0,0,0)
    pixels[190]=(0,0,0)
    pixels[189]=(0,0,0)
    pixels[188]=(0,0,0)
    pixels[187]=(0,0,0)
    pixels[186]=(0,0,0)
    pixels[185]=(0,0,0)
    pixels[184]=(0,0,0)
    pixels[183]=(0,0,0)
    pixels[182]=(0,0,0)

    pixels[196]=(0,0,0)
    pixels[197]=(0,0,0)
    pixels[198]=(0,0,0)
    pixels[199]=(0,0,0)
    pixels[200]=(0,0,0)
    pixels[201]=(0,0,0)
    pixels[202]=(0,0,0)
    pixels[203]=(0,0,0)
    pixels[204]=(0,0,0)
    pixels[205]=(0,0,0)
    pixels[206]=(0,0,0)
    pixels[207]=(0,0,0)
    pixels[208]=(0,0,0)
    pixels[209]=(0,0,0)

def rigth():
    pixels[0]=(0,0,0)
    pixels[1]=(0,0,0)
    pixels[2]=(0,0,0)
    pixels[3]=(0,0,0)
    pixels[4]=(0,0,0)
    pixels[5]=(0,0,0)
    pixels[6]=(0,0,0)
    pixels[7]=(0,0,0)
    pixels[8]=(0,0,0)
    pixels[9]=(0,0,0)
    pixels[10]=(0,0,0)
    pixels[11]=(0,0,0)
    pixels[12]=(0,0,0)
    pixels[13]=(0,0,0)

    pixels[27]=(0,0,0)
    pixels[26]=(0,0,0)
    pixels[25]=(0,0,0)
    pixels[24]=(0,0,0)
    pixels[23]=(0,0,0)
    pixels[22]=(0,0,0)
    pixels[21]=(0,0,0)
    pixels[20]=(0,0,0)
    pixels[19]=(0,0,0)
    pixels[18]=(0,0,0)
    pixels[17]=(0,0,0)
    pixels[16]=(0,0,0)
    pixels[15]=(0,0,0)
    pixels[14]=(0,0,0)

    pixels[28]=(0,0,0)
    pixels[29]=(0,0,0)
    pixels[30]=(0,0,0)
    pixels[31]=(0,0,0)
    pixels[32]=(0,0,0)
    pixels[33]=(0,0,0)
    pixels[34]=(0,0,0)
    pixels[35]=(244,255,82)
    pixels[36]=(244,255,82)
    pixels[37]=(0,0,0)
    pixels[38]=(0,0,0)
    pixels[39]=(0,0,0)
    pixels[40]=(0,0,0)
    pixels[41]=(0,0,0)

    pixels[55]=(0,0,0)
    pixels[54]=(0,0,0)
    pixels[53]=(0,0,0)
    pixels[52]=(0,0,0)
    pixels[51]=(0,0,0)
    pixels[50]=(0,0,0)
    pixels[49]=(0,0,0)
    pixels[48]=(244,255,82)
    pixels[47]=(244,255,82)
    pixels[46]=(244,255,82)
    pixels[45]=(0,0,0)
    pixels[44]=(0,0,0)
    pixels[43]=(0,0,0)
    pixels[42]=(0,0,0)

    pixels[56]=(0,0,0)
    pixels[57]=(0,0,0)
    pixels[58]=(0,0,0)
    pixels[59]=(0,0,0)
    pixels[60]=(0,0,0)
    pixels[61]=(0,0,0)
    pixels[62]=(0,0,0)
    pixels[63]=(244,255,82)
    pixels[64]=(244,255,82)
    pixels[65]=(244,255,82)
    pixels[66]=(244,255,82)
    pixels[67]=(0,0,0)
    pixels[68]=(0,0,0)
    pixels[69]=(0,0,0)

    pixels[83]=(0,0,0)
    pixels[82]=(0,0,0)
    pixels[81]=(0,0,0)
    pixels[80]=(0,0,0)
    pixels[79]=(0,0,0)
    pixels[78]=(0,0,0)
    pixels[77]=(0,0,0)
    pixels[76]=(244,255,82)
    pixels[75]=(244,255,82)
    pixels[74]=(244,255,82)
    pixels[73]=(244,255,82)
    pixels[72]=(244,255,82)
    pixels[71]=(0,0,0)
    pixels[70]=(0,0,0)

    pixels[84]=(244,255,82)
    pixels[85]=(244,255,82)
    pixels[86]=(244,255,82)
    pixels[87]=(244,255,82)
    pixels[88]=(244,255,82)
    pixels[89]=(244,255,82)
    pixels[90]=(244,255,82)
    pixels[91]=(244,255,82)
    pixels[92]=(244,255,82)
    pixels[93]=(244,255,82)
    pixels[94]=(244,255,82)
    pixels[95]=(244,255,82)
    pixels[96]=(244,255,82)
    pixels[97]=(0,0,0)

    pixels[111]=(244,255,82)
    pixels[110]=(244,255,82)
    pixels[109]=(244,255,82)
    pixels[108]=(244,255,82)
    pixels[107]=(244,255,82)
    pixels[106]=(244,255,82)
    pixels[105]=(244,255,82)
    pixels[104]=(244,255,82)
    pixels[103]=(244,255,82)
    pixels[102]=(244,255,82)
    pixels[101]=(244,255,82)
    pixels[100]=(244,255,82)
    pixels[99]=(244,255,82)
    pixels[98]=(244,255,82)

    pixels[112]=(244,255,82)
    pixels[113]=(244,255,82)
    pixels[114]=(244,255,82)
    pixels[115]=(244,255,82)
    pixels[116]=(244,255,82)
    pixels[117]=(244,255,82)
    pixels[118]=(244,255,82)
    pixels[119]=(244,255,82)
    pixels[120]=(244,255,82)
    pixels[121]=(244,255,82)
    pixels[122]=(244,255,82)
    pixels[123]=(244,255,82)
    pixels[124]=(244,255,82)
    pixels[125]=(0,0,0)

    pixels[139]=(0,0,0)
    pixels[138]=(0,0,0)
    pixels[137]=(0,0,0)
    pixels[136]=(0,0,0)
    pixels[135]=(0,0,0)
    pixels[134]=(0,0,0)
    pixels[133]=(0,0,0)
    pixels[132]=(244,255,82)
    pixels[131]=(244,255,82)
    pixels[130]=(244,255,82)
    pixels[129]=(244,255,82)
    pixels[128]=(244,255,82)
    pixels[127]=(0,0,0)
    pixels[126]=(0,0,0)

    pixels[140]=(0,0,0)
    pixels[141]=(0,0,0)
    pixels[142]=(0,0,0)
    pixels[143]=(0,0,0)
    pixels[144]=(0,0,0)
    pixels[145]=(0,0,0)
    pixels[146]=(0,0,0)
    pixels[147]=(244,255,82)
    pixels[148]=(244,255,82)
    pixels[149]=(244,255,82)
    pixels[150]=(244,255,82)
    pixels[151]=(0,0,0)
    pixels[152]=(0,0,0)
    pixels[153]=(0,0,0)

    pixels[167]=(0,0,0)
    pixels[166]=(0,0,0)
    pixels[165]=(0,0,0)
    pixels[164]=(0,0,0)
    pixels[163]=(0,0,0)
    pixels[162]=(0,0,0)
    pixels[161]=(0,0,0)
    pixels[160]=(244,255,82)
    pixels[159]=(244,255,82)
    pixels[158]=(244,255,82)
    pixels[157]=(0,0,0)
    pixels[156]=(0,0,0)
    pixels[155]=(0,0,0)
    pixels[154]=(0,0,0)

    pixels[168]=(0,0,0)
    pixels[169]=(0,0,0)
    pixels[170]=(0,0,0)
    pixels[171]=(0,0,0)
    pixels[172]=(0,0,0)
    pixels[173]=(0,0,0)
    pixels[174]=(0,0,0)
    pixels[175]=(244,255,82)
    pixels[176]=(244,255,82)
    pixels[177]=(0,0,0)
    pixels[178]=(0,0,0)
    pixels[179]=(0,0,0)
    pixels[180]=(0,0,0)
    pixels[181]=(0,0,0)

    pixels[195]=(0,0,0)
    pixels[194]=(0,0,0)
    pixels[193]=(0,0,0)
    pixels[192]=(0,0,0)
    pixels[191]=(0,0,0)
    pixels[190]=(0,0,0)
    pixels[189]=(0,0,0)
    pixels[188]=(0,0,0)
    pixels[187]=(0,0,0)
    pixels[186]=(0,0,0)
    pixels[185]=(0,0,0)
    pixels[184]=(0,0,0)
    pixels[183]=(0,0,0)
    pixels[182]=(0,0,0)

    pixels[196]=(0,0,0)
    pixels[197]=(0,0,0)
    pixels[198]=(0,0,0)
    pixels[199]=(0,0,0)
    pixels[200]=(0,0,0)
    pixels[201]=(0,0,0)
    pixels[202]=(0,0,0)
    pixels[203]=(0,0,0)
    pixels[204]=(0,0,0)
    pixels[205]=(0,0,0)
    pixels[206]=(0,0,0)
    pixels[207]=(0,0,0)
    pixels[208]=(0,0,0)
    pixels[209]=(0,0,0)

def like():
    pixels[0]=(0,0,0)
    pixels[1]=(0,0,0)
    pixels[2]=(0,0,0)
    pixels[3]=(0,0,0)
    pixels[4]=(0,0,0)
    pixels[5]=(0,0,0)
    pixels[6]=(0,0,0)
    pixels[7]=(0,0,0)
    pixels[8]=(0,0,0)
    pixels[9]=(0,0,0)
    pixels[10]=(0,0,0)
    pixels[11]=(0,0,0)
    pixels[12]=(0,0,0)
    pixels[13]=(0,0,0)
    pixels[27]=(0,0,0)
    pixels[26]=(0,0,0)
    pixels[25]=(0,0,0)
    pixels[24]=(0,0,0)
    pixels[23]=(0,0,0)
    pixels[22]=(0,0,0)
    pixels[21]=(0,0,0)
    pixels[20]=(0,0,0)
    pixels[19]=(0,0,0)
    pixels[18]=(1,111,185)
    pixels[17]=(1,111,185)
    pixels[16]=(1,111,185)
    pixels[15]=(0,0,0)
    pixels[14]=(0,0,0)
    pixels[28]=(0,0,0)
    pixels[29]=(0,0,0)
    pixels[30]=(0,0,0)
    pixels[31]=(0,0,0)
    pixels[32]=(0,0,0)
    pixels[33]=(0,0,0)
    pixels[34]=(0,0,0)
    pixels[35]=(0,0,0)
    pixels[36]=(1,111,185)
    pixels[37]=(255,255,255)
    pixels[38]=(255,255,255)
    pixels[39]=(1,111,185)
    pixels[40]=(0,0,0)
    pixels[41]=(0,0,0)
    pixels[55]=(0,0,0)
    pixels[54]=(0,0,0)
    pixels[53]=(0,0,0)
    pixels[52]=(0,0,0)
    pixels[51]=(0,0,0)
    pixels[50]=(0,0,0)
    pixels[49]=(0,0,0)
    pixels[48]=(0,0,0)
    pixels[47]=(1,111,185)
    pixels[46]=(255,255,255)
    pixels[45]=(255,255,255)
    pixels[44]=(1,111,185)
    pixels[43]=(0,0,0)
    pixels[42]=(0,0,0)
    pixels[56]=(0,0,0)
    pixels[57]=(0,0,0)
    pixels[58]=(0,0,0)
    pixels[59]=(0,0,0)
    pixels[60]=(0,0,0)
    pixels[61]=(0,0,0)
    pixels[62]=(0,0,0)
    pixels[63]=(1,111,185)
    pixels[64]=(1,111,185)
    pixels[65]=(255,255,255)
    pixels[66]=(255,255,255)
    pixels[67]=(1,111,185)
    pixels[68]=(0,0,0)
    pixels[69]=(0,0,0)
    pixels[83]=(0,0,0)
    pixels[82]=(0,0,0)
    pixels[81]=(0,0,0)
    pixels[80]=(0,0,0)
    pixels[79]=(0,0,0)
    pixels[78]=(0,0,0)
    pixels[77]=(1,111,185)
    pixels[76]=(1,111,185)
    pixels[75]=(255,255,255)
    pixels[74]=(255,255,255)
    pixels[73]=(255,255,255)
    pixels[72]=(1,111,185)
    pixels[71]=(0,0,0)
    pixels[70]=(0,0,0)
    pixels[84]=(1,111,185)
    pixels[85]=(1,111,185)
    pixels[86]=(1,111,185)
    pixels[87]=(1,111,185)
    pixels[88]=(0,0,0)
    pixels[89]=(0,0,0)
    pixels[90]=(1,111,185)
    pixels[91]=(255,255,255)
    pixels[92]=(255,255,255)
    pixels[93]=(255,255,255)
    pixels[94]=(255,255,255)
    pixels[95]=(1,111,185)
    pixels[96]=(1,111,185)
    pixels[97]=(1,111,185)
    pixels[111]=(1,111,185)
    pixels[110]=(1,111,185)
    pixels[109]=(1,111,185)
    pixels[108]=(1,111,185)
    pixels[107]=(1,111,185)
    pixels[106]=(1,111,185)
    pixels[105]=(1,111,185)
    pixels[104]=(255,255,255)
    pixels[103]=(255,255,255)
    pixels[102]=(255,255,255)
    pixels[101]=(255,255,255)
    pixels[100]=(255,255,255)
    pixels[99]=(255,255,255)
    pixels[98]=(1,111,185)
    pixels[112]=(1,111,185)
    pixels[113]=(1,111,185)
    pixels[114]=(1,111,185)
    pixels[115]=(1,111,185)
    pixels[116]=(255,255,255)
    pixels[117]=(255,255,255)
    pixels[118]=(255,255,255)
    pixels[119]=(255,255,255)
    pixels[120]=(255,255,255)
    pixels[121]=(255,255,255)
    pixels[122]=(255,255,255)
    pixels[123]=(255,255,255)
    pixels[124]=(255,255,255)
    pixels[125]=(1,111,185)
    pixels[139]=(1,111,185)
    pixels[138]=(1,111,185)
    pixels[137]=(1,111,185)
    pixels[136]=(1,111,185)
    pixels[135]=(255,255,255)
    pixels[134]=(255,255,255)
    pixels[133]=(255,255,255)
    pixels[132]=(255,255,255)
    pixels[131]=(255,255,255)
    pixels[130]=(255,255,255)
    pixels[129]=(255,255,255)
    pixels[128]=(255,255,255)
    pixels[127]=(255,255,255)
    pixels[126]=(1,111,185)
    pixels[140]=(1,111,185)
    pixels[141]=(1,111,185)
    pixels[142]=(1,111,185)
    pixels[143]=(1,111,185)
    pixels[144]=(255,255,255)
    pixels[145]=(255,255,255)
    pixels[146]=(255,255,255)
    pixels[147]=(255,255,255)
    pixels[148]=(255,255,255)
    pixels[149]=(255,255,255)
    pixels[150]=(255,255,255)
    pixels[151]=(255,255,255)
    pixels[152]=(255,255,255)
    pixels[153]=(1,111,185)
    pixels[167]=(1,111,185)
    pixels[166]=(1,111,185)
    pixels[165]=(1,111,185)
    pixels[164]=(1,111,185)
    pixels[163]=(255,255,255)
    pixels[162]=(255,255,255)
    pixels[161]=(255,255,255)
    pixels[160]=(255,255,255)
    pixels[159]=(255,255,255)
    pixels[158]=(255,255,255)
    pixels[157]=(255,255,255)
    pixels[156]=(255,255,255)
    pixels[155]=(255,255,255)
    pixels[154]=(1,111,185)
    pixels[168]=(1,111,185)
    pixels[169]=(1,111,185)
    pixels[170]=(255,255,255)
    pixels[171]=(1,111,185)
    pixels[172]=(1,111,185)
    pixels[173]=(1,111,185)
    pixels[174]=(1,111,185)
    pixels[175]=(1,111,185)
    pixels[176]=(1,111,185)
    pixels[177]=(255,255,255)
    pixels[178]=(255,255,255)
    pixels[179]=(255,255,255)
    pixels[180]=(255,255,255)
    pixels[181]=(1,111,185)
    pixels[195]=(1,111,185)
    pixels[194]=(1,111,185)
    pixels[193]=(1,111,185)
    pixels[192]=(1,111,185)
    pixels[191]=(0,0,0)
    pixels[190]=(0,0,0)
    pixels[189]=(0,0,0)
    pixels[188]=(1,111,185)
    pixels[187]=(1,111,185)
    pixels[186]=(1,111,185)
    pixels[185]=(1,111,185)
    pixels[184]=(1,111,185)
    pixels[183]=(1,111,185)
    pixels[182]=(1,111,185)
    pixels[196]=(0,0,0)
    pixels[197]=(0,0,0)
    pixels[198]=(0,0,0)
    pixels[199]=(0,0,0)
    pixels[200]=(0,0,0)
    pixels[201]=(0,0,0)
    pixels[202]=(0,0,0)
    pixels[203]=(0,0,0)
    pixels[204]=(0,0,0)
    pixels[205]=(0,0,0)
    pixels[206]=(0,0,0)
    pixels[207]=(0,0,0)
    pixels[208]=(0,0,0)
    pixels[209]=(0,0,0)

def block():
    pixels[0]=(0,0,0)
    pixels[1]=(0,0,0)
    pixels[2]=(0,0,0)
    pixels[3]=(0,0,0)
    pixels[4]=(0,0,0)
    pixels[5]=(0,0,0)
    pixels[6]=(0,0,0)
    pixels[7]=(0,0,0)
    pixels[8]=(0,0,0)
    pixels[9]=(0,0,0)
    pixels[10]=(0,0,0)
    pixels[11]=(0,0,0)
    pixels[12]=(0,0,0)
    pixels[13]=(0,0,0)
    pixels[27]=(0,0,0)
    pixels[26]=(0,0,0)
    pixels[25]=(0,0,0)
    pixels[24]=(0,0,0)
    pixels[23]=(0,0,0)
    pixels[22]=(0,0,0)
    pixels[21]=(0,0,0)
    pixels[20]=(0,0,0)
    pixels[19]=(0,0,0)
    pixels[18]=(0,0,0)
    pixels[17]=(0,0,0)
    pixels[16]=(0,0,0)
    pixels[15]=(0,0,0)
    pixels[14]=(0,0,0)
    pixels[28]=(0,0,0)
    pixels[29]=(0,0,0)
    pixels[30]=(0,0,0)
    pixels[31]=(0,0,0)
    pixels[32]=(255,27,28)
    pixels[33]=(255,27,28)
    pixels[34]=(255,27,28)
    pixels[35]=(255,27,28)
    pixels[36]=(255,27,28)
    pixels[37]=(0,0,0)
    pixels[38]=(0,0,0)
    pixels[39]=(0,0,0)
    pixels[40]=(0,0,0)
    pixels[41]=(0,0,0)
    pixels[55]=(0,0,0)
    pixels[54]=(0,0,0)
    pixels[53]=(0,0,0)
    pixels[52]=(255,27,28)
    pixels[51]=(0,0,0)
    pixels[50]=(0,0,0)
    pixels[49]=(0,0,0)
    pixels[48]=(0,0,0)
    pixels[47]=(0,0,0)
    pixels[46]=(255,27,28)
    pixels[45]=(0,0,0)
    pixels[44]=(0,0,0)
    pixels[43]=(0,0,0)
    pixels[42]=(0,0,0)
    pixels[56]=(0,0,0)
    pixels[57]=(0,0,0)
    pixels[58]=(255,27,28)
    pixels[59]=(255,27,28)
    pixels[60]=(0,0,0)
    pixels[61]=(0,0,0)
    pixels[62]=(0,0,0)
    pixels[63]=(0,0,0)
    pixels[64]=(0,0,0)
    pixels[65]=(0,0,0)
    pixels[66]=(255,27,28)
    pixels[67]=(0,0,0)
    pixels[68]=(0,0,0)
    pixels[69]=(0,0,0)
    pixels[83]=(0,0,0)
    pixels[82]=(255,27,28)
    pixels[81]=(0,0,0)
    pixels[80]=(0,0,0)
    pixels[79]=(255,27,28)
    pixels[78]=(0,0,0)
    pixels[77]=(0,0,0)
    pixels[76]=(0,0,0)
    pixels[75]=(0,0,0)
    pixels[74]=(0,0,0)
    pixels[73]=(0,0,0)
    pixels[72]=(255,27,28)
    pixels[71]=(0,0,0)
    pixels[70]=(0,0,0)
    pixels[84]=(0,0,0)
    pixels[85]=(255,27,28)
    pixels[86]=(0,0,0)
    pixels[87]=(0,0,0)
    pixels[88]=(0,0,0)
    pixels[89]=(255,27,28)
    pixels[90]=(0,0,0)
    pixels[91]=(0,0,0)
    pixels[92]=(0,0,0)
    pixels[93]=(0,0,0)
    pixels[94]=(0,0,0)
    pixels[95]=(255,27,28)
    pixels[96]=(0,0,0)
    pixels[97]=(0,0,0)
    pixels[111]=(0,0,0)
    pixels[110]=(255,27,28)
    pixels[109]=(0,0,0)
    pixels[108]=(0,0,0)
    pixels[107]=(0,0,0)
    pixels[106]=(0,0,0)
    pixels[105]=(255,27,28)
    pixels[104]=(0,0,0)
    pixels[103]=(0,0,0)
    pixels[102]=(0,0,0)
    pixels[101]=(0,0,0)
    pixels[100]=(255,27,28)
    pixels[99]=(0,0,0)
    pixels[98]=(0,0,0)
    pixels[112]=(0,0,0)
    pixels[113]=(255,27,28)
    pixels[114]=(0,0,0)
    pixels[115]=(0,0,0)
    pixels[116]=(0,0,0)
    pixels[117]=(0,0,0)
    pixels[118]=(0,0,0)
    pixels[119]=(255,27,28)
    pixels[120]=(0,0,0)
    pixels[121]=(0,0,0)
    pixels[122]=(0,0,0)
    pixels[123]=(255,27,28)
    pixels[124]=(0,0,0)
    pixels[125]=(0,0,0)
    pixels[139]=(0,0,0)
    pixels[138]=(255,27,28)
    pixels[137]=(0,0,0)
    pixels[136]=(0,0,0)
    pixels[135]=(0,0,0)
    pixels[134]=(0,0,0)
    pixels[133]=(0,0,0)
    pixels[132]=(0,0,0)
    pixels[131]=(255,27,28)
    pixels[130]=(0,0,0)
    pixels[129]=(0,0,0)
    pixels[128]=(255,27,28)
    pixels[127]=(0,0,0)
    pixels[126]=(0,0,0)
    pixels[140]=(0,0,0)
    pixels[141]=(0,0,0)
    pixels[142]=(255,27,28)
    pixels[143]=(0,0,0)
    pixels[144]=(0,0,0)
    pixels[145]=(0,0,0)
    pixels[146]=(0,0,0)
    pixels[147]=(0,0,0)
    pixels[148]=(0,0,0)
    pixels[149]=(255,27,28)
    pixels[150]=(255,27,28)
    pixels[151]=(0,0,0)
    pixels[152]=(0,0,0)
    pixels[153]=(0,0,0)
    pixels[167]=(0,0,0)
    pixels[166]=(0,0,0)
    pixels[165]=(0,0,0)
    pixels[164]=(255,27,28)
    pixels[163]=(0,0,0)
    pixels[162]=(0,0,0)
    pixels[161]=(0,0,0)
    pixels[160]=(0,0,0)
    pixels[159]=(0,0,0)
    pixels[158]=(255,27,28)
    pixels[157]=(0,0,0)
    pixels[156]=(0,0,0)
    pixels[155]=(0,0,0)
    pixels[154]=(0,0,0)
    pixels[168]=(0,0,0)
    pixels[169]=(0,0,0)
    pixels[170]=(0,0,0)
    pixels[171]=(0,0,0)
    pixels[172]=(255,27,28)
    pixels[173]=(255,27,28)
    pixels[174]=(255,27,28)
    pixels[175]=(255,27,28)
    pixels[176]=(255,27,28)
    pixels[177]=(0,0,0)
    pixels[178]=(0,0,0)
    pixels[179]=(0,0,0)
    pixels[180]=(0,0,0)
    pixels[181]=(0,0,0)
    pixels[195]=(0,0,0)
    pixels[194]=(0,0,0)
    pixels[193]=(0,0,0)
    pixels[192]=(0,0,0)
    pixels[191]=(0,0,0)
    pixels[190]=(0,0,0)
    pixels[189]=(0,0,0)
    pixels[188]=(0,0,0)
    pixels[187]=(0,0,0)
    pixels[186]=(0,0,0)
    pixels[185]=(0,0,0)
    pixels[184]=(0,0,0)
    pixels[183]=(0,0,0)
    pixels[182]=(0,0,0)
    pixels[196]=(0,0,0)
    pixels[197]=(0,0,0)
    pixels[198]=(0,0,0)
    pixels[199]=(0,0,0)
    pixels[200]=(0,0,0)
    pixels[201]=(0,0,0)
    pixels[202]=(0,0,0)
    pixels[203]=(0,0,0)
    pixels[204]=(0,0,0)
    pixels[205]=(0,0,0)
    pixels[206]=(0,0,0)
    pixels[207]=(0,0,0)
    pixels[208]=(0,0,0)
    pixels[209]=(0,0,0)

def mario():
    pixels[0]=(133,193,233)
    pixels[1]=(133,193,233)
    pixels[2]=(133,193,233)
    pixels[3]=(133,193,233)
    pixels[4]=(133,193,233)
    pixels[5]=(133,193,233)
    pixels[6]=(133,193,233)
    pixels[7]=(133,193,233)
    pixels[8]=(133,193,233)
    pixels[9]=(133,193,233)
    pixels[10]=(133,193,233)
    pixels[11]=(133,193,233)
    pixels[12]=(133,193,233)
    pixels[13]=(133,193,233)
    pixels[27]=(133,193,233)
    pixels[26]=(133,193,233)
    pixels[25]=(133,193,233)
    pixels[24]=(133,193,233)
    pixels[23]=(133,193,233)
    pixels[22]=(133,193,233)
    pixels[21]=(133,193,233)
    pixels[20]=(133,193,233)
    pixels[19]=(133,193,233)
    pixels[18]=(133,193,233)
    pixels[17]=(133,193,233)
    pixels[16]=(133,193,233)
    pixels[15]=(133,193,233)
    pixels[14]=(133,193,233)
    pixels[28]=(133,193,233)
    pixels[29]=(133,193,233)
    pixels[30]=(133,193,233)
    pixels[31]=(133,193,233)
    pixels[32]=(255,0,0)
    pixels[33]=(255,0,0)
    pixels[34]=(255,0,0)
    pixels[35]=(255,0,0)
    pixels[36]=(255,0,0)
    pixels[37]=(255,0,0)
    pixels[38]=(133,193,233)
    pixels[39]=(133,193,233)
    pixels[40]=(133,193,233)
    pixels[41]=(133,193,233)
    pixels[55]=(133,193,233)
    pixels[54]=(133,193,233)
    pixels[53]=(255,0,0)
    pixels[52]=(255,0,0)
    pixels[51]=(255,0,0)
    pixels[50]=(255,0,0)
    pixels[49]=(255,0,0)
    pixels[48]=(255,0,0)
    pixels[47]=(255,0,0)
    pixels[46]=(255,0,0)
    pixels[45]=(255,0,0)
    pixels[44]=(255,0,0)
    pixels[43]=(255,0,0)
    pixels[42]=(133,193,233)
    pixels[56]=(133,193,233)
    pixels[57]=(133,193,233)
    pixels[58]=(0,0,0)
    pixels[59]=(0,0,0)
    pixels[60]=(0,0,0)
    pixels[61]=(0,0,0)
    pixels[62]=(0,0,0)
    pixels[63]=(253,235,208)
    pixels[64]=(253,235,208)
    pixels[65]=(0,0,0)
    pixels[66]=(253,235,208)
    pixels[67]=(133,193,233)
    pixels[68]=(133,193,233)
    pixels[69]=(133,193,233)
    pixels[83]=(133,193,233)
    pixels[82]=(133,193,233)
    pixels[81]=(0,0,0)
    pixels[80]=(0,0,0)
    pixels[79]=(253,235,208)
    pixels[78]=(0,0,0)
    pixels[77]=(253,235,208)
    pixels[76]=(253,235,208)
    pixels[75]=(253,235,208)
    pixels[74]=(0,0,0)
    pixels[73]=(253,235,208)
    pixels[72]=(133,193,233)
    pixels[71]=(133,193,233)
    pixels[70]=(133,193,233)
    pixels[84]=(133,193,233)
    pixels[85]=(0,0,0)
    pixels[86]=(0,0,0)
    pixels[87]=(0,0,0)
    pixels[88]=(253,235,208)
    pixels[89]=(0,0,0)
    pixels[90]=(253,235,208)
    pixels[91]=(253,235,208)
    pixels[92]=(253,235,208)
    pixels[93]=(0,0,0)
    pixels[94]=(253,235,208)
    pixels[95]=(253,235,208)
    pixels[96]=(133,193,233)
    pixels[97]=(133,193,233)
    pixels[111]=(133,193,233)
    pixels[110]=(0,0,0)
    pixels[109]=(0,0,0)
    pixels[108]=(0,0,0)
    pixels[107]=(253,235,208)
    pixels[106]=(0,0,0)
    pixels[105]=(0,0,0)
    pixels[104]=(253,235,208)
    pixels[103]=(253,235,208)
    pixels[102]=(253,235,208)
    pixels[101]=(0,0,0)
    pixels[100]=(253,235,208)
    pixels[99]=(253,235,208)
    pixels[98]=(133,193,233)
    pixels[112]=(133,193,233)
    pixels[113]=(0,0,0)
    pixels[114]=(0,0,0)
    pixels[115]=(0,0,0)
    pixels[116]=(0,0,0)
    pixels[117]=(253,235,208)
    pixels[118]=(253,235,208)
    pixels[119]=(253,235,208)
    pixels[120]=(253,235,208)
    pixels[121]=(253,235,208)
    pixels[122]=(0,0,0)
    pixels[123]=(253,235,208)
    pixels[124]=(253,235,208)
    pixels[125]=(133,193,233)
    pixels[139]=(133,193,233)
    pixels[138]=(0,0,0)
    pixels[137]=(0,0,0)
    pixels[136]=(0,0,0)
    pixels[135]=(0,0,0)
    pixels[134]=(253,235,208)
    pixels[133]=(253,235,208)
    pixels[132]=(253,235,208)
    pixels[131]=(253,235,208)
    pixels[130]=(0,0,0)
    pixels[129]=(0,0,0)
    pixels[128]=(0,0,0)
    pixels[127]=(0,0,0)
    pixels[126]=(133,193,233)
    pixels[140]=(133,193,233)
    pixels[141]=(133,193,233)
    pixels[142]=(133,193,233)
    pixels[143]=(253,235,208)
    pixels[144]=(253,235,208)
    pixels[145]=(253,235,208)
    pixels[146]=(253,235,208)
    pixels[147]=(253,235,208)
    pixels[148]=(253,235,208)
    pixels[149]=(253,235,208)
    pixels[150]=(253,235,208)
    pixels[151]=(253,235,208)
    pixels[152]=(133,193,233)
    pixels[153]=(133,193,233)
    pixels[167]=(133,193,233)
    pixels[166]=(133,193,233)
    pixels[165]=(133,193,233)
    pixels[164]=(133,193,233)
    pixels[163]=(253,235,208)
    pixels[162]=(253,235,208)
    pixels[161]=(253,235,208)
    pixels[160]=(253,235,208)
    pixels[159]=(253,235,208)
    pixels[158]=(253,235,208)
    pixels[157]=(253,235,208)
    pixels[156]=(133,193,233)
    pixels[155]=(133,193,233)
    pixels[154]=(133,193,233)
    pixels[168]=(133,193,233)
    pixels[169]=(133,193,233)
    pixels[170]=(133,193,233)
    pixels[171]=(133,193,233)
    pixels[172]=(133,193,233)
    pixels[173]=(133,193,233)
    pixels[174]=(133,193,233)
    pixels[175]=(133,193,233)
    pixels[176]=(133,193,233)
    pixels[177]=(133,193,233)
    pixels[178]=(133,193,233)
    pixels[179]=(133,193,233)
    pixels[180]=(133,193,233)
    pixels[181]=(133,193,233)
    pixels[195]=(133,193,233)
    pixels[194]=(133,193,233)
    pixels[193]=(133,193,233)
    pixels[192]=(133,193,233)
    pixels[191]=(133,193,233)
    pixels[190]=(133,193,233)
    pixels[189]=(133,193,233)
    pixels[188]=(133,193,233)
    pixels[187]=(133,193,233)
    pixels[186]=(133,193,233)
    pixels[185]=(133,193,233)
    pixels[184]=(133,193,233)
    pixels[183]=(133,193,233)
    pixels[182]=(133,193,233)
    pixels[196]=(133,193,233)
    pixels[197]=(133,193,233)
    pixels[198]=(133,193,233)
    pixels[199]=(133,193,233)
    pixels[200]=(133,193,233)
    pixels[201]=(133,193,233)
    pixels[202]=(133,193,233)
    pixels[203]=(133,193,233)
    pixels[204]=(133,193,233)
    pixels[205]=(133,193,233)
    pixels[206]=(133,193,233)
    pixels[207]=(133,193,233)
    pixels[208]=(133,193,233)
    pixels[209]=(133,193,233)


def leer(data):
    print('inicia proceso de pintado')
    data = data.split(',')
    indice = 0

    while indice < len(data):
        dataT = data[indice].strip()
        try:
            if dataT == 'a':
                pixels.fill((0, 0, 0))
            elif dataT == 'b':
                pixels.fill((255, 255, 255))
            elif dataT == 'c':
                left()
            elif dataT == 'd':
               rigth()    
            elif dataT == 'f':
               like()   
            elif dataT == 'g':
               block()      
            elif dataT == 'h':
               mario()     
            else:
                pixels[indice] = pintar_color(dataT)
        except Exception as e:
            print(f"Error: {e}")
        indice += 1

print("Inicia servicio")
s = BluetoothServer(leer)

while True:
    pass
