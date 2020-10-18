#!/usr/bin/env python

"""
    partybot.py - Version 0.2 2019-03-30
    
    A party robot to serve guests and entertainment.
    
"""

import rospy
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient
import sys
from subprocess import call
from geometry_msgs.msg import Twist
from math import radians
import os
from turtlebot_msgs.srv import SetFollowState

class Bot:
    def __init__(self, script_path):
        rospy.init_node('bot') #node name

        rospy.on_shutdown(self.cleanup)
        
        # Set the default TTS voice to use
        # self.voice = rospy.get_param("~voice", "voice_don_diphone")
        
        # Set the wave file path if used
        self.wavepath = rospy.get_param("~wavepath", script_path + "/../sounds")
        
        # Create the sound client object
        #self.soundhandle = SoundClient()
        self.soundhandle = SoundClient(blocking=True)
        
        # Wait a moment to let the client connect to the sound_play server
        rospy.sleep(1)
        
        # Make sure any lingering sound_play processes are stopped.
        self.soundhandle.stopAll()
        
        # Announce that we are ready for input
        self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        #rospy.sleep(1)
        # self.soundhandle.say("Ready")
        
        rospy.loginfo("Ready, waiting for commands...")
	self.soundhandle.say('Hello, I am Bot. What can I do for you?')
	#rospy.sleep(2)

        # Subscribe to the recognizer output and set the callback function
        rospy.Subscriber('/lm_data', String, self.talkback)



    def talkback(self, msg):
        # Print the recognized words on the screen
        #msg.data=msg.data.lower()
        rospy.loginfo(msg.data)
        
        # Speak the recognized words in the selected voice
        # self.soundhandle.say(msg.data, self.voice)
        # call('rosrun sound_play say.py "montreal"', shell=True)
        # rospy.sleep(1)

	if msg.data.find('INTRODUCE-YOURSELF-PLEASE')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	#rospy.sleep(1)
		self.soundhandle.say("I heard you want me to introduce myself. I am Bot. I am a robot to serve you and chat with you.")
		rospy.loginfo("I heard you want me to introduce myself. I am Bot. I am a robot to serve you and chat with you.")
		#rospy.sleep(10) 
	elif msg.data.find('COME-FOLLOW-ME')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	#rospy.sleep(1)
		self.soundhandle.say("OK. I am following you.")
		rospy.loginfo("OK. I am following you.")
		#rospy.sleep(10)
	elif msg.data.find('GOOD-MORNING-HOW-ARE-YOU-RIGHT-NOW')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	#rospy.sleep(1)
		self.soundhandle.say("I am fine. Thank you for your concern.")
		rospy.loginfo("I am fine. Thank you for your concern.")
		#rospy.sleep(10)
	elif msg.data.find('CAN-YOU-SPEAK')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	#rospy.sleep(1)
		self.soundhandle.say("Yes of couse. Dumb ass.")
		rospy.loginfo("Yes of couse. Dumb ass.")
		#rospy.sleep(10)
	elif msg.data.find('HELLO-WHERE-ARE-YOU')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	#rospy.sleep(1)
		self.soundhandle.say("I am right in front of you")
		rospy.loginfo("I am right in front of you.")
		#rospy.sleep(10)
	elif msg.data.find('WHAT-IS-THE-CURE-FOR-LONELINESS')>-1:
        	self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")
        	#rospy.sleep(1)
		self.soundhandle.say("What is the cure? let me play you a song")
		rospy.loginfo("What is the cure? let me play you a song")
		#rospy.sleep(3)
		self.soundhandle.playWave(self.wavepath + "/swtheme.wav", blocking=False)
		#rospy.sleep(10)	
	
	
	#else: rospy.sleep(3)
              #self.soundhandle.say("Sorry, I cannot hear you clearly. Please say again.")
              #rospy.sleep(100)

	# Uncomment to play one of the built-in sounds
        #rospy.sleep(2)
        #self.soundhandle.play(5)
        
        # Uncomment to play a wave file
        #rospy.sleep(2)
        #self.soundhandle.playWave(self.wavepath + "/R2D2a.wav")

	rospy.sleep(10)
	rospy.loginfo("Speak now")
	rospy.sleep(5)

    def cleanup(self):
        self.soundhandle.stopAll()
        rospy.loginfo("Shutting down bot node...")

if __name__=="__main__":
    try:
        Bot(sys.path[0])
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Bot node terminated.")
