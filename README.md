# shipyard

An application that loads and unloads containers onto a ship.  Offloaded containers are put on appropriate trucks or train cars.  There will be several different kinds of containers but at first there will be three kinds of containers:

    A normal basic container that is used for most shipping
    A heavy container is a kind of basic container
    A refrigerated container which is a kind of heavy container

Any container may have special properties for containing explosives
Any container may have special properties for containing toxics

After the initial project is done, students will be required to add a new kind of heavy container that can contain liquids.  This new container must be introduced without changing even recompiling any of their existing code, but by creating a new .jar file.

Each ship has capacity that may be different.  The capacity has the following parts:

    Maximum number of toxic and explosive containers (optional for a ship)
    Maximum number of refrigerated containers (optional for a ship)
    Maximum number of heavy containers
    Maximum number of all containers including basic containers

The application will read an XML file that contains the name and capacity information of the ship to be loaded and a list of containers including the serial number of each and type and properties of each. When run the program will read the XML file and print a manifest including serial numbers and information about each container put on the ship.  The correct answer would be to max out heavy, refrigerated, and toxic containers and explosive containers for a ship

The instructor may decide to give the students a .JAR file that contains specific interfaces that the students will use.  This is the dependency injection that allows the students to build an object oriented system that can accept new kinds of containers without changing or recompiling their code through the Reflection properties of a new .jar.  I think a more realistic approach is to let the students design these interfaces collaboratively and implement the .jar file themselves since that's generally what happens when a piece of software like this is built commercially.

The instructor will supply a .xsd file that is the schema for input xml file.

A well designed solution will be made up at first of the following jar files:

    The dependency inject jar, containing interfaces, a basic container, a heavy container that inherits from basic container
    The main program
    A jar file that implements the refrigerated container
    A jar file that implements the liquid container.
