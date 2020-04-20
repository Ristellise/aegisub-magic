import colorsys, itertools
N = 5
HSV_tuples = [(x*1.0/N, 0.8,1.0, ) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
paired = []
for pair in RGB_tuples:
    rgb = [round(pair[0]*255),round(pair[1]*255),round(pair[2]*255)]
    #print(f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    paired.append(f"&H{rgb[2]:02x}{rgb[1]:02x}{rgb[0]:02x}&")

timestep = 150
duration = 3000
t=0
transitionstring = ""
ic = itertools.cycle(paired)
while t < duration:
    transitionstring+=f"\\t({t},{t+timestep},\\1c{next(ic)})"
    t+=timestep
print(transitionstring)