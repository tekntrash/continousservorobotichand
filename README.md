# Continuous Servo Robotic Hand

Robotic hands typically use servos with positional control mechanisms such as potentiometers, resolvers, or hall effect sensors to track finger positions. However, this approach introduces several challenges:

1. Increased complexity
2. Higher costs
3. Space constraints for servo horns and positional sensors
4. Limited rotation (usually up to 180 degrees), restricting finger movement
5. Reduced finger force

### Alternative Approach: Linear Servos
Linear servos offer distinct advantages:

1. Unlimited finger movement
2. Higher force output

However, they lack built-in rotational control and require external sensors, leading to the same issues of cost, complexity, and space constraints.

### Time-Based Control Method
We propose a time-based approach to finger position estimation. This method involves:

1. Calibrating each finger by moving it in and out multiple times at various speeds.
2. Attaching a tactile switch to the tip of each finger to detect movement limits.
3. Recording movement duration, servo channel, speed, and direction to build a database of motion profiles.
4. Using this database to estimate finger positions based on past movement data.

A secondary program continuously updates the last recorded position of each finger based on its most recent movement, allowing the system to predict positioning with reasonable accuracy.

### Hardware and Setup
For testing, we used the widely known 3D-printed prosthetic hand from Thingiverse:
- [https://www.thingiverse.com/thing:1691704](https://www.thingiverse.com/thing:1691704) (modified for 5 servos)
- Alternative: [https://www.thingiverse.com/thing:4807141](https://www.thingiverse.com/thing:4807141) (designed for 5 servos)
- Best option: [Inmoov I2 Hand](https://inmoov.fr/hand-i2/) (spring-based for improved precision and durability)

Our prototype uses inexpensive DS04-NFC servos controlled by a PCA-9685 servo driver, connected to a Jetson Orin AGX 64. However, any Jetson board should work.

### How to Use
1. Assemble a suitable robotic hand and attach a TS-02 tactile switch to both sides of each finger.
2. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```
3. Edit `measure.py` to specify the correct servo channel for the finger being trained.
4. Run the program:
   ```sh
   python measure.py
   ```
   - The script will move the finger back and forth at random speeds, recording movement times in a file (`servo(channel).txt`).
   - The longer the program runs, the more precise future movements will be.
5. Repeat the process for each finger.

### Future Improvements
- Enhancing position estimation accuracy with additional sensors or feedback mechanisms.
- Implementing machine learning for adaptive motion prediction.
- Exploring alternative servo and motor options for better performance.

This project aims to create a more cost-effective and flexible control system for robotic hands, removing the limitations of traditional position-controlled servos.

