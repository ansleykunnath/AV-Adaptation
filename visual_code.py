#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on October 04, 2022, at 14:38
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet

# introducing LSL pipeline that will send triggers to EEG system
info = StreamInfo(name='EventStream', type='Markers', channel_count=1, nominal_srate=1,
                    channel_format= 'int32', source_id='wallacelab')
outlet = StreamOutlet(info)

# testing trigger
outlet.push_sample([5])

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'Visual'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\WALLACE LAB\\Documents\\PsychoPy\\Repetition & Novelty Detection\\Visual.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "visual__repetition"
visual__repetitionClock = core.Clock()
visual_reps = visual.ImageStim(
    win=win,
    name='visual_reps', 
    image='C:/Users/Documents/circle_repetition.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
blank_circle = visual.ImageStim(
    win=win,
    name='blank_circle', 
    image='C:/Users/Documents/no_circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
visual_rep_2 = visual.ImageStim(
    win=win,
    name='visual_rep_2', 
    image='C:/Documents/circle_repetition.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
blank_space = visual.ImageStim(
    win=win,
    name='blank_space', 
    image='C:/Users/Documents/no_circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "visual_alternation"
visual_alternationClock = core.Clock()
visual_alternation_1 = visual.ImageStim(
    win=win,
    name='visual_alternation_1', 
    image='circle_repetition.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='C:/Users/Documents/no_circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='C:/Users/Documents/circle_alternation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
blank_space = visual.ImageStim(
    win=win,
    name='blank_space', 
    image='C:/Users/Documents/no_circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "visual_attention"
visual_attentionClock = core.Clock()
visual_attention_1 = visual.ImageStim(
    win=win,
    name='visual_attention_1', 
    image='circle_repetition.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='C:/Users/Documents/no_circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='C:/Users/Documents/circle_attention.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
blank_space = visual.ImageStim(
    win=win,
    name='blank_space', 
    image='C:/Users/Documents/no_circle.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

def vis_rep():
    # ------Prepare to start Routine "visual__repetition"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    visual__repetitionComponents = [visual_reps, blank_circle, visual_rep_2]
    for thisComponent in visual__repetitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    visual__repetitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    outlet.push_sample([1])
    # -------Run Routine "visual__repetition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = visual__repetitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=visual__repetitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *visual_reps* updates
        if visual_reps.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            visual_reps.frameNStart = frameN  # exact frame index
            visual_reps.tStart = t  # local t and not account for scr refresh
            visual_reps.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(visual_reps, 'tStartRefresh')  # time at next scr refresh
            visual_reps.setAutoDraw(True)
        if visual_reps.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > visual_reps.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                visual_reps.tStop = t  # not accounting for scr refresh
                visual_reps.frameNStop = frameN  # exact frame index
                win.timeOnFlip(visual_reps, 'tStopRefresh')  # time at next scr refresh
                visual_reps.setAutoDraw(False)
        
        # *blank_circle* updates
        if blank_circle.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            blank_circle.frameNStart = frameN  # exact frame index
            blank_circle.tStart = t  # local t and not account for scr refresh
            blank_circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_circle, 'tStartRefresh')  # time at next scr refresh
            blank_circle.setAutoDraw(True)
        if blank_circle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_circle.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_circle.tStop = t  # not accounting for scr refresh
                blank_circle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_circle, 'tStopRefresh')  # time at next scr refresh
                blank_circle.setAutoDraw(False)
        
        # *visual_rep_2* updates
        if visual_rep_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            visual_rep_2.frameNStart = frameN  # exact frame index
            visual_rep_2.tStart = t  # local t and not account for scr refresh
            visual_rep_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(visual_rep_2, 'tStartRefresh')  # time at next scr refresh
            visual_rep_2.setAutoDraw(True)
        if visual_rep_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > visual_rep_2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                visual_rep_2.tStop = t  # not accounting for scr refresh
                visual_rep_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(visual_rep_2, 'tStopRefresh')  # time at next scr refresh
                visual_rep_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visual__repetitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "visual__repetition"-------
    for thisComponent in visual__repetitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('visual_reps.started', visual_reps.tStartRefresh)
    thisExp.addData('visual_reps.stopped', visual_reps.tStopRefresh)
    thisExp.addData('blank_circle.started', blank_circle.tStartRefresh)
    thisExp.addData('blank_circle.stopped', blank_circle.tStopRefresh)
    thisExp.addData('visual_rep_2.started', visual_rep_2.tStartRefresh)
    thisExp.addData('visual_rep_2.stopped', visual_rep_2.tStopRefresh)

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [blank_space]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_space* updates
        if blank_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_space.frameNStart = frameN  # exact frame index
            blank_space.tStart = t  # local t and not account for scr refresh
            blank_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_space, 'tStartRefresh')  # time at next scr refresh
            blank_space.setAutoDraw(True)
        if blank_space.status == STARTED:
            rand_time = randint(2,3)
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_space.tStartRefresh + rand_time -frameTolerance:
                # keep track of stop time/frame for later
                blank_space.tStop = t  # not accounting for scr refresh
                blank_space.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_space, 'tStopRefresh')  # time at next scr refresh
                blank_space.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank_space.started', blank_space.tStartRefresh)
    thisExp.addData('blank_space.stopped', blank_space.tStopRefresh)

def vis_alt():
    # ------Prepare to start Routine "visual_alternation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    visual_alternationComponents = [visual_alternation_1, image, image_2]
    for thisComponent in visual_alternationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    visual_alternationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    outlet.push_sample([2])
    # -------Run Routine "visual_alternation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = visual_alternationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=visual_alternationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *visual_alternation_1* updates
        if visual_alternation_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            visual_alternation_1.frameNStart = frameN  # exact frame index
            visual_alternation_1.tStart = t  # local t and not account for scr refresh
            visual_alternation_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(visual_alternation_1, 'tStartRefresh')  # time at next scr refresh
            visual_alternation_1.setAutoDraw(True)
        if visual_alternation_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > visual_alternation_1.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                visual_alternation_1.tStop = t  # not accounting for scr refresh
                visual_alternation_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(visual_alternation_1, 'tStopRefresh')  # time at next scr refresh
                visual_alternation_1.setAutoDraw(False)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visual_alternationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "visual_alternation"-------
    for thisComponent in visual_alternationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('visual_alternation_1.started', visual_alternation_1.tStartRefresh)
    thisExp.addData('visual_alternation_1.stopped', visual_alternation_1.tStopRefresh)
    thisExp.addData('image.started', image.tStartRefresh)
    thisExp.addData('image.stopped', image.tStopRefresh)
    thisExp.addData('image_2.started', image_2.tStartRefresh)
    thisExp.addData('image_2.stopped', image_2.tStopRefresh)

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [blank_space]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_space* updates
        if blank_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_space.frameNStart = frameN  # exact frame index
            blank_space.tStart = t  # local t and not account for scr refresh
            blank_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_space, 'tStartRefresh')  # time at next scr refresh
            blank_space.setAutoDraw(True)
        if blank_space.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            rand_time = randint(2,3)
            if tThisFlipGlobal > blank_space.tStartRefresh + rand_time -frameTolerance:
                # keep track of stop time/frame for later
                blank_space.tStop = t  # not accounting for scr refresh
                blank_space.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_space, 'tStopRefresh')  # time at next scr refresh
                blank_space.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank_space.started', blank_space.tStartRefresh)
    thisExp.addData('blank_space.stopped', blank_space.tStopRefresh)

def vis_att():
    # ------Prepare to start Routine "visual_attention"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    visual_attentionComponents = [visual_attention_1, image_3, image_4]
    for thisComponent in visual_attentionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    visual_attentionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    outlet.push_sample([3])
    # -------Run Routine "visual_attention"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = visual_attentionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=visual_attentionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *visual_attention_1* updates
        if visual_attention_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            visual_attention_1.frameNStart = frameN  # exact frame index
            visual_attention_1.tStart = t  # local t and not account for scr refresh
            visual_attention_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(visual_attention_1, 'tStartRefresh')  # time at next scr refresh
            visual_attention_1.setAutoDraw(True)
        if visual_attention_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > visual_attention_1.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                visual_attention_1.tStop = t  # not accounting for scr refresh
                visual_attention_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(visual_attention_1, 'tStopRefresh')  # time at next scr refresh
                visual_attention_1.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        if image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_4.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visual_attentionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "visual_attention"-------
    for thisComponent in visual_attentionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('visual_attention_1.started', visual_attention_1.tStartRefresh)
    thisExp.addData('visual_attention_1.stopped', visual_attention_1.tStopRefresh)
    thisExp.addData('image_3.started', image_3.tStartRefresh)
    thisExp.addData('image_3.stopped', image_3.tStopRefresh)
    thisExp.addData('image_4.started', image_4.tStartRefresh)
    thisExp.addData('image_4.stopped', image_4.tStopRefresh)

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [blank_space]
    for thisComponent in break_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "break_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_space* updates
        if blank_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_space.frameNStart = frameN  # exact frame index
            blank_space.tStart = t  # local t and not account for scr refresh
            blank_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_space, 'tStartRefresh')  # time at next scr refresh
            blank_space.setAutoDraw(True)
        if blank_space.status == STARTED:
            rand_time = randint(2,3)
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_space.tStartRefresh + rand_time -frameTolerance:
                # keep track of stop time/frame for later
                blank_space.tStop = t  # not accounting for scr refresh
                blank_space.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank_space, 'tStopRefresh')  # time at next scr refresh
                blank_space.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('blank_space.started', blank_space.tStartRefresh)
    thisExp.addData('blank_space.stopped', blank_space.tStopRefresh)


n = 0
for i in range(200):
    n += 1
    if n== 5 or n == 10 or n == 18 or n == 25 or n == 33 or n == 41 or n == 49 or n == 58 or n == 64 or n == 71 or n == 77 or n == 88 or n == 98 or n == 106 or n == 116 or n == 126 or n == 135 or n == 143 or n == 155 or n == 168:
        vis_alt()
    elif n == 14 or n == 36 or n == 53 or n == 73 or n == 92 or n == 111 or n == 128 or n == 131 or n == 146 or n == 157:
        vis_att()
    else:
        vis_rep()


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
