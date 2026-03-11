package de.tum.cit.ase;

public class LectureName {
    private final String name;
    
    public LectureName(String name) {
        this.name = name;
    }
    
    public String getValue() {
        return name;
    }
    
    @Override
    public String toString() {
        return name;
    }
}
