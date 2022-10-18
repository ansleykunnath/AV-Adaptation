#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on October 11, 2022, at 14:16
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
expName = 'Auditory'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\WALLACE LAB\\Documents\\PsychoPy\\Repetition & Novelty Detection\\Auditory.py',
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "auditory_repetition"
auditory_repetitionClock = core.Clock()
rep_50 = sound.Sound('500', secs=0.250, stereo=True, hamming=True,
    name='rep_50')
rep_50.setVolume(1.0)
rep_50_2 = sound.Sound('500', secs=0.25, stereo=True, hamming=True,
    name='rep_50_2')
rep_50_2.setVolume(1.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "auditory_alternation"
auditory_alternationClock = core.Clock()
alt_50 = sound.Sound('500', secs=0.250, stereo=True, hamming=True,
    name='alt_50')
alt_50.setVolume(1.0)
alt_1000 = sound.Sound('1000', secs=.25, stereo=True, hamming=True,
    name='alt_1000')
alt_1000.setVolume(1.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "auditory_attention"
auditory_attentionClock = core.Clock()
att_50 = sound.Sound('500', secs=0.25, stereo=True, hamming=True,
    name='att_50')
att_50.setVolume(1.0)
static = sound.Sound('C:/Users/WALLACE LAB/Documents/PsychoPy/tv-static-02.wav', secs=0.25, stereo=True, hamming=True,
    name='static')
static.setVolume(1.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

def aud_rep():
    # ------Prepare to start Routine "auditory_repetition"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    rep_50.setSound('500', secs=0.250, hamming=True)
    rep_50.setVolume(1.0, log=False)
    rep_50_2.setSound('500', secs=0.25, hamming=True)
    rep_50_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    auditory_repetitionComponents = [rep_50, rep_50_2]
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
        #pyautogui.press('2')
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
        #pyautogui.press('2')
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

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [text]
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0 -frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
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
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)

def aud_alt():
    # ------Prepare to start Routine "auditory_alternation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    alt_50.setSound('500', secs=0.250, hamming=True)
    alt_50.setVolume(1.0, log=False)
    alt_1000.setSound('1000', secs=.25, hamming=True)
    alt_1000.setVolume(1.0, log=False)
    # keep track of which components have finished
    auditory_alternationComponents = [alt_50, alt_1000]
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
        #pyautogui.press('3')
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
        #pyautogui.press('3')
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

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [text]
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0 -frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
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
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)


def aud_att():
    # ------Prepare to start Routine "auditory_attention"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    att_50.setSound('500', secs=0.25, hamming=True)
    att_50.setVolume(1.0, log=False)
    static.setSound('C:/Users/WALLACE LAB/Documents/PsychoPy/tv-static-02.wav', secs=0.25, hamming=True)
    static.setVolume(1.0, log=False)
    # keep track of which components have finished
    auditory_attentionComponents = [att_50, static]
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
        #pyautogui.press('4')
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
        #pyautogui.press('4')
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

    # ------Prepare to start Routine "break_2"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2Components = [text]
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 2.0 -frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
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
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)

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
