/* VOICE CODE PEDAL CONTROL
 *  relies on atom package "keyboard-scroll"
 *  Does actions with pedals
 */


#include <Keyboard.h>

//Input pins
#define PEDAL_PIN_1 6
#define PEDAL_PIN_2 7
#define PEDAL_PIN_3 4
#define PEDAL_PIN_4 5

//current states
int pedalState1 = HIGH;
int pedalState2 = HIGH;
int pedalState3 = HIGH;
int pedalState4 = HIGH;

unsigned long debounceDelay = 50;

void setup() {
  //set inputs
  pinMode(PEDAL_PIN_1, INPUT_PULLUP);
  pinMode(PEDAL_PIN_2, INPUT_PULLUP);
  pinMode(PEDAL_PIN_3, INPUT_PULLUP);
  pinMode(PEDAL_PIN_4, INPUT_PULLUP);

  Keyboard.begin();
}

void loop() {

  //refresh pedal states
  int pedalReading1 = digitalRead(PEDAL_PIN_1);
  int pedalReading2 = digitalRead(PEDAL_PIN_2);
  int pedalReading3 = digitalRead(PEDAL_PIN_3);
  int pedalReading4 = digitalRead(PEDAL_PIN_4);

  if(pedalReading1 == LOW) {
    Keyboard.press(KEY_LEFT_CTRL);
    Keyboard.press(KEY_LEFT_ALT);
    Keyboard.press(KEY_UP_ARROW);

    while(pedalReading1 == LOW) {
      delay(100);
    }
    Keyboard.releaseAll();
  }

}
