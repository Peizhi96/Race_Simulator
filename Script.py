#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Structures section
struct Race {
  int numberOfLaps;
  int currentLap;
  char firstPlaceDriverName[40];
  char firstPlaceRaceCarColor[40];
};
// Print functions section
struct RaceCar {
  char driverName[52];
  char raceCarColor[40];
  int totalLapTime;
};

void printIntro() {
  printf("Welcome to our main event digital race fans!\n");
  printf("I hope everybody has their snacks because we are about to begin!\n");
}

void printCountDown() {
  printf("Racers Ready! In...\n");
  for (int i = 5; i > 0; i--) {
    printf("%d", i);
  }
  printf("Race!");
}

void printFirstPlaceAfterLap(struct Race race) {
  printf("After lap number %d\n", race.numberOfLaps);
  printf("First Place Is: %s in the %s race car!", race.firstPlaceDriverName, race.firstPlaceRaceCarColor);
}

void printCongratulation(struct RaceCar raceCar) {
  printf("Let's all congratulate %s in the %s race car for an amazing performance.\n", raceCar.driverName, raceCar.raceCarColor);
  printf("It truly was a great race and everybody have a goodnight!\n");
}

// Logic functions section
int calculateTimeToCompleteLap() {
  int speed;
  int acceleration;
  int nerves;
  int sum;
  srand(time(0));
  speed = rand() % 3 + 1;
  acceleration = rand() % 3 + 1;
  nerves = rand() % 3 + 1;
  sum = speed + acceleration + nerves;
  return sum;
}

void updateRaceCar(struct RaceCar* raceCar) {
  int laptime = calculateTimeToCompleteLap();
  raceCar->totalLapTime += laptime;
}

void updateFirstPlace(struct Race* race, struct RaceCar* raceCar1, struct RaceCar* raceCar2) {
      if (raceCar1->totalLapTime <= raceCar2->totalLapTime) {
        strcpy(race->firstPlaceDriverName, raceCar1->driverName);
        strcpy(race->firstPlaceRaceCarColor, raceCar1->raceCarColor);
    } else {
        strcpy(race->firstPlaceDriverName, raceCar2->driverName);
        strcpy(race->firstPlaceRaceCarColor, raceCar2->raceCarColor);
    }
}


void startRace(struct RaceCar* raceCar1, struct RaceCar* raceCar2) {
    struct Race race;
    race.numberOfLaps = 5;
    race.currentLap = 1;
    race.firstPlaceDriverName[0] = '\0';
    race.firstPlaceRaceCarColor[0] = '\0';

    for (int i = 0; i <= race.numberOfLaps; i++) {
    updateRaceCar(raceCar1);
    updateRaceCar(raceCar2);
    updateFirstPlace(&race, raceCar1, raceCar2);
    printFirstPlaceAfterLap(race);
  }
};


int main() {
	srand(time(0));
  struct Race race;
  struct RaceCar raceCar1;
  struct RaceCar raceCar2;
  
  

};
