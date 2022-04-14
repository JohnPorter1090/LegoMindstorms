"""
Gameplan:


1. Robot is always at a set angle
2. If detects offset, it gets back in line
3. Start in bottom right corner/ top left corner
4. Start by going forward
5. When color sensor detects other side of arena, continues to move forward for a few seconds, closes box and moves backwards to go home
6. Ultrasonic on back detects back wall and starts the goal dropoff sequence once certain distance-FIND THIS DISTANCE WITH TEST to see when turn 
    if whole robot + cap holder will stay in goal (check that against movement values of location to see if there is another robot)
7. Drop off sequence: Check floor for correct color, then turn 90 drive to far end and open box, back up and continue sequence of picking up caps
8. MAybe something cool at end like steal caps

9. at end bulldoze other teams goal

-Touch in front if robot detected goes to ultrasonic in back to get position
-Upon robot detected, do something (ram into maybe) and then leave using ultrasonic for position

"""