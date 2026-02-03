package de.tum.cit.ase;

public class StudentCount {
    private final int count;
    
    public StudentCount(int count) {
        this.count = count;
    }
    
    public int getValue() {
        return count;
    }
    
    @Override
    public String toString() {
        return String.valueOf(count);
    }
}
