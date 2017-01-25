#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import rospy
from std_msgs.msg import Int32
import numpy as np
import random

n=0
l=0
width=25
width1=25

cell=np.zeros((width,width1),"int")
cell1=np.zeros((width,width1),"int")
for i in range(width):
	for j in range (width1):
		cell[i,j]=0
#random.randint(0,1)

def cb(message):
	l=0
	for i in range(width):
        	for j in range (width1):
			if i==0:
				if j==0:
					if cell[width-1,width1-1]==1:
						l=l+1
					if cell[0,width1-1]==1:
                                                l=l+1
                                        if cell[1,0]==1:
                                                l=l+1
                                        if cell[width-1,0]==1:
                                                l=l+1
                                        if cell[1,0]==1:
                                                l=l+1
                                        if cell[width-1,1]==1:
                                                l=l+1
                                        if cell[0,1]==1:
                                                l=l+1
                                        if cell[1,1]==1:
                                                l=l+1

                        if i==0:
                                if j==width1-1:
                                        if cell[width-1,width1-2]==1:
                                                l=l+1
                                        if cell[0,width1-2]==1:
                                                l=l+1
                                        if cell[1,width1-2]==1:
                                                l=l+1
                                        if cell[width-1,width1-1]==1:
                                                l=l+1
                                        if cell[1,width1-1]==1:
                                                l=l+1
                                        if cell[width-1,0]==1:
                                                l=l+1
                                        if cell[0,0]==1:
                                                l=l+1
                                        if cell[1,0]==1:
                                                l=l+1
			if i==width-1:

                                if j==0:
                                        if cell[width-2,width1-1]==1:
                                                l=l+1
                                        if cell[width-1,width1-1]==1:
                                                l=l+1
                                        if cell[0,width1-1]==1:
                                                l=l+1
                                        if cell[width-2,0]==1:
                                                l=l+1
                                        if cell[0,0]==1:
                                                l=l+1
                                        if cell[width-2,1]==1:
                                                l=l+1
                                        if cell[width-1,1]==1:
                                                l=l+1
                                        if cell[0,1]==1:
                                                l=l+1
                        if i==width-1:

                                if j==width1-1:
                                        if cell[width-2,width1-2]==1:
                                                l=l+1
                                        if cell[width-1,width1-2]==1:
                                                l=l+1
                                        if cell[0,width1-2]==1:
                                                l=l+1
                                        if cell[width-2,width1-1]==1:
                                                l=l+1
                                        if cell[0,width1-1]==1:
                                                l=l+1
                                        if cell[width-2,0]==1:
                                                l=l+1
                                        if cell[width-1,0]==1:
                                                l=l+1
                                        if cell[0,0]==1:
                                                l=l+1

                        if i==0:
				if  0 < j < width1-1:
					if cell[width-1,j-1]==1:
						l=l+1
                               		if cell[width-1,j]==1:
                                       		 l=l+1
                               		if cell[width-1,j+1]==1:
                              	 	        l=l+1
                               	 	if cell[0,j-1]==1:
                                        	l=l+1
                                	if cell[0,j+1]==1:
                                        	l=l+1
                                	if cell[1,j-1]==1:
                                        	l=l+1
                                	if cell[1,j]==1:
                                        	l=l+1
                                	if cell[1,j+1]==1:
                                        	l=l+1
                        if i==width-1:
				if  0 < j <  width1-1:
                                	if cell[width-2,j-1]==1:
                                        	l=l+1
                                	if cell[width-2,j]==1:
                                        	l=l+1
                               		if cell[width-2,j+1]==1:
                                        	l=l+1
                                	if cell[width-1,j-1]==1:
                                        	l=l+1
                                	if cell[width-1,j+1]==1:
                                        	l=l+1
                                	if cell[0,j-1]==1:
                                        	l=l+1
                                	if cell[0,j]==1:
                                        	l=l+1
                                	if cell[0,j+1]==1:
                                        	l=l+1
                        if j==0:
				if 0 < i < width-1:
                                	if cell[i-1,width1-1]==1:
                                        	l=l+1
                                	if cell[i-1,0]==1:
                                        	l=l+1
                                	if cell[i-1,1]==1:
                                        	l=l+1
                                	if cell[i,width1-1]==1:
                                        	l=l+1
                                	if cell[i,1]==1:
                                        	l=l+1
                                	if cell[i+1,width1-1]==1:
                                        	l=l+1
                                	if cell[i+1,0]==1:
                                        	l=l+1
                                	if cell[i+1,1]==1:
                                        	l=l+1
                        if j==width1-1:
				if 0 < i < width-1:
                                	if cell[i-1,width1-2]==1:
                                        	l=l+1
                                	if cell[i-1,width1-1]==1:
                                        	l=l+1
                                	if cell[i-1,0]==1:
                                        	l=l+1
                                	if cell[i,width1-2]==1:
                                        	l=l+1
                                	if cell[i,0]==1:
                                        	l=l+1
                                	if cell[i+1,width1-2]==1:
                                        	l=l+1
                                	if cell[i+1,width1-1]==1:
                                        	l=l+1
                                	if cell[i+1,0]==1:
                                        	l=l+1
                        if 0 < i < width-1:
				if 0 < j <  width1-1:
                                	if cell[i-1,j-1]==1:
                                        	l=l+1
                                	if cell[i,j-1]==1:
                                        	l=l+1
                                	if cell[i+1,j-1]==1:
                                        	l=l+1
					if cell[i-1,j]==1:
                                        	l=l+1
                                	if cell[i+1,j]==1:
                                        	l=l+1
                                	if cell[i-1,j+1]==1:
                                        	l=l+1
                                	if cell[i,j+1]==1:
                                        	l=l+1
                                	if cell[i+1,j+1]==1:
                                        	l=l+1

			if cell[i,j]==0:
				if l==3:
					cell1[i,j]=1

			if cell[i,j]==1:
				if l==2 or l==3:
					cell1[i,j]=1
				if l<=1:
					cell1[i,j]=0
				if l>=4:
					cell1[i,j]=0

			l=0
			random.seed(message.data)
			for o in range(10,15):
        			for p in range (10,15):
               				cell[o,p]=random.randint(0,1)

	m=""
	os.system("clear")
	print "Seed値 "+str(message.data)
	for i in range(width):
		for j in range (width1):
			if 9  < i < 15 and 9  < j < 15:
				if cell[i,j]==0:
                                        m=m+u"○"
                                else:
                                        m=m+u"●"
			else:
				if cell[i,j]==0:
					m=m+u"□"
				else:
					m=m+u"■"
		m=m+"\n"
	print m

	for i in range(width):
                for j in range (width1):
			cell[i,j]=cell1[i,j]

if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up', Int32, cb)
	pub = rospy.Publisher('twice', Int32, queue_size=1)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(n)
		rate.sleep()






