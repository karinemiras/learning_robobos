
"use strict";

let PlaySound = require('./PlaySound.js')
let SetSensorFrequency = require('./SetSensorFrequency.js')
let ResetWheels = require('./ResetWheels.js')
let SetEmotion = require('./SetEmotion.js')
let MovePanTilt = require('./MovePanTilt.js')
let SetLed = require('./SetLed.js')
let SetCamera = require('./SetCamera.js')
let Talk = require('./Talk.js')
let MoveWheels = require('./MoveWheels.js')

module.exports = {
  PlaySound: PlaySound,
  SetSensorFrequency: SetSensorFrequency,
  ResetWheels: ResetWheels,
  SetEmotion: SetEmotion,
  MovePanTilt: MovePanTilt,
  SetLed: SetLed,
  SetCamera: SetCamera,
  Talk: Talk,
  MoveWheels: MoveWheels,
};
