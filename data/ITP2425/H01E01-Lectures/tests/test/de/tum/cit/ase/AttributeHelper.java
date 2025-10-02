package de.tum.cit.ase;

import java.lang.reflect.Field;

import static org.junit.jupiter.api.Assertions.fail;

public class AttributeHelper {

    public static void setAttribute(Class<?> clz, String attributeName, Object instance, Object value) {
        try {
            Field field = clz.getDeclaredField(attributeName);
            field.setAccessible(true);
            field.set(instance, value);
        } catch (NoSuchFieldException e) {
            fail("Expected field " + attributeName + " of class " + clz.getSimpleName() + " does not exist.");
        } catch (IllegalAccessException e) {
            fail("Internal Test Error: ", e);
        }
    }

    public static <T> T readAttribute(Class<?> clazz, String fieldName, Object instance, Class<T> expectedType) {
        try {
            Field field = clazz.getDeclaredField(fieldName);
            field.setAccessible(true);
            Object value = field.get(instance);
            return checkAttributeType(value, expectedType, fieldName, clazz.getSimpleName());
        } catch (ReflectiveOperationException e) {
            fail("Expected field " + fieldName + " of class " + clazz.getSimpleName() + " does not exist.");
        }
        return null;
    }

    @SuppressWarnings("unchecked")
    public static <T> T checkAttributeType(Object object, Class<T> tClass, String attributeName, String className) {
        if (!tClass.isInstance(object))
            fail("Attribute " + attributeName + " of class " + className + " must be from type " + tClass.getSimpleName());
        return (T) object;
    }
}
