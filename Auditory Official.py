#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on October 31, 2022, at 15:42
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

from pylsl import StreamInfo, StreamOutlet

import psychopy.iohub as io
from psychopy.hardware import keyboard

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
expName = 'Auditory Official'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\WALLACE LAB\\Documents\\PsychoPy\\Repetition & Novelty Detection\\Auditory Official.py',
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

# Initialize components for Routine "Instructions1"
Instructions1Clock = core.Clock()
instructions_1 = visual.TextStim(win=win, name='instructions_1',
    text="Welcome to the experiment!\n\nYou will hear sounds presented at different frequencies and varying patterns. Your job is to press '1' on the keyboard whenever you are presented with any sound.\n\n\n\nTry to answer as accurately as possible. If you're not sure, just make your best guess.\n\n\n(Press 3 to continue.)",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_instruction_A = keyboard.Keyboard()

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
end_instruction_b = keyboard.Keyboard()
InstructionsB = visual.TextStim(win=win, name='InstructionsB',
    text='\n\nSometimes two sounds of the same or different frequencies will be presented consecutively. Other times, a sound is played and followed by static.\n\nTry to stay focused, remain still, and look at the white cross in the middle of the screen when it appears.\n\n\n\n(Press 3 to continue.)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice_round"
practice_roundClock = core.Clock()
practice = visual.TextStim(win=win, name='practice',
    text="Now let's go through a practice round.\n\n\n\n\n(Press 3 to continue.)",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_key = keyboard.Keyboard()

# Initialize components for Routine "break1"
break1Clock = core.Clock()
grace_period = visual.TextStim(win=win, name='grace_period',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
test1 = sound.Sound('500', secs=0.25, stereo=True, hamming=True,
    name='test1')
test1.setVolume(0.1)
test2 = sound.Sound('1000', secs=0.25, stereo=True, hamming=True,
    name='test2')
test2.setVolume(0.05)

# Initialize components for Routine "correct_answer"
correct_answerClock = core.Clock()
practice_correct = visual.TextStim(win=win, name='practice_correct',
    text="\nThat time, two sounds were played, so you should have pressed '1' twice; once immediately after each sound.\n\n\nRemember that it's okay to mess up!",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "please_wait"
please_waitClock = core.Clock()
lets_start = visual.TextStim(win=win, name='lets_start',
    text='\n\n\n\n\n\n\n\n\nPlease wait.\n\n\n\n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_start = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
white_cross = visual.ImageStim(
    win=win,
    name='white_cross', 
    image='C:/Users/Documents/Fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "auditory_repetition"
auditory_repetitionClock = core.Clock()
rep_50 = sound.Sound('500', secs=0.250, stereo=True, hamming=True,
    name='rep_50')
rep_50.setVolume(0.1)
rep_50_2 = sound.Sound('500', secs=0.25, stereo=True, hamming=True,
    name='rep_50_2')
rep_50_2.setVolume(0.1)
response_rep = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
white_cross = visual.ImageStim(
    win=win,
    name='white_cross', 
    image='C:/Users/Documents/Fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "auditory_alternation"
auditory_alternationClock = core.Clock()
alt_50 = sound.Sound('500', secs=0.250, stereo=True, hamming=True,
    name='alt_50')
alt_50.setVolume(0.1)
alt_1000 = sound.Sound('1000', secs=.25, stereo=True, hamming=True,
    name='alt_1000')
alt_1000.setVolume(0.05)
response_alt = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
white_cross = visual.ImageStim(
    win=win,
    name='white_cross', 
    image='C:/Users/Documents/Fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "auditory_attention"
auditory_attentionClock = core.Clock()
att_50 = sound.Sound('500', secs=0.25, stereo=True, hamming=True,
    name='att_50')
att_50.setVolume(0.1)
static = sound.Sound('C:/Users/Documents/tv-static-02.wav', secs=0.25, stereo=True, hamming=True,
    name='static')
static.setVolume(0.08)
response_att = keyboard.Keyboard()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
white_cross = visual.ImageStim(
    win=win,
    name='white_cross', 
    image='C:/Users/Documents/Fixation.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions1"-------
continueRoutine = True
# update component parameters for each repeat
end_instruction_A.keys = []
end_instruction_A.rt = []
_end_instruction_A_allKeys = []
# keep track of which components have finished
Instructions1Components = [instructions_1, end_instruction_A]
for thisComponent in Instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions1"-------
while continueRoutine:
    # get current time
    t = Instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_1* updates
    if instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_1.frameNStart = frameN  # exact frame index
        instructions_1.tStart = t  # local t and not account for scr refresh
        instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_1, 'tStartRefresh')  # time at next scr refresh
        instructions_1.setAutoDraw(True)
    if instructions_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_1.tStartRefresh + end_instruction_A.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            instructions_1.tStop = t  # not accounting for scr refresh
            instructions_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions_1, 'tStopRefresh')  # time at next scr refresh
            instructions_1.setAutoDraw(False)
    
    # *end_instruction_A* updates
    waitOnFlip = False
    if end_instruction_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_instruction_A.frameNStart = frameN  # exact frame index
        end_instruction_A.tStart = t  # local t and not account for scr refresh
        end_instruction_A.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_instruction_A, 'tStartRefresh')  # time at next scr refresh
        end_instruction_A.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_instruction_A.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_instruction_A.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_instruction_A.status == STARTED and not waitOnFlip:
        theseKeys = end_instruction_A.getKeys(keyList=['3'], waitRelease=False)
        _end_instruction_A_allKeys.extend(theseKeys)
        if len(_end_instruction_A_allKeys):
            end_instruction_A.keys = _end_instruction_A_allKeys[-1].name  # just the last key pressed
            end_instruction_A.rt = _end_instruction_A_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions1"-------
for thisComponent in Instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_1.started', instructions_1.tStartRefresh)
thisExp.addData('instructions_1.stopped', instructions_1.tStopRefresh)
# check responses
if end_instruction_A.keys in ['', [], None]:  # No response was made
    end_instruction_A.keys = None
thisExp.addData('end_instruction_A.keys',end_instruction_A.keys)
if end_instruction_A.keys != None:  # we had a response
    thisExp.addData('end_instruction_A.rt', end_instruction_A.rt)
thisExp.addData('end_instruction_A.started', end_instruction_A.tStartRefresh)
thisExp.addData('end_instruction_A.stopped', end_instruction_A.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions2"-------
continueRoutine = True
# update component parameters for each repeat
end_instruction_b.keys = []
end_instruction_b.rt = []
_end_instruction_b_allKeys = []
# keep track of which components have finished
Instructions2Components = [end_instruction_b, InstructionsB]
for thisComponent in Instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_instruction_b* updates
    waitOnFlip = False
    if end_instruction_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_instruction_b.frameNStart = frameN  # exact frame index
        end_instruction_b.tStart = t  # local t and not account for scr refresh
        end_instruction_b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_instruction_b, 'tStartRefresh')  # time at next scr refresh
        end_instruction_b.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_instruction_b.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_instruction_b.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_instruction_b.status == STARTED and not waitOnFlip:
        theseKeys = end_instruction_b.getKeys(keyList=['3'], waitRelease=False)
        _end_instruction_b_allKeys.extend(theseKeys)
        if len(_end_instruction_b_allKeys):
            end_instruction_b.keys = _end_instruction_b_allKeys[-1].name  # just the last key pressed
            end_instruction_b.rt = _end_instruction_b_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *InstructionsB* updates
    if InstructionsB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsB.frameNStart = frameN  # exact frame index
        InstructionsB.tStart = t  # local t and not account for scr refresh
        InstructionsB.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsB, 'tStartRefresh')  # time at next scr refresh
        InstructionsB.setAutoDraw(True)
    if InstructionsB.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > InstructionsB.tStartRefresh + end_instruction_b.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            InstructionsB.tStop = t  # not accounting for scr refresh
            InstructionsB.frameNStop = frameN  # exact frame index
            win.timeOnFlip(InstructionsB, 'tStopRefresh')  # time at next scr refresh
            InstructionsB.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instruction_b.keys in ['', [], None]:  # No response was made
    end_instruction_b.keys = None
thisExp.addData('end_instruction_b.keys',end_instruction_b.keys)
if end_instruction_b.keys != None:  # we had a response
    thisExp.addData('end_instruction_b.rt', end_instruction_b.rt)
thisExp.addData('end_instruction_b.started', end_instruction_b.tStartRefresh)
thisExp.addData('end_instruction_b.stopped', end_instruction_b.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('InstructionsB.started', InstructionsB.tStartRefresh)
thisExp.addData('InstructionsB.stopped', InstructionsB.tStopRefresh)
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_round"-------
continueRoutine = True
# update component parameters for each repeat
practice_key.keys = []
practice_key.rt = []
_practice_key_allKeys = []
# keep track of which components have finished
practice_roundComponents = [practice, practice_key]
for thisComponent in practice_roundComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_roundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_round"-------
while continueRoutine:
    # get current time
    t = practice_roundClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_roundClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice* updates
    if practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice.frameNStart = frameN  # exact frame index
        practice.tStart = t  # local t and not account for scr refresh
        practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice, 'tStartRefresh')  # time at next scr refresh
        practice.setAutoDraw(True)
    if practice.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice.tStartRefresh + practice_key.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            practice.tStop = t  # not accounting for scr refresh
            practice.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice, 'tStopRefresh')  # time at next scr refresh
            practice.setAutoDraw(False)
    
    # *practice_key* updates
    waitOnFlip = False
    if practice_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_key.frameNStart = frameN  # exact frame index
        practice_key.tStart = t  # local t and not account for scr refresh
        practice_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_key, 'tStartRefresh')  # time at next scr refresh
        practice_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practice_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practice_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_key.status == STARTED and not waitOnFlip:
        theseKeys = practice_key.getKeys(keyList=['3'], waitRelease=False)
        _practice_key_allKeys.extend(theseKeys)
        if len(_practice_key_allKeys):
            practice_key.keys = _practice_key_allKeys[-1].name  # just the last key pressed
            practice_key.rt = _practice_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_roundComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_round"-------
for thisComponent in practice_roundComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice.started', practice.tStartRefresh)
thisExp.addData('practice.stopped', practice.tStopRefresh)
# check responses
if practice_key.keys in ['', [], None]:  # No response was made
    practice_key.keys = None
thisExp.addData('practice_key.keys',practice_key.keys)
if practice_key.keys != None:  # we had a response
    thisExp.addData('practice_key.rt', practice_key.rt)
thisExp.addData('practice_key.started', practice_key.tStartRefresh)
thisExp.addData('practice_key.stopped', practice_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_round" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "break1"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
break1Components = [grace_period]
for thisComponent in break1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *grace_period* updates
    if grace_period.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        grace_period.frameNStart = frameN  # exact frame index
        grace_period.tStart = t  # local t and not account for scr refresh
        grace_period.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(grace_period, 'tStartRefresh')  # time at next scr refresh
        grace_period.setAutoDraw(True)
    if grace_period.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > grace_period.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            grace_period.tStop = t  # not accounting for scr refresh
            grace_period.frameNStop = frameN  # exact frame index
            win.timeOnFlip(grace_period, 'tStopRefresh')  # time at next scr refresh
            grace_period.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break1"-------
for thisComponent in break1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('grace_period.started', grace_period.tStartRefresh)
thisExp.addData('grace_period.stopped', grace_period.tStopRefresh)

# ------Prepare to start Routine "test_trial"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
test1.setSound('500', secs=0.25, hamming=True)
test1.setVolume(0.1, log=False)
test2.setSound('1000', secs=0.25, hamming=True)
test2.setVolume(0.05, log=False)
# keep track of which components have finished
test_trialComponents = [test1, test2]
for thisComponent in test_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = test_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop test1
    if test1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1.frameNStart = frameN  # exact frame index
        test1.tStart = t  # local t and not account for scr refresh
        test1.tStartRefresh = tThisFlipGlobal  # on global time
        test1.play(when=win)  # sync with win flip
    if test1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test1.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            test1.tStop = t  # not accounting for scr refresh
            test1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test1, 'tStopRefresh')  # time at next scr refresh
            test1.stop()
    # start/stop test2
    if test2.status == NOT_STARTED and t >= 0.75-frameTolerance:
        # keep track of start time/frame for later
        test2.frameNStart = frameN  # exact frame index
        test2.tStart = t  # local t and not account for scr refresh
        test2.tStartRefresh = tThisFlipGlobal  # on global time
        test2.play()  # start the sound (it finishes automatically)
    if test2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > test2.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            test2.tStop = t  # not accounting for scr refresh
            test2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(test2, 'tStopRefresh')  # time at next scr refresh
            test2.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_trial"-------
for thisComponent in test_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
test1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('test1.started', test1.tStartRefresh)
thisExp.addData('test1.stopped', test1.tStopRefresh)
test2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('test2.started', test2.tStart)
thisExp.addData('test2.stopped', test2.tStop)

# ------Prepare to start Routine "correct_answer"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
correct_answerComponents = [practice_correct]
for thisComponent in correct_answerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
correct_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "correct_answer"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = correct_answerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=correct_answerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_correct* updates
    if practice_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_correct.frameNStart = frameN  # exact frame index
        practice_correct.tStart = t  # local t and not account for scr refresh
        practice_correct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_correct, 'tStartRefresh')  # time at next scr refresh
        practice_correct.setAutoDraw(True)
    if practice_correct.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_correct.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            practice_correct.tStop = t  # not accounting for scr refresh
            practice_correct.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_correct, 'tStopRefresh')  # time at next scr refresh
            practice_correct.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in correct_answerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "correct_answer"-------
for thisComponent in correct_answerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_correct.started', practice_correct.tStartRefresh)
thisExp.addData('practice_correct.stopped', practice_correct.tStopRefresh)

# ------Prepare to start Routine "please_wait"-------
continueRoutine = True
# update component parameters for each repeat
end_start.keys = []
end_start.rt = []
_end_start_allKeys = []
# keep track of which components have finished
please_waitComponents = [lets_start, end_start]
for thisComponent in please_waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
please_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "please_wait"-------
while continueRoutine:
    # get current time
    t = please_waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=please_waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *lets_start* updates
    if lets_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        lets_start.frameNStart = frameN  # exact frame index
        lets_start.tStart = t  # local t and not account for scr refresh
        lets_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lets_start, 'tStartRefresh')  # time at next scr refresh
        lets_start.setAutoDraw(True)
    if lets_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lets_start.tStartRefresh + end_start.status==FINISHED-frameTolerance:
            # keep track of stop time/frame for later
            lets_start.tStop = t  # not accounting for scr refresh
            lets_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lets_start, 'tStopRefresh')  # time at next scr refresh
            lets_start.setAutoDraw(False)
    
    # *end_start* updates
    waitOnFlip = False
    if end_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_start.frameNStart = frameN  # exact frame index
        end_start.tStart = t  # local t and not account for scr refresh
        end_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_start, 'tStartRefresh')  # time at next scr refresh
        end_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_start.status == STARTED and not waitOnFlip:
        theseKeys = end_start.getKeys(keyList=['space'], waitRelease=False)
        _end_start_allKeys.extend(theseKeys)
        if len(_end_start_allKeys):
            end_start.keys = _end_start_allKeys[-1].name  # just the last key pressed
            end_start.rt = _end_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in please_waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "please_wait"-------
for thisComponent in please_waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('lets_start.started', lets_start.tStartRefresh)
thisExp.addData('lets_start.stopped', lets_start.tStopRefresh)
# check responses
if end_start.keys in ['', [], None]:  # No response was made
    end_start.keys = None
thisExp.addData('end_start.keys',end_start.keys)
if end_start.keys != None:  # we had a response
    thisExp.addData('end_start.rt', end_start.rt)
thisExp.addData('end_start.started', end_start.tStartRefresh)
thisExp.addData('end_start.stopped', end_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "please_wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "break_2"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
break_2Components = [white_cross]
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
    
    # *white_cross* updates
    if white_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        white_cross.frameNStart = frameN  # exact frame index
        white_cross.tStart = t  # local t and not account for scr refresh
        white_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(white_cross, 'tStartRefresh')  # time at next scr refresh
        white_cross.setAutoDraw(True)
    if white_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > white_cross.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            white_cross.tStop = t  # not accounting for scr refresh
            white_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(white_cross, 'tStopRefresh')  # time at next scr refresh
            white_cross.setAutoDraw(False)
    
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
thisExp.addData('white_cross.started', white_cross.tStartRefresh)
thisExp.addData('white_cross.stopped', white_cross.tStopRefresh)

def aud_rep():
    # ------Prepare to start Routine "auditory_repetition"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    rep_50.setSound('500', secs=0.250, hamming=True)
    rep_50.setVolume(0.1, log=False)
    rep_50_2.setSound('500', secs=0.25, hamming=True)
    rep_50_2.setVolume(0.1, log=False)
    response_rep.keys = []
    response_rep.rt = []
    _response_rep_allKeys = []
    # keep track of which components have finished
    auditory_repetitionComponents = [rep_50, rep_50_2, response_rep]
    for thisComponent in auditory_repetitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    auditory_repetitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    outlet.push_sample([1])
    # -------Run Routine "auditory_repetition"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = auditory_repetitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=auditory_repetitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop rep_50
        if rep_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rep_50.frameNStart = frameN  # exact frame index
            rep_50.tStart = t  # local t and not account for scr refresh
            rep_50.tStartRefresh = tThisFlipGlobal  # on global time
            rep_50.play(when=win)  # sync with win flip
        if rep_50.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rep_50.tStartRefresh + 0.250-frameTolerance:
                # keep track of stop time/frame for later
                rep_50.tStop = t  # not accounting for scr refresh
                rep_50.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rep_50, 'tStopRefresh')  # time at next scr refresh
                rep_50.stop()
        # start/stop rep_50_2
        if rep_50_2.status == NOT_STARTED and tThisFlip >= 0.750-frameTolerance:
            # keep track of start time/frame for later
            rep_50_2.frameNStart = frameN  # exact frame index
            rep_50_2.tStart = t  # local t and not account for scr refresh
            rep_50_2.tStartRefresh = tThisFlipGlobal  # on global time
            rep_50_2.play(when=win)  # sync with win flip
        if rep_50_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rep_50_2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                rep_50_2.tStop = t  # not accounting for scr refresh
                rep_50_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rep_50_2, 'tStopRefresh')  # time at next scr refresh
                rep_50_2.stop()
        
        # *response_rep* updates
        waitOnFlip = False
        if response_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_rep.frameNStart = frameN  # exact frame index
            response_rep.tStart = t  # local t and not account for scr refresh
            response_rep.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_rep, 'tStartRefresh')  # time at next scr refresh
            response_rep.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_rep.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_rep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_rep.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response_rep.tStop = t  # not accounting for scr refresh
                response_rep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response_rep, 'tStopRefresh')  # time at next scr refresh
                response_rep.status = FINISHED
        if response_rep.status == STARTED and not waitOnFlip:
            theseKeys = response_rep.getKeys(keyList=['1'], waitRelease=False)
            outlet.push_sample([4])
            _response_rep_allKeys.extend(theseKeys)
            if len(_response_rep_allKeys):
                response_rep.keys = _response_rep_allKeys[-1].name  # just the last key pressed
                response_rep.rt = _response_rep_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in auditory_repetitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "auditory_repetition"-------
    for thisComponent in auditory_repetitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    rep_50.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('rep_50.started', rep_50.tStartRefresh)
    thisExp.addData('rep_50.stopped', rep_50.tStopRefresh)
    rep_50_2.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('rep_50_2.started', rep_50_2.tStartRefresh)
    thisExp.addData('rep_50_2.stopped', rep_50_2.tStopRefresh)
    # check responses
    if response_rep.keys in ['', [], None]:  # No response was made
        response_rep.keys = None
    thisExp.addData('response_rep.keys',response_rep.keys)
    if response_rep.keys != None:  # we had a response
        thisExp.addData('response_rep.rt', response_rep.rt)
    thisExp.addData('response_rep.started', response_rep.tStartRefresh)
    thisExp.addData('response_rep.stopped', response_rep.tStopRefresh)
    thisExp.nextEntry()

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [white_cross]
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
        
        # *white_cross* updates
        if white_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_cross.frameNStart = frameN  # exact frame index
            white_cross.tStart = t  # local t and not account for scr refresh
            white_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_cross, 'tStartRefresh')  # time at next scr refresh
            white_cross.setAutoDraw(True)
        if white_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_cross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                white_cross.tStop = t  # not accounting for scr refresh
                white_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_cross, 'tStopRefresh')  # time at next scr refresh
                white_cross.setAutoDraw(False)
        
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
    thisExp.addData('white_cross.started', white_cross.tStartRefresh)
    thisExp.addData('white_cross.stopped', white_cross.tStopRefresh)
    
def aud_alt():
    # ------Prepare to start Routine "auditory_alternation"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    alt_50.setSound('500', secs=0.250, hamming=True)
    alt_50.setVolume(0.1, log=False)
    alt_1000.setSound('1000', secs=.25, hamming=True)
    alt_1000.setVolume(0.05, log=False)
    response_alt.keys = []
    response_alt.rt = []
    _response_alt_allKeys = []
    # keep track of which components have finished
    auditory_alternationComponents = [alt_50, alt_1000, response_alt]
    for thisComponent in auditory_alternationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    auditory_alternationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    outlet.push_sample([2])
    # -------Run Routine "auditory_alternation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = auditory_alternationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=auditory_alternationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop alt_50
        if alt_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alt_50.frameNStart = frameN  # exact frame index
            alt_50.tStart = t  # local t and not account for scr refresh
            alt_50.tStartRefresh = tThisFlipGlobal  # on global time
            alt_50.play(when=win)  # sync with win flip
        if alt_50.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alt_50.tStartRefresh + 0.250-frameTolerance:
                # keep track of stop time/frame for later
                alt_50.tStop = t  # not accounting for scr refresh
                alt_50.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alt_50, 'tStopRefresh')  # time at next scr refresh
                alt_50.stop()
        # start/stop alt_1000
        if alt_1000.status == NOT_STARTED and tThisFlip >= .750-frameTolerance:
            # keep track of start time/frame for later
            alt_1000.frameNStart = frameN  # exact frame index
            alt_1000.tStart = t  # local t and not account for scr refresh
            alt_1000.tStartRefresh = tThisFlipGlobal  # on global time
            alt_1000.play(when=win)  # sync with win flip
        if alt_1000.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alt_1000.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                alt_1000.tStop = t  # not accounting for scr refresh
                alt_1000.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alt_1000, 'tStopRefresh')  # time at next scr refresh
                alt_1000.stop()
        
        # *response_alt* updates
        waitOnFlip = False
        if response_alt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_alt.frameNStart = frameN  # exact frame index
            response_alt.tStart = t  # local t and not account for scr refresh
            response_alt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_alt, 'tStartRefresh')  # time at next scr refresh
            response_alt.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_alt.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_alt.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_alt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_alt.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response_alt.tStop = t  # not accounting for scr refresh
                response_alt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response_alt, 'tStopRefresh')  # time at next scr refresh
                response_alt.status = FINISHED
        if response_alt.status == STARTED and not waitOnFlip:
            theseKeys = response_alt.getKeys(keyList=['1'], waitRelease=False)
            outlet.push_sample([4])
            _response_alt_allKeys.extend(theseKeys)
            if len(_response_alt_allKeys):
                response_alt.keys = _response_alt_allKeys[-1].name  # just the last key pressed
                response_alt.rt = _response_alt_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in auditory_alternationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "auditory_alternation"-------
    for thisComponent in auditory_alternationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    alt_50.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('alt_50.started', alt_50.tStartRefresh)
    thisExp.addData('alt_50.stopped', alt_50.tStopRefresh)
    alt_1000.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('alt_1000.started', alt_1000.tStartRefresh)
    thisExp.addData('alt_1000.stopped', alt_1000.tStopRefresh)
    # check responses
    if response_alt.keys in ['', [], None]:  # No response was made
        response_alt.keys = None
    thisExp.addData('response_alt.keys',response_alt.keys)
    if response_alt.keys != None:  # we had a response
        thisExp.addData('response_alt.rt', response_alt.rt)
    thisExp.addData('response_alt.started', response_alt.tStartRefresh)
    thisExp.addData('response_alt.stopped', response_alt.tStopRefresh)
    thisExp.nextEntry()

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [white_cross]
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
        
        # *white_cross* updates
        if white_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_cross.frameNStart = frameN  # exact frame index
            white_cross.tStart = t  # local t and not account for scr refresh
            white_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_cross, 'tStartRefresh')  # time at next scr refresh
            white_cross.setAutoDraw(True)
        if white_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_cross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                white_cross.tStop = t  # not accounting for scr refresh
                white_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_cross, 'tStopRefresh')  # time at next scr refresh
                white_cross.setAutoDraw(False)
        
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
    thisExp.addData('white_cross.started', white_cross.tStartRefresh)
    thisExp.addData('white_cross.stopped', white_cross.tStopRefresh)

def aud_att():
    # ------Prepare to start Routine "auditory_attention"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    att_50.setSound('500', secs=0.25, hamming=True)
    att_50.setVolume(0.1, log=False)
    static.setSound('C:/Users/Documents/tv-static-02.wav', secs=0.25, hamming=True)
    static.setVolume(0.08, log=False)
    response_att.keys = []
    response_att.rt = []
    _response_att_allKeys = []
    # keep track of which components have finished
    auditory_attentionComponents = [att_50, static, response_att]
    for thisComponent in auditory_attentionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    auditory_attentionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    outlet.push_sample([3])
    # -------Run Routine "auditory_attention"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = auditory_attentionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=auditory_attentionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop att_50
        if att_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            att_50.frameNStart = frameN  # exact frame index
            att_50.tStart = t  # local t and not account for scr refresh
            att_50.tStartRefresh = tThisFlipGlobal  # on global time
            att_50.play(when=win)  # sync with win flip
        if att_50.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > att_50.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                att_50.tStop = t  # not accounting for scr refresh
                att_50.frameNStop = frameN  # exact frame index
                win.timeOnFlip(att_50, 'tStopRefresh')  # time at next scr refresh
                att_50.stop()
        # start/stop static
        if static.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            static.frameNStart = frameN  # exact frame index
            static.tStart = t  # local t and not account for scr refresh
            static.tStartRefresh = tThisFlipGlobal  # on global time
            static.play(when=win)  # sync with win flip
        if static.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > static.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                static.tStop = t  # not accounting for scr refresh
                static.frameNStop = frameN  # exact frame index
                win.timeOnFlip(static, 'tStopRefresh')  # time at next scr refresh
                static.stop()
        
        # *response_att* updates
        waitOnFlip = False
        if response_att.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_att.frameNStart = frameN  # exact frame index
            response_att.tStart = t  # local t and not account for scr refresh
            response_att.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_att, 'tStartRefresh')  # time at next scr refresh
            response_att.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_att.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_att.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_att.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response_att.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                response_att.tStop = t  # not accounting for scr refresh
                response_att.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response_att, 'tStopRefresh')  # time at next scr refresh
                response_att.status = FINISHED
        if response_att.status == STARTED and not waitOnFlip:
            theseKeys = response_att.getKeys(keyList=['1'], waitRelease=False)
            outlet.push_sample([4])
            _response_att_allKeys.extend(theseKeys)
            if len(_response_att_allKeys):
                response_att.keys = _response_att_allKeys[-1].name  # just the last key pressed
                response_att.rt = _response_att_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in auditory_attentionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "auditory_attention"-------
    for thisComponent in auditory_attentionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    att_50.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('att_50.started', att_50.tStartRefresh)
    thisExp.addData('att_50.stopped', att_50.tStopRefresh)
    static.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('static.started', static.tStartRefresh)
    thisExp.addData('static.stopped', static.tStopRefresh)
    # check responses
    if response_att.keys in ['', [], None]:  # No response was made
        response_att.keys = None
    thisExp.addData('response_att.keys',response_att.keys)
    if response_att.keys != None:  # we had a response
        thisExp.addData('response_att.rt', response_att.rt)
    thisExp.addData('response_att.started', response_att.tStartRefresh)
    thisExp.addData('response_att.stopped', response_att.tStopRefresh)
    thisExp.nextEntry()

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [white_cross]
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
        
        # *white_cross* updates
        if white_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            white_cross.frameNStart = frameN  # exact frame index
            white_cross.tStart = t  # local t and not account for scr refresh
            white_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(white_cross, 'tStartRefresh')  # time at next scr refresh
            white_cross.setAutoDraw(True)
        if white_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > white_cross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                white_cross.tStop = t  # not accounting for scr refresh
                white_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(white_cross, 'tStopRefresh')  # time at next scr refresh
                white_cross.setAutoDraw(False)
        
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
    thisExp.addData('white_cross.started', white_cross.tStartRefresh)
    thisExp.addData('white_cross.stopped', white_cross.tStopRefresh)
    
n = 0
for i in range(200):
    n += 1
    if n== 5 or n == 10 or n == 18 or n == 25 or n == 33 or n == 41 or n == 49 or n == 58 or n == 64 or n == 71 or n == 77 or n == 88 or n == 98 or n == 106 or n == 116 or n == 126 or n == 135 or n == 143 or n == 155 or n == 168:
        aud_alt()
    elif n == 14 or n == 36 or n == 53 or n == 73 or n == 92 or n == 111 or n == 128 or n == 131 or n == 146 or n == 157:
        aud_att()
    else:
        aud_rep()

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
