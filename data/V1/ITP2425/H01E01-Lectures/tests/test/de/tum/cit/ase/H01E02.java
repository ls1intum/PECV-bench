package de.tum.cit.ase;

import de.tum.in.test.api.*;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.RetentionPolicy.RUNTIME;

@WhitelistPath("target") // mainly for Artemis
@WhitelistPath(value = "../testprog23h01e02**", type = PathType.GLOB) // for manual assessment and development
@WhitelistClass(AttributeHelper.class)
@WhitelistClass(BehaviorTest.class)
@BlacklistPath(value = "target/test-classes**Test*.{java,class}", type = PathType.GLOB)
@StrictTimeout(3)
@MirrorOutput
@Retention(RUNTIME)
@Target({ElementType.TYPE, ElementType.ANNOTATION_TYPE})
public @interface H01E02 {
}
