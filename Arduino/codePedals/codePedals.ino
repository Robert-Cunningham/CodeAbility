/* VOICE CODE PEDAL CONTROL
 *  relies on atom package "keyboard-scroll"
 *  Sends characters to Serial at 9600 baud on change in pedal state.
 *  
 *  States: 
 *   -- 0-(num_pedals-1): this index has been pressed
 *   -- num_pedals - 2*(num_pedals)-1 : (this index - num_pedals) has been released
 *   
 *   ex) 2 : pedal number two has been pressed
 *       4 : pedal zero has been released
 */

//Input pins
const int num_pedals = 4;
const int pedal_pins[] = {6, 7, 8, 9};

//previous states
bool lastPedalStates[] = {LOW, LOW, LOW, LOW};

void setup() {
  //set inputs
  for(pin:pedal_pins) {
    pinMode(pin, INPUT);
  }

  Serial.begin(9600);
}

void loop() {
  //Read all the buttons
  bool pedalStates[num_pedals];

  for(int i=0; i<num_pedals; i++) {
    pedalStates[i] = digitalRead(pedal_pins[i]);
  }
  
  for(int i=0; i<num_pedals; i++) {
    if (pedalStates[i] != lastPedalStates[i]) {
      if (pedalStates[i] == HIGH) {
        // if the current state is HIGH then the button went from off to on:
        Serial.println(i);
      } else {
        // if the current state is LOW then the button went from on to off:
        Serial.println(i+num_pedals);
      }
      // Delay a little bit to avoid bouncing
      delay(50);
    }
    // save the current state as the last state, for next time through the loop
    lastPedalStates[i] = pedalStates[i];
  }

}
