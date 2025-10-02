# H05E01 - Space Farm! 

In our cosmic adventure, Old MacDonald has set out to build an intergalactic seal sanctuary using the latest and greatest object-oriented technologies. In this futuristic twist on the traditional “Old MacDonald Had a Farm,” our hero isn’t herding cows and chickens but rather floating alongside space seals in the vast depths of outer space.

Each verse of the song swaps in a new cosmic creature, complete with its unique sound resonating through the stars. For example, if our intergalactic verse features a Seal, the sound might be an ethereal "moo,” echoing across the void. To create a foundation for our “Old MacDonald Had a Farm” reimagined with seals, pigs, and star-bound goats, we’ll explore the principles of inheritance, interface implementation, and abstract classes. Therefore, it’s essential to be familiar with these concepts from the lecture to build our space sanctuary’s object-oriented architecture.

## Project Structure

In the template repository folder `src/de/tum/cit/ase`, you can already find the `Main` class for testing the rest of the classes, which must also be created in the same directory according to the UML diagram below:


@startuml
 

together {
class Farm { 
<color:testsColor(testMethods[Farm])>- animals: List<Animal></color>
<color:testsColor(testMethods[Farm])>+ addAnimal(animal: Animal):void</color>
<color:testsColor(testMethods[Farm])>- singFarmSongVerse(animal: Animal):void</color>
<color:testsColor(testMethods[Farm])>+ singFarmSong():void</color>
<color:testsColor(testMethods[Farm])>+ feedAllAnimals():void</color>
}
}

together {
abstract class Animal <<abstract>> #text:testsColor(testClass[Animal]) {
<color:testsColor(testAttributes[Animal])>- name: String</color>
{abstract} <color:testsColor(testMethods[Animal])>+ messageOnFeed():String</color>
}

class Seal #text:testsColor(testClass[Seal]){
<color:testsColor(testMethods[Seal])>+ messageOnFeed():String</color>
<color:testsColor(testMethods[Seal])>+ messageOnMilk():String</color>
<color:testsColor(testMethods[Seal])>+ messageOnRide():String</color>
}

class Pig #text:testsColor(testClass[Pig]){
<color:testsColor(testMethods[Pig])>+ messageOnFeed():String</color>
<color:testsColor(testMethods[Pig])>+ messageOnRide():String</color>
}

class Goat #text:testsColor(testClass[Goat]){
<color:testsColor(testMethods[Goat])>+ messageOnFeed():String</color>
<color:testsColor(testMethods[Goat])>+ messageOnMilk():String</color>
}

interface Rideable <<interface>> #text:testsColor(testClass[Rideable]){
<color:testsColor(testMethods[Rideable])>{abstract} messageOnRide():String</color>
}

interface Milkable <<interface>> #text:testsColor(testClass[Milkable]){
<color:testsColor(testMethods[Milkable])>{abstract} messageOnMilk():String</color>
}
 }

Farm -d-> "*" Animal #testsColor(testAttributes[Farm]);text:testsColor(testAttributes[Farm]) : animals

Milkable <|-- Seal #testsColor(testClass[Seal])
Milkable <|-- Goat #testsColor(testClass[Goat])


Rideable <|-- Pig #testsColor(testClass[Pig])
Rideable <|-- Seal #testsColor(testClass[Seal])

Animal <|-[hidden]right- Rideable
Milkable <|-[hidden]left- Rideable

Animal <|--Seal #testsColor(testClass[Seal])
Animal <|--Pig #testsColor(testClass[Pig])
Animal <|--Goat #testsColor(testClass[Goat]) 
 

hide circles
hide empty members
@enduml


## Your tasks

First of all, we need to set up the structure for our song "Old MacDonald had a Farm". Therefore, we need to implement the structure from the UML diagram above. Each class should have a constructor that initializes all class attributes. The animal is an abstract class, which can be a pig, a goat, or a seal. All three animals have something in common: they have a name.

### Part 1

1. [task][Implement the Animal class](testClass[Animal],testAttributes[Animal],testMethods[Animal],testConstructors[Animal])
    Create an `abstract` class `Animal` according to the UML diagram above and define method `messageOnFeed()` as `abstract`. Also, don't forget to implement a `getter` and a `setter`.

2. [task][Create Interfaces](testClass[Rideable],testClass[Milkable],testMethods[Milkable],testMethods[Rideable]) 
    Define the `Rideable` and `Milkable` interfaces and remember that their methods are not `default` or `static`.
    
### Part 2

Now, in our classes Goat, Seal, and Pig, you have to implement the interfaces as shown in the UML diagram and implement the methods.
- The method `messageOnMilk()` should return <code class="string">"[Animal Type] [name] is milked"</code>
- The method `messageOnRide()` should return <code class= "string"> "Riding on [Animal Type] [name]" </code>

1. [task][Implement the Seal class](testClass[Seal],testConstructors[Seal],testMethods[Seal],feedSealTest(),milkSealTest(),rideSealTest())
    Implement the class `Seal` according to the UML diagram. A seal is an `Animal` which is `Rideable` and `Milkable`, and `messageOnFeed()` should return <code class="string">"Arf Arf!"</code>

2. [task][Implement the Pig class](testClass[Pig],testConstructors[Pig],testMethods[Pig],feedPigTest(),ridePigTest())
    Implement the class `Pig` according to the UML diagram. A pig is a `Rideable` `Animal`, and `messageOnFeed()` should return <code class="string">"Oink!"</code>

3. [task][Implement the Goat class](testClass[Goat],testConstructors[Goat],testMethods[Goat],feedGoatTest(),milkGoatTest())
    Implement the class `Goat` according to the UML diagram. A goat is a `Milkable` `Animal`, and `messageOnFeed()` should return <code class="string">"Maah!"</code>

### Part 3

1. [task][Implement the Farm class](testMethods[Farm],testAttributes[Farm],farmConstructs(),getAnimalsTest())
    Implement the class `Farm` according to the UML diagram. In a farm, there are a list of animals. The aggregation between Farm and Animal is realized using a `List`, implemented using an `ArrayList`. Initialize the ArrayList in a constructor with no arguments. Also, don't forget to implement a `getter` and a `setter`.
    - `addAnimal(Animal a)` adds an animal to the list. 
    - `feedAllAnimals()` calls `messageOnFeed()` on all animals in the Farm, printing out the message for each animal.

2. [task][Play the Song](testMethods[Farm],executeSongMethod(IOTester)) 
    Implement the method `singFarmSong()` inside `Farm.java`, which prints the **Old MacDonald had a Farm** song. Your song must be printed correctly for a farm with any number of animals. The song consists of multiple verses, where each verse is sung by one Animal. A verse looks like this:
    Hint: Use animal.getClass().getSimpleName() to get the class name of the animal 

```
    Old MacDonald had a farm
    Ee i ee i o
    And on his farm he had some [Animal Type]s
    Ee i ee i oh
    With a 
    [messageOnFeed() Return value]
    [messageOnFeed() Return value]
    here, and a 
    [messageOnFeed() Return value]
    [messageOnFeed() Return value]
    there.
    Here a 
    [messageOnFeed() Return value]
    There a 
    [messageOnFeed() Return value]
    Everywhere a 
    [messageOnFeed() Return value]
    [messageOnFeed() Return value]
    Old MacDonald had a farm
    Ee i ee i o
```

Verses are printed back to back, so no space or blank line is added between verses, only line breaks.

<style>
code.string {
    background-color: rgba(var(--bs-body-color-rgb), 0.10);;
    border: 2px;
    border-radius: 3px;
    padding: 2px;
}  
#plantUml-11 {
  display: flex;
  justify-content: center;  
  align-items: center;  
}

#plantUml-11 svg[width="1444px"][height="280px"][viewBox="0 0 1444 280"] { 
  transform-origin: center;  
}


</style>