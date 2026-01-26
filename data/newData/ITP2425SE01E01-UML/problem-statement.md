# Excellence Land 

The seals are convinced that creating a TUM-inspired amusement park (called "Excellence Land") is the next decisive step in the university's overarching excellence strategy. Therefore they are preparing the IT platform to manage the amusement park's rides.

The seals already created the UML class diagram below. Your task is to understand and correctly use it. Create all classes/interfaces, attributes, constructors and methods and add public getters for all attributes (for this exercise it is not required to add setters for the attributes). Every class/interface has to be declared **public**. Provide a **public constructor** for each class that takes all attributes defined in the UML class diagram as a parameter **in the same order as in the UML diagram** (first attribute on top of the UML class => First parameter in the constructor) and assign them to the class attributes correspondingly.

---

### UML Diagram

@startuml

    hide circles
    hide empty members

    interface Pneumatic <<interface>> {
        {abstract} raisePressure(pressureIncrease: int): void
        {abstract} openValve(): void
    }

    abstract class Ride <<abstract>> {
        -name: String
        -abbreviation: char
    }

    abstract class RollerCoaster <<abstract>> {
        -numberOfLoopings: int
    }

    class LaunchedRollerCoaster

    class LaunchedDropdownTower

    class ExcellenceLand {
        -excellencyLevel: double
        -excellentEnough: boolean
    }

    Ride <|-down- RollerCoaster
    RollerCoaster <|-down- LaunchedRollerCoaster
    LaunchedDropdownTower -up-|> Pneumatic
    LaunchedRollerCoaster -up-|> Pneumatic

    Ride <|-down- LaunchedDropdownTower
    ExcellenceLand -right-> "*" Ride: rides
    Ride -[hidden]right-> Pneumatic
@enduml

---

### Tasks 

1. [task][Declare Pneumatic](testClass[Pneumatic],testMethods[Pneumatic]) 
    According to the UML diagram, declare `Pneumatic` and its abstract methods.
2. [task][Declare and Implement Ride](testClass[Ride],testAttributes[Ride],testConstructors[Ride],testMethods[Ride])
    According to the UML diagram, declare and implement `Ride`, its attributes, its constructor, and its getters.
3. [task][Declare and Implement ExcellenceLand](testClass[ExcellenceLand],testAttributes[ExcellenceLand],testConstructors[ExcellenceLand],testMethods[ExcellenceLand],checkExcellentLandConstructorAndGetters())
    According to the UML diagram, declare and implement `ExcellenceLand`, its attributes, its constructor, and its getters. The attribute `rides` is of type `List<Ride>` and private.
4. [task][Declare and Implement RollerCoaster](testClass[RollerCoaster],testAttributes[RollerCoaster],testConstructors[RollerCoaster],testMethods[RollerCoaster])
    According to the UML diagram, declare and implement `RollerCoaster`, its attributes, its constructor and its getters.
5. [task][Declare and Implement LaunchedDropdownTower](testClass[LaunchedDropdownTower],testConstructors[LaunchedDropdownTower],testMethods[LaunchedDropdownTower],checkLaunchedDropdownTowerConstructorAndGetters())
    According to the UML diagram, declare and implement `LaunchedDropdownTower`, its constructor, and its methods.
6. [task][Declare and Implement LaunchedRollerCoaster](testClass[LaunchedRollerCoaster],testConstructors[LaunchedRollerCoaster],testMethods[LaunchedRollerCoaster],checkLaunchedRollerCoasterConstructorAndGetters())
    According to the UML diagram, declare and implement `LaunchedRollerCoaster`, its constructor, and its methods.

---

### Remarks

- All classes, attributes and methods must not be final.
- You do **not** need to implement any logic for `raisePressure(int pressureIncrease)` and `openValve()` in `LaunchedDropdownTower` and `LaunchedRollerCoaster`.
- You can always use the `Main` class to test your implementation.