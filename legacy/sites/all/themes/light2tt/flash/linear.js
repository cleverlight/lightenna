// v1.1
// Linear Event
// Javascript event handler for 'linear' Flash movie integration
// Copyright 2007 Lightenna Ltd

function linear_DoFSCommand(command, args) { 
	if (command == "linear_movieEnd") {
		linear_movieEnd(args);
	}
}

var linearID = null;
var linear_lastID = null;
function linear_movieEnd(name) {
	linear_getFlashObject();
	// name is the filename of the movie that's just finished
	// alert(name);

	var trigger = document.getElementById(name);
	// if a trigger (div#id) is setup on this name, swap in
	if (trigger != null) {
		if (linear_lastID != null) {
			var outgoing = document.getElementById(linear_lastID);
			if (outgoing != null) {
				outgoing.className = "summary summary-invisible";
			}
		}
		trigger.className = "summary summary-visible";
		linear_lastID = trigger.id;
		// automatically paused by flash after swap
		if (linearID != null) {			
			// setup callback to carry on playing
			linear_pause();
			linear_showControls();
			linear_timeoutSetup();
		}
	} else {
		linear_play();
	}
}

function linear_getFlashObject() {
	if (linearID == null)
		linearID = document.getElementById("linear");
}

/****** timeout functions ******/

var linear_timeoutID = null;
var linear_timeout_microInterval = 100;
var linear_timeout_macroInterval = 3000;
function linear_timeoutSetup() {
	// if we're already waiting, refresh
	if (linear_timeoutID)
		clearTimeout(linear_timeoutID);
	linear_timeoutID = setTimeout(linear_timeoutTarget, linear_timeout_microInterval);
}

var linear_timeout_pauseFirst = false;
var linear_timeout_timeRemaining = linear_timeout_macroInterval;
function linear_timeoutTarget() {
	if (linear_timeout_timeRemaining <= 0) {		
		// resume player
		if (linearID != null) {			
			linear_play();
		}
		// don't schedule next timeout (will happen on play complete)
		linear_hideControls();
	} else {
		if (linear_timeout_pauseFirst) {
			// only pause the first movie clip, leave the rest to play
			linear_timeout_pauseFirst = false;
		} else {
			linear_timeout_timeRemaining -= linear_timeout_microInterval;
			linear_updateProgressAuto();
			// schedule next micro timeout
			linear_timeoutID = setTimeout(linear_timeoutTarget, linear_timeout_microInterval);
		}
	}
}

function linear_timeoutClear() {
	if (linear_timeoutID) {
		linear_timeout_timeRemaining = linear_timeout_macroInterval;
		linear_updateProgressAuto();
		clearTimeout(linear_timeoutID);
	}
}

/****** progress functions ******/
var linear_progressBar_id = null;
var linear_progressBar_maxWidth = null;
function linear_setupProgress(name, wide) {
	linear_progressBar_id = document.getElementById(name);
	linear_progressBar_maxWidth = wide;
}

function linear_updateProgressAuto() {
	linear_updateProgress(linear_timeout_macroInterval - linear_timeout_timeRemaining, linear_timeout_macroInterval);
}

function linear_updateProgress(completed, total) {
	comfac = completed / total;
	if (linear_progressBar_id) {
		// set component width
		newwidth = linear_progressBar_maxWidth * comfac;
		linear_progressBar_id.style.width = newwidth + 'px';
		// alert(linear_progressBar_id.style.width);
	}
}

var linear_controls_play = null;
var linear_controls_pause = null;
function linear_findControls() {
	if (linear_controls_play == null)
		linear_controls_play = document.getElementById('linear_play');
	if (linear_controls_pause == null)
		linear_controls_pause = document.getElementById('linear_pause');
}

function linear_showControls() {
	linear_findControls();
	if (linear_controls_play != null)
		linear_controls_play.style.display = 'inline';
	if (linear_controls_pause != null)
		linear_controls_pause.style.display = 'inline';
}

function linear_hideControls() {
	linear_findControls();
	if (linear_controls_play != null)
		linear_controls_play.style.display = 'none';
	if (linear_controls_pause != null)
		linear_controls_pause.style.display = 'none';
}

/****** external action functions ******/

function linear_play() {
	linear_getFlashObject();
	// explicit user action, deschedule timeout
	linear_timeoutClear();
	if ((linearID != null) && (linearID.external_play)) {			
		linearID.external_play();
	}
	linear_hideControls();
}

function linear_pause() {
	linear_getFlashObject();
	// explicit user action, deschedule timeout
	linear_timeoutClear();
	if ((linearID != null) && (linearID.external_pause)) {			
		linearID.external_pause();
	}
}
