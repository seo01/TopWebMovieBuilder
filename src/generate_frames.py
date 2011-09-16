#!/usr/bin/python

"""
Takes in a directory containing images and outputs a bash script which further generates the frames
"""

import os
CLEANIMGS = '../data/cleanimgs2'
FRAMES = '../data/frames'
SCRIPTS = '../data/scripts'
HEIGHT = 600
WIDTH = 800


def main():
    listing = os.listdir(CLEANIMGS)
    files = []
    for infile in listing:
        files.append(infile)
    
    files = sorted(files)
    current_frame = 1
    current_image = 0
    print "#!/bin/bash"
    current_frame, current_image = full_screen_frames(files,current_frame,current_image,cycles=20)
    current_frame, current_image = full_screen_frames(files,current_frame,current_image,cycles=40,frames_per_image=6)
    current_frame, current_image = corners_half_second_main_quarter_frames(files,current_frame,current_image)
    current_frame, current_image = opp_corners_half_second_main_quarter_frames(files,current_frame,current_image)
    current_frame, current_image = quarter_frames(files,current_frame,current_image)
    current_frame, current_image = quarter_frames(files,current_frame,current_image,cycles=80, inner_cycles=1)
    current_frame, current_image = corners_half_second_main_quarter_frames(files,current_frame,current_image,frames_per_image=3,inner_cycles=2,cycles=40)
    current_frame, current_image = opp_corners_half_second_main_quarter_frames(files,current_frame,current_image,frames_per_image=3,inner_cycles=2,cycles=40)
    current_frame, current_image = corners_frames(files,current_frame,current_image)
    current_frame, current_image = corners_frames(files,current_frame,current_image,frames_per_image=3,inner_cycles=2,cycles=80)
    current_frame, current_image = grid_frames(files,current_frame,current_image)
    
def full_screen_frames(files,current_frame,current_image,frames_per_image=12,cycles=40):
    for j in range(cycles):
        for i in range(frames_per_image):
            print "cp %s/%s %s/%06d.jpg" % (CLEANIMGS,files[current_image],FRAMES,current_frame)
            current_frame += 1
        current_image += 1
    return current_frame, current_image

def corners_half_second_main_quarter_frames(files,current_frame,current_image,frames_per_image=6,inner_cycles=2,cycles=20):
    for k in range(cycles):
        bottom_left = files[current_image]
        current_image+=1
        top_right = files[current_image]
        current_image+=1
        for j in range(inner_cycles):
            main = files[current_image]
            current_image+=1
            for i in range(frames_per_image):
                print "./timeout3.sh convert -size %sx%s %s/%s -page +0+%s \\( -resize %sx%s %s/%s \\) -page +%s+0 \\( -resize %sx%s %s/%s \) -background white -flatten %s/%06d.jpg"% \
                    (WIDTH,HEIGHT,CLEANIMGS,main,2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_left,2*WIDTH,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_right,FRAMES,current_frame)
                current_frame += 1
    return current_frame, current_image

def opp_corners_half_second_main_quarter_frames(files,current_frame,current_image,frames_per_image=6,inner_cycles=2,cycles=20):
    for k in range(cycles):
        bottom_left = files[current_image]
        current_image+=1
        top_right = files[current_image]
        current_image+=1
        for j in range(inner_cycles):
            main = files[current_image]
            current_image+=1
            for i in range(frames_per_image):
                print "./timeout3.sh convert -size %sx%s %s/%s -page +0+0 \\( -resize %sx%s %s/%s \\) -page +%s+%s \\( -resize %sx%s %s/%s \) -background white -flatten %s/%06d.jpg"% \
                    (WIDTH,HEIGHT,CLEANIMGS,main,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_left,2*WIDTH,2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_right,FRAMES,current_frame)
                current_frame += 1
    return current_frame, current_image

def corners_frames(files,current_frame,current_image,frames_per_image=6,inner_cycles=2,cycles=40):
    for k in range(cycles):
        bottom_left = files[current_image]
        current_image+=1
        top_right = files[current_image]
        current_image+=1
        top_left = files[current_image]
        current_image+=1
        bottom_right = files[current_image]
        current_image+=1
        for j in range(inner_cycles):
            main = files[current_image]
            current_image+=1
            for i in range(frames_per_image):
                print "./timeout3.sh convert -size %sx%s %s/%s -page +0+0 \\( -resize %sx%s %s/%s \\) -page +%s+%s \\( -resize %sx%s %s/%s \) -page +0+%s \\( -resize %sx%s %s/%s \\) -page +%s+0 \\( -resize %sx%s %s/%s \) -background white -flatten %s/%06d.jpg"% \
                    (WIDTH,HEIGHT,CLEANIMGS,main,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_left,2*WIDTH,2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_right,2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_left,2*WIDTH,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_right,FRAMES,current_frame)
                current_frame += 1
    return current_frame, current_image

def quarter_frames(files,current_frame,current_image,frames_per_image=6,cycles=40, inner_cycles=2):
    for k in range(cycles):
        top_left = files[current_image]
        current_image+=1
        bottom_right = files[current_image]
        current_image+=1
        for j in range(inner_cycles):
            bottom_left = files[current_image]
            current_image+=1
            top_right = files[current_image]
            current_image+=1
            for i in range(frames_per_image):
                print "./timeout3.sh convert -size %sx%s -page +0+0 \\( -resize %sx%s %s/%s \\) -page +0+%s \\( -resize %sx%s %s/%s \\) -page +%s+0 \\( -resize %sx%s %s/%s \) -page +%s+%s \\( -resize %sx%s %s/%s \) -background white -mosaic %s/%06d.jpg"% \
                    (WIDTH,HEIGHT,0.5*WIDTH,0.5*HEIGHT,CLEANIMGS,top_left,HEIGHT,0.5*WIDTH,0.5*HEIGHT,CLEANIMGS,bottom_left,WIDTH,0.5*WIDTH,0.5*HEIGHT,CLEANIMGS,top_right,WIDTH,HEIGHT,0.5*WIDTH,0.5*HEIGHT,CLEANIMGS,bottom_right,FRAMES,current_frame)
                current_frame += 1
    return current_frame, current_image

def grid_frames(files,current_frame,current_image,cycles=160,frames_per_image=3):
    for k in range(cycles):
        bottom_left = files[current_image]
        current_image+=1
        top_right = files[current_image]
        current_image+=1
        top_left = files[current_image]
        current_image+=1
        bottom_right = files[current_image]
        current_image+=1
        mid_left = files[current_image]
        current_image+=1
        mid_right = files[current_image]
        current_image+=1
        top_mid = files[current_image]
        current_image+=1
        bottom_mid = files[current_image]
        current_image+=1
        mid = files[current_image]
        current_image+=1
        for j in range(frames_per_image):
            print \
                ("./timeout3.sh convert -size %sx%s "+\
                "-page +0+0 \\( -resize %sx%s %s/%s \\) "+\
                "-page +%s+%s \\( -resize %sx%s %s/%s \) "+ \
                "-page +0+%s \\( -resize %sx%s %s/%s \\) "+ \
                "-page +%s+0 \\( -resize %sx%s %s/%s \) " + \
                "-page +%s+0 \\( -resize %sx%s %s/%s \) " + \
                "-page +0+%s \\( -resize %sx%s %s/%s \\) "+ \
                "-page +%s+%s \\( -resize %sx%s %s/%s \\) "+ \
                "-page +%s+%s \\( -resize %sx%s %s/%s \\) "+ \
                "-page +%s+%s \\( -resize %sx%s %s/%s \\) "+ \
                "-background white -mosaic %s/%06d.jpg")% \
                ( WIDTH,HEIGHT, \
                0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_left, \
                2*WIDTH,2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_right, \
                2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_left, \
                2*WIDTH,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_right, \
                WIDTH,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,top_mid, \
                HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,mid_left, \
                WIDTH,HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,mid, \
                WIDTH,2*HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,bottom_mid, \
                2*WIDTH,HEIGHT,0.33*WIDTH,0.33*HEIGHT,CLEANIMGS,mid_right, \
                FRAMES,current_frame)
            current_frame += 1
    return current_frame, current_image
if __name__ == '__main__':
    main()
