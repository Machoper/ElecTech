# ElecTech Voting System

--------------------------------

run docker-compose up to start the container. Then go to localhost:8000 to view the app.

--------------------------------
# ElecTech Technical Specification Report

## System can check in a voter that is supposed to vote at this polling place and refuses a voter that should not vote here.
This system has an active precinct-ID variable.  During check-in, if the registered user attempting to check-in does not have a matching precinct-ID, then a pop-up window is displayed informing the voter that they are at the wrong polling location.

They are denied check-in services and are unable to move to the next voting stage.

## System allows a voter to successfully record their vote on various election items.
Although this seems like a trivial requirement for a voting system, it is important to note that we do accomplish this core task.

After a user opens their ballot, selects an option, confirms their selection and submits their vote, the system updates that option in the database with a +1 to the vote column.

## System creates a physical, traceable way to perform a manual recount.
After a vote is cast, that vote information (question and option) is sent to a printer queue.  A computer with a thermal printer listens for changes in the queue and prints the vote and clears it from the queue.  This provides a physical, traceable way to perform a manual recount.


## System provides an easy-to-use, functional API for getting information about vote counts.  Documentation for the API is clear and well-written.
From the home page of the voting system, the user is able to access an api documentation screen by clicking a button that says API.  On this page, it lists all the API calls that a user is able to use for any data gathering needed, along with the data that is required for input and said data types.  It also lists how to use it, along with the way the data is presented once a user makes an API call.
System is robust enough to handle misuse cases (i.e. trying to vote for more than one candidate, print more than one receipt, etc.)
We have tested multiple misuses cases.  A user is unable to vote for more than one candidate.  A user also will not be able to access a ballot that they have already voted for.  More than one receipt cannot be printed because when the computer printing makes a call into the database,  the database will be cleared once all of the votes are printed.

## System is considered "easy to use" by the course staff.
From the beginning of the voting process to the end of the voting process, the user is given a linear experience.  All the user has to do is check in, then login.  Afterwards, they are presented with a ballot to select, and after selecting a ballot and voting using said ballot, they are sent back to the login screen.  This is the end of the process of voting, and they may leave the booth.
Overall system design and user experience is well-thought-out and looks professional.
Since our system is very linear, it is very easy for someone to vote.  All the buttons are very large and readable, so it is clear what a user is voting for when they click on their candidates.  It is also very clear which ballot is available, so a user is able to easily click on what ballot they are voting for.

