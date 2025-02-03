# continousservorobotichand
Robotic hands usually use servos with some kind of positional control such as potentiometers, resolvers, hall effect sensors, etc in order to know at all times the position of the fingers. This however brings a number of problems:
1 - Extra layer of complexity
2 - Increased costs
3 - Servo horns and positional sensors do not fit into the limited space robotic hands usually have
4 - Rotation limited to 180 degrees, which can lead to incomplete finger movements
5 - Lower finger force

An alternative approach is the use of linear servos.They offer:
1 - No limitation on the amount of movement fingers can have
2 - Higher finger forces
However, Thesetdo not have any rotational control, depending on external sensors such as the ones described. These brings us then to the original problems of higher costs, complexity, and lack of space.

We propose then a time-based approach to control. In this, each finger is previously tested several times with complete movements in and out and all the entire speed range of the servo. A switch is attached to each side of the tip of each finger, detecting when it reaches its limit. The program then records the time it took for that movement, the servo involved, the speed used, and the direction (in our out). This creates a database of movements which can bs used to, to some accuracy, predict the position of each finger whenever it makes a movement in or out at different speeds. 

To that end, another program reads from that database and keeps a record on the last movement of each finger. This last record is then read, thereby allowing the system to predict the last position of that finger, and move accordingly.

For our tests, we used the widely known 3D printed prosthetic hand available at Thingiverse (https://www.thingiverse.com/thing:1691704). This hand was meant to have only 2 servos, so we adapted it for 5 servos (see photos). A simpler solution could be to just use a variation of that which does offer 5 servos (https://www.thingiverse.com/thing:4807141). The I2 hand by Inmoov (https://inmoov.fr/hand-i2/) is a much better option, as it employs springs which provide much more precision and durability than the nylon paracord of the previous ones. In this project, we used the inexpensive DS04-NFC servos controlled by a PCA-9685 servo driver attached to a Jetson Orin AGX 64, but any regular Jetson should work.

Build a suitable robot hand and glue a TS-02 tactile switch in each side of the finger to be studied, as the pictures show. 
