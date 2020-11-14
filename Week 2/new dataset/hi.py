import numpy as np
import statistics
import time
from astropy.coordinates import SkyCoord
from astropy import units as u
import pandas as pd

def crossmatch(cat1, cat2, max_dist):
    matches = []
    nomatches = []



    start = time.perf_counter()

    skycat1 = SkyCoord(cat1*u.degree, frame='icrs')
    skycat2 = SkyCoord(cat2*u.degree, frame='icrs')
    closest_ids, closest_dists, closest_dists3d = skycat1.match_to_catalog_sky(skycat2)
    closest_dists_deg = closest_dists.value

    for cat1idx in range(len(cat1)):
        if closest_dists_deg[cat1idx] > max_dist:
            nomatches.append(cat1idx)
        else:
            matches.append((cat1idx,closest_ids[cat1idx],closest_dists_deg[cat1idx]))

    #closest_dist.value returns an array of degrees
    #print("vals", closest_ids)
    #print("dists", closest_dists)
    #print("dists.val", closest_dists.value)

    return (matches, nomatches, time.perf_counter() - start)

#to create a text file
def conv(match):
    match_1 = matches
    f = open('neewfiles.txt', 'w')
    for t in match_1:
        line = ' '.join(str(x) for x in t)
        f.write(line + '\n')
    f.close()


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # The example in the question
    cat1 = np.genfromtxt('gmrt.csv', delimiter=',',skip_header=55,usecols=[5,6],max_rows=5434)
    cat2 = np.genfromtxt('opticalsdata.csv', delimiter=',',skip_header=1,usecols=[1,2],max_rows=252198)
    matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
    text = conv(matches)

    print('matches:', matches)
    print('unmatched:', no_matches)
    print('time taken:', time_taken)






