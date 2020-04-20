beatpts = [340,670,1000,1340,1670,2010,2390,2720,3050,3390,3720,4050,4429,4763]

tin = 100
tout = 100

def fmt_t(beatpt,in_t,out_t):
    fmt = "\\t({},{},{})"
    comp_in = fmt.format(beatpt-in_t,beatpt,"\\fscx101\\fscy101")
    comp_out = fmt.format(beatpt,beatpt+out_t,"\\fscx100\\fscy100")
    return ("".join([comp_in,comp_out]))

print("".join([fmt_t(beat,tin,tout) for beat in beatpts]))
